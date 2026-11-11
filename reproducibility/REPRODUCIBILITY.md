# Reproducibility

This review is a qualitative, PRISMA 2020-guided synthesis, so there is no model to retrain and no experiment to rerun. "Reproducibility" here means **being able to inspect the evidence behind the article and check the internal consistency of what it reports**. This document states what this repository allows a reader to verify, and what it does not.

## 1. What is in the repository, by file class

[`../evidence/EVIDENCE_PROVENANCE.md`](../evidence/EVIDENCE_PROVENANCE.md#four-categories-of-information) defines the four categories of information used in this repository and the [file classes](../evidence/EVIDENCE_PROVENANCE.md#file-classes) below. No item in category 4 is presented as verified.

| Class | Files | What a reader can do with it |
|---|---|---|
| **Methodology documents** | `methodology/*.md` | Read the published methodological descriptions alongside the archived evidence and repository-level comparisons, with their sources and limitations documented |
| **Original record (derivative)** (metadata only; partial) | `evidence/original/*` | Inspect the Google Scholar and IEEE identification exports, the **historical, partial** Zotero screening records and the original extraction matrices, and compare their counts with the reported counts |
| **Published transcription** | `evidence/published_transcriptions/*`, `analysis/quality_scores.csv` | Check Table 2, Figure 1, Table 4, Table 5, Table 6 and Table 7 values and their arithmetic |
| **Derived table** | `analysis/primary_studies.csv`, `analysis/comparison_matrix.csv` | See how each of the 24 studies links to its DOI, search export, screening record, extraction row and published characteristics, with a verification status per row |
| **Missing record** | listed in [`../evidence/EVIDENCE_PROVENANCE.md`](../evidence/EVIDENCE_PROVENANCE.md#missing-records) | See what cannot be checked |

## 2. Automated checks

Run from the repository root (Python 3.8+, standard library only):

```bash
python reproducibility/verify_package.py
```

The script runs 24 pass/fail checks and prints 5 information lines:

- **Included studies (8 checks):** `quality_scores.csv` has exactly 24 studies, each reference number appears once and the study IDs S01–S24 are unique; `primary_studies.csv`, `comparison_matrix.csv` and the Table 7 transcription cover the same 24 reference numbers; and the study ID–reference pairs in `primary_studies.csv` and `comparison_matrix.csv` match `quality_scores.csv`.
- **Quality-score arithmetic (7 checks):** every Q1–Q5 score is an integer from 0 to 2; every total equals the sum of the five scores; every included study scores at least 5; the distribution is 20 strong and 4 moderate and matches the Table 4 transcription (34 assessed); the Table 5 totals equal the Table 7 QS column; and all 24 decisions are "Included".
- **Reference [34] (4 checks):** [34] is listed as Myrzashova et al. in `quality_scores.csv` and `comparison_matrix.csv`; its study-specific fields in `comparison_matrix.csv` are marked NOT VERIFIED; its published score (9) is retained with a NOT VERIFIED source note; and its Table 7 transcription is kept as printed.
- **Screening-record labels (1 check):** every row of `zotero_screening_collections.csv` carries the historical, partial screening record label.
- **Reported counts (4 checks):** Table 2 lists eight databases, which sum to the reported 5,127; the Google Scholar intervals sum to 4,045; and the Figure 1 PRISMA counts are internally consistent.
- **Original records against reported counts (5 information lines):** the script recounts the original-record derivatives and reports where they agree with the reported counts (IEEE Xplore: 244) and where they do not (Google Scholar: 4,882 against 4,045; the Zotero collection counts against the PRISMA stages). It also notes that no exports are held for the six other databases and summarises the evidence status of the 24 studies. These differences are reported as information, not as failures, because they describe the evidence rather than errors in the repository.

## 3. Manual checks for the 24 included studies

1. Open [`../analysis/primary_studies.csv`](../analysis/primary_studies.csv).
2. For each row, resolve the `doi` at `https://doi.org/<doi>` and compare the title with the `title` and `published_reference` columns.
   - 21 DOIs were verified against both the published reference link and the DOI printed in the full text held by the authors.
   - Reference [34] has a DOI from the published reference only.
   - References [25] and [49] have no DOI in the published reference list.
3. Compare the Q1–Q5 values in [`../analysis/quality_scores.csv`](../analysis/quality_scores.csv) with Table 5 of the article, and the characteristics in [`../analysis/comparison_matrix.csv`](../analysis/comparison_matrix.csv) with Table 7.
4. Read the `evidence_status` and `notes` columns to see which studies are fully traced to original search and screening records and which are not.

## 4. What cannot be reproduced

- **The 5,127-record identification.** Of the eight database searches, only the Google Scholar (4,882 records) and IEEE Xplore (244 records) exports are held in the inspected archive; none are held for the other six databases (838 reported records). The reported Google Scholar total of 4,045 cannot be derived from the held exports. See [`../methodology/SEARCH_STRATEGY.md` §3](../methodology/SEARCH_STRATEGY.md#3-google-scholar-reported-versus-held).
- **The reported PRISMA stages** (3,411 duplicates; 1,710 / 376 / 85 / 34 records). The held Zotero screening collections (1,357 / 67 / 52 / 31 records; 17 excluded) do not correspond to these stages and record no exclusion reasons. They are provided as **historical, partial screening evidence**, not as a reconstruction of the reported flow. See [`../methodology/STUDY_SELECTION.md` §3](../methodology/STUDY_SELECTION.md#3-original-screening-records-held-in-the-archive-historical-and-partial).
- **The quality assessment itself.** No original per-criterion scoring worksheet is held in the inspected archive. The published scores can be checked for arithmetic consistency, but the assessment cannot be independently reconstructed or re-derived. The 10 excluded candidates cannot be identified.
- **Reference [34].** The published article identifies [34] as Myrzashova et al. (2023), and its published quality score of 9 is preserved as printed. Because the published entries for [34] coincide with records of Wang et al. (2026), and no record or full text of Myrzashova et al. is held, the attribution of the score and all study-specific characteristics remain NOT VERIFIED; no resolution is inferred. The published Table 7 entries are kept unchanged in the Table 7 transcription. See [`../methodology/QUALITY_ASSESSMENT.md` §4](../methodology/QUALITY_ASSESSMENT.md#4-provenance-and-limitations).
- **Characteristic checks for other studies.** Local full texts are held for 23 studies, of which 21 have a corresponding original extraction row. For these 21, `comparison_matrix.csv` reports indicative exact-string checks of the published dataset and method terms against the extraction row and the full text. Ahmed et al. [3] and Areia et al. [50] have no original extraction row, so their checks rely on the full text only. A low match count does not indicate an error: the published table often paraphrases.
- **Full texts.** These are not redistributed for copyright reasons. Readers can obtain the studies through the DOIs.

## 5. Recomputing the original-record counts yourself

Each derivative CSV keeps one row per original record, so the counts can be recomputed with any spreadsheet tool or a few lines of code. For example:

```python
import csv, collections
rows = list(csv.DictReader(open("evidence/original/google_scholar_exports_metadata.csv", encoding="utf-8")))
print(collections.Counter(r["source_file"] for r in rows))   # records per Google Scholar export
```

The SHA-256 checksums of the source files these derivatives were produced from are in [`../evidence/original/SOURCE_MANIFEST.csv`](../evidence/original/SOURCE_MANIFEST.csv).
