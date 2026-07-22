# Write Canonical Identity Model Doc

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- Create `.claude/references/agent-identity-model.md`: define swarm run ID, backlog item ID, worker ID (task subfolder), task ID, worktree ID
- One mapping table showing how each state filename derives from exactly one ID kind (agent-{worker}-workflow.json, agent-{worker}-session-state.json, agent-{worker}-actions.jsonl, agent-{backlog}-state.json for swarm monitor, review-status keyed by backlog)
- Document the live bug this fixes: swarm monitor tracked backlog-ID files while run-task.sh wrote worker-ID files (0/5 forever, 2026-07-21)
- Wikilink the doc from the protocol References section (one line added to sr_dev-protocol.md References table is sanctioned by this user-approved pipeline)

## Acceptance Criteria
- [ ] Doc exists with 5 ID kinds + mapping table
- [ ] Protocol References table links it

## Gates Satisfied
- SI-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
