# Paper Hub — Team Literature Knowledge Base

A structured, peer-reviewed knowledge base for tracking, evaluating, and organizing research papers across the team's active domains and projects. Built on GitHub native features.

**This is a decision hub, not a PDF library.** Every entry answers: *Is this paper worth my time, and how does it relate to our work?*

## Quick Start

1. **Browse** — Pick your [research domain](#research-domains) or [project](#active-projects) below
2. **Submit** — Found a relevant paper? Open an Issue using the [Paper Ingest](../../issues/new/choose) template
3. **Contribute** — Want to write a full entry? See [CONTRIBUTING.md](CONTRIBUTING.md)

## Repository Structure

```
literature/
├── domains/           # Paper entries organized by research direction
│   ├── ocean-forecasting/
│   ├── scientific-sr/
│   ├── uncertainty-calibration/
│   └── code-agent/
├── projects/          # Goal-oriented views linking papers to team projects
├── standards/         # Templates, rubrics, and tag definitions
├── scripts/           # Utility tools for creating entries
└── .github/           # Issue/PR templates, CI workflows
```

## Research Domains

| Domain | Focus | Entry Point |
|--------|-------|-------------|
| **Ocean Forecasting** | Ocean/atmosphere prediction, data assimilation, spatiotemporal forecasting | [domains/ocean-forecasting/](domains/ocean-forecasting/) |
| **Scientific SR** | Super-resolution for scientific imagery (satellite, climate, remote sensing) | [domains/scientific-sr/](domains/scientific-sr/) |
| **Uncertainty Calibration** | Uncertainty quantification, calibration, conformal prediction | [domains/uncertainty-calibration/](domains/uncertainty-calibration/) |
| **Code Agent** | LLM-based code generation agents, tool use, planning | [domains/code-agent/](domains/code-agent/) |

## Active Projects

| Project | Goal | Related Domains |
|---------|------|-----------------|
| [ocean-sr](projects/ocean-sr.md) | Super-resolution for ocean remote sensing variables | ocean-forecasting, scientific-sr |
| [chl-sr-reliability](projects/chl-sr-reliability.md) | Chlorophyll-a SR with calibrated uncertainty | scientific-sr, uncertainty-calibration |
| [agent-loss-migration](projects/agent-loss-migration.md) | Agent-assisted loss function migration | code-agent |

## Curated vs. Backlog

- **Curated** (`domains/<domain>/curated/`): Thoroughly reviewed, all sections substantive, approved by Domain Owner. These are the entries the team should read first.
- **Backlog** (`domains/<domain>/backlog/`): Worth tracking but evaluation may be incomplete. Lower quality bar — at minimum: one-line verdict + project relation + initial judgment.

## Governance

- [PROJECT_CHARTER.md](PROJECT_CHARTER.md) — What this repo is and isn't
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to submit and review entries
- [ROLES.md](ROLES.md) — Who does what
- [standards/](standards/) — Templates, review rubric, tag system
