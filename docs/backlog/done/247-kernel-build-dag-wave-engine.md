# Build: DAG Wave Execution Engine for Swarm Dispatch

## Status
Open

## Priority
High — 241 verdict + combined 241/242/243 recommendation: the primary ordering mechanism; replaces manual sequencing and soft "read siblings if present" tolerance, both of which are incorrect under real dependencies.

## Summary
Implement the 241 YAH verdict in `/spawn-agent-swarm`: backlogs/task indexes declare `depends_on`, step-01 parses dependencies and runs Kahn's algorithm (BFS topological sort) to produce execution waves with cycle detection at sort time; step-03 dispatches only the current wave; a notification-driven barrier (not polling) dispatches Wave N+1 when Wave N completes, with partial dispatch on failure (only downstream dependents blocked) and a 30-minute per-wave timeout. Backward-compatible: no dependencies → single wave → current flat-parallel behavior. The 2026-07-21 two-wave 241/242→243 run is the manual prototype this automates.

## Requirements
- Dependency metadata format per `projects/kernel-dag-wave-research/01-metadata-and-sorting.md` (read it — it chose the format and parse rules); cycle detection rejects circular deps with a clear error BEFORE any spawn
- Wave sort in spawn-agent-swarm step-01; wave-scoped dispatch in step-03; `wave` field + wave plan in `agent-swarm.json` (already prototyped manually)
- Barrier per `02-barrier-monitor-and-failures.md`: notification-driven, failure semantics decision table implemented (fail/skip → block only dependents; independent agents proceed), orchestrator-restart resume from manifest
- Skill docs updated with wikilink tiered indexing (SKILL.md stays an index; wave logic in references/)
- L3 test: run a real 3-backlog dependent swarm (two independent + one dependent) and assert the dependent spawns only after both complete; plus a cycle-rejection test
- Reconciliation: update the STRICTLY-SEQUENTIAL lesson via /kernel/learn on completion (sequence = degenerate DAG; contention rationale satisfied by 244)

## References
- Backlogs done: 241, 243 (combined recommendation `projects/kernel-artifact-bus-research/03-combined-recommendation.md`)
- **Depends on: 244** (per-agent session-state isolation) — MUST be merged first
- `.claude/skills/spawn-agent-swarm/` (steps 01-05)

## Task Builder Input
- **Deliverable:** Wave-sorted dispatch in spawn-agent-swarm with barrier + failure semantics + L3 dependent-swarm test green
- **Location:** workspace:.claude/skills/spawn-agent-swarm/
- **Scope:** BUILD
- **Constraints:** BLOCKED until 244 accepted via /kernel/review-queue. Preserve the outer-agent pattern: run-task.sh remains the only execution path; flat invocations must behave exactly as today.
