# Task 002 — Compaction Survival Audit

## Type
RESEARCH

## Description
Audit state fidelity after a real compaction event in a live long session (not assumption — RULE ZERO): what survives from (1) session_state.json context key, (2) workflow JSON, (3) the harness-generated summary — and what is lost (failed-attempt history, decision rationale, terminal output). Use anchor-logs and any observed compactions as evidence.

## Acceptance Criteria
- [ ] File `projects/kernel-rolling-summarization-research/01-compaction-survival-audit.md` exists
- [ ] Covers: survival matrix for the three state layers
- [ ] Covers: concrete examples of lost signal from real sessions
- [ ] Covers: how DEFECT_LOG partially covers failed-attempt history
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001
