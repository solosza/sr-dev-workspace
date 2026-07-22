# Write Output Contract Template

## Context
Write the JSON template for loop output contracts. Defines what a loop returns to its caller.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/output-template.json`
- JSON schema with fields: `loop_name`, `returns` (object with typed fields), `result_codes` (array of valid result strings), `state_updates` (object describing what state fields change), `narration_required` (boolean)

## Acceptance Criteria
- [ ] File exists and is valid JSON
- [ ] Contains `loop_name`, `returns`, `result_codes`, `state_updates` keys

## Gates Satisfied
- BUILD-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
