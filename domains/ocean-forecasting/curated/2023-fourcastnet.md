---
title: "FourCastNet: A Global Data-driven High-resolution Weather Forecasting Model"
authors: ["Jaideep Pathak", "Shashank Subramanian", "Peter Harrington", "Sanjeev Raja", "Ashesh Chattopadhyay", "Morteza Mardani", "Thorsten Kurth", "David Hall", "Zongyi Li", "Kamyar Azizzadenesheli", "Pedram Hassanzadeh", "Karthik Kashinath", "Animashree Anandkumar"]
year: 2023
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2202.11214"
code_url: "https://github.com/NVlabs/FourCastNet"
domain: "ocean-forecasting"
tags: ["forecasting", "fno", "atmosphere"]
status: "curated"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["ocean-sr"]
priority: "high"
---

## One-Line Verdict

Demonstrates that FNO-based architectures can match IFS at 0.25deg resolution for short-range (1-3 day) weather forecasting, but accuracy degrades significantly beyond 5 days, suggesting the architecture captures spatial patterns far better than temporal dynamics.

## Project Relation

**ocean-sr**: The Adaptive Fourier Neural Operator (AFNO) backbone is directly relevant as a potential encoder for our ocean SR pipeline. The spectral processing approach may help preserve physical gradients during upscaling, which is our core challenge.

## Why Noteworthy

First demonstration that a pure data-driven model can match operational NWP at 0.25deg global resolution for short-range forecasting. The AFNO architecture introduces a vision-transformer-like structure with Fourier attention that efficiently handles high-resolution global grids — a key bottleneck for our ocean data processing. The 45,000x speedup over IFS makes iterative experimental workflows feasible.

## Core Method

Uses Adaptive Fourier Neural Operator (AFNO) — essentially a Vision Transformer where self-attention is replaced with token mixing in the Fourier domain. Operates on 720x1440 equirectangular grids at 0.25deg. Trained autoregressively on ERA5 reanalysis data (1979-2015). The model takes current atmospheric state (20 variables at multiple pressure levels + surface) and predicts 6-hour lead time; longer forecasts via autoregressive rollout. Pre-training uses single-step prediction; fine-tuning extends to multi-step.

## Hidden Assumptions & Weaknesses

- **Resolution ceiling**: 0.25deg is coarse for ocean applications where mesoscale eddies (10-100km) matter. The paper does not address how the architecture scales to higher resolution.
- **Temporal degradation**: Autoregressive rollout amplifies errors rapidly after day 5. No explicit temporal modeling mechanism — purely spatial pattern matching rolled forward.
- **ERA5 dependence**: Trained only on reanalysis data, not raw observations. Performance on real-time operational data with missing/noisy observations is unknown.
- **No ocean variables**: Despite the "weather" claim, focuses on atmospheric variables. SST/SSH performance not evaluated.
- **No uncertainty quantification**: Single deterministic forecast. No ensemble or probabilistic extension in this paper.

## Reading Advice

- **Read carefully**: Section 3 (AFNO architecture), Figure 2 (architecture diagram), Table 1 (comparison with IFS)
- **Skim**: Section 2 (related work), Appendix training details
- **Skip**: Tropical cyclone tracking (Section 4.2) — interesting but not relevant to our SR work
- **Prerequisite**: Basic understanding of Fourier Neural Operators (Li et al., 2021) and Vision Transformers

## Reproduction Value

**Medium-high**. Code is released and well-documented. The AFNO backbone is worth extracting and testing as an encoder for our ocean SR pipeline. Main engineering challenge: adapting from atmospheric variables on equirectangular grids to ocean variables on potentially irregular grids. Estimated effort: 1-2 weeks to integrate AFNO backbone into our pipeline.

## Evidence

1. **Table 1**: AFNO achieves RMSE of 3.67 m/s for 10m wind speed at 24h lead (IFS: 3.69 m/s) — competitive at short range
2. **Figure 3**: ACC (Anomaly Correlation Coefficient) for Z500 drops below 0.6 at ~day 7 vs. IFS at ~day 9 — the 2-day gap quantifies temporal degradation
3. **Table 2**: Inference time of 0.01s per forecast step vs. ~1 hour for IFS — 45,000x speedup
4. **Figure 5**: Spatial error maps show largest errors at polar regions and sharp orographic boundaries — relevant for understanding where the method breaks

## Notes

- The AFNO architecture was later adopted in several follow-up works (Pangu-Weather, GenCast). Worth tracking the lineage.
- Key question for our work: does Fourier-domain token mixing preserve the spectral characteristics of ocean variables better than pixel-domain attention?
- Related entries: check uncertainty-calibration domain for papers on ensemble extensions of neural weather models.
