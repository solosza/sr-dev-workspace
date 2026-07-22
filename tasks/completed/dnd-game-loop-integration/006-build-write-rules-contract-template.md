# Write Rules Contract Template

## Context
Write the JSON template for loop rules contracts. Defines the mechanics/logic a loop applies deterministically.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/rules-template.json`
- JSON schema with fields: `loop_name`, `mechanics` (array of rule objects with `name`, `source`, `when`, `then`), `constraints` (what the loop must NOT do), `randomization` (dice/RNG rules if applicable)

## Acceptance Criteria
- [ ] File exists and is valid JSON
- [ ] Contains `loop_name`, `mechanics`, `constraints` keys

## Gates Satisfied
- BUILD-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
