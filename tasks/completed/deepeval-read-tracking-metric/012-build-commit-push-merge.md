# Commit, Push, and Merge Feature Branch

## Context
All code is written and tests pass. Commit everything on the feature branch, push to remote, and merge to main.

## Type
BUILD

## Execution
inline

## Dependencies
- 011-test-run-read-compliance-tests

## Phase Gate
- [ ] All tests pass (task 011 complete)
- [ ] On branch `feature/143-read-tracking-metric`

## Requirements
- Stage all new/modified files in test-platform-deepeval
- Commit with message: "feat: add ReadComplianceMetric for procedure compliance evaluation"
- Push feature branch to origin
- Merge feature branch to main (fast-forward or merge commit)
- Push main to origin
- Do NOT delete the feature branch (leave for reference)

## Acceptance Criteria
- [ ] Feature branch pushed to origin
- [ ] Main branch contains all read-tracking metric files
- [ ] `git log --oneline -1` on main shows the merge/feature commit

## Gates Satisfied
- None (delivery task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
