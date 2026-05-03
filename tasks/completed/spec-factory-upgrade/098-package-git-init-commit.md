# Git Init + Commit

## Context
Initialize repo and create initial commit.

## Type
BUILD

## Dependencies
- 097

## Phase Gate
- [ ] README verified (task 097)

## Requirements
- `git -C C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing init`
- `git -C C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing add -A`
- `git -C C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing commit -m 'feat: SSH spec'`

## Acceptance Criteria
- [ ] `.git/` exists and git log shows commit (verify: run_code)

## Gates Satisfied
PKG-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
