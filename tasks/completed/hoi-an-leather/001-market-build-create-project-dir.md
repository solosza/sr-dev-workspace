# Create projects/hoi-an-leather/ Directory

## Context
Setup task. Creates the subproject root directory for all research deliverables. All subsequent tasks write files into this directory.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create directory `projects/hoi-an-leather/` at the workspace root

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/` directory exists (`test -d projects/hoi-an-leather/`)

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
