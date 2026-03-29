# Project: Ocean Super-Resolution

## Goal

Develop and benchmark super-resolution methods for ocean remote sensing variables (SST, SSH, chlorophyll-a) that are physically consistent and operationally deployable.

## Key Questions

1. Which SR architectures best preserve physical gradients (temperature fronts, current boundaries, eddy structures)?
2. How to evaluate SR quality beyond PSNR — what ocean-specific metrics matter (spectral fidelity, gradient preservation, geostrophic consistency)?
3. Can physics-informed losses improve SR for ocean variables while maintaining computational efficiency?
4. What is the minimum input resolution for useful 4x/8x upscaling on ocean data?
5. How to handle cloud-masked and missing-data regions that are endemic to satellite ocean observations?

## Related Domains

- **ocean-forecasting** (primary) — Forecasting architectures as SR backbones; physics constraints from ocean dynamics
- **scientific-sr** (primary) — SR methodology and evaluation frameworks
- **uncertainty-calibration** (secondary) — Uncertainty-aware SR evaluation metrics

## Must-Read Papers

| Paper | Domain | Why Essential |
|-------|--------|---------------|
| [FourCastNet](../domains/ocean-forecasting/curated/2023-fourcastnet.md) | ocean-forecasting | AFNO backbone candidate for SR encoder |
| [Diffusion SR for Remote Sensing](../domains/scientific-sr/curated/2024-diffusion-sr-remote-sensing.md) | scientific-sr | Benchmark of diffusion SR methods; defines current SOTA and gaps |

## Supplementary Papers

| Paper | Domain | Value |
|-------|--------|-------|
| [Neural Ocean Model](../domains/ocean-forecasting/backlog/2024-neural-ocean-model.md) | ocean-forecasting | Hybrid neural-physical architecture concept |
| [SR Benchmark](../domains/scientific-sr/backlog/2024-sr-benchmark.md) | scientific-sr | Evaluation methodology reference |

## Not Recommended

Papers to deprioritize for this project:
- Pure natural image SR (SISR on faces, text, etc.) without scientific data evaluation
- SR methods tested only on classification tasks (land-use, scene recognition)
- Papers without quantitative evaluation on geophysical variables

## Current Gaps

- **No entry on physics-constrained SR loss functions** for ocean data (e.g., spectral loss, gradient penalty, geostrophic consistency loss)
- **No entry on SR evaluation metrics** beyond PSNR/SSIM for scientific data
- **No entry on handling missing data** in SR inputs (cloud masking, ice coverage)
- **No entry on temporal consistency** in SR sequences (multi-frame SR for ocean time series)
- **Limited entries on diffusion models** specifically applied to ocean variables
