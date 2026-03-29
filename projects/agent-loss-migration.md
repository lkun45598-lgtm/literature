# Project: Agent-Assisted Loss Function Migration

## Goal

Use LLM code agents to automate the migration and optimization of loss functions across deep learning projects — enabling rapid experimentation with loss designs without manual re-implementation.

## Key Questions

1. Can code agents understand the mathematical semantics of loss functions (not just syntax)?
2. How to evaluate whether a migrated loss function is semantically equivalent to the original (same gradients, same optimization landscape)?
3. What agent planning strategies work for multi-file code modifications where the loss function touches the training loop, model forward pass, and evaluation code?
4. How to handle domain-specific constraints during loss migration (differentiability requirements, tensor shape expectations, numerical stability)?
5. What is the right interface design for a loss migration agent (tools, feedback mechanisms, verification steps)?

## Related Domains

- **code-agent** (primary) — Agent architectures, tool use, planning strategies
- **scientific-sr** (secondary) — Application domain where loss migration would be used
- **ocean-forecasting** (secondary) — Application domain with complex physics-based losses

## Must-Read Papers

| Paper | Domain | Why Essential |
|-------|--------|---------------|
| [SWE-Agent](../domains/code-agent/curated/2024-swe-agent.md) | code-agent | ACI design principles for code editing agents |

## Supplementary Papers

| Paper | Domain | Value |
|-------|--------|-------|
| [Code Repair Agent](../domains/code-agent/backlog/2024-code-repair-agent.md) | code-agent | Error feedback loop architecture |

## Not Recommended

Papers to deprioritize for this project:
- General code generation benchmarks (HumanEval, MBPP) without relevance to scientific computing
- NLP-focused LLM papers without code/agent applications
- Loss function surveys that don't address automation or migration

## Current Gaps

- **Very few papers on agent-assisted loss function design** — this may be a novel research direction
- **No entry on code understanding for mathematical expressions** — how do LLMs parse and reason about mathematical code?
- **No entry on semantic equivalence testing for code** — beyond syntactic diffing, how to verify two loss implementations compute the same thing?
- **No entry on domain-specific code agents** for scientific computing (vs. general software engineering)
- **No entry on gradient-based verification** — using automatic differentiation to verify migrated loss functions
