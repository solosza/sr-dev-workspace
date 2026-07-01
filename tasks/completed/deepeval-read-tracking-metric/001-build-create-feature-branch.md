# Create Feature Branch for Read-Tracking Metric

## Context
Create a feature branch in the test-platform-deepeval repo to isolate all read-tracking metric work. This keeps main clean until all tests pass.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create branch `feature/143-read-tracking-metric` from main in `D:/my_ai_projects/project_test_repos/test-platform-deepeval`
- Create `tests/fixtures/read-compliance/` directory for golden datasets

## Acceptance Criteria
- [ ] Branch `feature/143-read-tracking-metric` exists in test-platform-deepeval
- [ ] `tests/fixtures/read-compliance/` directory exists
- [ ] `git branch --show-current` outputs `feature/143-read-tracking-metric`

## Gates Satisfied
- None (setup task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
