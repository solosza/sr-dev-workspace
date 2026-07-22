# Create Loop Template Directory Structure

## Context
Create the generalized loop template directory in the workspace. This template is repo-agnostic — any project with loops instantiates from it. The D&D game engine is the first consumer.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create directory structure at `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/`
- Subdirectories: `contracts/`, `references/`, `_test/fixtures/`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/` exists
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/contracts/` exists
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/references/` exists
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/_test/fixtures/` exists

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
