# Task 004 — Deadlock + Staleness Analysis

## Type
RESEARCH

## Description
Analyze failure modes: two agents waiting on each other's outputs (deadlock) — detection or prevention, with timeout as backstop, compared to 241's sort-time cycle detection; stale prerequisite files from prior runs satisfying gates incorrectly; and partial upstream outputs (file exists but task later skipped). Recommend standalone adoption vs. defense-in-depth under the wave engine (backlog 241).

## Acceptance Criteria
- [ ] File `projects/kernel-barrier-gate-research/03-deadlock-and-staleness.md` exists
- [ ] Covers: deadlock scenario analysis with prevention/detection recommendation
- [ ] Covers: staleness and partial-output failure modes with mitigations
- [ ] Covers: standalone vs defense-in-depth recommendation
- [ ] Minimum 300 words

## Gate
DOC-05, DOC-06

## Dependencies
001
