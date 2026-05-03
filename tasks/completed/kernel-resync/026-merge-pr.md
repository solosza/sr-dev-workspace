# Merge PR to main

## Context
Merge v2 updates.

## Type
BUILD

## Execution
inline

## Dependencies
- 025

## Phase Gate
- [ ] PR created (025)

## Requirements
- Run `gh pr merge --repo isagawa-co/isagawa-kernel --merge` then `git -C C:/Users/solos/my_ai_projects/isagawa-kernel checkout main && git -C C:/Users/solos/my_ai_projects/isagawa-kernel pull`

## Acceptance Criteria
- [ ] Main includes v2 (verify: git log)

## Gates Satisfied
BUILD-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
