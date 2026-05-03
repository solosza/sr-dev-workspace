# Edit CLAUDE.md — Add execute-pipeline Command

## Context
CLAUDE.md lists all kernel commands. The new execute-pipeline command must be registered there so the agent knows it exists.

## Type
BUILD

## Execution
inline

## Dependencies
- 010 (command file must exist)

## Requirements
- Edit `CLAUDE.md`
- Add `execute-pipeline.md` to the Commands section, in the correct alphabetical position
- Add description: `← Backlog → tasks → run-task.sh (fully autonomous)`
- Do NOT modify any other content in CLAUDE.md

## Acceptance Criteria
- [ ] `grep -q 'execute-pipeline' CLAUDE.md` exits 0
- [ ] Entry appears in the Commands code block section

## Gates Satisfied
- BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
