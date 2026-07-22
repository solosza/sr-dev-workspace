# Task 003 — Wait/Poll Loop + Monitor Visibility

## Type
RESEARCH

## Description
Design the wait/poll loop: poll interval, timeout, and timeout behavior (skip per the 3-attempt cycling contract vs. abort vs. mark BLOCKED). The WAIT must happen in run-task.sh BEFORE agent spawn, keeping the one-shot contract unchanged. Define how per-agent state exposes WAITING vs RUNNING so the swarm monitor does not false-positive a waiting agent as stalled/failed. Quantify the cost of a polling runner holding a process open vs. backlog 241's approach of not spawning downstream agents at all.

## Acceptance Criteria
- [ ] File `projects/kernel-barrier-gate-research/02-wait-loop-design.md` exists
- [ ] Covers: loop parameters + timeout behavior decision
- [ ] Covers: WAITING state exposure in per-agent state files + monitor rule changes
- [ ] Covers: cost comparison vs wave-based non-spawning
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001
