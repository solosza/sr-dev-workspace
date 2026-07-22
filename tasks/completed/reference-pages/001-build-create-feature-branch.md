# Create Feature Branch

## Context
Backlog 204 (V1). Branch from main (BrowserInterface now merged).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" checkout -b build/204-qa-build-reference-pages main`

## Acceptance Criteria
- [ ] branch --show-current → build/204-qa-build-reference-pages

## Gates Satisfied
- PAG-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
