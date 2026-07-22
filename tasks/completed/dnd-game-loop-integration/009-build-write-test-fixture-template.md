# Write Test Fixture Template

## Context
Write the JSON template for loop test fixtures. Standardizes scenario-based testing for any loop.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/_test/fixtures/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/_test/fixtures/scenario-template.json`
- Standard test fixture format with sections: test_cases array (id, name, description, input, expected_output, validation), coverage summary
- Each test case has input matching input-contract fields, expected_output matching output-contract fields, and validation checks
- Include `[DOMAIN-SPECIFIC]` and `[LOOP-NAME]` placeholders
- Reference: `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/ability-saves/_test/fixtures/success-scenario.json`

## Acceptance Criteria
- [ ] File exists at specified path
- [ ] Contains "test_cases" array with at least one template entry
- [ ] Contains `[DOMAIN-SPECIFIC]` placeholder
- [ ] Each test case has "input", "expected_output", and "validation" keys

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
