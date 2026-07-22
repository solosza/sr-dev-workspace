# Task 004 — Integration Design vs State-Contention Lessons

## Type
RESEARCH

## Description
Design what expanded ephemeral execution would look like in the kernel: which workflows move to sub-agents (orchestrator-per-vertical?), the state handoff schema, and the anchor policy per agent tier (orchestrator vs one-shot). Reconcile against lessons.md multi-agent state isolation, state contention, and backlog 183 worktree isolation. Identify hard blockers.

## Acceptance Criteria
- [ ] File `projects/kernel-ephemeral-subagents-research/03-integration-design.md` exists
- [ ] Covers: candidate workflows to move, with anchor policy per tier
- [ ] Covers: state handoff schema proposal
- [ ] Covers: reconciliation with state-contention lessons + blockers
- [ ] Minimum 300 words

## Gate
DOC-05, DOC-06

## Dependencies
001
