# Create Project Directory

## Context
Subproject location requires the `projects/hoi-an-knockoff-shirts/` directory to exist before any research files can be written. This is a mandatory setup task — all subsequent tasks write their deliverables here.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create `projects/hoi-an-knockoff-shirts/` directory in the workspace

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists (`test -d projects/hoi-an-knockoff-shirts/`)

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
