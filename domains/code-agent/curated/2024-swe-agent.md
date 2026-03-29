---
title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
authors: ["John Yang", "Carlos E. Jimenez", "Alexander Wettig", "Kilian Lieret", "Shunyu Yao", "Karthik Narasimhan", "Ofir Press"]
year: 2024
venue: "NeurIPS 2024"
url: "https://arxiv.org/abs/2405.15793"
code_url: "https://github.com/princeton-nlp/SWE-agent"
domain: "code-agent"
tags: ["code-generation", "tool-use", "planning", "llm"]
status: "curated"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["agent-loss-migration"]
priority: "high"
---

## One-Line Verdict

Introduces the Agent-Computer Interface (ACI) concept showing that carefully designed tool interfaces dramatically improve LLM coding performance, resolving 12.5% of SWE-bench issues — but limited to well-scoped single-file bug fixes and does not address multi-file code migration or domain-specific scientific code understanding.

## Project Relation

**agent-loss-migration**: The ACI design principles are directly applicable — our loss migration agent needs well-designed interfaces for reading/modifying loss functions across files. However, loss migration requires understanding mathematical semantics (not just code syntax), which SWE-agent does not address.

## Why Noteworthy

Demonstrates that the bottleneck in LLM coding agents is not model capability but interface design. The ACI concept — giving the agent carefully curated tools for file navigation, editing, and testing — is the design paradigm we should adopt for our loss migration agent. The open-source implementation provides a solid starting framework.

## Core Method

SWE-agent wraps an LLM (GPT-4, Claude) with a custom Agent-Computer Interface (ACI): (1) a file viewer with search, scroll, and context commands; (2) a structured edit tool that shows diffs; (3) a test runner for verification; (4) a linter for syntax checking. The agent iterates: read code → form hypothesis → edit → test → refine. Key insight: traditional terminal interfaces overwhelm LLMs; the ACI filters and structures information to match LLM processing strengths.

## Hidden Assumptions & Weaknesses

- **Single-issue scope**: Each SWE-bench task is a well-defined bug fix. Loss function migration involves understanding intent across multiple files and ensuring semantic equivalence — fundamentally harder.
- **No mathematical reasoning**: SWE-agent treats code as text. It cannot verify that a migrated loss function is mathematically equivalent to the original.
- **Repository-scale limitation**: Struggles with large codebases where the relevant code spans many files. Our scientific projects typically have deeply interconnected modules.
- **No domain knowledge**: Cannot leverage domain-specific constraints (e.g., loss functions must be differentiable, must handle specific tensor shapes).
- **Evaluation bias**: SWE-bench favors well-documented Python projects with good test coverage. Scientific code often lacks both.

## Reading Advice

- **Read carefully**: Section 3 (ACI design principles), Section 4 (ablation studies on different interface choices), Table 1 (comparison with other agents)
- **Skim**: Section 5 (SWE-bench results breakdown — informative but not directly applicable)
- **Look for**: The specific tool definitions and how they constrain the action space — this is the transferable design pattern
- **Prerequisite**: Familiarity with LLM tool use / function calling

## Reproduction Value

**High**. Fully open-source, well-documented, actively maintained. The framework can be forked and adapted for our loss migration task. Main effort: designing domain-specific tools (loss function parser, semantic equivalence checker, tensor shape validator). Estimated effort: 2-3 weeks to adapt the framework, ongoing iteration on tool design.

## Evidence

1. **Table 1**: SWE-agent resolves 12.47% of SWE-bench issues vs. 3.8% for unassisted GPT-4 — 3.3x improvement from ACI alone
2. **Table 3**: Ablation shows that removing the structured edit tool drops performance by 40% — confirming tool interface is the key factor
3. **Figure 4**: Average 5.2 edit-test cycles per resolved issue — iterative refinement is essential, not one-shot generation
4. **Section 4.3**: File viewer with context window management outperforms full-file dumps by 2x — information filtering matters

## Notes

- Key design transfer: our loss migration agent should have tools for (1) parsing loss function signatures, (2) extracting mathematical operations as AST, (3) comparing tensor shape flows, (4) running gradient checks.
- The iterative edit-test cycle is promising for loss migration — migrate → test → check gradients → refine.
- Consider combining with code-repair-agent entry for error recovery patterns.
