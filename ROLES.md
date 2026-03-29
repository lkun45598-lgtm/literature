# Roles and Responsibilities

## Role Definitions

### Maintainer

**Current:** @lkun45598-lgtm

- Merge authority on `main`
- Manages labels, milestones, and Project board
- Resolves disputes on entry quality or domain assignment
- Edits governance documents (this file, CONTRIBUTING.md, PROJECT_CHARTER.md)
- Can override CODEOWNERS assignment when domain owner is unavailable

### Domain Owner

One per research domain. Responsible for the quality and relevance of their domain's entries.

| Domain | Owner |
|--------|-------|
| ocean-forecasting | @member-ocean |
| scientific-sr | @member-sr |
| uncertainty-calibration | @member-uc |
| code-agent | @member-agent |

**Responsibilities:**
- Review PRs touching their domain (auto-assigned via CODEOWNERS)
- Curate the backlog: promote worthy entries, archive stale ones
- Maintain domain `README.md` with up-to-date curated/backlog lists
- Serve as suggested reviewer for cross-domain papers touching their area

### Submitter

Any team member who contributes paper entries.

**Responsibilities:**
- Open Issues via the `paper_ingest` template for new papers
- Submit PRs with properly formatted entries following `standards/paper_template.md`
- Respond to review feedback within **3 business days**
- Self-check all items in the PR template before requesting review

### Reader

Any team member who uses the knowledge base but does not submit.

**Responsibilities:**
- Can comment on Issues, PRs, and Discussions
- Can suggest papers for others to evaluate (via Discussions)
- Cannot merge PRs or modify `main` directly

## Reviewer SLA

- **First response** within **5 business days** of PR creation
- If no response by deadline, Maintainer reassigns to another Domain Owner or reviews directly
- Reviewer must provide one of the 4 allowed conclusions (see `standards/review_rubric.md`)
- "LGTM" without a conclusion is not a valid review

## Onboarding

New team members should:
1. Read `PROJECT_CHARTER.md` to understand the purpose
2. Read `CONTRIBUTING.md` to understand the workflow
3. Browse their relevant domain's `curated/` entries to see quality standards
4. Submit their first entry as a `backlog` PR to get familiar with the process
