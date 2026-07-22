# Create Feature Branch

## Context
Backlog 209: all writes on the target-repo feature branch.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform checkout -b build/209-qa-build-harness-api-slice` from main (at 207 merge 19f1686 or later)

## Acceptance Criteria
- [ ] Branch exists, checked out; main untouched

## Gates Satisfied
- API-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
