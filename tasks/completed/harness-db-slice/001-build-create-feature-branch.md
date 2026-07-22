# Task 001: Create Feature Branch

**Type:** BUILD | **Gates:** DB-01

## Action
In `D:/my_ai_projects/project_test_repos/hmsa-qa-platform`: create branch `build/214-qa-build-harness-db-slice` from current main and check it out (ONE git operation). If the repo is on another branch with uncommitted work, stop and report — do not stash or discard.

## Acceptance
`git -C D:/my_ai_projects/project_test_repos/hmsa-qa-platform branch --show-current` prints the branch; merge-base equals main HEAD.
