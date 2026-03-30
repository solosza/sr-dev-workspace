# Write cross-repo delegation reference doc

## Context
Reference doc explaining how factory delegation works: when to use, prompt format, verification.

## Type
BUILD

## Execution
inline

## Dependencies
- 003

## Phase Gate
- [ ] workflow updated (003)

## Requirements
- Write `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder/references/cross-repo-delegation.md`
- When to use: goal requires work in another repo (factory, template platform)
- Task format: ## Factory section with target_repo, command, expected_output
- Agent prompt template
- How parent verifies: read output, check expected files
- HUMAN REQUIRED handling: agent tries gh CLI, API calls first

## Acceptance Criteria
- [ ] cross-repo-delegation.md exists (verify: file_exists)

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
