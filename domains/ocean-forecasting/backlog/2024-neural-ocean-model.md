---
title: "Neural General Circulation Models for Weather and Climate"
authors: ["Dmitrii Kochkov", "Janni Yuval", "Ian Langmore", "Peter Norgaard", "Jamie Smith", "Griffin Mooers", "Milan Klöwer", "James Lottes", "Stephan Rasp", "Peter Düben", "Sam Hatfield", "Peter Battaglia", "Alvaro Sanchez-Gonzalez", "Matthew Willson", "Michael P. Brenner", "Stephan Hoyer"]
year: 2024
venue: "Nature"
url: "https://arxiv.org/abs/2311.07222"
code_url: null
domain: "ocean-forecasting"
tags: ["forecasting", "physics-informed", "atmosphere"]
status: "backlog"
added_by: "lkun45598-lgtm"
added_date: "2026-03-29"
projects: ["ocean-sr"]
priority: "medium"
---

## One-Line Verdict

Hybrid neural GCM that embeds learned components within a differentiable dynamical core, achieving competitive multi-day forecasting while maintaining physical consistency — potentially a better paradigm than pure data-driven models for ocean applications where physics constraints matter.

## Project Relation

**ocean-sr**: The hybrid approach (learned + physics core) may inspire architectures for our SR pipeline where we want to preserve physical constraints (e.g., geostrophic balance) while learning fine-scale patterns.

## Why Noteworthy

Shows that hybrid neural-physical models can outperform both pure ML and pure physics models at medium-range forecasting. The differentiable dynamical core concept is directly relevant to our need for physics-constrained ocean modeling.

## Core Method

Replaces specific parameterizations within a traditional GCM with neural network components while keeping the dynamical core. The entire system is differentiable and trained end-to-end on reanalysis data.

## Hidden Assumptions & Weaknesses

- Code not publicly released (as of submission date)
- Computational cost likely higher than pure neural approaches like FourCastNet
- Tested primarily on atmospheric variables; ocean extension unclear

## Reading Advice

Focus on Section 2 (architecture of the hybrid model) and Section 4 (comparison with operational models). The supplementary materials contain important ablation studies.

## Reproduction Value

**Low for now** — no code release. Worth monitoring.

## Evidence

- Competitive with ECMWF's operational model for 5-10 day forecasting while maintaining physical conservation laws
- Demonstrates stable multi-year climate simulations (unlike most pure ML models)

## Notes

TODO: Revisit when code is released. The differentiable GCM paradigm deserves a deeper evaluation for ocean applications.
