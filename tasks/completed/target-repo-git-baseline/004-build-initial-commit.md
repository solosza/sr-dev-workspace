# Create the Baseline Commit on Main

## Context
Backlog 198 (Wave 0): the baseline commit is what feature branches (build/NNN-*) fork from; /kernel/review-queue accept will merge them back to this main.

## Type
BUILD

## Execution
inline

## Dependencies
- 001, 002, 003

## Phase Gate
- [ ] `.gitignore` exists in target repo (GIT-02 passing)
- [ ] `README.md` exists in target repo (GIT-03 passing)

## Requirements
- `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" add -A`
- Commit with message: `baseline: repo init (.gitignore, README) — Wave 0, backlog 198`
- Absolute paths only — never cd

## Acceptance Criteria
- [ ] `git -C <target> log --oneline` exits 0 and shows ≥ 1 commit
- [ ] `git -C <target> status --porcelain` is empty (everything committed or ignored)
- [ ] Current branch is main

## Gates Satisfied
- GIT-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
