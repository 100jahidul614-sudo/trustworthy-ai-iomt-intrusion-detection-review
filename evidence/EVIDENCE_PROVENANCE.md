# Evidence provenance

## Four categories of information

| Category | What it covers | Where it appears |
|---|---|---|
| **1. Author-confirmed research methods** | The eight-database search, the eligibility criteria, the five-criterion quality framework and the six analytical dimensions, as described in the article and confirmed by the authors. The authors also confirm that Myrzashova et al. (2023) replaced Wang et al. (2026) in the final selection. | `methodology/` |
| **2. Results and tables reported in the publication** | The PRISMA counts, Table 2 retrieval counts, the 24 included studies, Table 5 quality scores, and Table 6 and Table 7 entries, transcribed exactly as published | `evidence/published_transcriptions/`, `analysis/quality_scores.csv` |
| **3. Original, locally available evidence** | Metadata from the Google Scholar and IEEE Xplore exports, historical partial Zotero screening records, and the original extraction matrices | `evidence/original/` |
| **4. Information that cannot currently be independently verified** | Searches of the six other databases, the derivation of the Google Scholar count, the PRISMA stage records, the original quality scores, and the study-specific characteristics of [34] | Marked **NOT VERIFIED** in `analysis/` and listed under [Missing records](#missing-records) |

## File classes

Every data file in this repository belongs to one of four classes:

| Class | Location | Meaning |
|---|---|---|
| **Original record (derivative)** | `evidence/original/` | Derived from a file in the authors' research archive. Metadata only (no abstracts, no full text), or verbatim cell text from the authors' own extraction workbooks. |
| **Published transcription** | `evidence/published_transcriptions/`, `analysis/quality_scores.csv` | Values transcribed from the published article, *Sensors* 2026, 26, 5182 (CC BY 4.0). These reflect what the article reports; they are not independent evidence. |
| **Derived table** | `analysis/primary_studies.csv`, `analysis/comparison_matrix.csv` | Combines published transcriptions with cross-references to the original records. Each row states its source and verification status. |
| **Missing record** | listed below | Required to reproduce the reported workflow, but not present in the research archive. Nothing has been reconstructed. |

SHA-256 checksums of every source file, record counts and the exact derivation rules are in [`original/SOURCE_MANIFEST.csv`](original/SOURCE_MANIFEST.csv).

## Original-record derivatives

| File | Source in the research archive | Records | Fields kept | Removed |
|---|---|---|---|---|
| `google_scholar_exports_metadata.csv` | Five Google Scholar RIS exports, saved 2–3 June 2026 | 4,882 | Year window, RIS type, title, authors, year, source title, publisher, DOI | Abstracts, citation-count notes, URLs |
| `ieee_xplore_export_metadata.csv` | IEEE Xplore CSV export, 2021–2026, saved 3 June 2026 | 244 | Title, authors, year, publication title, DOI, document type | Abstracts, affiliations, keywords, funding, URLs, licence fields |
| `zotero_screening_collections.csv` | Zotero library collections: Initial Search, Title Screening, IoMT IDS Candidates, Abstract Screening, Final Papers, Excluded Papers. **Historical, partial screening record; it does not reproduce the published PRISMA flow** (see `methodology/STUDY_SELECTION.md` §3). | 1,533 rows (1,357 / 67 / 9 / 52 / 31 / 17) | `record_status` label (added by this package), collection, Zotero item key, item type, first author, year, title, publication, DOI, catalogue, date added (UTC) | Notes, tags, attachments, file paths, all other library content |
| `zotero_export_376_metadata.csv` | Zotero CSV export of a 376-item set, 4 June 2026. Historical record; it cannot be shown to be the PRISMA "376 sought for retrieval" stage. | 376 | Zotero key, item type, title, authors, year, publication, DOI, catalogue, date added | Abstracts, tags, notes, URLs, attachment paths |
| `extraction_primary_original.csv` | *Final analysis file for all the papers.xlsx*, Sheet2 (last saved 1 July 2026) | 24 | All original columns verbatim, plus two columns added by this package: `publication_status` and `inline_marker_note` | none |
| `extraction_supporting_original.csv` | Same workbook, Sheet1 (supporting literature) | 116 | All columns verbatim | none |

### Notes on the original extraction matrices

- **Pre-publication snapshot.** Sheet2 records the 24 primary studies as they stood on 1 July 2026. Twenty-one rows match published primary studies (identity confirmed by DOI or title in the local full text). Three rows do not:
  - Iseal et al. and Titoriya & Prasad Singh were removed from the included set during revision. They were replaced by Ahmed et al. [3] and Areia et al. [50], which have no extraction rows.
  - The row for Wang et al. (2026) corresponds to the slot that the published article assigns to Myrzashova et al. [34]. That row is **not** copied into any Myrzashova record.
- **Supporting sheet.** Sheet1 lists 116 entries, including one author-year label ("Rani et al. (2023)") that appears twice for two different papers. It does not map one-to-one onto the 115 supporting references in the published reference list.
- **Duplicate workbooks.** *main 24 papers.xlsx* is identical (columns B–I) to Sheet2. *rest 25.xlsx* and *rest 25 (Autosaved).xlsx* each contain 24 rows duplicated from Sheet1. None of these is exported separately.
- **Verbatim text and inline markers.** Cell text is reproduced exactly as recorded, with no scientific content altered. Three Sheet2 rows contain 39 inline markers of the form `[cite: N]`, with N between 14 and 2,344:
  - Wang et al., 17 markers
  - Khurana et al. (Eds.), 8 markers
  - Singhal et al., 14 markers, one of them in the citation cell
  
  These markers are retained unaltered and flagged in the `inline_marker_note` column. They are **not references**: they do not resolve to any source in the archive, have not been verified, and their origin is not documented. They should not be read as citations supporting the cell text. The Wang et al. row is not one of the published 24 studies.
- **Exploratory matrix.** An early exploratory matrix (*IoMT Extended review metrix table.xlsx*, 1–8 June 2026, 8 rows in each of two sheets) is listed in the manifest for completeness. Its text was not used for the published tables and is not exported.

## Published transcriptions

| File | Published source |
|---|---|
| `table2_search_strategy.csv` | Table 2: databases, dates, filters, methods, records |
| `google_scholar_intervals_reported.csv` | Section 2.1: Google Scholar interval counts |
| `figure1_prisma_counts.csv` | Figure 1: PRISMA counts |
| `table4_quality_distribution.csv` | Table 4: quality score distribution |
| `../analysis/quality_scores.csv` | Table 5: study-level quality scores |
| `table6_thematic_classification.csv` | Table 6: thematic classification, as printed (including "Wang et al. [34]") |
| `table7_study_characteristics.csv` | Table 7: study characteristics, as printed |

Transcriptions reproduce the published values exactly, including values flagged elsewhere as inconsistent. Table 7 was extracted from the article PDF by cell position and checked row by row against the printed table.

## Missing records

These records would be needed to reproduce the reported search and selection, but they are not in the research archive:

1. Search exports or search histories for Scopus, Web of Science, ACM Digital Library, ScienceDirect, SpringerLink and PubMed (reported dates 5–7 June 2026; 838 records in total).
2. Any intermediate file deriving the reported Google Scholar counts (798 / 810 / 817 / 813 / 807; total 4,045) from the exports (4,882 records).
3. A deduplication log supporting 3,411 duplicates removed and 6 non-English records removed.
4. Record lists for the reported stages: 1,710 screened; 376 sought for retrieval; 85 full-text assessed; 34 quality-assessed.
5. Exclusion reasons at any stage, and the identities of the 10 candidates excluded at quality assessment.
6. Original per-criterion quality scores, reviewer-level scoring and records of co-author verification.
7. Any search, screening, extraction, scoring or full-text record for Myrzashova et al. (2023) [34]. Its study-specific characteristics are therefore marked NOT VERIFIED in `analysis/comparison_matrix.csv`.
8. Extraction rows for Ahmed et al. [3] and Areia et al. [50].
9. Data underlying the qualitative radar-style Figures 4 and 7. The article describes these figures as non-quantitative.
