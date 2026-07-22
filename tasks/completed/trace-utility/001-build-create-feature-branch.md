# Create Feature Branch in Target Repo

## Context
Backlog 199 (V-BASE). All writes land on a feature branch; /kernel/review-queue accept merges to main.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" checkout -b build/199-qa-build-trace-utility main`
- Absolute paths; never cd

## Acceptance Criteria
- [ ] `git -C <target> branch --show-current` → `build/199-qa-build-trace-utility`

## Gates Satisfied
- TRC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
