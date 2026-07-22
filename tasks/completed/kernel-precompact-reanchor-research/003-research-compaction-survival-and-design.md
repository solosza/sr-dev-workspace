# Task 003 — Compaction Survival Audit + Hook Design

## Type
RESEARCH

## Description
Audit what currently survives compaction: how well the session_state.json context key re-injection performs today post-compaction. Then design the event-driven flow: PreCompact fires, hook sets anchored:false + writes a structured anchor payload, next tool call blocks, full /kernel/anchor runs on the fresh context. Validate the design against the existing universal-gate-enforcer flow.

## Acceptance Criteria
- [ ] File `projects/kernel-precompact-reanchor-research/02-compaction-survival-and-design.md` exists
- [ ] Covers: what survives compaction today (context key, workflow state, harness summary)
- [ ] Covers: full PreCompact-to-anchor flow design with state fields
- [ ] Covers: compatibility with existing gate-enforcer hooks
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001
