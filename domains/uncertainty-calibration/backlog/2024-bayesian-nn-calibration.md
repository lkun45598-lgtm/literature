---
title: "Calibrated Uncertainty Quantification with Bayesian Neural Networks for Image Regression"
authors: ["Placeholder Author E", "Placeholder Author F"]
year: 2024
venue: "ICML"
url: "https://arxiv.org/abs/2403.00000"
code_url: "https://github.com/placeholder/bnn-calibration"
domain: "uncertainty-calibration"
tags: ["bayesian", "calibration", "uncertainty-quantification", "cnn"]
status: "backlog"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["chl-sr-reliability"]
priority: "medium"
---

## One-Line Verdict

Demonstrates that well-calibrated BNNs can produce pixel-wise uncertainty maps for image regression tasks with better calibration than MC Dropout, but computational overhead is 10x and testing is limited to natural images — spatial scientific data performance unknown.

## Project Relation

**chl-sr-reliability**: BNN uncertainty is an alternative to conformal prediction for our pipeline. This paper helps us understand the BNN approach's strengths and costs.

## Why Noteworthy

One of the few papers that systematically evaluates calibration quality (not just uncertainty magnitude) of BNNs for image regression — directly relevant to our pixel-wise uncertainty estimation needs.

## Core Method

Uses Bayes-by-Backprop and SWAG for approximate Bayesian inference in convolutional architectures. Evaluates calibration using reliability diagrams and Expected Calibration Error (ECE) adapted for regression.

## Hidden Assumptions & Weaknesses

- Natural image benchmarks only — no scientific data
- 10x computational overhead vs. deterministic model
- Approximate inference methods may not capture multi-modal posteriors

## Reading Advice

Focus on the calibration evaluation methodology (Section 4) — the metrics are useful regardless of whether we adopt BNNs.

## Reproduction Value

**Medium** — code available, but the BNN overhead may be impractical for our large-scale ocean SR.

## Evidence

- BNN ECE improved by 40% over MC Dropout on ImageNet regression tasks
- SWAG achieves the best cost-calibration tradeoff

## Notes

Compare with conformal prediction survey entry — CP has no distributional assumptions while BNN assumes approximate posterior. For operational deployment, CP's simplicity may win.
