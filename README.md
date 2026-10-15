# ai-insect-keys

Generated identification keys and checklist notes for insect-identification
projects.

## Repository layout

Folder inventory checked on 2026-10-15. The tree summarizes the directories
present; PDF filenames and citations are listed under References below.

```text
ai-insect-keys/
|-- README.md
|-- .gitignore
|-- keys/                         # Generated Markdown keys and identification notes
|   |-- anthidium/
|   |-- bees/
|   |-- bembicidae/
|   |-- broad-sphecidae/
|   |-- chrysididae/
|   |-- tiphiidae/
|   `-- vespidae/
|-- checklists/                   # Working lists and occurrence summaries (MD/TSV)
|   |-- anthidium/
|   |-- bees/
|   |-- bembicidae/
|   |-- broad-sphecidae/
|   `-- chrysididae/
|-- html/                         # Rendered static keys and notes
|   |-- bembicidae/assets/
|   |-- broad-sphecidae/assets/
|   |-- tiphiidae/assets/
|   `-- vespidae/assets/
|-- references/                   # Local-only; ignored by Git
|   |-- Gonzalez-Griswold-2013-Anthidium-Western-Hemisphere-key.pdf
|   |-- bees/
|   |-- bembicidae/
|   |   `-- rendered-pages/
|   |-- broad-sphecidae/
|   |-- chrysididae/
|   |-- tiphiidae/
|   `-- vespidae/
|-- photos/
|   `-- 2026_07_31/               # Two specimen photographs
|-- tools/                        # HTML renderers and GBIF retrieval script
|-- work/                         # Intermediate data, OCR, and PDF processing
|   |-- bees/gbif/
|   |-- ocr/
|   |-- pdf-render/
|   |   |-- cis19/
|   |   `-- sphecid-world/
|   `-- pdf-text/
`-- tmp/                          # Temporary PDF page images
    |-- pdf_pages/evans_matthews_1968b/
    `-- pdfs/
        |-- aesa61-1284/
        `-- chrysididae/
```

`references/` also contains extracted text, source notes, and rendered pages.
Version-control internals, `.DS_Store`, and Python caches are omitted above.
Reference links below resolve on a local checkout with those files present;
they will not resolve on GitHub because the reference directory is ignored.

## Checklists

### Bees

- [Working bee genera list for Dangermond Preserve and nearby mainland context](checklists/bees/dangermond-bee-genera.md)

### Anthidium

- [Possible `Anthidium` species from coastal Santa Barbara County, California](checklists/anthidium/coastal-santa-barbara-county.md)

### Broad Sphecidae / spheciform wasps

- [Working California broad-Sphecidae scope with Dangermond and Eastern Sierra flags](checklists/broad-sphecidae/eastern-sierra-and-dangermond-scope.md)

### Bembicidae

- [Eastern Sierra Bembicidae working list](checklists/bembicidae/eastern-sierra-working-list.md)
- [Checklist of California `Bembix` species](checklists/bembicidae/california-bembix.md)

## Keys

### Bees

- [Identification table and working key to Dangermond bee genera](keys/bees/dangermond-bee-genera-key.md)

### Anthidium

- [Key to candidate `Anthidium` species from coastal Santa Barbara County, California](keys/anthidium/coastal-santa-barbara-county.md)

### Broad Sphecidae / spheciform wasps

- [California broad-Sphecidae family key and field-screen notes](keys/broad-sphecidae/california-family-key.md)
- [DOCX-derived California broad-Sphecidae family key and 90-genera list](keys/broad-sphecidae/california-family-key-and-genera.md)
- [DOCX-derived small keys to California broad-Sphecidae genera by tribe](keys/broad-sphecidae/california-genus-keys-by-tribe.md)
- [Direct key to the California genera of Sphecidae](keys/broad-sphecidae/california-sphecidae-direct-genus-key.md)
- [Rendered broad-Sphecidae HTML pages](html/broad-sphecidae/index.html)

### Bembicidae

- [California Bembicidae genus key](keys/bembicidae/california-genera-key.md)
- [California `Bembix` female foreleg-spine comparison and short key](keys/bembicidae/california-bembix-foreleg-spines.md)
- [Rendered Bembicidae HTML pages](html/bembicidae/index.html)

## References

Keep all reference material under `references/`. The folder is local-only and
ignored by Git; generated Markdown files should cite source filenames and page
numbers, but the PDFs and extracted notes themselves should not be committed.

### Local PDF bibliography

Inventory checked on 2026-10-15: **20 PDF files representing 19 works**.
Citations were compiled from the local PDFs and existing key/checklist source
notes. This is an inventory of the project holdings, not a new online literature
search. Filenames are preserved exactly, including abbreviated scan names.

#### Anthidium

- Gonzalez, V. H., and T. L. Griswold. 2013. Wool carder bees of the genus *Anthidium* in the Western Hemisphere (Hymenoptera: Megachilidae): diversity, host plant associations, phylogeny, and biogeography. *Zoological Journal of the Linnean Society* 168(2):221-425. DOI: 10.1111/zoj.12017.
  Local PDF: [Gonzalez-Griswold-2013-Anthidium-Western-Hemisphere-key.pdf](references/Gonzalez-Griswold-2013-Anthidium-Western-Hemisphere-key.pdf).

#### Bees

- Danforth, B. N., S. G. Brady, K. Darrow, S. Bossert, E. A. B. Almeida, J. Gibbs, J. L. Neff, T. Griswold, L. Packer, R. J. McGinley, and C. D. Michener. 2026. *The Bee Genera of North and Central America (Hymenoptera: Apoidea): Second Edition*. Smithsonian Institution Scholarly Press.
  Local PDF: [BeeGenera-2ed_VOR.pdf](references/bees/BeeGenera-2ed_VOR.pdf).

- Michener, C. D. 2007. *The Bees of the World*. 2nd edition. Johns Hopkins University Press, Baltimore.
  Local PDF: [Michener-2007-Bees-of-the-World.pdf](references/bees/Michener-2007-Bees-of-the-World.pdf).

#### Bembicidae

- Bohart, R. M., and D. S. Horning, Jr. 1971. *California Bembicine Sand Wasps*. *Bulletin of the California Insect Survey* 13:1-49.
  Local PDF: [Bohart-Horning-1971-California-bembicine-sand-wasps.pdf](references/bembicidae/Bohart-Horning-1971-California-bembicine-sand-wasps.pdf).

- Evans, H. E., and R. W. Matthews. 1968. North American *Bembix*, a revised key and suggested grouping. *Annals of the Entomological Society of America* 61(5):1284-1299. Two local scans of the same work:
  Local PDFs: [aesa61-1284.pdf](references/bembicidae/aesa61-1284.pdf), [Evans_Matthews_1968b.pdf](references/bembicidae/Evans_Matthews_1968b.pdf).

- Frank, J. A. 2022. The biology and research history of the solitary wasp genus *Bembix* (Hymenoptera: Bembicidae): a brief review. *Annals of the Entomological Society of America* 115(3):232-238. DOI: 10.1093/aesa/saab050.
  Local PDF: [saab050.pdf](references/bembicidae/saab050.pdf).

- Griswold, T. L. 1983. A new species of *Bembix* from Lower California (Hymenoptera: Sphecidae). *Pan-Pacific Entomologist* 59(1-4):103-107.
  Local PDF: [Griswold-1983-Bembix-boharti-Lower-California.pdf](references/bembicidae/Griswold-1983-Bembix-boharti-Lower-California.pdf).

- Parker, J. B. 1917. A revision of the bembicine wasps of America north of Mexico. *Proceedings of the United States National Museum* 52(2173):1-155.
  Local PDF: [USNMP-52_2173_1917.pdf](references/bembicidae/USNMP-52_2173_1917.pdf).

- Pulawski, W. J. 2026. Catalog of Sphecidae sensu lato: *Bembix*. California Academy of Sciences. Local version last updated 29 July 2026.
  Local PDF: [Pulawski-2026-Bembix-catalog.pdf](references/bembicidae/Pulawski-2026-Bembix-catalog.pdf).

#### Broad Sphecidae / spheciform wasps

- Bohart, R. M., and E. E. Grissell. 1975. *California Wasps of the Subfamily Philanthinae (Hymenoptera: Sphecidae)*. *Bulletin of the California Insect Survey* 19:1-92.
  Local PDF: [Bohart-Grissell-1975-California-Philanthinae.pdf](references/broad-sphecidae/Bohart-Grissell-1975-California-Philanthinae.pdf).

- Bohart, R. M., and A. S. Menke. 1963. A reclassification of the Sphecinae with a revision of the Nearctic species of the tribes Sceliphronini and Sphecini. *University of California Publications in Entomology* 30(2):91-182.
  Local PDF: [Bohart-Menke-1963-Sphecinae-reclassification.pdf](references/broad-sphecidae/Bohart-Menke-1963-Sphecinae-reclassification.pdf).

- Bohart, R. M., and A. S. Menke. 1976. *Sphecid Wasps of the World: A Generic Revision*. University of California Press.
  Local PDF: [Bohart-Menke-1976-Sphecid-Wasps-of-the-World.pdf](references/broad-sphecidae/Bohart-Menke-1976-Sphecid-Wasps-of-the-World.pdf).

#### Chrysididae

- Kimsey, L. S. 2006. *California Cuckoo Wasps in the Family Chrysididae (Hymenoptera)*. *University of California Publications in Entomology* 125. University of California Press. The book copyright is 2006; the eScholarship repository cover gives a 2014 deposit/publication date.
  Local PDF: [Kimsey-2006-California-Cuckoo-Wasps.pdf](references/chrysididae/Kimsey-2006-California-Cuckoo-Wasps.pdf).

#### Tiphiidae / Brachycistidinae

- Kimsey, L. S., and M. S. Wasbauer. 2006. Phylogeny and checklist of the nocturnal tiphiids of the Western Hemisphere (Hymenoptera: Tiphiidae: Brachycistidinae). *Journal of Hymenoptera Research* 15(1):9-25.
  Local PDF: [Kimsey-Wasbauer-2006-Brachycistidinae.pdf](references/tiphiidae/Kimsey-Wasbauer-2006-Brachycistidinae.pdf).

#### Vespidae

- Bequaert, J. 1944 [year used in the project notes and filename]. The North American species of *Ancistrocerus*, proper (Hymenoptera, Vespidae). *Entomologica Americana* 23(4):225-286. The scanned issue heading reads October 1943; actual publication year needs bibliographic confirmation.
  Local PDF: [Bequaert-1944-North-American-Ancistrocerus.pdf](references/vespidae/Bequaert-1944-North-American-Ancistrocerus.pdf).

- Bohart, R. M., and R. C. Bechtel. 1957. The social wasps of California (Vespinae, Polistinae, Polybiinae). *Bulletin of the California Insect Survey* 4:73-101.
  Local PDF: [Bohart-Bechtel-1957-Social-Wasps-California.pdf](references/vespidae/Bohart-Bechtel-1957-Social-Wasps-California.pdf).

- Buck, M., S. A. Marshall, and D. K. B. Cheung. 2008. Identification atlas of the Vespidae (Hymenoptera, Aculeata) of the northeastern Nearctic region. *Canadian Journal of Arthropod Identification* 5. DOI: 10.3752/cjai.2008.05.
  Local PDF: [Buck-Marshall-Cheung-2008-Identification-Atlas-Vespidae.pdf](references/vespidae/Buck-Marshall-Cheung-2008-Identification-Atlas-Vespidae.pdf).

- Piekarski, P. K., J. M. Carpenter, and B. J. Sharanowski. 2017. New species of *Ancistrocerus* (Vespidae, Eumeninae) from the Neotropics with a checklist and key to all species south of the Rio Grande. *ZooKeys* 718:139-154. DOI: 10.3897/zookeys.718.21096.
  Local PDF: [Piekarski-Carpenter-Sharanowski-2017-Ancistrocerus-Neotropics.pdf](references/vespidae/Piekarski-Carpenter-Sharanowski-2017-Ancistrocerus-Neotropics.pdf).

- Richards, O. W. 1966. New records of *Pseudomasaris* Ashmead (Hymenoptera: Vespoidea, Masaridae), with notes on *P. phaceliae* Rohwer and *P. cazieri* R. M. Bohart. *Proceedings of the Royal Entomological Society of London. Series B, Taxonomy* 35:41-49. DOI: 10.1111/j.1365-3113.1966.tb00466.x. Page range follows the local scan; the existing key notes instead list 47-55.
  Local PDF: [Richards-1966-New-records-of-Pseudomasaris.pdf](references/vespidae/Richards-1966-New-records-of-Pseudomasaris.pdf).

### Citation notes

- The recommended citation on PDF page 6 of `BeeGenera-2ed_VOR.pdf` credits
  **Danforth and colleagues (2026)**. Existing bee key/checklist notes attribute
  this title to Griswold and Ascher; those notes have not been revised as part
  of this README inventory.
- Evans and Matthews (1968) is counted once in the bibliography, with both
  local scan filenames listed.
- The Richards page-range discrepancy and Bequaert publication-year uncertainty
  are recorded above so they remain visible during later citation cleanup.
- Bibliographic details supplied only by existing project notes have not all
  been independently checked against publishers. This inventory does not
  change taxonomic determinations or validate the generated keys.

### Additional literature cited in the project

The following works are cited in keys or checklists but do not have a matching
PDF in this repository's `references/` directory as of the inventory date.
These entries reproduce the existing project citations; abbreviated or uncertain
entries remain identified as such.

- Bohart, R. M., and J. E. Gillaspy. 1985. *California Sand Wasps of the Subtribe Stictiellina*. *Bulletin of the California Insect Survey* 27:1-89.
- Bohart, R. M., and L. S. Kimsey. 1979. A key to the species of *Ectemnius* in America north of Mexico, with notes and description of a new species. *Proceedings of the Entomological Society of Washington* 81:486-498.
- Carpenter, J. M. 2004. *Ancistroceroides* de Saussure, a potter wasp genus new for the United States, with a new key to the genera of Eumeninae of America north of Mexico (Hymenoptera: Vespidae). *Journal of the Kansas Entomological Society* 77(4):721-741. DOI: 10.2317/E-33.1.
- Carpenter, J. M., and L. S. Kimsey. 2009. The genus *Euparagia* Cresson (Hymenoptera: Vespidae; Euparagiinae). *American Museum Novitates* 3643:1-11. DOI: 10.1206/626.1.
- Fateryga, Carpenter, and Fateryga. 2023. *Ancistrocerus capra* (De Saussure, 1857), a valid species, not a synonym of *A. antilope* (Panzer, 1798). DOI: 10.1206/4002.1. Author names are abbreviated here as in the source notes.
- Finnamore, A. T. 1995. Revision of the world genera of the subtribe Stigmina, Part 1. *Journal of Hymenoptera Research* 4:204-284.
- Gonzalez, V. H., T. Griswold, and H. Ikerd. 2014. AnthWest, occurrence records for wool carder bees of the genus *Anthidium* (Hymenoptera, Megachilidae, Anthidiini) in the Western Hemisphere. *ZooKeys* 408:31-49. DOI: 10.3897/zookeys.408.5633.
- Kimsey, L. S., and R. B. Kimsey. 1981. A new species of *Bembix* from the California Desert (Hymenoptera: Sphecidae). *Journal of the Kansas Entomological Society* 54(3):486-488.
- Kimsey, L. S., R. B. Kimsey, and C. A. Toft. 1981. Life history of *Bembix inyoensis* in Death Valley (Hymenoptera: Sphecidae). *Journal of the Kansas Entomological Society* 54(4):665-672.
- Krombein, K. V., P. D. Hurd, Jr., D. R. Smith, and B. D. Burks, eds. 1979. *Catalog of Hymenoptera in America North of Mexico*. Volume 2. Smithsonian Institution Press.
- Pate, V. S. L. 1947. A revision of the genus *Arigorytes* (Hymenoptera: Sphecidae: Gorytini). *Canadian Entomologist* 79:47-57.
- Rust, R. W., A. S. Menke, and D. R. Miller. 1985. A biogeographic comparison of the bees, sphecid wasps, and mealybugs of the California Channel Islands (Hymenoptera, Homoptera). In A. S. Menke and D. R. Miller, eds., *Entomology of the California Channel Islands: Proceedings of the First Symposium*, pp. 29-58. Santa Barbara Museum of Natural History.
- Smith, N. J. 2008/2009. Reviews of Nearctic *Ammoplanus* and *Parammoplanus*. *Pan-Pacific Entomologist* 84:301-333 and 85:107-149. Summary citation from the tribe-key notes; full individual titles and dates need confirmation.
- Smith, N. J. 2011/2012. Review of *Timberlakena*, reestablishing *Mohavena* and *Riparena* at generic rank. *Pan-Pacific Entomologist* 87:227-275. Summary citation from the tribe-key notes; publication date needs confirmation.
- Smith, N. J. 2019. Review of the North American species of *Ammoplanellus*. *Pan-Pacific Entomologist* 95:65-120.
- Smith, N. J. 2020. *Andrewsena*, a new genus of Ammoplanidae. *Proceedings of the Entomological Society of Washington* 122:239-251.

### Online identification and occurrence sources recorded in the project

These are links already cited in the project notes; they were not rechecked
online for this inventory. See the linked project documents for access dates,
individual fact sheets, filters, and query details.

- Burrows, S., C. Ritner, M. Christman, L. R. Spears, A. Smith-Pardo, S. Price, R. A. Ramirez, T. Griswold, and A. J. Redford. 2021. [*Exotic Bee ID*](https://idtools.org/exotic_bee/), edition 3. USDA APHIS Identification Technology Program and Utah State University. Includes the North American *Anthidium* key and fact sheets cited in [the regional key](keys/anthidium/coastal-santa-barbara-county.md).
- California Academy of Sciences / W. J. Pulawski. [Catalog of Sphecidae](https://www.calacademy.org/scientists/projects/catalog-of-sphecidae), including generic nomenclature and the family-group classification cited in [the broad-Sphecidae keys](keys/broad-sphecidae/california-family-key-and-genera.md).
- Harris, Kerri-Lee. 2025. [Crabronid ID clues](https://southernforestlife.net/notes/2025/crabronid-id-clues). *Life in a Southern Forest*. Cited in [the Bembicidae genus key](keys/bembicidae/california-genera-key.md).
- [BugGuide](https://bugguide.net/). Family, subfamily, genus, and species pages; the Tiphiinae key is attributed to Allen (1966) in [the tiphiid key notes](keys/tiphiidae/eastern-sierra-genera-key.md). A full Allen citation is not supplied there.
- [GBIF.org](https://www.gbif.org/) and its occurrence/species APIs. Used for regional occurrence screens and the [Dangermond bee summary](checklists/bees/dangermond-bee-gbif-summary.tsv).
- [iNaturalist](https://www.inaturalist.org/) and its API. Used for regional *Anthidium* species counts and selected *Ancistrocerus* record checks.

### Inventory provenance

This README inventory was prepared on 2026-10-15 with AI assistance in Codex.
Work included listing local directories and reference files, reading the existing
source notes, and checking PDF title/copyright/citation pages where available.
Only this README was edited; source PDFs, generated keys, and checklist records
were preserved. The existing project review requirements below still apply.

## Document Provenance and AI Assistance Statement

This repository contains working identification keys, comparison tables, and
checklists prepared with AI assistance in Codex. AI assistance may be used to
organize source material, extract and summarize cited taxonomic characters,
draft Markdown, and maintain repository structure.

The taxonomic authorities remain the cited literature, specimen evidence, and
data sources named in each document. Generated materials are working drafts for
review and should not be treated as peer-reviewed taxonomic revisions or final
species determinations. Identifications, especially from photographs or unusual
specimens, should be verified against the cited sources and by qualified
taxonomic review when needed.

Each generated key or checklist should retain its own provenance and AI
assistance statement, including the date prepared, local reference files used
from `references/`, and the role of AI assistance.
