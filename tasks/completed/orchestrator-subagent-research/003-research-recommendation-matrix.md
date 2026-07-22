# Per-Command Recommendation Matrix

## Context
Backlog 230: apply the survey's criteria to this workspace's actual commands.

## Type
RESEARCH
## Execution
inline
## Dependencies
- 001, 002
## Phase Gate
- [ ] 01-current-state.md and 02-industry-survey.md exist

## Requirements
- Read both prior outputs; do not re-research
- Evaluate AT MINIMUM: gap-check (per-check subagents?), eval platform (per-metric?), audit-workflow (per-scan?), task-builder plan review, walkthrough (composability contract exists), the vertical build chain's validate-merge-launch loop, /kernel/project-run outer-loop candidate (README Process note)
- Per command: verdict (stay-inline / orchestrator+subagents / hybrid), the criterion that decides it, cost acknowledged (latency/context/state), kernel governance implication (hooks + per-agent state)
- Write `projects/orchestrator-subagent-research/03-recommendation-matrix.md`

## Acceptance Criteria
- [ ] Matrix covers all named candidates with verdict + criterion + cost per row

## Gates Satisfied
- OSR-04, OSR-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
