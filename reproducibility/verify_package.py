#!/usr/bin/env python3
"""Consistency checks for the companion repository of Sensors 2026, 26, 5182.

Standard library only. Run from the repository root:
    python reproducibility/verify_package.py

PASS/FAIL lines test the internal consistency of the published values and of this package.
INFO lines compare original-record derivatives with reported counts; differences there
describe the evidence and are not failures of the package.
"""
import csv
import os
import sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
results = []


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def check(name, ok, detail=""):
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" - {detail}" if detail else ""))


def info(name, detail):
    print(f"[INFO] {name} - {detail}")


q = load("analysis/quality_scores.csv")
p = load("analysis/primary_studies.csv")
c = load("analysis/comparison_matrix.csv")
t7 = load("evidence/published_transcriptions/table7_study_characteristics.csv")
t4 = load("evidence/published_transcriptions/table4_quality_distribution.csv")
t2 = load("evidence/published_transcriptions/table2_search_strategy.csv")
f1 = {r["box"]: int(r["n"]) for r in load("evidence/published_transcriptions/figure1_prisma_counts.csv")}
gsi = load("evidence/published_transcriptions/google_scholar_intervals_reported.csv")

# ---- included studies
check("quality_scores.csv has exactly 24 studies", len(q) == 24, f"{len(q)} rows")
refs = [r["reference_number"] for r in q]
check("each reference number appears once", len(set(refs)) == 24)
check("study IDs S01-S24 unique", sorted(r["study_id"] for r in q) == [f"S{i:02d}" for i in range(1, 25)])
for name, rows in [("primary_studies.csv", p), ("comparison_matrix.csv", c), ("Table 7 transcription", t7)]:
    check(f"{name} covers the same 24 reference numbers", sorted(r["reference_number"] for r in rows) == sorted(refs))
for name, rows in [("primary_studies.csv", p), ("comparison_matrix.csv", c)]:
    pairs = {(r["study_id"], r["reference_number"]) for r in rows}
    check(f"{name} study_id/reference pairs match quality_scores.csv", pairs == {(r["study_id"], r["reference_number"]) for r in q})

# ---- quality-score arithmetic
ints_ok = all(r[k].isdigit() and 0 <= int(r[k]) <= 2 for r in q for k in ("q1", "q2", "q3", "q4", "q5"))
check("every Q1-Q5 score is an integer from 0 to 2", ints_ok)
check("every total equals Q1+Q2+Q3+Q4+Q5", all(int(r["total"]) == sum(int(r[k]) for k in ("q1", "q2", "q3", "q4", "q5")) for r in q))
check("every included study scores >= 5", all(int(r["total"]) >= 5 for r in q))
strong = sum(int(r["total"]) >= 8 for r in q)
moderate = sum(5 <= int(r["total"]) <= 7 for r in q)
check("distribution is 20 strong (8-10) and 4 moderate (5-7)", (strong, moderate) == (20, 4), f"{strong}/{moderate}")
t4c = {r["quality_score_range"]: int(r["count"]) for r in t4}
check("distribution matches Table 4 transcription", t4c.get("8-10") == strong and t4c.get("5-7") == moderate and t4c.get("Total assessed") == 34)
qs7 = {r["reference_number"]: r["qs"] for r in t7}
check("Table 5 totals equal Table 7 QS column", all(qs7[r["reference_number"]] == r["total"] for r in q))
check("all decisions are 'Included'", all(r["decision"] == "Included" for r in q))

# ---- reference [34]: final study kept; unverifiable fields flagged; published transcription untouched
s11 = [r for r in c if r["reference_number"] == "34"][0]
study_fields = ["study_type", "dataset_or_benchmark", "ai_ids_approach", "explainability", "privacy_preserving_mechanism_fl_bc",
                "evaluation_metrics", "principal_contribution", "principal_limitation"]
check("[34] listed as Myrzashova et al. in quality_scores and comparison_matrix",
      [r for r in q if r["reference_number"] == "34"][0]["authors"].startswith("Myrzashova") and s11["study_label_as_published"].startswith("Myrzashova"))
check("[34] study-specific fields marked NOT VERIFIED in comparison_matrix", all(s11[k] == "NOT VERIFIED" for k in study_fields))
check("[34] published quality score (9) retained as a published value", s11["quality_score"] == "9" and "NOT VERIFIED" in [r for r in q if r["reference_number"] == "34"][0]["source"])
check("[34] published Table 7 transcription kept as printed", [r for r in t7 if r["reference_number"] == "34"][0]["dataset"] == "BraTS 2020, Pima, CC-19")
zrows_ = load("evidence/original/zotero_screening_collections.csv")
check("every Zotero screening row labelled as historical partial record", all(r["record_status"].startswith("Historical partial screening record") for r in zrows_))

# ---- reported counts
db = [r for r in t2 if r["database"] != "Total"]
tot = int([r for r in t2 if r["database"] == "Total"][0]["records_retrieved"])
check("Table 2 databases sum to reported total (5,127)", sum(int(r["records_retrieved"]) for r in db) == tot == 5127)
check("Table 2 lists eight databases", len(db) == 8)
check("Google Scholar intervals sum to 4,045", sum(int(r["records_reported"]) for r in gsi) == 4045)
f = f1
chain = [
    (f["Records identified from databases"] - f["Duplicates removed"] - f["Non-English records removed"], f["Records screened"]),
    (f["Records screened"] - f["Records excluded after title and abstract keyword screening"], f["Reports sought for retrieval screening"]),
    (f["Reports sought for retrieval screening"] - f["Reports excluded after IoMT and RPM relevance screening"], f["Full-text articles assessed for eligibility"]),
    (f["Full-text articles assessed for eligibility"] - f["Reports excluded after full-text review"], f["Candidate papers after full-text screening"]),
    (f["Candidate papers after full-text screening"] - f["Reports excluded after critical relevance assessment"], f["Studies included in final review"]),
]
check("Figure 1 PRISMA counts are internally consistent", all(a == b for a, b in chain))

# ---- original records vs reported counts (information)
gs = load("evidence/original/google_scholar_exports_metadata.csv")
ie = load("evidence/original/ieee_xplore_export_metadata.csv")
zc = Counter(r["collection"] for r in load("evidence/original/zotero_screening_collections.csv"))
info("IEEE Xplore", f"original export {len(ie)} records; reported 244 -> {'agrees' if len(ie) == 244 else 'differs'}")
info("Google Scholar", f"original exports {len(gs)} records {dict(Counter(r['source_file'] for r in gs))}; reported 4,045 -> not reproduced")
info("Six other databases", "no original exports in this package (reported 838 records)")
info("Zotero screening collections", ", ".join(f"{k}={v}" for k, v in zc.items()) + "; reported PRISMA stages 1,710 / 376 / 85 / 34 -> not reproduced")
status = Counter(r["evidence_status"].split(":")[0] for r in p)
info("Evidence status of the 24 studies", dict(status))

print()
print(f"{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
