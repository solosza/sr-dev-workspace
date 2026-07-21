# Seed Per-Agent Session State

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- In run-task.sh, before the first iteration: create agent-{worker-id}-session-state.json with the same anchored/one_shot template it already seeds for the workflow file
- Skip creation if the file already exists (resume support)

## Acceptance Criteria
- [ ] Seed logic present; resume-safe

## Gates Satisfied
- SI-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
