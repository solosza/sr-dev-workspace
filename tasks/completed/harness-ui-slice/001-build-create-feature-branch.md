# Create Feature Branch

## Context
Backlog 202 (V1 opener). Branch from main (V-BASE merged: trace, retry, contract).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" checkout -b build/202-qa-build-harness-ui-slice main`

## Acceptance Criteria
- [ ] branch --show-current → build/202-qa-build-harness-ui-slice

## Gates Satisfied
- HUI-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
