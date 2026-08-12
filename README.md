# ai-insect-keys

Generated identification keys and checklist notes for insect-identification
projects.

## Repository layout

- `keys/<taxon>/`: generated keys, comparison tables, and identification notes.
- `checklists/<taxon>/`: working species lists and occurrence summaries.
- `html/<taxon>/`: rendered static HTML versions of selected keys and notes.
- `references/`: local-only source PDFs, extracted text, rendered pages, and
  source notes. This folder is intentionally ignored by Git so reference
  material can stay out of GitHub.

## Checklists

### Anthidium

- [Possible `Anthidium` species from coastal Santa Barbara County, California](checklists/anthidium/coastal-santa-barbara-county.md)

### Broad Sphecidae / spheciform wasps

- [Working California broad-Sphecidae scope with Dangermond and Eastern Sierra flags](checklists/broad-sphecidae/eastern-sierra-and-dangermond-scope.md)

### Bembicidae

- [Eastern Sierra Bembicidae working list](checklists/bembicidae/eastern-sierra-working-list.md)
- [Checklist of California `Bembix` species](checklists/bembicidae/california-bembix.md)

## Keys

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
