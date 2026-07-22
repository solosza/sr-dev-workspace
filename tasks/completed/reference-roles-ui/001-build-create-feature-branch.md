# Create Feature Branch

## Context
Backlog 207: all writes on the target-repo feature branch, never main.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform checkout -b build/207-qa-build-reference-roles-ui` (from main at the 206 merge 9ce512f or later)

## Acceptance Criteria
- [ ] Branch exists and is checked out; main untouched

## Gates Satisfied
- ROL-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
