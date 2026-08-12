#!/usr/bin/env python3
"""Render the Bembicidae Markdown pages as static HTML."""

from __future__ import annotations

import html
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "html" / "bembicidae"
ASSET_DIR = OUT_DIR / "assets"

RENDERER_PATH = ROOT / "tools" / "render_broad_sphecidae_html.py"
SPEC = importlib.util.spec_from_file_location("broad_sphecidae_renderer", RENDERER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load renderer from {RENDERER_PATH}")
renderer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = renderer
SPEC.loader.exec_module(renderer)


PAGES = [
    renderer.Page(
        "Workspace Overview",
        ROOT / "keys" / "bembicidae" / "README.md",
        "overview.html",
        "Family-level workspace map for Bembicidae keys, checklists, and notes.",
    ),
    renderer.Page(
        "California Genus Key",
        ROOT / "keys" / "bembicidae" / "california-genera-key.md",
        "california-genera-key.html",
        "Working key to the 26 California genera of Bembicidae.",
    ),
    renderer.Page(
        "Eastern Sierra Working List",
        ROOT / "checklists" / "bembicidae" / "eastern-sierra-working-list.md",
        "eastern-sierra-working-list.html",
        "Regional Bembicidae scope and first-pass eastern-Sierra priorities.",
    ),
    renderer.Page(
        "California Bembix Checklist",
        ROOT / "checklists" / "bembicidae" / "california-bembix.md",
        "california-bembix.html",
        "Species checklist for California Bembix retained as genus-level work.",
    ),
    renderer.Page(
        "Bembix Foreleg-Spine Key",
        ROOT / "keys" / "bembicidae" / "california-bembix-foreleg-spines.md",
        "california-bembix-foreleg-spines.html",
        "Reduced California Bembix comparison and short key for foreleg-spine questions.",
    ),
]

renderer.SOURCE_TO_OUTPUT = {page.source.resolve(): page.output for page in PAGES}


def sidebar(active: str | None = None) -> str:
    links = [
        '<a href="index.html"'
        + (' aria-current="page"' if active == "index.html" else "")
        + ">Overview</a>"
    ]
    for page in PAGES:
        current = ' aria-current="page"' if page.output == active else ""
        links.append(f'<a href="{page.output}"{current}>{html.escape(page.title)}</a>')
    return "\n".join(links)


def page_shell(title: str, body: str, active: str, source_note: str | None = None) -> str:
    note = f'<p class="source-note">{html.escape(source_note)}</p>' if source_note else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Bembicidae</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <p class="site-title">Bembicidae</p>
      <p class="site-subtitle">California family keys and eastern-Sierra working notes</p>
      <nav class="nav" aria-label="Bembicidae pages">
{sidebar(active)}
      </nav>
    </aside>
    <main class="content">
      <article class="document">
{note}
{body}
      </article>
    </main>
  </div>
</body>
</html>
"""


def render_index() -> str:
    items = []
    for page in PAGES:
        source = page.source.relative_to(ROOT).as_posix()
        items.append(
            f'<li><a href="{page.output}"><strong>{html.escape(page.title)}</strong>'
            f"<span>{html.escape(page.description)}</span>"
            f"<span>Source: {html.escape(source)}</span></a></li>"
        )
    body = (
        "<h1>Bembicidae HTML Pages</h1>\n"
        "<p>Static browser-rendered versions of the Bembicidae family workspace, "
        "including the California genus key and eastern-Sierra working list.</p>\n"
        f'<ul class="page-list">{"".join(items)}</ul>'
    )
    return page_shell("Bembicidae HTML Pages", body, "index.html")


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (ASSET_DIR / "style.css").write_text(renderer.CSS + "\n", encoding="utf-8")
    (OUT_DIR / "index.html").write_text(render_index(), encoding="utf-8")

    for page in PAGES:
        markdown_text = page.source.read_text(encoding="utf-8")
        title, body = renderer.render_blocks(markdown_text, page.source)
        source_note = f"Rendered from {page.source.relative_to(ROOT).as_posix()}"
        (OUT_DIR / page.output).write_text(
            page_shell(title, body, page.output, source_note),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
