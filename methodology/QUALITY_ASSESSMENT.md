# Methodological quality assessment

Source: Section 2.2 and Tables 4–5 of *Sensors* 2026, 26, 5182 (CC BY 4.0); for reference [34], also Tables 6–7 and the reference list.

## 1. Framework (reported)

Quality assessment was the final selection stage. It was applied to the 34 candidates that passed full-text eligibility screening.

| Code | Criterion | Scale |
|---|---|---|
| Q1 | Relevance to IoMT intrusion detection and healthcare cybersecurity | 0–2 |
| Q2 | Methodological transparency and reproducibility | 0–2 |
| Q3 | Dataset description and evaluation reporting | 0–2 |
| Q4 | Experimental or comparative validation | 0–2 |
| Q5 | Contribution to explainability, privacy preservation, deployment readiness, or broader healthcare cybersecurity | 0–2 |

- **Scoring:** 0 = insufficient evidence; 1 = partial fulfilment; 2 = strong fulfilment.
- **Maximum score:** 10.
- **Inclusion threshold:** a total of **5 or higher**. Studies scoring below 5 were excluded for insufficient methodological rigour, limited technical relevance or inadequate experimental reporting.

## 2. Reported distribution (Table 4)

| Score range | Count | Interpretation (as published) |
|---|---|---|
| 8–10 | 20 | Strong methodological quality and high relevance to IoMT IDS research |
| 5–7 | 4 | Moderate methodological quality with clear relevance to healthcare cybersecurity |
| 0–4 | 10 | Insufficient methodological rigor or relevance; excluded from the primary synthesis |
| **Total assessed** | **34** | |

The article explains that the high concentration of scores reflects the sequential selection process: only studies that had already passed relevance and full-text screening were scored.

## 3. Published study-level scores (Table 5)

[`../analysis/quality_scores.csv`](../analysis/quality_scores.csv) is a **transcription of published Table 5**. It is not a recovered original scoring worksheet.

| ID | Study [ref] | Year | Q1 | Q2 | Q3 | Q4 | Q5 | Total |
|---|---|---|---|---|---|---|---|---|
| S01 | Siqueira et al. [23] | 2025 | 2 | 2 | 2 | 2 | 2 | 10 |
| S02 | Naghib et al. [22] | 2025 | 2 | 2 | 2 | 2 | 2 | 10 |
| S03 | Szczepaniuk and Szczepaniuk [35] | 2023 | 1 | 2 | 1 | 1 | 2 | 7 |
| S04 | Almotiri et al. [30] | 2025 | 2 | 2 | 2 | 2 | 1 | 9 |
| S05 | Islam et al. [43] | 2024 | 1 | 2 | 1 | 1 | 1 | 6 |
| S06 | Harshith et al. [44] | 2026 | 2 | 2 | 2 | 2 | 1 | 9 |
| S07 | El Khatib et al. [45] | 2023 | 1 | 2 | 1 | 1 | 2 | 7 |
| S08 | Ahmed et al. [3] | 2024 | 2 | 2 | 0 | 2 | 2 | 8 |
| S09 | Bensaid et al. [46] | 2024 | 2 | 2 | 2 | 2 | 2 | 10 |
| S10 | Zubair et al. [47] | 2022 | 2 | 2 | 2 | 2 | 1 | 9 |
| S11 | Myrzashova et al. [34] | 2023 | 2 | 2 | 2 | 1 | 2 | 9 |
| S12 | Mohammadi et al. [25] | 2024 | 2 | 2 | 2 | 2 | 1 | 9 |
| S13 | Akram et al. [48] | 2021 | 2 | 2 | 2 | 2 | 2 | 10 |
| S14 | Khurana et al. [49] | 2024 | 1 | 2 | 1 | 1 | 1 | 6 |
| S15 | Singhal et al. [2] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |
| S16 | Areia et al. [50] | 2024 | 2 | 2 | 2 | 1 | 1 | 8 |
| S17 | Adohinzin and Harrath [24] | 2026 | 2 | 2 | 2 | 2 | 2 | 10 |
| S18 | Abreu et al. [51] | 2024 | 1 | 2 | 2 | 2 | 1 | 8 |
| S19 | Villafranca et al. [52] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |
| S20 | Trivedi et al. [5] | 2025 | 2 | 2 | 2 | 2 | 2 | 10 |
| S21 | Pinto et al. [31] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |
| S22 | Makris et al. [32] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |
| S23 | Matthew et al. [1] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |
| S24 | Mulo et al. [29] | 2025 | 2 | 2 | 2 | 1 | 2 | 9 |

Arithmetic checks, run by [`../reproducibility/verify_package.py`](../reproducibility/verify_package.py):
- Every score is an integer from 0 to 2.
- Every total equals Q1 + Q2 + Q3 + Q4 + Q5.
- Every included study scores at least 5.
- The distribution is 20 strong (8–10) and 4 moderate (5–7), matching Table 4.
- The totals equal the QS column of published Table 7.

## 4. Provenance and limitations

- **Original scoring records.** No original per-criterion scoring worksheet, reviewer-level scoring record or record of co-author verification is held in the inspected research archive. Study-level scores are present in Table 5 of the pre-publication revised manuscript and of the published article. These manuscript tables report assessment outcomes but are not substitutes for original scoring records. The revised manuscript labels the study at reference [34] as Wang et al. (2026), whereas the published Table 5 labels it Myrzashova et al. (2023) (see below). The scores presented here are transcribed from the published article.
- **Excluded candidates.** The 10 candidates excluded at quality assessment, and their scores, are not recorded in the archive and are not listed here.
- **Reference [34]: Myrzashova et al. (2023), final included study.** The authors confirm that this study replaced an earlier candidate, Wang et al. (2026), in the final selection. Its published score of 9 is transcribed in `quality_scores.csv` as a published value, marked **NOT VERIFIED**. In `analysis/comparison_matrix.csv` all of its study-specific characteristics are marked **NOT VERIFIED**; the published Table 7 entries are kept unchanged only in the Table 7 transcription. The following points are noted:
  - The published reference-list entry [34] is Myrzashova et al. (2023), *IEEE Internet of Things Journal*, and published Table 5 identifies [34] as Myrzashova et al. (2023).
  - Table 5 of the pre-publication revised manuscript identifies [34] as Wang et al. (2026), with the same scores (2-2-2-1-2 = 9) as published for Myrzashova et al.
  - The published Table 7 characteristics for [34] (BraTS 2020, Pima and CC-19 datasets; BCFL, HE, SMPC and PBFT) match the full text and original extraction row of Wang et al. (2026).
  - Published Table 6 lists "Wang et al. [34]" under "Federated Learning and Privacy-Preserving IDS" and "Myrzashova et al. [34]" under "Blockchain-Assisted Healthcare Security".

  No local search, screening, extraction or scoring record for Myrzashova et al. (2023) is held in the inspected research archive, and its full text is not held, so its published score could not be independently checked. The value is transcribed exactly as published and flagged. It has not been altered.
- **Reference [49].** This reference cites a complete proceedings volume, *Machine Learning Algorithms: ICMLA 2024* (editors Khurana et al.). The Zotero screening records hold one chapter from that volume (Goel et al.). It is not stated which item the score assesses.
- **Labelling.** Table 5 prints "Almotiri et al." for reference [30], which has a single author. The label is transcribed as printed.
