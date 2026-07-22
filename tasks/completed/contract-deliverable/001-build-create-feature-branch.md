# Create Feature Branch

## Context
Backlog 201 (V-BASE, last item). Branch from main (now carrying trace.py + retry.py).

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" checkout -b build/201-qa-build-contract-deliverable main`

## Acceptance Criteria
- [ ] branch --show-current → build/201-qa-build-contract-deliverable

## Gates Satisfied
- CON-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
