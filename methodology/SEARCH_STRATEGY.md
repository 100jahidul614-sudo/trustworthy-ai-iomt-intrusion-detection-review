# Search strategy

Source: Section 2.1 and Table 2 of Islam, Datta and Akhter, *Sensors* 2026, 26, 5182 (CC BY 4.0). The status labels in this document mean:

| Label | Meaning |
|---|---|
| **Reported** | Stated in the published article |
| **Author-confirmed** | Confirmed by the authors for this repository |
| **Original record** | An original search export is held in the research archive and is provided here as a metadata-only derivative |
| **Not recoverable** | No original record is held in the local research archive |

## 1. Scope and search string (reported)

- **Period:** studies published 2021–2026, English language.
- **Databases (reported; author-confirmed):** IEEE Xplore, Google Scholar, Scopus, Web of Science, ACM Digital Library, ScienceDirect, SpringerLink and PubMed.
- **Core Boolean string** (adapted with minor syntax changes for each interface):

```text
("Internet of Medical Things" OR "IoMT")
AND ("Intrusion Detection System" OR "IDS" OR "Anomaly Detection")
AND ("Artificial Intelligence" OR "Machine Learning" OR "Deep Learning"
     OR "Explainable Artificial Intelligence" OR "Explainable AI" OR "XAI"
     OR "Federated Learning" OR "Blockchain")
AND ("Healthcare Cybersecurity" OR "Medical Device Security"
     OR "Remote Patient Monitoring" OR "RPM" OR "Healthcare 5.0")
```

- **Google Scholar:** searched in overlapping publication-year intervals (2021–2022, 2022–2023, 2023–2024, 2024–2025, 2025–2026). The article reports that "approximately 800 records were screened within each interval according to title relevance, abstract relevance, keyword alignment, source quality, and relevance to AI-powered IoMT intrusion detection before duplicate removal and eligibility assessment."

## 2. Retrieval by database and evidence status

| Database | Search date (reported) | Records (reported) | Original record in archive | Status |
|---|---|---|---|---|
| IEEE Xplore | 2–4 June 2026 | 244 | CSV export, 244 records, file saved 3 June 2026 | **Original record; matches reported count** |
| Google Scholar | 2–4 June 2026 | 4,045 | Five RIS exports, 4,882 records, files saved 2–3 June 2026 | **Original record; does not reproduce the reported count** (see §3) |
| Scopus | 5 June 2026 | 64 | none | Reported; author-confirmed; **not recoverable** |
| Web of Science | 5 June 2026 | 57 | none | Reported; author-confirmed; **not recoverable** |
| ACM Digital Library | 5 June 2026 | 185 | none | Reported; author-confirmed; **not recoverable** |
| ScienceDirect | 6–7 June 2026 | 189 | none | Reported; author-confirmed; **not recoverable** |
| SpringerLink | 6–7 June 2026 | 117 | none | Reported; author-confirmed; **not recoverable** |
| PubMed | 6–7 June 2026 | 226 | none | Reported; author-confirmed; **not recoverable** |
| **Total** | | **5,127** | 5,126 records held (4,882 + 244) | Reported total cannot be re-derived from local records |

The full transcription of published Table 2, including the filters for each database, is in [`../evidence/published_transcriptions/table2_search_strategy.csv`](../evidence/published_transcriptions/table2_search_strategy.csv). The metadata-only derivatives are:
- [`google_scholar_exports_metadata.csv`](../evidence/original/google_scholar_exports_metadata.csv)
- [`ieee_xplore_export_metadata.csv`](../evidence/original/ieee_xplore_export_metadata.csv)

## 3. Google Scholar: reported versus held

| Interval | Reported records | Records in local export | Local file |
|---|---|---|---|
| 2021–2022 | 798 | 900 | `Google scholer 2021-2022.ris` |
| 2022–2023 | 810 | 997 | `Google scholer 2022-2023.ris` |
| 2023–2024 | 817 | 995 | `Google scholer 2023-2024.ris` |
| 2024–2025 | 813 | 993 | `Google scholer 2024-2025.ris` |
| 2025–2026 | 807 | 997 | `Google scholer.ris` (unlabelled; records dated 2025–2026) |
| **Total** | **4,045** | **4,882** | |

Observations from the local exports:
- The local window boundaries match the reported intervals.
- Four of the five local exports sit close to Google Scholar's 1,000-result retrieval limit.
- Overlapping windows produce substantial cross-window duplication: 300–524 shared titles between adjacent windows.
- The reported per-interval counts cannot be reproduced from the local exports by record type, publication year, abstract availability or duplicate removal.
- The reported figures follow an interval-level relevance screen, and no record of that screen is held. The difference is therefore documented here, not reconciled.

## 4. Records imported before the review searches

The reference library already contained some items before the June 2026 searches. These items came from earlier exploratory work that is not part of the published method. Two included studies (S06, S15) are recorded in the review's Zotero screening collections but appear in neither the Google Scholar export nor the IEEE export; their library entries date from 30 March 2026. [`../analysis/primary_studies.csv`](../analysis/primary_studies.csv) records this. The earlier exploratory export itself is not part of this repository, because it is not the PubMed search reported in Table 2.

## 5. Limitations acknowledged in the article

The article itself notes (Section 5.3) that Google Scholar contributed 4,045 of 5,127 records (79%), retrieved by relevance ranking rather than structured querying. It describes this as a potential selection-bias risk.
