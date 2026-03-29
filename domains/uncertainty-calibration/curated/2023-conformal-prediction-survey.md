---
title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
authors: ["Anastasios N. Angelopoulos", "Stephen Bates"]
year: 2023
venue: "Foundations and Trends in Machine Learning"
url: "https://arxiv.org/abs/2107.07511"
code_url: "https://github.com/aangelopoulos/conformal-prediction"
domain: "uncertainty-calibration"
tags: ["conformal-prediction", "calibration", "uncertainty-quantification", "survey"]
status: "curated"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["chl-sr-reliability"]
priority: "high"
---

## One-Line Verdict

The most accessible and complete introduction to conformal prediction, providing both theoretical foundations and practical implementation recipes — essential reading for anyone building prediction systems that need distribution-free coverage guarantees.

## Project Relation

**chl-sr-reliability**: Conformal prediction is our leading candidate for providing calibrated uncertainty bounds on SR outputs. This survey gives us the theoretical foundation and implementation roadmap. Key question: how to extend from i.i.d. settings to spatially correlated ocean data.

## Why Noteworthy

Conformal prediction offers coverage guarantees without distributional assumptions — exactly what we need for operational ocean SR where the data distribution shifts seasonally and regionally. This survey converts the theory into implementable algorithms with code. It's the foundation for our uncertainty pipeline.

## Core Method

Survey paper covering: (1) split conformal prediction (simplest — hold out calibration set, compute nonconformity scores, derive prediction sets); (2) full conformal and jackknife+ variants; (3) conformalized quantile regression for regression tasks; (4) extensions to structured prediction. The key insight: any pre-trained model can be "conformalized" post-hoc by calibrating its outputs on held-out data to achieve exact finite-sample coverage.

## Hidden Assumptions & Weaknesses

- **Exchangeability assumption**: Standard conformal prediction requires exchangeable (roughly, i.i.d.) calibration data. Spatial ocean data is strongly correlated — directly applying these methods may yield under-coverage.
- **Marginal vs. conditional coverage**: Standard CP guarantees marginal coverage (averaged over the calibration set), not conditional coverage (for each specific input). For spatial data, we need conditional coverage per pixel/region.
- **Prediction set size**: CP guarantees coverage but not efficiency. In high-uncertainty regions, prediction intervals may be so wide as to be useless for decision-making.
- **Computational cost**: Full conformal and CV+ methods require re-training or caching model predictions, which may be expensive for large SR models.

## Reading Advice

- **Read carefully**: Sections 1-3 (core CP framework), Section 4 (conformalized quantile regression — most relevant for our regression task), Algorithm boxes throughout
- **Skim**: Section 5 (classification extensions — less relevant for SR)
- **Skip**: Proofs in the appendix (unless you need the theory)
- **Prerequisite**: Basic probability and statistics; no ML-specific prerequisites needed

## Reproduction Value

**High**. Code is released and well-documented. The algorithms are simple to implement. The main challenge for us is not implementation but adaptation to spatially correlated data. Estimated effort: 2-3 days to implement basic split CP for our SR pipeline; 2-3 weeks to develop and validate a spatial extension.

## Evidence

1. Split conformal achieves exact 1-α coverage on any exchangeable dataset regardless of model quality (Theorem 1)
2. CQR (Conformalized Quantile Regression) produces adaptive prediction intervals — tighter in easy regions, wider in hard regions (Section 4, Figure 4)
3. Computational overhead of split CP is negligible — only requires sorting nonconformity scores on the calibration set
4. Empirical coverage on tabular benchmarks consistently within 0.5% of target (Table 2)

## Notes

- Critical gap for our work: need to find papers on CP for spatial/temporal data with dependence structure. Check if there are conformal prediction extensions for time series or spatial processes.
- The conformalized quantile regression approach is most promising for pixel-wise uncertainty in SR.
- Consider linking to ensemble methods in this domain — ensemble disagreement + CP calibration could be a practical pipeline.
