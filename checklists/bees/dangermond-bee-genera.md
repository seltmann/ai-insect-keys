# Working list: bee genera findable at Dangermond Preserve

Last updated: 2026-08-14

## Scope

This is a first-pass bee-genera project for the Jack and Laura Dangermond
Preserve, based on GBIF occurrence records and the two local bee references
listed below.

Occurrence tiers:

- `Expected`: genus-resolved GBIF bee-family records in the tight preserve
  bounding box.
- `Nearby candidate`: genus-resolved GBIF bee-family records in the broader
  mainland context box, but no genus-resolved record in the tight preserve box.

Spatial filters:

- Tight preserve box: `POLYGON((-120.50739455434 34.4366467326054,
  -120.354177720553 34.4366467326054, -120.354177720553 34.5801262497771,
  -120.50739455434 34.5801262497771, -120.50739455434 34.4366467326054))`.
  This follows the public Dangermond LiDAR dataset extent from OpenTopography.
- Broader mainland context box: `POLYGON((-120.85 34.25, -119.75 34.25,
  -119.75 34.85, -120.85 34.85, -120.85 34.25))`. This is meant to sample
  western and central Santa Barbara mainland context while avoiding Channel
  Islands-only signals.

GBIF filters:

- Bee families queried separately: Apidae, Andrenidae, Colletidae, Halictidae,
  Megachilidae, and Melittidae.
- Filters: `hasCoordinate=true` and `hasGeospatialIssue=false`.
- The tight preserve query found 101 bee-family records, of which 86 were
  genus-resolved. The broader mainland query found 8,709 bee-family records,
  of which 8,637 were genus-resolved after excluding one doubtful non-bee facet.

Taxonomic normalizations applied:

- GBIF `Dialictus` and `Evylaeus` are folded into `Lasioglossum`.
- GBIF `Pyrobombus` is folded into `Bombus`.
- GBIF `Zadontomerus` is folded into `Ceratina`.
- GBIF `Peponapis` and New World `Tetraloniella` are folded into
  `Xenoglossa`, following BeeGenera's treatment of `Peponapis` and former New
  World `Tetraloniella` groups as subgeneric units in `Xenoglossa`.
- GBIF `Xeromelecta` is folded into `Brachymelecta`, following BeeGenera's
  note that `Xeromelecta` was recently synonymized under `Brachymelecta`.
- One doubtful GBIF facet resolving as `Crustacea` under Apidae was excluded.

The full normalized occurrence table is
[`dangermond-bee-gbif-summary.tsv`](dangermond-bee-gbif-summary.tsv), generated
with [`../../tools/fetch_dangermond_bee_gbif.py`](../../tools/fetch_dangermond_bee_gbif.py).

## Expected genera: direct preserve-box records

| Family | Genus | GBIF evidence | Below genus possible from this pass | Key characters for genus recognition |
| --- | --- | --- | --- | --- |
| Andrenidae | `Andrena` | 3 preserve-box records; nearby context 144. | Preserve species signal: `Andrena prunorum`. The books provide subgeneric routes, but species-level confirmation needs an `Andrena` revision or specimen-level key. | Mostly small to medium andreniform bees; females with distinctive velvety facial foveae, often with propodeal scopa and hind-trochanter flocculus; many species have apical tergal hair bands. |
| Apidae | `Anthophora` | 1 preserve-box record; nearby context 124. | Preserve species signal: `Anthophora urbana`; nearby also `A. californica`, `A. curta`, `A. flavocincta`, `A. edwardsii`, and `A. pacifica`. | Robust, hairy anthophoriform bees, often with pale clypeal, scape, or paraocular markings; some have tergal hair bands; nests usually excavated in soil, sometimes with turreted entrances. |
| Apidae | `Apis` | 10 preserve-box records; nearby context 1,470. | `Apis mellifera`; BeeGenera treats this as the only `Apis` species in the North and Central American area. | Honey bees; moderate-sized apiform bees separable locally by hairy eyes plus absence of hind tibial spurs; advanced eusocial, usually nesting in cavities or managed hives. |
| Apidae | `Bombus` | 18 preserve-box records; nearby context 1,370. | Preserve species signals: `B. vosnesenskii`, `B. californicus`, `B. melanopygus`, and `B. caliginosus`; GBIF `Pyrobombus` facets are folded here as subgenus-level signal. | Bumble bees; moderate to very large, bombiform, densely hairy, with black, yellow, red, or white vestiture; mostly eusocial, with some social-parasitic subgroups. |
| Apidae | `Ceratina` | 9 preserve-box records; nearby context 246. | Preserve species signals: `C. acantha`, `C. arizonensis`, and `C. nanula`; GBIF `Zadontomerus` is folded here as subgenus-level signal. | Small carpenter bees; minute to moderate, shiny, slender, sparsely haired, black to weakly blue or green; long glossa and labial palpi; clypeus shaped like a thick inverted T; tibial scopa present; nests in pithy stems. |
| Apidae | `Epeolus` | 1 preserve-box genus record; nearby context 1. | No species-level GBIF facet in this pass. BeeGenera notes a revised New World subgeneric classification, but species identification needs the Epeolus revision. | Small to moderate epeoliform brood parasites of `Colletes`; often patterned with short pale pubescence, but some species are mostly black or have red metasoma; scopa absent. |
| Apidae | `Melissodes` | 2 preserve-box genus records; nearby context 241. | Preserve records were genus-level. Nearby species signals include `M. tepidus`, `M. lupinus`, `M. lustrus`, `M. plumosus`, `M. robustior`, and `M. stearnsi`. | Eucerine bees, small to large, often with pale tergal hair bands; males usually long-antennate; the anteriorly narrowed tegulae are diagnostic but subtle and may require moving hair. |
| Apidae | `Zacosmia` | 1 preserve-box record; nearby context 1. | `Zacosmia maculata`; BeeGenera treats `Zacosmia` as a one-species genus in the area. | Small anthophoriform brood parasite without scopa; metasoma variegated by short appressed gray or brown hair; male flagellum greatly thickened; wings patterned light and dark; parasite of `Anthophora`. |
| Colletidae | `Hylaeus` | 3 preserve-box records; nearby context 200. | Preserve species signal: `Hylaeus mesillae`; nearby also `H. polifolii`, `H. punctatus`, `H. verticalis`, and `H. calvus`. | Minute to small, slender, nearly hairless wasp-like bees; usually black with limited yellow or white facial marks; glossa broadly truncate; females lack an external scopa and transport pollen internally. |
| Halictidae | `Agapostemon` | 2 preserve-box records; nearby context 326. | Preserve species signal: `Agapostemon texanus`. | Moderate to large andreniform sweat bees; head and thorax usually bright green; males usually with strong transverse yellow tergal bands; polylectic soil nesters. |
| Halictidae | `Halictus` | 3 preserve-box records; nearby context 1,187. | Preserve species signal: `Halictus tripartitus`; nearby also `H. ligatus`, `H. farinosus`, and `H. rubicundus`. | Small to rather large andreniform sweat bees; unlike American `Lasioglossum`, both sexes have pale apical tergal hair bands and stronger distal forewing venation. |
| Halictidae | `Lasioglossum` | 25 preserve-box records; nearby context 2,126. | Preserve species signals: `L. incompletum`, `L. knereri`, `L. pavonotum`, and `L. microlepoides`; GBIF `Dialictus` and `Evylaeus` are folded here as subgeneric signals. | Minute to moderate andreniform sweat bees; distal forewing veins weakened; American species lack the pale apical tergal bands typical of `Halictus`; basal tergal tomentum or lateral patches often present. |
| Halictidae | `Sphecodes` | 2 preserve-box records; nearby context 26. | Preserve species signal: `Sphecodes mandibularis`. | Minute to moderate cleptoparasitic halictids; broad head, shiny sparsely haired terga, usually black with metasoma partly or wholly red; tergal hair bands absent, sculpture often coarse. |
| Megachilidae | `Anthidium` | 4 preserve-box records; nearby context 89. | Preserve species signal: `Anthidium palliventre`; nearby also `A. edwardsii`, `A. palmarum`, `A. tenuiflorae`, `A. illustre`, and `A. utahense`. BeeGenera treats native species as `Anthidium` sensu stricto. | Moderate to large, broad, squarish megachilids with extensive yellow markings; female mandibles with multiple close-set teeth; cells made of plant hairs in cavities, soil, stems, stones, or similar spaces. |
| Megachilidae | `Megachile` | 1 preserve-box record; nearby context 137. | Preserve species signal: `Megachile mendica`; nearby species examples include `M. perihirta`, `M. gentilis`, `M. frugalis`, `M. apicalis`, and `M. fidelis`. | Leafcutter and dauber bees; small to large megachiliform bees, usually with pale tergal hair bands; females carry pollen in ventral metasomal scopa; nests use leaf discs, resin, mud, or mixed materials. |
| Megachilidae | `Osmia` | 1 preserve-box genus record; nearby context 150. | Preserve record was genus-level. Nearby examples include `O. tristella`, `O. cyanella`, `O. gabrielis`, `O. aglaia`, `O. nemoris`, and `O. exigua`. | Mason bees; small to moderate megachilids, usually metallic blue or green and usually without strong tergal hair bands; nest in cavities, old nests, snail shells, crevices, soil, sand, or exposed cells. |

## Nearby candidate genera: broader mainland records only

| Family | Genus | GBIF evidence | Below genus possible from this pass | Key characters for genus recognition |
| --- | --- | --- | --- | --- |
| Andrenidae | `Calliopsis` | 6 nearby-context records. | `Calliopsis zonalis`; the books route subgenera such as `Calliopsis`, `Nomadopsis`, and `Hypomacrotera`. | Mainly small, flattened andreniform panurgines; often with yellow integumental tergal bands or hair bands and facial pale marks; male genitalia have greatly enlarged penis valves and essentially absent gonostyli. |
| Andrenidae | `Panurginus` | 18 nearby-context records. | `Panurginus bilobatus`. | Small, slender, black andreniform bees; males often hylaeiform with yellow clypeus; recognized among North American panurgines by the first recurrent vein meeting the first transverse cubital. |
| Andrenidae | `Perdita` | 7 nearby-context records. | `Perdita californica` and `P. interrupta`; most species require specialized `Perdita` keys. | Minute to small andreniform bees, often with extensive yellow or white markings and sometimes metallic blue or green; most are oligolectic; most have the short truncate marginal cell typical of Perditini. |
| Apidae | `Brachymelecta` | 12 nearby-context records after folding GBIF `Xeromelecta`. | `Brachymelecta californica`; GBIF `Xeromelecta californica` folded here. | Melectine brood parasites of `Anthophora`; euceriform but without scopa, head and thorax somewhat hairy, metasoma usually with patches or broken bands of short white hair. |
| Apidae | `Centris` | 1 nearby-context genus record. | No species-level GBIF facet in this pass. | Moderate to very large anthophoriform bees; hind legs have longer, denser hairs than `Anthophora`; many local species are oil collectors, with specialized setal combs on fore- and mid-basitarsi. |
| Apidae | `Diadasia` | 134 nearby-context records. | Examples: `D. bituberculata`, `D. ochracea`, `D. laticauda`, `D. consociata`, `D. nitidifrons`, and `D. enavata`. | Hairy anthophoriform or euceriform bees, often with pale metasomal hair bands; males with T7 ending in two small lobes or points; many are narrow host-plant specialists and gregarious soil nesters. |
| Apidae | `Eucera` | 15 nearby-context records. | Examples: `E. actuosa`, `E. cordleyi`, `E. edwardsii`, and `E. amsinckiae`; BeeGenera treats North American `Eucera` in subgenus `Synhalonia`. | Moderate to large eucerine bees, often spring-active; clypeus strongly protuberant, males with long black antennae, terga often with weak broad pale hair bands. |
| Apidae | `Habropoda` | 12 nearby-context records. | Examples: `H. depressa`, `H. tristissima`, and `H. miserabilis`. | Moderate to large anthophoriform bees resembling `Anthophora`; western North American soil nesters; North and Central American species historically placed in `Emphoropsis`. |
| Apidae | `Melecta` | 4 nearby-context records. | Examples: `M. separata` and `M. edwardsii`. | Large hairy anthophoriform brood parasites without scopa; head, thorax, and base of metasoma hairy; metasoma may have limited patches of short white hair. |
| Apidae | `Nomada` | 17 nearby-context records. | Species facets sparse (`Nomada spec`, `N. tintinnabulum`); BeeGenera notes subgeneric classification is not stable. | Wasp-like brood parasites, minute to large, slender and mostly without conspicuous pubescence; black or red, commonly with yellow or white markings; many temperate species attack `Andrena`. |
| Apidae | `Oreopasites` | 1 nearby-context genus record. | No species-level GBIF facet in this pass. | Minute to small epeoliform brood parasites, usually red metasoma and lacking sharply defined pale hair patches; known hosts include `Calliopsis` and `Perdita`. |
| Apidae | `Townsendiella` | 1 nearby-context record. | `Townsendiella rufiventris`. | Minute to small epeoliform bees, sometimes red, commonly with bands or areas of short white pubescence; brood parasites of `Hesperapis` and probably `Conanthalictus`. |
| Apidae | `Triepeolus` | 6 nearby-context records. | Examples: `T. verbesinae` and `T. melanarius`; BeeGenera notes a revised subgeneric classification and keys. | Moderate to large epeoliform brood parasites with striking bands and spots of short pale pubescence; males can be difficult to separate from `Epeolus`; hosts mostly eucerine bees. |
| Apidae | `Xenoglossa` | 24 nearby-context records after folding GBIF `Peponapis` and New World `Tetraloniella`. | GBIF signals include `Peponapis pruinosa` and `Tetraloniella pomonae`; under BeeGenera, treat these as `Xenoglossa (Peponapis)` and former New World `Tetraloniella` in `Xenoglossa (Xenoglossodes)` pending specimen review. | Small to large, hairy, fast-flying anthophoriform or euceriform bees; many subgroups are narrow specialists, especially `Peponapis` and `Xenoglossa` on `Cucurbita`; subgeneric limits remain challenging. |
| Apidae | `Xylocopa` | 310 nearby-context records. | Examples: `X. tabaniformis`, `X. sonorina`, `X. varipuncta`, `X. micans`, and `X. californica`. | Carpenter bees; large to very large anthophoriform or bombiform bees, often black to metallic; females nest by excavating wood or stems, depending on subgenus. |
| Colletidae | `Colletes` | 57 nearby-context records. | Examples: `C. hyalinus`, `C. slevini`, `C. ochraceus`, `C. angelicus`, and `C. phaceliae`. | Moderately hairy andreniform to apiform colletids with pale tergal hair bands; face tapers below with strongly converging inner eye margins; glossa short and shallowly bilobed; second recurrent vein arcuate distally. |
| Halictidae | `Augochlorella` | 7 nearby-context records. | `Augochlorella pomoniella` and `A. aurata`. | Small bright metallic green, bluish, or brassy andreniform halictids; eusocial in small colonies; uncommon in deserts but otherwise often common. |
| Halictidae | `Conanthalictus` | 20 nearby-context records. | `Conanthalictus nigricans`; Michener places `C. nigricans` in subgenus `Phaceliapis`. | Minute to small rophitine halictids, blackish or greenish, with dull minutely roughened integument; often associated with Hydrophyllaceae. |
| Halictidae | `Dufourea` | 8 nearby-context records. | Examples: `D. sandhouseae`, `D. virgata`, and `D. vernalis`. | Minute to moderate rophitine bees, andreniform to slender andreniform, black to metallic bluish or greenish, sometimes red, and sometimes with pale tergal hair bands; many species are oligolectic. |
| Halictidae | `Micralictoides` | 1 nearby-context record. | `Micralictoides ruficaudus`. | Minute to small rophitine bees, andreniform, sometimes red on metasoma, without tergal hair bands; Southern California/desert-associated oligolectic genus. |
| Megachilidae | `Anthidiellum` | 13 nearby-context records. | `Anthidiellum robertsoni`; BeeGenera places local species in subgenus `Loyolanthidium`. | Small, very robust anthidiine megachilids, black or red with yellow markings; short robust body distinguishes them from other North American anthidiines; resin nests constructed in the open. |
| Megachilidae | `Ashmeadiella` | 19 nearby-context records. | Examples: `A. salviae`, `A. californica`, `A. timberlakei`, and `A. cactorum`. | Minute to small robust osmiines, black or red-metasomal, with pale tergal hair bands; anterior T1 concave and delimited by a carina; males usually with four teeth on T6. |
| Megachilidae | `Atoposmia` | 1 nearby-context record. | `Atoposmia copelandica`. | Small to moderate megachilids, often black but sometimes weakly metallic green; western North American, often montane; some species specialize on `Penstemon` and `Keckiella`. |
| Megachilidae | `Chelostoma` | 3 nearby-context records. | `Chelostoma phaceliae` and `C. incisulum`; BeeGenera treats western North American species as subgenus `Neochelostoma`. | Minute to small, unusually slender heriadiform bees; very weak or absent tergal hair bands; male metasoma only slightly curled under with six exposed sterna; fine sculpture and no basal propodeal pit row. |
| Megachilidae | `Coelioxys` | 1 nearby-context genus record. | No species-level GBIF facet in this pass. | Megachilid brood parasites, small to large; metasoma tapering apically, sharply pointed in females and toothed in males; usually with transverse basal tergal grooves and narrow white hair bands. |
| Megachilidae | `Dianthidium` | 15 nearby-context records. | Examples: `D. ulkei`, `D. subparvum`, and `D. dubium`; BeeGenera provides a subgenus key. | Small to moderate anthidiines, yellow-to-white and black or sometimes red; male T7 curled under with characteristic median and lateral lobes; nests of pebbles and resin on stones, branches, or in soil cavities. |
| Megachilidae | `Hoplitis` | 46 nearby-context records. | Examples: `H. producta`, `H. howardi`, `H. grinnelli`, `H. seminigra`, `H. fulgida`, `H. sambuci`, `H. deserticola`, and `H. cryptanthae`; BeeGenera provides New World subgeneric routes. | Minute to moderate osmiines, heriadiform or megachiliform, often black but sometimes metallic, frequently with pale tergal hair bands; diverse cavity, ground, stem, crack, and exposed nesters. |
| Megachilidae | `Protosmia` | 26 nearby-context records. | `Protosmia rubifloris`; BeeGenera treats this as the only species in the North and Central American area, in subgenus `Chelostomopsis`. | Minute to small heriadiform bees, almost without pale tergal hair bands; resin nests in above-ground cavities, closed pine cones, and nesting blocks. |
| Megachilidae | `Stelis` | 3 nearby-context records. | `Stelis montana` and `S. laticincta`; Michener provides a key to three subgenera. | Megachilid brood parasites, minute to moderate, black or metallic blue/green, with or without yellow or white metasomal markings; parasites of anthidiine, osmiine, and megachiline bees. |
| Megachilidae | `Trachusa` | 9 nearby-context records. | `Trachusa timberlakei`; BeeGenera provides a subgenus key. | Moderate to rather large anthidiines; strong carinae absent except sometimes on pronotal lobe; propodeal foveae and basal pits absent; resin cells in soil burrows. |
| Melittidae | `Hesperapis` | 2 nearby-context records. | `Hesperapis regularis`; subgeneric keys available in Michener and BeeGenera. | Minute to large andreniform melittids, usually with tergal hair bands and flattened soft metasoma; separated from similar `Andrena`, `Halictus`, `Lasioglossum`, and `Colletes` by tibial rather than trochanteral/femoral scopa. |

## Next work

- Pull the individual GBIF occurrence records for all `Expected` genera and
  audit basis of record, dataset, date, uncertainty, and photograph/voucher
  quality.
- Refine the new
  [identification table and working key](../../keys/bees/dangermond-bee-genera-key.md)
  after specimen-level testing.
- Add species- or subgenus-level mini-keys only where the two books provide a
  stable route, beginning with `Lasioglossum`, `Xenoglossa`, `Anthidium`,
  `Bombus`, `Ceratina`, `Hoplitis`, `Osmia`, and `Megachile`.

## References and data sources

GBIF.org occurrence search API. Accessed 2026-08-14. Query facets generated by
`tools/fetch_dangermond_bee_gbif.py` using the family keys and WKT geometries
listed above. https://api.gbif.org/v1/occurrence/search

OpenTopography. `Lidar Survey of Dangermond Preserve, CA`, dataset extent.
Accessed 2026-08-14. https://opentopography.org/meta/OT.042022.32611.1

Griswold, T., and J. S. Ascher. `The Bee Genera of North and Central America`,
2nd ed. Local reference file:
`references/bees/BeeGenera-2ed_VOR.pdf`. Genus accounts and keys used especially
from chapter 12, pp. 136-179.

Michener, C. D. 2007. `The Bees of the World`, 2nd ed. Local reference file:
`references/bees/Michener-2007-Bees-of-the-World.pdf`. Used for world-genera
context and subgeneric routes, especially where BeeGenera notes difficult or
recently changed subgeneric placement.

## Document provenance and AI assistance statement

Prepared on 2026-08-14 as an AI-assisted working checklist scaffold for the
`ai-insect-keys` repository. Codex was used to query and normalize GBIF
occurrence facets, inspect the local bee reference PDFs, reconcile obvious
GBIF/book taxonomy conflicts, and draft this Markdown file. The taxonomic
authorities remain the cited literature, specimen evidence, GBIF source
records, and review by qualified bee taxonomists.
