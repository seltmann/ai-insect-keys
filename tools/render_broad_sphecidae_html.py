#!/usr/bin/env python3
"""Render the broad-Sphecidae Markdown pages as static HTML.

This is intentionally small and dependency-free. It supports the Markdown
features used in the broad-Sphecidae notes: headings, paragraphs, simple lists,
tables, fenced code blocks, inline code, and links.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "html" / "broad-sphecidae"
ASSET_DIR = OUT_DIR / "assets"


@dataclass(frozen=True)
class Page:
    title: str
    source: Path
    output: str
    description: str


PAGES = [
    Page(
        "Field-Screen Family Key",
        ROOT / "keys" / "broad-sphecidae" / "california-family-key.md",
        "california-family-key.html",
        "Short family key and practical screening notes.",
    ),
    Page(
        "Family Key And 90 Genera",
        ROOT / "keys" / "broad-sphecidae" / "california-family-key-and-genera.md",
        "california-family-key-and-genera.html",
        "DOCX-derived family key with all 90 California genera listed by family.",
    ),
    Page(
        "Genus Keys By Tribe",
        ROOT / "keys" / "broad-sphecidae" / "california-genus-keys-by-tribe.md",
        "california-genus-keys-by-tribe.html",
        "DOCX-derived small genus keys organized by tribe, subtribe, or practical group.",
    ),
    Page(
        "Direct Sphecidae Genus Key",
        ROOT / "keys" / "broad-sphecidae" / "california-sphecidae-direct-genus-key.md",
        "california-sphecidae-direct-genus-key.html",
        "Direct key from restricted California Sphecidae to genus.",
    ),
    Page(
        "Dangermond And Eastern Sierra Scope",
        ROOT
        / "checklists"
        / "broad-sphecidae"
        / "eastern-sierra-and-dangermond-scope.md",
        "eastern-sierra-and-dangermond-scope.html",
        "Regional flag definitions and Sierra-priority audit scaffold.",
    ),
]

SOURCE_TO_OUTPUT = {page.source.resolve(): page.output for page in PAGES}


CSS = """
:root {
  color-scheme: light;
  --ink: #18201c;
  --muted: #5f6c65;
  --line: #d9dfda;
  --paper: #fbfcfa;
  --panel: #ffffff;
  --accent: #315f4d;
  --accent-2: #8a5a18;
  --table-head: #edf3ef;
  --code-bg: #f1f4f2;
  --shadow: 0 18px 40px rgba(23, 35, 29, 0.08);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  line-height: 1.55;
}

a {
  color: var(--accent);
  text-decoration-thickness: 1px;
  text-underline-offset: 0.18em;
}

a:hover {
  color: var(--accent-2);
}

.layout {
  display: grid;
  grid-template-columns: minmax(220px, 300px) minmax(0, 1fr);
  min-height: 100vh;
}

.sidebar {
  position: sticky;
  top: 0;
  align-self: start;
  height: 100vh;
  overflow: auto;
  border-right: 1px solid var(--line);
  background: #f5f7f4;
  padding: 28px 22px;
}

.site-title {
  color: var(--accent);
  font-size: 18px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 6px;
}

.site-subtitle {
  color: var(--muted);
  font-size: 13px;
  margin: 0 0 24px;
}

.nav {
  display: grid;
  gap: 8px;
}

.nav a {
  border: 1px solid transparent;
  border-radius: 6px;
  color: var(--ink);
  display: block;
  font-size: 14px;
  padding: 8px 10px;
  text-decoration: none;
}

.nav a[aria-current="page"] {
  background: var(--panel);
  border-color: var(--line);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03);
  color: var(--accent);
  font-weight: 700;
}

.content {
  min-width: 0;
  padding: 42px min(6vw, 76px) 80px;
}

.document {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin: 0 auto;
  max-width: 1180px;
  padding: 40px min(5vw, 64px);
}

.source-note {
  color: var(--muted);
  font-size: 13px;
  margin: 0 0 26px;
}

h1,
h2,
h3,
h4 {
  letter-spacing: 0;
  line-height: 1.2;
}

h1 {
  color: var(--accent);
  font-size: 34px;
  margin: 0 0 14px;
}

h2 {
  border-top: 1px solid var(--line);
  color: #27372f;
  font-size: 24px;
  margin: 34px 0 12px;
  padding-top: 22px;
}

h3 {
  color: #34483d;
  font-size: 19px;
  margin: 26px 0 10px;
}

h4 {
  color: #415b4d;
  font-size: 16px;
  margin: 22px 0 8px;
}

p,
ul,
ol {
  margin: 0 0 14px;
}

li + li {
  margin-top: 6px;
}

code {
  background: var(--code-bg);
  border: 1px solid #e1e7e3;
  border-radius: 4px;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  font-size: 0.92em;
  padding: 0.1em 0.28em;
}

pre {
  background: var(--code-bg);
  border: 1px solid var(--line);
  border-radius: 6px;
  overflow-x: auto;
  padding: 14px 16px;
}

pre code {
  background: transparent;
  border: 0;
  padding: 0;
}

.table-wrap {
  margin: 18px 0 24px;
  overflow-x: auto;
}

table {
  border-collapse: collapse;
  font-size: 14px;
  min-width: 760px;
  width: 100%;
}

th,
td {
  border: 1px solid var(--line);
  padding: 9px 10px;
  text-align: left;
  vertical-align: top;
}

th {
  background: var(--table-head);
  color: #23362d;
  font-weight: 700;
}

tr:nth-child(even) td {
  background: #fafbf9;
}

.page-list {
  display: grid;
  gap: 12px;
  list-style: none;
  padding: 0;
}

.page-list a {
  background: #f8faf8;
  border: 1px solid var(--line);
  border-radius: 8px;
  display: block;
  padding: 14px 16px;
  text-decoration: none;
}

.page-list strong {
  color: var(--accent);
  display: block;
}

.page-list span {
  color: var(--muted);
  display: block;
  font-size: 14px;
  margin-top: 3px;
}

@media (max-width: 820px) {
  .layout {
    display: block;
  }

  .sidebar {
    height: auto;
    position: static;
  }

  .content {
    padding: 18px;
  }

  .document {
    padding: 26px 20px;
  }

  h1 {
    font-size: 28px;
  }
}
""".strip()


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped:
        if char == "\\" and not escaped:
            escaped = True
            continue
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        if escaped:
            current.append("\\")
        current.append(char)
        escaped = False
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def link_target(target: str, source: Path) -> str:
    if not target or "://" in target or target.startswith(("mailto:", "#", "/")):
        return target
    path_part, hash_mark, fragment = target.partition("#")
    resolved = (source.parent / path_part).resolve()
    if resolved in SOURCE_TO_OUTPUT:
        return SOURCE_TO_OUTPUT[resolved] + (hash_mark + fragment if hash_mark else "")
    if path_part.endswith(".md"):
        return Path(path_part).with_suffix(".html").as_posix() + (
            hash_mark + fragment if hash_mark else ""
        )
    return target


def inline_markdown(text: str, source: Path) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def code_repl(match: re.Match[str]) -> str:
        return stash(f"<code>{html.escape(match.group(1))}</code>")

    text = re.sub(r"`([^`]+)`", code_repl, text)
    escaped = html.escape(text)

    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        href = html.escape(link_target(target, source), quote=True)
        return f'<a href="{href}">{label}</a>'

    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, escaped)
    for index, value in enumerate(placeholders):
        escaped = escaped.replace(f"\u0000{index}\u0000", value)
    return escaped


def render_blocks(markdown_text: str, source: Path) -> tuple[str, str]:
    lines = markdown_text.splitlines()
    title = source.stem.replace("-", " ").title()
    body: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            language = stripped.removeprefix("```").strip()
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_attr = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            body.append(f"<pre><code{class_attr}>{html.escape(chr(10).join(code_lines))}</code></pre>")
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            content = inline_markdown(heading.group(2), source)
            if level == 1:
                title = re.sub(r"<[^>]+>", "", content)
            body.append(f"<h{level}>{content}</h{level}>")
            index += 1
            continue

        if stripped.startswith("|") and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            header = split_table_row(lines[index])
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(split_table_row(lines[index]))
                index += 1
            body.append(render_table(header, rows, source))
            continue

        if stripped.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(lines[index].strip()[2:].strip())
                index += 1
                while index < len(lines) and lines[index].startswith("  ") and lines[index].strip():
                    items[-1] += " " + lines[index].strip()
                    index += 1
            body.append(
                "<ul>"
                + "".join(f"<li>{inline_markdown(item, source)}</li>" for item in items)
                + "</ul>"
            )
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while index < len(lines) and re.match(r"^\d+\.\s+", lines[index].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[index].strip()))
                index += 1
                while index < len(lines) and lines[index].startswith("   ") and lines[index].strip():
                    items[-1] += " " + lines[index].strip()
                    index += 1
            body.append(
                "<ol>"
                + "".join(f"<li>{inline_markdown(item, source)}</li>" for item in items)
                + "</ol>"
            )
            continue

        paragraph = [stripped]
        index += 1
        while index < len(lines):
            next_line = lines[index]
            next_stripped = next_line.strip()
            if (
                not next_stripped
                or next_stripped.startswith(("#", "|", "- ", "```"))
                or re.match(r"^\d+\.\s+", next_stripped)
            ):
                break
            paragraph.append(next_stripped)
            index += 1
        body.append(f"<p>{inline_markdown(' '.join(paragraph), source)}</p>")

    return title, "\n".join(body)


def render_table(header: list[str], rows: list[list[str]], source: Path) -> str:
    width = max([len(header), *(len(row) for row in rows)] or [0])
    header = header + [""] * (width - len(header))
    normalized = [row + [""] * (width - len(row)) for row in rows]
    thead = "".join(f"<th>{inline_markdown(cell, source)}</th>" for cell in header)
    body_rows = []
    for row in normalized:
        cells = "".join(f"<td>{inline_markdown(cell, source)}</td>" for cell in row)
        body_rows.append(f"<tr>{cells}</tr>")
    return (
        '<div class="table-wrap"><table>'
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table></div>"
    )


def sidebar(active: str | None = None) -> str:
    links = ['<a href="index.html"' + (' aria-current="page"' if active == "index.html" else "") + ">Overview</a>"]
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
  <title>{html.escape(title)} - Broad Sphecidae</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <p class="site-title">Broad Sphecidae</p>
      <p class="site-subtitle">California keys and Sierra/Dangermond working notes</p>
      <nav class="nav" aria-label="Broad Sphecidae pages">
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
        "<h1>Broad Sphecidae HTML Pages</h1>\n"
        "<p>Static browser-rendered versions of the broad-Sphecidae Markdown "
        "keys and regional working notes.</p>\n"
        f'<ul class="page-list">{"".join(items)}</ul>'
    )
    return page_shell("Broad Sphecidae HTML Pages", body, "index.html")


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (ASSET_DIR / "style.css").write_text(CSS + "\n", encoding="utf-8")
    (OUT_DIR / "index.html").write_text(render_index(), encoding="utf-8")

    for page in PAGES:
        markdown_text = page.source.read_text(encoding="utf-8")
        title, body = render_blocks(markdown_text, page.source)
        source_note = f"Rendered from {page.source.relative_to(ROOT).as_posix()}"
        (OUT_DIR / page.output).write_text(
            page_shell(title, body, page.output, source_note),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
