# Project Charter

## Purpose

This repository is the team's **paper decision hub** — a structured, peer-reviewed knowledge base that helps members quickly determine whether a paper is worth reading and how it relates to our active projects.

**It is NOT a PDF library, a Zotero replacement, or a bookmark collection.**

## Audience

AI-for-Science research engineers within our team. Every entry is written for internal consumption — the first reader is always a teammate deciding how to spend their reading time.

## Goals

1. **Reduce duplicate reading** — if someone has already evaluated a paper, the team should benefit.
2. **Accumulate critical judgment** — entries must contain original evaluation, not just summaries.
3. **Map papers to projects** — every entry must state its relationship (or lack thereof) to our active projects.
4. **Enforce quality via peer review** — no entry enters `curated/` without an approved review.

## Non-Goals

- PDF hosting (use arXiv, Sci-Hub, or institutional access)
- Citation management (use Zotero, Mendeley, etc.)
- AI auto-generated summaries (judgment must be human-authored)
- Exhaustive bibliography of any field
- External-facing documentation

## Success Criteria

- Over 80% of project-relevant papers have entries within 2 weeks of discovery
- Every `curated` entry has at least 1 approved review
- Backlog-to-curated promotion rate is tracked and reviewed monthly
- Team members report using the hub as their first stop before reading a new paper

## Phase 1 Scope

- 4 research domains: `ocean-forecasting`, `scientific-sr`, `uncertainty-calibration`, `code-agent`
- 3 active projects: `ocean-sr`, `chl-sr-reliability`, `agent-loss-migration`
- Issue-based ingestion, PR-based review, basic CI validation
- Manual curation workflow (no automation beyond front matter checks)

## Expansion Boundaries (Future Phases)

- arXiv RSS integration and auto-triage
- Tag-based search and aggregation dashboard
- Reading group scheduling via Discussions
- Cross-team sharing and external visibility
- GitHub Pages for a browsable web interface
