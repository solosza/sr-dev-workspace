# Task 004 — Hybrid Policy Comparison

## Type
RESEARCH

## Description
Compare three policies with token-cost estimates: (a) pure N-action timer (current), (b) pure event-driven PreCompact, (c) hybrid — event-driven primary with a raised-N timer fallback. Cover the failure mode where PreCompact never fires (short sessions, one-shot agents) and quantify anchor token cost per policy over a representative long pipeline run.

## Acceptance Criteria
- [ ] File `projects/kernel-precompact-reanchor-research/03-hybrid-policy.md` exists
- [ ] Covers: three-policy comparison table with token estimates
- [ ] Covers: failure modes per policy
- [ ] Covers: recommended policy with rationale
- [ ] Minimum 300 words

## Gate
DOC-05, DOC-06

## Dependencies
001
