# Add factory task handling to autonomous-cycling workflow.md

## Context
Cycling workflow needs to know how to handle Execution: factory tasks.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] step-07 updated (002)

## Requirements
- Edit `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/autonomous-cycling/workflow.md`
- Add to verification table: factory tasks verified by reading agent output
- Add note: factory tasks spawn agent in target repo, agent runs under that repo's kernel enforcement

## Acceptance Criteria
- [ ] workflow.md mentions factory execution (verify: grep 'factory')

## Gates Satisfied
BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
