# Write Gate Contract Template

## Context
Write the markdown template for loop gate contracts. Standard enforcement pattern for any loop.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/gate-contract-template.md`
- Standard gate contract format with sections: Pre-conditions (what must be true before loop runs), Post-conditions (what must be true after loop completes), Contract validation (input/output match), State integrity (no corruption)
- Include `[LOOP-NAME]` and `[DOMAIN-SPECIFIC]` placeholders
- Reference: `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/ability-saves/gate-contract.md`

## Acceptance Criteria
- [ ] File exists at specified path
- [ ] Contains "Pre-conditions" and "Post-conditions" sections
- [ ] Contains `[LOOP-NAME]` placeholder

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
