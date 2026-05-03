# Analyze Architectural Gaps

## Type
RESEARCH

## Description
Identify what would need to change in the Isagawa harness to support full agent swarms/teams: parallel task execution (currently sequential), agent identity/persistence (currently one-shot), inter-agent communication (currently via files/state), visual dashboard (currently terminal-only). For each gap, assess: effort, value, and whether it's necessary or nice-to-have.

## Depends On
- 002 (codebase mapping — know current architecture)
- 003 (dedicated-job agents — know current specialization patterns)

## Deliverable
`projects/kernel-architecture/swarms-architectural-gaps.md`

## Acceptance Criteria
- [ ] `projects/kernel-architecture/swarms-architectural-gaps.md` exists
- [ ] Covers: parallel execution, agent persistence, inter-agent comms, visual dashboard
- [ ] Each gap has effort/value/necessity assessment
