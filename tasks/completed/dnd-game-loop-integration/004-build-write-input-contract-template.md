# Write Input Contract Template

## Context
Write the JSON template for loop input contracts. Defines what a loop receives from its caller.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/input-template.json`
- JSON schema with fields: `loop_name`, `receives` (object with typed fields), `required_context` (array of prerequisite state keys), `validation` (input validation rules)
- Include `[DOMAIN-SPECIFIC]` comments for domain-customizable fields

## Acceptance Criteria
- [ ] File exists and is valid JSON
- [ ] Contains `loop_name`, `receives`, `required_context`, `validation` keys

## Gates Satisfied
- BUILD-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
