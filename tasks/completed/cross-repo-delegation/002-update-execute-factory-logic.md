# Add factory delegation logic to step-07-execute.md

## Context
When cycling encounters a task with Execution: factory, spawn agent with target repo path and command.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] step-06 updated (001)

## Requirements
- Edit `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder/references/step-07-execute.md`
- Add section: Factory Task Execution
- Logic: read `## Factory` section from task (target_repo, command, expected_output)
- Spawn Agent tool with prompt containing: target repo path, command to run, expected output to verify
- Wait for agent result, read output, continue cycling

## Acceptance Criteria
- [ ] step-07-execute.md has factory delegation section (verify: grep 'Factory Task')

## Gates Satisfied
BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
