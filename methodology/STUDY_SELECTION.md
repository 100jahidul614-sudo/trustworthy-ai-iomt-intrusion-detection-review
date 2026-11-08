# Study selection

Source: Section 2.1, Table 3 and Figure 1 of *Sensors* 2026, 26, 5182 (CC BY 4.0), together with the original screening records held in the research archive. No screening decision, exclusion reason or stage count has been reconstructed for this repository.

## 1. Eligibility criteria (reported, Table 3)

| Category | Inclusion | Exclusion |
|---|---|---|
| Domain | IoMT, healthcare cybersecurity, RPM, medical device security, or healthcare network protection | Unrelated to healthcare, IoMT, cybersecurity, or digital health technologies |
| Technology | AI, ML, DL, FL, blockchain, XAI, or intelligent security frameworks | Solely clinical diagnosis or healthcare management without cybersecurity relevance |
| Security focus | Intrusion detection, anomaly detection, threat intelligence, privacy preservation, authentication, trust management, or secure healthcare communication | Unrelated to cyber defence, privacy protection, or attack detection |
| Research contribution | IDS architectures, security frameworks, benchmarking analyses, healthcare threat models, or security evaluation methodologies | No clear security contribution or technical evaluation |
| Publication type | Peer-reviewed journal articles and conference papers | Editorials, patents, theses, short communications, and non-peer-reviewed publications |
| Publication period | 2021–2026 | Outside the selected period |
| Study quality | Sufficient methodological or experimental detail | Insufficient methodological or technical information |
| Language | English | Non-English |

## 2. Reported selection process

The article describes four sequential stages:
1. Duplicate removal across the eight databases using Zotero's duplicate detection.
2. Title and abstract screening.
3. Full-text eligibility assessment.
4. Structured quality assessment (see [`QUALITY_ASSESSMENT.md`](QUALITY_ASSESSMENT.md)).

The article reports that title and abstract screening was performed by the first author, and that full-text eligibility and quality evaluation were independently verified by the co-authors.

**Reported PRISMA counts (Figure 1):**

| Stage | Reported n |
|---|---|
| Records identified (eight databases) | 5,127 |
| Duplicates removed / non-English removed | 3,411 / 6 |
| Records screened | 1,710 |
| Excluded after title and abstract keyword screening | 1,334 |
| Reports sought for retrieval screening | 376 |
| Excluded after IoMT and RPM relevance screening | 291 |
| Full-text articles assessed for eligibility | 85 |
| Excluded after full-text review | 51 |
| Candidates after full-text screening (quality-assessed) | 34 |
| Excluded at quality / critical relevance assessment | 10 |
| **Studies included** | **24** |

The reported counts are internally consistent: each stage equals the previous stage minus its exclusions. A machine-readable transcription is in [`../evidence/published_transcriptions/figure1_prisma_counts.csv`](../evidence/published_transcriptions/figure1_prisma_counts.csv).

## 3. Original screening records held in the archive (historical and partial)

The records below are **historical, partial screening evidence**. They do not reproduce the published PRISMA flow, and they are not presented as doing so.

| Published PRISMA stage (reported) | n | Closest original record available | n |
|---|---|---|---|
| Records after duplicate and language removal (screened) | 1,710 | Zotero "Initial Search" collection | 1,357 |
| Reports sought for retrieval | 376 | Zotero export of a 376-item set (see below); Zotero "Title Screening" collection | 376; 67 |
| Full-text articles assessed | 85 | Zotero "Abstract Screening" collection | 52 |
| Candidates quality-assessed | 34 | Zotero "Final Papers" collection | 31 |
| Excluded at quality assessment | 10 | none (the Zotero "Excluded Papers" collection, 17 items, records no stage or reason) | — |
| Included | 24 | Published Table 5 (no original selection record) | 24 |

The pairings in this table are approximate and show only the nearest available record; the original records do not label which PRISMA stage they belong to.

| Record | Content | File |
|---|---|---|
| Zotero collections (created 3–4 June 2026) | Initial Search **1,357**; Title Screening **67** (with a 9-item "IoMT IDS Candidates" sub-collection); Abstract Screening **52**; Final Papers **31**; Excluded Papers **17**. Zotero records 4,096 merged duplicate items in the library. Every row is labelled `record_status = Historical partial screening record`. | [`zotero_screening_collections.csv`](../evidence/original/zotero_screening_collections.csv) |
| Zotero export of a 376-item set (4 June 2026) | 376 items, mostly from the Google Scholar and IEEE imports | [`zotero_export_376_metadata.csv`](../evidence/original/zotero_export_376_metadata.csv) |

What these records do and do not show:
- **Counts:** the Zotero collection counts (1,357 / 67 / 52 / 31) do not correspond to the reported PRISMA stage counts (1,710 / 376 / 85 / 34).
- **Collection structure:** the collections are not strictly nested. For example, only 9 of the 52 Abstract Screening items are also in Title Screening. Abstract Screening equals Final Papers (31) plus Excluded Papers (17) plus 4 unassigned items.
- **The 376-item export:** its size matches the reported "reports sought for retrieval" count. However, 367 of its 376 Zotero items were later merged as duplicates, only 5 of its items appear in the Title Screening collection, and it contains 2 of the 24 included studies. It therefore cannot be shown to be the PRISMA stage of that name.
- **Exclusion reasons:** none are recorded, at any stage.
- **Timing:** the screening collections and the 376-item export were all created by 4 June 2026. The article reports search dates of 5–7 June 2026 for six databases, and the archive contains no record of how records from those databases entered screening.
- **Not held:** the 85 full-text assessments, the list of 34 quality-assessed candidates, and the 10 exclusions.

## 4. How each included study is documented

[`../analysis/primary_studies.csv`](../analysis/primary_studies.csv) gives, for each of the 24 published studies, its original search source, its screening record, its original extraction row and its full-text availability. In summary:

| Evidence status | Studies |
|---|---|
| Present in a June 2026 search export **and** in the Zotero Final Papers collection **and** with an extraction row | 8 (S01, S03, S05, S07, S09, S10, S12, S13) |
| In the Zotero Final Papers collection with an extraction row, but no June 2026 search-export record (library item imported 30 March 2026, before the review searches) | 2 (S06, S15) |
| Present in a June 2026 search export but with no screening-collection record | 7 (S02, S04, S16, S17, S19, S21, S22) |
| No record in any June 2026 search export or screening collection | 5 (S08, S18, S20, S23, S24) |
| Conflicting record | 2: S11 (reference [34]; see [`QUALITY_ASSESSMENT.md`](QUALITY_ASSESSMENT.md)) and S14 (reference [49] cites a whole proceedings volume, while the screened item was one chapter within it) |

These statements describe the local archive only. They do not establish how studies were selected in practice, and they are not a substitute for the authors' account.
