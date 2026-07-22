# Create Feature Branch

## Context
Backlog 206: all writes happen on the target-repo feature branch, never main.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform checkout -b build/206-qa-build-reference-tasks-browser` (from main, which must be at the 205/MCP merges or later)

## Acceptance Criteria
- [ ] Branch exists and is checked out; main untouched

## Gates Satisfied
- TSK-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
