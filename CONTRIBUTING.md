# Contributing Guide

## What We Collect

Papers that:
- Relate to at least one of our [research domains](domains/)
- Have a clear method contribution or empirical insight
- Are published in peer-reviewed venues, or credible preprints from established groups

## What We Do NOT Collect

- Blog posts, tutorials, slide decks (use [Discussions](https://github.com/lkun45598-lgtm/literature/discussions) for those)
- Papers already well-covered by existing entries (unless adding genuinely new judgment)
- Papers with no connection to any active project or research domain
- PDF files — this repo stores evaluations, not documents

## Submission Flow

### Step 1: Open an Issue (Quick Capture)

Use the **Paper Ingest** issue template. This captures the essential metadata and your initial judgment. Good for quick triage — you don't need a full entry yet.

### Step 2: Create a Full Entry (PR)

If the paper is worth a detailed entry:

1. Create a branch: `paper/<domain>/<short-name>`
2. Run `python scripts/new_paper.py --title "..." --domain ... --year ... --venue "..." --url "..."`
3. Fill in all sections of the generated template (see `standards/paper_template.md`)
4. Open a PR targeting `main`

### Step 3: Review

- Domain Owner is auto-assigned via CODEOWNERS
- Reviewer evaluates entry quality using `standards/review_rubric.md`
- Reviewer gives one of 4 conclusions: `merge-to-backlog`, `promote-to-curated`, `request-revision`, `reject`

### Step 4: Merge

- Approved PRs are merged to `main`
- Default target is `domains/<domain>/backlog/`
- Promotion to `curated/` requires a separate PR with upgraded content

### Step 5: Promotion (Optional)

To promote a backlog entry to curated:
1. Open a new PR moving the file from `backlog/` to `curated/`
2. Ensure all template sections are substantively filled
3. Domain Owner reviews and approves the promotion

## Curated Admission Standards

A `curated` entry must:
- Have ALL template sections filled with substantive content (not placeholders)
- Contain genuine analysis in "Hidden Assumptions & Weaknesses" (not "none")
- Have at least 1 approved review from a Domain Owner
- Include a clear reproduction value assessment
- Provide at least 3 pieces of evidence (key results, figures, tables)

## Writing Requirements

- **Front matter**: All YAML fields must be complete and valid
- **One-line verdict**: Must be evaluative, not just descriptive. Bad: "This paper proposes X." Good: "Achieves X but fails under condition Y, making it useful only for Z."
- **Language**: Framework and metadata in English. Body content sections may use Chinese.
- **Filename**: `<year>-<short-slug>.md` (e.g., `2024-diffusion-sr-remote-sensing.md`)
- **Tags**: Only use tags from `standards/tag_system.md`

## Prohibited Actions

- Direct push to `main` (all changes via PR)
- Deleting others' entries without an Issue discussion
- Adding custom tags not in `standards/tag_system.md`
- Storing PDF files in the repository
- Copying abstracts as the "one-line verdict" or "core method"
- Submitting entries with empty required sections
