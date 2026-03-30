# Factory: Score SSH domain on 8 dimensions, calculate composite, BUILD/QUEUE decision

## Context
Score SSH domain on 8 dimensions, calculate composite, BUILD/QUEUE decision

## Type
BUILD

## Dependencies
- 045

## Phase Gate
- [ ] All Phase 3 tests passed (tasks 036-043 complete)

## Requirements
- Read spec factory step docs for process
- Score SSH domain on 8 dimensions, calculate composite, BUILD/QUEUE decision
- Output: `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-03-score.md`

## Acceptance Criteria
- [ ] `step-03-score.md` exists at output path (verify: file_exists)

## Gates Satisfied
FAC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
