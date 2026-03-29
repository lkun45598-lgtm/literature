# Review Rubric

This rubric guides the review of **paper entry PRs** — not the papers themselves. The question is: *Does this entry help the team decide whether and how to engage with this paper?*

## Veto Items (Any One Triggers "Request Revision")

- [ ] Missing or incomplete front matter fields
- [ ] One-line verdict is purely descriptive (restates the abstract, no judgment)
- [ ] "Hidden Assumptions & Weaknesses" is empty, says "none", or is trivially obvious
- [ ] `domain` or `tags` not from the approved lists in `tag_system.md`
- [ ] Paper URL is missing or clearly broken
- [ ] File is in `curated/` but has placeholder or incomplete sections
- [ ] Content is copied directly from the paper's abstract

## Qualitative Dimensions

### 1. Relevance

Does this paper actually matter for our domains and projects?
- Is the domain assignment correct?
- Is the project relation specific and actionable?
- Would a teammate's reading priority change based on this entry?

### 2. Judgment Quality

Does the entry go beyond the abstract?
- Is the one-line verdict genuinely evaluative?
- Does the submitter demonstrate understanding of the method, not just surface-level description?
- Are the weaknesses identified from a critical reading, not just parroting the paper's "Limitations" section?

### 3. Actionability

Can a reader decide whether to read the paper based on this entry alone?
- Is the reading advice specific enough to save time?
- Is the reproduction value assessment realistic?
- Would this entry change someone's project approach?

### 4. Risk Identification

Are assumptions and failure modes genuinely identified?
- Does the entry flag conditions where the method might not transfer to our data/problems?
- Are there unstated assumptions about data scale, distribution, or computational budget?

### 5. Information Density

Is the entry concise?
- No filler paragraphs or unnecessary hedging
- Evidence section contains specific numbers, not vague statements
- Every sentence earns its place

## Allowed Reviewer Conclusions

| Conclusion | Meaning | Action |
|------------|---------|--------|
| `merge-to-backlog` | Entry meets minimum quality; useful reference | Merge PR to `backlog/` |
| `promote-to-curated` | Entry is excellent; all sections substantive; worth featuring | Merge PR to `curated/` (or approve promotion PR) |
| `request-revision` | Specific issues identified | Submitter addresses within 3 business days |
| `reject` | Paper is out of scope, or entry quality is unsalvageable | Close PR with explanation |

## Review Format

Reviewers should structure their review as:

```markdown
**Conclusion:** <one of the 4 options above>

**Strengths:**
- ...

**Issues (if any):**
- ...

**Suggestions (optional):**
- ...
```
