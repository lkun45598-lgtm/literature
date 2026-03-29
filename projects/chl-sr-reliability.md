# Project: Chlorophyll-a SR with Reliability Estimation

## Goal

Super-resolution for chlorophyll-a concentration maps with calibrated, pixel-wise uncertainty estimates, enabling reliable decision-making for ecological monitoring and fisheries management.

## Key Questions

1. How to produce pixel-wise uncertainty maps for SR outputs that are well-calibrated (predicted 90% intervals actually contain the truth 90% of the time)?
2. Which calibration methods (conformal prediction, Bayesian, ensemble) best suit spatially correlated scientific data?
3. At what resolution does SR uncertainty become too large for downstream ecological models to be useful?
4. Can we validate SR reliability against in-situ chlorophyll measurements (buoys, ship tracks)?
5. How does Chl-a's extreme dynamic range (0.01–100 mg/m³) and log-normal distribution affect SR and uncertainty estimation?

## Related Domains

- **scientific-sr** (primary) — SR architectures and evaluation methodology
- **uncertainty-calibration** (primary) — Calibration methods and coverage guarantees
- **ocean-forecasting** (secondary) — Ocean dynamics context; temporal patterns in Chl-a

## Must-Read Papers

| Paper | Domain | Why Essential |
|-------|--------|---------------|
| [Conformal Prediction Survey](../domains/uncertainty-calibration/curated/2023-conformal-prediction-survey.md) | uncertainty-calibration | Foundation for distribution-free coverage guarantees |
| [Diffusion SR for Remote Sensing](../domains/scientific-sr/curated/2024-diffusion-sr-remote-sensing.md) | scientific-sr | SR architecture candidates for Chl-a |

## Supplementary Papers

| Paper | Domain | Value |
|-------|--------|-------|
| [Bayesian NN Calibration](../domains/uncertainty-calibration/backlog/2024-bayesian-nn-calibration.md) | uncertainty-calibration | Alternative to CP for pixel-wise uncertainty |
| [SR Benchmark](../domains/scientific-sr/backlog/2024-sr-benchmark.md) | scientific-sr | Evaluation methodology |

## Not Recommended

Papers to deprioritize for this project:
- Uncertainty quantification papers without spatial/image applications
- Calibration methods tested only on tabular data
- SR methods without uncertainty estimation capability

## Current Gaps

- **No entry on conformal prediction for image/spatial data** — the survey covers theory but we need applications to 2D spatial fields
- **No entry on ensemble-based uncertainty for SR** — comparing deep ensemble vs. MC Dropout for image regression
- **No entry on Chl-a specific SR methods** — do any exist? If not, what's the closest analog?
- **No entry on log-transform strategies** for Chl-a modeling (the distribution is highly skewed)
- **No entry comparing CP vs. Bayesian vs. ensemble** approaches specifically for scientific image regression
