# Create Feature Branch

## Context
Backlog 203 (V1). Branch from main (now carrying V-BASE + the Orderly harness).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" checkout -b build/203-qa-build-browser-interface main`

## Acceptance Criteria
- [ ] branch --show-current → build/203-qa-build-browser-interface

## Gates Satisfied
- BRI-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
