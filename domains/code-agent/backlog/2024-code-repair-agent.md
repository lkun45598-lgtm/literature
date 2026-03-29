---
title: "Automated Code Repair with LLM Agents: Error Feedback and Iterative Refinement"
authors: ["Placeholder Author G", "Placeholder Author H"]
year: 2024
venue: "ICLR 2024"
url: "https://arxiv.org/abs/2404.00000"
code_url: "https://github.com/placeholder/code-repair-agent"
domain: "code-agent"
tags: ["code-generation", "tool-use", "llm"]
status: "backlog"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["agent-loss-migration"]
priority: "medium"
---

## One-Line Verdict

Demonstrates that structured error feedback (compiler errors, test failures, type mismatches) significantly improves LLM code repair over naive retry, achieving 85% repair rate on common bug patterns — the iterative refinement architecture is directly transferable to loss migration error recovery.

## Project Relation

**agent-loss-migration**: The error feedback loop architecture (try → fail → analyze error → retry with context) is the pattern we need for handling failed loss migration attempts where gradients break or tensor shapes mismatch.

## Why Noteworthy

The structured error feedback mechanism is generalizable beyond code repair. For loss migration, we can design analogous feedback: gradient check failures, shape mismatches, numerical divergence — all structured as actionable feedback for the agent.

## Core Method

LLM agent with error-aware retry: (1) attempt repair, (2) run tests, (3) parse error messages into structured feedback, (4) condition next attempt on error context. Uses a diminishing temperature schedule across retries.

## Hidden Assumptions & Weaknesses

- Tested only on well-defined bugs with clear error messages
- Scientific code errors (numerical instability, silent gradient issues) produce less informative feedback
- Limited to Python; no multi-language support

## Reading Advice

Focus on the error feedback structuring mechanism (Section 3) and the ablation on feedback types (Section 5).

## Reproduction Value

**Medium** — the feedback loop architecture is straightforward to implement; the value is in the design pattern, not the specific implementation.

## Evidence

- 85% repair rate on common bugs with structured feedback vs. 52% with naive retry
- Structured error parsing contributes more than additional retry attempts

## Notes

Consider combining SWE-agent's ACI with this paper's error feedback mechanism for our loss migration agent.
