# Commit Branch

## Type
BUILD
## Execution
inline
## Dependencies
- 004

## Requirements
- `git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform add framework/_reference/tests/ && git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform commit` on build/208-qa-build-reference-tests-ui with a descriptive message
- NO merge to main — merge happens via /kernel/review-queue accept (orchestrator concern)

## Acceptance Criteria
- [ ] Commit on branch; `git status --porcelain` clean; main untouched

## Gates Satisfied
- UT-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
