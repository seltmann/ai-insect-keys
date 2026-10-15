#!/usr/bin/env python3
"""Fetch and normalize GBIF bee occurrence facets for Dangermond work.

The tracked output is a compact genus summary table. Raw query/facet tables are
written under work/ so they stay local.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path


FAMILY_KEYS = {
    "Apidae": 4334,
    "Andrenidae": 7901,
    "Colletidae": 7905,
    "Halictidae": 7908,
    "Megachilidae": 7911,
    "Melittidae": 4345,
}

REGIONS = {
    "preserve_box": (
        -120.50739455434,
        34.4366467326054,
        -120.354177720553,
        34.5801262497771,
    ),
    "surrounding_mainland": (-120.85, 34.25, -119.75, 34.85),
}

GENUS_FOLDS = {
    "Dialictus": "Lasioglossum",
    "Evylaeus": "Lasioglossum",
    "Pyrobombus": "Bombus",
    "Zadontomerus": "Ceratina",
    "Peponapis": "Xenoglossa",
    "Tetraloniella": "Xenoglossa",
    "Xeromelecta": "Brachymelecta",
}

EXCLUDED_GENERA = {
    # One GBIF facet currently resolves a doubtful Apidae record to this
    # non-bee name. Keep it out of the bee working list.
    "Crustacea",
}

BASE_URL = "https://api.gbif.org/v1/occurrence/search"


def wkt_box(bounds: tuple[float, float, float, float]) -> str:
    west, south, east, north = bounds
    return (
        "POLYGON(("
        f"{west} {south},{east} {south},{east} {north},"
        f"{west} {north},{west} {south}"
        "))"
    )


def get_json(url: str, tries: int = 4) -> dict:
    last_error: Exception | None = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                return json.load(response)
        except Exception as error:  # pragma: no cover - depends on network
            last_error = error
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GBIF request failed after {tries} tries: {url}") from last_error


def resolve_taxon(key: str, cache: dict[str, dict]) -> dict:
    if key in cache:
        return cache[key]
    url = f"https://api.gbif.org/v1/species/{key}"
    try:
        data = get_json(url)
    except Exception as error:  # pragma: no cover - keep a partial audit trail
        data = {"key": key, "error": str(error)}
    cache[key] = data
    time.sleep(0.05)
    return data


def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def read_tsv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def fetch_facets(work_dir: Path) -> None:
    query_rows: list[dict] = []
    genus_rows: list[dict] = []
    species_rows: list[dict] = []
    taxon_cache: dict[str, dict] = {}

    for region, bounds in REGIONS.items():
        geometry = wkt_box(bounds)
        for family, family_key in FAMILY_KEYS.items():
            common = {
                "familyKey": str(family_key),
                "hasCoordinate": "true",
                "hasGeospatialIssue": "false",
                "geometry": geometry,
                "limit": "0",
            }

            genus_params = common | {
                "facet": "GENUS_KEY",
                "GENUS_KEY.facetLimit": "300",
            }
            genus_url = BASE_URL + "?" + urllib.parse.urlencode(genus_params)
            genus_data = get_json(genus_url)
            query_rows.append(
                {
                    "region": region,
                    "family": family,
                    "familyKey": family_key,
                    "count": genus_data.get("count", 0),
                    "query_url": genus_url,
                }
            )
            for count in (genus_data.get("facets") or [{}])[0].get("counts", []):
                taxon = resolve_taxon(count["name"], taxon_cache)
                genus_rows.append(
                    {
                        "region": region,
                        "family": family,
                        "genusKey": count["name"],
                        "genus": taxon.get("canonicalName")
                        or taxon.get("genus")
                        or taxon.get("scientificName")
                        or count["name"],
                        "count": count.get("count", 0),
                        "taxonomicStatus": taxon.get("taxonomicStatus")
                        or taxon.get("status", ""),
                        "rank": taxon.get("rank", ""),
                    }
                )

            species_params = common | {
                "facet": "SPECIES_KEY",
                "SPECIES_KEY.facetLimit": "500",
            }
            species_url = BASE_URL + "?" + urllib.parse.urlencode(species_params)
            species_data = get_json(species_url)
            for count in (species_data.get("facets") or [{}])[0].get("counts", []):
                taxon = resolve_taxon(count["name"], taxon_cache)
                species = (
                    taxon.get("canonicalName")
                    or taxon.get("scientificName")
                    or count["name"]
                )
                genus = taxon.get("genus") or species.split()[0]
                species_rows.append(
                    {
                        "region": region,
                        "family": family,
                        "speciesKey": count["name"],
                        "genus": genus,
                        "species": species,
                        "count": count.get("count", 0),
                        "taxonomicStatus": taxon.get("taxonomicStatus")
                        or taxon.get("status", ""),
                        "rank": taxon.get("rank", ""),
                    }
                )
            print(
                f"{region} {family}: {genus_data.get('count', 0)} records",
                file=sys.stderr,
                flush=True,
            )

    write_tsv(
        work_dir / "query-summary.tsv",
        query_rows,
        ["region", "family", "familyKey", "count", "query_url"],
    )
    write_tsv(
        work_dir / "genus-facets.tsv",
        genus_rows,
        ["region", "family", "genusKey", "genus", "count", "taxonomicStatus", "rank"],
    )
    write_tsv(
        work_dir / "species-facets.tsv",
        species_rows,
        [
            "region",
            "family",
            "speciesKey",
            "genus",
            "species",
            "count",
            "taxonomicStatus",
            "rank",
        ],
    )


def normalized_genus(name: str) -> str | None:
    if name in EXCLUDED_GENERA:
        return None
    return GENUS_FOLDS.get(name, name)


def top_species(species_counts: Counter[str], limit: int = 8) -> str:
    return "; ".join(
        f"{species} ({count})" for species, count in species_counts.most_common(limit)
    )


def build_summary(work_dir: Path, output_path: Path) -> None:
    genus_rows = read_tsv(work_dir / "genus-facets.tsv")
    species_rows = read_tsv(work_dir / "species-facets.tsv")

    counts: dict[str, Counter[str]] = defaultdict(Counter)
    family_by_genus: dict[str, Counter[str]] = defaultdict(Counter)
    folded: dict[str, Counter[str]] = defaultdict(Counter)
    species_by_region: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)

    for row in genus_rows:
        source_genus = row["genus"]
        genus = normalized_genus(source_genus)
        if genus is None:
            continue
        count = int(row["count"])
        region = row["region"]
        counts[genus][region] += count
        family_by_genus[genus][row["family"]] += count
        if source_genus != genus:
            folded[genus][source_genus] += count

    for row in species_rows:
        genus = normalized_genus(row["genus"])
        if genus is None:
            continue
        species_by_region[(genus, row["region"])][row["species"]] += int(row["count"])

    summary_rows: list[dict] = []
    for genus in sorted(counts, key=lambda g: (family_by_genus[g].most_common(1)[0][0], g)):
        family = family_by_genus[genus].most_common(1)[0][0]
        preserve_count = counts[genus]["preserve_box"]
        context_count = counts[genus]["surrounding_mainland"]
        folded_names = "; ".join(
            f"{name} ({count})" for name, count in folded[genus].most_common()
        )
        summary_rows.append(
            {
                "family": family,
                "genus": genus,
                "evidence_status": "preserve_box"
                if preserve_count
                else "surrounding_mainland_only",
                "preserve_box_records": preserve_count,
                "surrounding_mainland_records": context_count,
                "folded_gbif_names": folded_names,
                "preserve_species_gbif": top_species(
                    species_by_region[(genus, "preserve_box")]
                ),
                "surrounding_species_examples_gbif": top_species(
                    species_by_region[(genus, "surrounding_mainland")]
                ),
            }
        )

    write_tsv(
        output_path,
        summary_rows,
        [
            "family",
            "genus",
            "evidence_status",
            "preserve_box_records",
            "surrounding_mainland_records",
            "folded_gbif_names",
            "preserve_species_gbif",
            "surrounding_species_examples_gbif",
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from-work-cache",
        action="store_true",
        help="reuse existing work/bees/gbif facet files instead of querying GBIF",
    )
    parser.add_argument("--work-dir", default="work/bees/gbif")
    parser.add_argument(
        "--output",
        default="checklists/bees/dangermond-bee-gbif-summary.tsv",
    )
    args = parser.parse_args()

    work_dir = Path(args.work_dir)
    if not args.from_work_cache:
        fetch_facets(work_dir)
    build_summary(work_dir, Path(args.output))


if __name__ == "__main__":
    main()
