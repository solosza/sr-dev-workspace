# Task 004 — Lesson Reconciliation + Cross-Proposal Comparison

## Type
RESEARCH

## Description
Reconcile waves with the STRICTLY-SEQUENTIAL multi-backlog lesson in lessons.md: sequence is a degenerate DAG, so confirm the lesson's contention rationale is satisfied by per-agent state isolation before allowing intra-wave parallelism — cite the 2026-07-21 live evidence (session_state overwrites during swarm 237-240). Then compare against Proposal 2 (task-level barrier gates, backlog 242) and Proposal 3 (artifact bus, backlog 243): which layer should own ordering, and how the three compose without redundancy.

## Acceptance Criteria
- [ ] File `projects/kernel-dag-wave-research/03-lesson-reconciliation-and-comparison.md` exists
- [ ] Covers: STRICTLY-SEQUENTIAL lesson analysis with contention evidence
- [ ] Covers: layer-ownership comparison vs backlogs 242/243
- [ ] Covers: composition proposal (which layers coexist, which is primary)
- [ ] Minimum 300 words

## Gate
DOC-05, DOC-06

## Dependencies
001
