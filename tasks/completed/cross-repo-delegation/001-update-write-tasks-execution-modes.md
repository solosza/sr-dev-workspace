# Add factory execution mode to step-06-write-tasks.md

## Context
Add `factory` as third execution mode alongside inline and agent. Factory tasks spawn an agent in a target repo.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Edit `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder/references/step-06-write-tasks.md`
- Add `factory` to Execution field: `inline | agent | factory`
- Add description: factory tasks spawn agent in target repo path, agent runs under that repo's kernel

## Acceptance Criteria
- [ ] step-06-write-tasks.md has 'factory' execution mode (verify: grep 'factory')

## Gates Satisfied
BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
