# Copy new lessons to factory

## Context
Do not overwrite factory-specific lessons.

## Type
BUILD

## Execution
inline

## Dependencies
- 026

## Phase Gate
- [ ] Kernel main updated (026)

## Requirements
- Copy task-atomicity.md, testing-completeness.md, autonomous-cycling-lesson.md from sr-dev-workspace to factory lessons dir

## Acceptance Criteria
- [ ] task-atomicity.md exists in factory (verify: file_exists)

## Gates Satisfied
SYNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
