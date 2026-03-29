---
title: "A Comprehensive Benchmark for Single Image Super-Resolution in Remote Sensing"
authors: ["Placeholder Author C", "Placeholder Author D"]
year: 2024
venue: "Remote Sensing of Environment"
url: "https://arxiv.org/abs/2402.00000"
code_url: null
domain: "scientific-sr"
tags: ["super-resolution", "benchmark", "remote-sensing", "satellite"]
status: "backlog"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["ocean-sr"]
priority: "medium"
---

## One-Line Verdict

Comprehensive benchmark covering 15+ SR methods on remote sensing data with unified evaluation, but lacks ocean-specific variables (SST, SSH, Chl-a) and focuses exclusively on land-use classification imagery.

## Project Relation

**ocean-sr**: Useful as a reference for benchmark methodology and evaluation protocol design, but we need to extend significantly for ocean variables.

## Why Noteworthy

Provides a well-structured evaluation framework that we can adapt. The methodology for fair comparison across different SR architectures is solid and saves us experimental design effort.

## Core Method

Systematic benchmark comparing CNN-based (SRCNN, EDSR, RCAN), GAN-based (ESRGAN, Real-ESRGAN), and transformer-based (SwinIR, HAT) methods on multiple remote sensing datasets.

## Hidden Assumptions & Weaknesses

- Land-use imagery only — no ocean or atmospheric variables
- Standard pixel metrics (PSNR, SSIM) — no domain-specific evaluation
- 2x and 4x factors only

## Reading Advice

Focus on evaluation protocol design (Section 3) and the comparison tables. Skip individual method descriptions if already familiar.

## Reproduction Value

**Low** — code not released. Methodology is the main value, not the implementation.

## Evidence

- SwinIR and HAT consistently outperform CNN-based methods at 4x upscaling
- GAN-based methods trade pixel accuracy for perceptual quality

## Notes

TODO: Check if any ocean-specific SR benchmark exists. If not, this is a gap we could fill.
