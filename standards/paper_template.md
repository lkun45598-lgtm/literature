# Paper Entry Template

This is the canonical template for all paper entries. Use `scripts/new_paper.py` to generate a new entry with this structure pre-filled.

---

## Front Matter (YAML)

Every entry must start with a YAML front matter block:

```yaml
---
title: "<Full paper title>"
authors: ["<Author 1>", "<Author 2>"]
year: <YYYY>
venue: "<Conference or Journal>"
url: "<Paper URL (arXiv, DOI, etc.)>"
code_url: "<Code repository URL or null>"
domain: "<ocean-forecasting | scientific-sr | uncertainty-calibration | code-agent>"
tags: [<tag1>, <tag2>]
status: "<backlog | curated>"
added_by: "<github-username>"
added_date: "<YYYY-MM-DD>"
projects: ["<project-slug or none>"]
priority: "<high | medium | low>"
---
```

**All fields are required.** Use `null` for `code_url` if no code is available. Use `"none"` in `projects` if unrelated to any active project.

---

## Body Sections

### One-Line Verdict

<!-- A single evaluative sentence. What this paper actually achieves, not what it claims.
     BAD: "This paper proposes a new method for ocean forecasting."
     GOOD: "Achieves 0.25deg global weather forecasting competitive with IFS at 5-day lead but degrades rapidly beyond, suggesting spatial pattern capture outpaces temporal dynamics." -->

### Project Relation

<!-- Which of our active projects does this serve? Be specific about HOW it relates.
     If none, write "None — general reference for <domain>." -->

### Why Noteworthy

<!-- 2-3 sentences: why this paper matters to OUR work specifically.
     Not why it's a good paper in general — why should a teammate read it? -->

### Core Method

<!-- 3-5 sentences describing the actual technical approach.
     Not the abstract — your understanding of what they did and how.
     Focus on the architecture, training strategy, or experimental design that matters. -->

### Hidden Assumptions & Weaknesses

<!-- What the authors do NOT say. Limitations they understate.
     Conditions under which this method breaks.
     This section CANNOT be "none" for curated entries. -->

### Reading Advice

<!-- Which sections to read carefully, which to skim.
     What prerequisite knowledge is needed.
     What to look for vs. what to skip. -->

### Reproduction Value

<!-- Is it worth reimplementing? What would you gain?
     Estimate effort: days/weeks? What's the main engineering challenge?
     Is the released code usable? -->

### Evidence

<!-- Key quantitative results that support your verdict.
     Reference specific tables, figures, or metrics.
     At least 3 pieces of evidence for curated entries. -->

### Notes

<!-- Connections to other entries in this knowledge base.
     Open questions this paper raises.
     Follow-up ideas or experiments it suggests. -->
