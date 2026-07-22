# Task 003 — Barrier Monitor + Failure Semantics

## Type
RESEARCH

## Description
Design the barrier monitor: the current swarm monitor polls per-agent state files with a 5-minute cap, while waves need a long-lived barrier that dispatches Wave N+1 when all of Wave N exits COMPLETE. Reconcile with the background-task notification flow (runner exit notifications) vs. polling. Define failure semantics: if a Wave N agent fails or is skipped, does Wave N+1 block entirely, dispatch partially (only children whose specific prerequisites completed), or time out? Cover orphaned-wave cleanup and resume after orchestrator restart.

## Acceptance Criteria
- [ ] File `projects/kernel-dag-wave-research/02-barrier-monitor-and-failures.md` exists
- [ ] Covers: barrier mechanism design (poll vs notification-driven) with timeout policy
- [ ] Covers: failure semantics decision table (fail/skip/timeout x block/partial/abort)
- [ ] Covers: resume behavior if the orchestrator session restarts mid-wave
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001
