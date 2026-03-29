# Tag System

All entries must use tags from the approved lists below. **No custom tags.** If no existing tag fits, open an Issue with label `tag-proposal` and wait for approval before using it.

Every entry requires at least **2 tags**: at least 1 task tag + at least 1 method tag.

## Task Tags

Tags describing the problem being solved.

| Tag | Description |
|-----|-------------|
| `super-resolution` | Enhancing spatial/temporal resolution of data |
| `forecasting` | Predicting future states of a system |
| `data-assimilation` | Combining observations with models |
| `uncertainty-quantification` | Estimating prediction uncertainty |
| `calibration` | Ensuring predicted probabilities match observed frequencies |
| `conformal-prediction` | Distribution-free uncertainty coverage guarantees |
| `code-generation` | Automated code writing by AI |
| `tool-use` | AI agents using external tools/APIs |
| `planning` | Multi-step reasoning and action planning |
| `loss-design` | Designing or optimizing loss functions |
| `imputation` | Filling missing data values |
| `downscaling` | Statistical or dynamical downscaling of coarse data |

## Method Tags

Tags describing the technical approach.

| Tag | Description |
|-----|-------------|
| `cnn` | Convolutional Neural Networks |
| `transformer` | Transformer / attention-based architectures |
| `diffusion` | Diffusion probabilistic models |
| `gan` | Generative Adversarial Networks |
| `flow-matching` | Flow matching / continuous normalizing flows |
| `ensemble` | Ensemble methods |
| `bayesian` | Bayesian inference / BNNs |
| `llm` | Large Language Models |
| `reinforcement-learning` | RL-based approaches |
| `physics-informed` | Physics-constrained / PINN-style methods |
| `fno` | Fourier Neural Operator and variants |
| `graph-nn` | Graph Neural Networks |
| `vae` | Variational Autoencoders |

## Scenario Tags

Tags describing the application domain or data type.

| Tag | Description |
|-----|-------------|
| `ocean` | Ocean science (SST, SSH, currents, waves) |
| `atmosphere` | Atmospheric science (weather, wind, precipitation) |
| `satellite` | Satellite remote sensing data |
| `climate` | Climate modeling and projection |
| `medical` | Medical imaging |
| `remote-sensing` | General remote sensing |
| `software-engineering` | Software development and maintenance |

## Value Tags

Tags describing the paper's role in the literature.

| Tag | Description |
|-----|-------------|
| `foundational` | Seminal or foundational work |
| `state-of-the-art` | Current best results on a benchmark |
| `negative-result` | Important negative or null result |
| `benchmark` | Introduces or evaluates benchmarks |
| `survey` | Survey or review paper |
| `tooling` | Introduces a tool, library, or framework |

## Rules

1. Use only tags from the tables above
2. Minimum 2 tags per entry (1 task + 1 method)
3. Use the most specific applicable tag (prefer `ocean` over `remote-sensing` for SST work)
4. To propose a new tag: open an Issue with label `tag-proposal`, include the tag name, description, and 3 example papers that would use it
5. New tags require Maintainer approval before use
