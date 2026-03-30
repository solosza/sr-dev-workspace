# Merge feature/hook-fixes to main

## Context
1 commit: counter fix + auto-approve + anchor/complete.

## Type
BUILD

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] 002 merged

## Requirements
- Run `git -C C:/Users/solos/my_ai_projects/isagawa-kernel merge feature/hook-fixes`

## Acceptance Criteria
- [ ] Merge succeeds (verify: git log)

## Gates Satisfied
MERGE-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
