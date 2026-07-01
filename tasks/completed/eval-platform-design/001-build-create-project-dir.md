# Create Project Directory

## Context
The eval-platform-design deliverables go to `projects/eval-platform-design/`. This task creates the directory so all subsequent tasks can write their design documents there.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create directory `projects/eval-platform-design/`

## Acceptance Criteria
- [ ] `projects/eval-platform-design/` directory exists (`test -d projects/eval-platform-design/`)

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
