# Six-dimension analytical framework

Source: Sections 2.3–2.4 and 3–5, Tables 8–15 and Figures 2 and 4–7 of *Sensors* 2026, 26, 5182 (CC BY 4.0). This document summarises the article. It makes no experimental claims of its own, and no new data or measurements were produced.

The 24 primary studies were extracted with a predefined comparative synthesis matrix, covering:
- datasets
- AI/IDS methods
- detection objectives
- architecture
- explainability
- privacy mechanisms
- metrics
- findings, limitations and future directions

The original extraction matrix is provided as [`../evidence/original/extraction_primary_original.csv`](../evidence/original/extraction_primary_original.csv); its relationship to the published set of 24 studies is described in [`../evidence/EVIDENCE_PROVENANCE.md`](../evidence/EVIDENCE_PROVENANCE.md#notes-on-the-original-extraction-matrices).

Only the 24 primary studies entered the formal comparative synthesis. The 115 supporting references provided conceptual background, methodological justification and Healthcare 5.0 and RPM context; they were not quality-assessed or included in the formal comparison (Section 2.4). A quantitative meta-analysis was not performed because the included studies differed substantially in datasets, attack categories, AI architectures, evaluation metrics, experimental settings and validation protocols.

The extracted evidence was therefore synthesised qualitatively across six dimensions. The article describes these dimensions as "a common analytical framework to evaluate the same carefully selected body of evidence rather than as independent evidence syntheses."

---

## 1. Detection performance

*Main sources: Section 3.2; Table 8; Figure 4.*

**Why it matters.** Detection capability is the technical foundation of any IDS. Signature-based mechanisms are inadequate for evolving attacks on heterogeneous, data-intensive healthcare networks.

**What the review examined.** The progression from traditional ML (DT, RF, SVM, LR, XGBoost) to deep learning (CNN, LSTM, autoencoders, DBN, Transformers) and then to hybrid and ensemble architectures (CNN-LSTM, Transformer-enhanced, stacking, graph-enhanced). Table 8 adds a fourth paradigm, adaptive learning, which addresses concept drift and evolving attacks but has limited real-world validation.

**Common limitations.**
- Many studies report accuracies above 95% on benchmarks such as CIC-IoMT-2024 and WUSTL-EHMS-2020.
- These gains often come with higher computational complexity, lower transparency and greater implementation overhead.
- Tree-based ML depends on handcrafted, dataset-specific features.

**Implications.** Recent advances are increasingly driven by architectural integration rather than by entirely new learning algorithms. Each paradigm resolves earlier weaknesses while introducing new trade-offs, so no single paradigm meets every deployment requirement. Benchmark accuracy should be read as evidence of algorithmic capability, not of operational readiness (Section 3.5).

## 2. Explainability

*Main sources: Section 3.3; Tables 9–10; Figure 5.*

**Why it matters.** IDS decisions can affect clinical workflows, connected medical devices and patient safety. False positives drive alert fatigue, while false negatives can expose life-critical systems. Clinicians and security analysts need to understand why an alert was raised before they can act on it.

**What the review examined.** Five explainability paradigms:
- SHAP
- LIME
- attention mechanisms
- intrinsically interpretable models
- explainable ensembles

The review also examined explainability's place within a wider trustworthy-AI framework of reliability, robustness, fairness, privacy, accountability and human oversight (Table 10; Figure 5).

**Common limitations.**
- Explanation methods add computational overhead.
- Their evaluation methodology is inconsistent.
- Human-centred and usability evaluation is limited.
- Evidence on adversarial robustness, fairness, long-term reliability, AI governance and regulatory compliance remains limited (Sections 3.3 and 3.6).

**Implications.** Explainability is a deployment requirement, not an optional add-on. The choice of XAI technique is a design decision that has to balance fidelity, cost and the needs of each stakeholder.

## 3. Privacy preservation

*Main sources: Section 3.4; Table 11; Figure 6.*

**Why it matters.** Centralised learning requires sensitive patient data to be pooled. Healthcare collaboration must preserve privacy, data sovereignty and regulatory compliance.

**What the review examined.**
- **Federated Learning** for training across institutions without sharing raw data.
- **Blockchain** for audit trails, identity, provenance and verifiable model updates.
- **XAI** as a complementary transparency layer (Figure 6).
- **Secure aggregation** to protect collaborative model updates (Table 11).

Differential privacy and homomorphic encryption are listed among the privacy criteria of the deployment-readiness checklist (Table 13).

**Common limitations.**
- **Federated Learning:** non-IID healthcare data, communication overhead and latency.
- **Attacks on collaborative training:** poisoning, membership inference and model inversion.
- **Blockchain:** consensus latency, communication overhead, scalability, interoperability across heterogeneous IoMT infrastructures and resource consumption.

**Implications.** Privacy preservation alone does not establish trustworthy collaboration. FL, blockchain-assisted trust and XAI need to work as complementary architectural layers. The review lists research priorities for this:
- personalised FL
- adaptive and secure aggregation
- lightweight blockchain and hybrid on-chain/off-chain architectures

## 4. Computational efficiency

*Main sources: Sections 2.3, 3.5 and 5.1; Tables 12–13.*

**Why it matters.** IoMT IDSs run on wearable sensors, implantable devices, edge gateways and battery-powered RPM platforms, where memory, latency and energy are tightly constrained.

**What the review examined.** The resource cost of deep and hybrid models, and efficiency strategies including:
- lightweight deep learning
- TinyML
- pruning, model compression and knowledge distillation
- edge intelligence

**Common limitations.** Computational efficiency is reported inconsistently across the primary studies, and the literature provides limited evidence on latency and energy consumption.

**Implications.** The deployment-readiness checklist (Table 13) recommends reporting end-to-end latency, energy use (J/inference), RAM utilisation and model size alongside detection metrics.

## 5. Benchmarking practices

*Main sources: Sections 2.3, 3.5 and 3.6; Figure 2; Tables 12–13.*

**Why it matters.** Benchmark design determines what reported performance actually means.

**What the review examined.** The datasets used across the primary studies (Figure 2) and the evaluation metrics they report. Evaluations concentrate on:
- WUSTL-EHMS-2020
- CIC-IoMT-2024
- ToN-IoT
- BoT-IoT
- Edge-IIoTset
- CIC-IDS2017

**Common limitations.**
- Single-dataset evaluation, static train–test splits, balanced attack distributions and synthetic traffic.
- Metrics focused on accuracy, precision, recall, F1 and ROC-AUC.
- Little assessment of latency, energy, interoperability, adversarial resilience or clinical usability.

**Implications.** The field needs healthcare-specific datasets and standardised, deployment-oriented evaluation protocols (Tables 12–13).

## 6. Cross-dataset generalisation

*Main sources: Sections 3.5 and 5.1; Tables 12–13.*

**Why it matters.** Deployed IDSs must perform reliably across hospitals, devices, protocols and attack distributions that differ from their training data.

**What the review examined.** Evidence on how performance changes when models are evaluated on unseen datasets and environments. Cross-dataset generalisation is the most widely reported deployment challenge in the reviewed literature.

**Common limitations.**
- Models often learn dataset-specific artefacts rather than general attack behaviour.
- The causes are differences in devices, traffic, feature pipelines and attack mixes.

**Implications.** The review recommends train-on-one, test-on-another protocols (for example, CIC-IoMT-2024 → WUSTL-EHMS-2020), together with:
- multi-centre benchmarking
- domain adaptation and transfer learning
- continual learning

---

## Synthesis

Across the six dimensions, the article concludes that advances in detection capability have outpaced progress in explainability, privacy-preserving collaboration, computational efficiency, benchmarking consistency and generalisation. This imbalance helps explain why many IDSs perform well on benchmarks yet remain immature for routine Healthcare 5.0 deployment. It also motivates the review's central conclusion: **deployment readiness, rather than benchmark accuracy, is the defining challenge.**

The dimensions also structure the article's later findings. Section 3.5 identifies four interrelated deployment barriers: limited cross-dataset generalisation, computational constraints, dynamic healthcare environments affected by concept drift, and insufficient integration with clinical workflows; Table 12 links these and related barriers to research priorities. Section 3.6 sets out five research gaps, Section 4.2 (Table 14) the trade-offs between dimensions, and Section 5.1 (Table 15) the resulting strategic research priorities.

The conceptual radar-style comparisons in the article (Figures 4 and 7) are described there as "illustrative qualitative synthesis … rather than a quantitative evaluation or formal scoring system". Their axes overlap with, but are not the same as, the six dimensions. Figure 4 compares traditional ML, deep learning and hybrid AI on detection accuracy, interpretability, computational efficiency, scalability, generalisation and deployment readiness. Figure 7 compares six IDS categories on detection performance, explainability, privacy preservation, computational efficiency and cross-dataset generalisation. The figures are not reproduced here, and no tabulated rating values for them are held in the available research archive (see [missing records](../evidence/EVIDENCE_PROVENANCE.md#missing-records)).
