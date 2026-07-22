# Write Integration Contract Template

## Context
Write the JSON template for loop integration contracts. Defines how a loop connects to its caller (outer loop) and callees (inner/downstream loops).

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/integration-template.json`
- JSON schema per design doc `docs/backlog/180-domain-build-dnd-game-loop-integration/integration-contracts.md`
- Fields: `loop_name`, `invoked_by` (array of caller loops), `receives` (what caller passes), `returns` (what caller expects back), `downstream_invocations` (array of loops this loop calls, with `loop`, `when`, `mandatory` fields)

## Acceptance Criteria
- [ ] File exists and is valid JSON
- [ ] Contains `loop_name`, `invoked_by`, `receives`, `returns`, `downstream_invocations` keys

## Gates Satisfied
- BUILD-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
