# Reproducibility

This review is a qualitative, PRISMA 2020-guided synthesis, so there is no model to retrain and no experiment to rerun. "Reproducibility" here means **being able to inspect the evidence behind the article and check the internal consistency of what it reports**. This document states what this package allows a reader to verify, and what it does not.

## 1. What is in the package, by evidence class

The package separates four kinds of information:
1. author-confirmed research methods
2. results and tables reported in the publication
3. original evidence that is available locally
4. information that cannot currently be independently verified

[`../evidence/EVIDENCE_PROVENANCE.md`](../evidence/EVIDENCE_PROVENANCE.md#four-categories-of-information) defines each category. No item in category 4 is presented as verified.

| Class | Files | What a reader can do with it |
|---|---|---|
| **Published-method descriptions** (author-confirmed) | `methodology/*.md` | Read the search strategy, eligibility criteria, quality framework and six-dimension framework as reported, with the source of each statement marked |
| **Original research records** (metadata-only derivatives; partial) | `evidence/original/*` | Inspect the Google Scholar and IEEE identification exports, the **historical, partial** Zotero screening records and the original extraction matrices, and compare their counts with the reported counts |
| **Published-table transcriptions** | `evidence/published_transcriptions/*`, `analysis/quality_scores.csv` | Check Table 2, Figure 1, Table 4, Table 5, Table 6 and Table 7 values and their arithmetic |
| **Derived comparison tables** | `analysis/primary_studies.csv`, `analysis/comparison_matrix.csv` | See how each of the 24 studies links to its DOI, search export, screening record, extraction row and published characteristics, with a verification status per row |
| **Missing historical records** | listed in [`../evidence/EVIDENCE_PROVENANCE.md`](../evidence/EVIDENCE_PROVENANCE.md#missing-records) | See what cannot be checked |

## 2. Automated checks

Run from the repository root (Python 3.8+, standard library only):

```bash
python reproducibility/verify_package.py
```

The script runs these checks:

- **Included studies:** exactly 24 studies, each appearing once with a unique reference number, consistent across `quality_scores.csv`, `primary_studies.csv`, `comparison_matrix.csv` and the Table 7 transcription.
- **Quality-score arithmetic:** every Q1–Q5 score is an integer from 0 to 2; every total equals the sum of the five scores; every included study scores at least 5; the distribution is 20 strong and 4 moderate (matching Table 4); and the Table 5 totals equal the Table 7 QS column.
- **Reported counts:** the Figure 1 PRISMA counts are internally consistent; the Table 2 databases sum to 5,127; the Google Scholar intervals sum to 4,045.
- **Original records against reported counts:** the script recounts the original-record derivatives and reports where they agree with the reported counts (IEEE Xplore: 244) and where they do not (Google Scholar: 4,882 against 4,045; the Zotero collection counts against the PRISMA stages). These differences are reported as information, not as failures, because they describe the evidence rather than errors in the package.

## 3. Manual checks for the 24 included studies

1. Open [`../analysis/primary_studies.csv`](../analysis/primary_studies.csv).
2. For each row, resolve the `doi` at `https://doi.org/<doi>` and compare the title with the `title` and `published_reference` columns.
   - 21 DOIs were verified against both the published reference link and the DOI printed in the full text held by the authors.
   - Reference [34] has a DOI from the published reference only.
   - References [25] and [49] have no DOI in the published reference list.
3. Compare the Q1–Q5 values in [`../analysis/quality_scores.csv`](../analysis/quality_scores.csv) with Table 5 of the article, and the characteristics in [`../analysis/comparison_matrix.csv`](../analysis/comparison_matrix.csv) with Table 7.
4. Read the `evidence_status` and `notes` columns to see which studies are fully traced to original search and screening records and which are not.

## 4. What cannot be reproduced

- **The 5,127-record identification.** Only the Google Scholar (4,882 records) and IEEE Xplore (244 records) exports exist. The exports for the other six databases (838 reported records) are not in the archive. The reported Google Scholar total of 4,045 cannot be derived from the exports.
- **The reported PRISMA stages** (3,411 duplicates; 1,710 / 376 / 85 / 34 records). The original Zotero screening collections hold 1,357 / 67 / 52 / 31 records (17 excluded). They do not correspond to the reported stages and record no exclusion reasons. They are provided as **historical, partial screening evidence**, so that readers can see what was recorded, not as a reconstruction of the reported flow. [`../methodology/STUDY_SELECTION.md`](../methodology/STUDY_SELECTION.md) sets the two side by side.
- **The quality assessment itself.** No original scoring worksheet exists. The scores can be checked for arithmetic consistency only, not re-derived. The 10 excluded candidates cannot be identified.
- **Reference [34].** Myrzashova et al. (2023) is the final included study (author-confirmed). However:
  - Its published quality score (9) is transcribed but NOT VERIFIED.
  - All its study-specific characteristics are marked NOT VERIFIED in `analysis/comparison_matrix.csv`, because the published Table 7 entries for [34] coincide with records of the study it replaced, Wang et al. (2026), and no record or full text of Myrzashova et al. is available locally.
  - The published Table 7 entries are kept unchanged in the Table 7 transcription.
  
  See [`../methodology/QUALITY_ASSESSMENT.md`](../methodology/QUALITY_ASSESSMENT.md#4-provenance-and-limitations).
- **Characteristic checks for other studies.** For the 23 studies with local full texts, `comparison_matrix.csv` reports indicative exact-string checks of the published dataset and method terms against the original extraction row and the full text. A low match count does not indicate an error: the published table often paraphrases.
- **Full texts.** These are not redistributed for copyright reasons. Readers can obtain the studies through the DOIs.

## 5. Recomputing the original-record counts yourself

Each derivative CSV keeps one row per original record, so the counts can be recomputed with any spreadsheet tool or a few lines of code. For example:

```python
import csv, collections
rows = list(csv.DictReader(open("evidence/original/google_scholar_exports_metadata.csv", encoding="utf-8")))
print(collections.Counter(r["source_file"] for r in rows))   # records per Google Scholar export
```

The SHA-256 checksums of the source files these derivatives were produced from are in [`../evidence/original/SOURCE_MANIFEST.csv`](../evidence/original/SOURCE_MANIFEST.csv).
