# Create Project Directory

## Context
Mandatory first task for subproject deliverables. Creates `projects/claude-agents-research/` so all subsequent research tasks have a location to write their output files.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create directory `projects/claude-agents-research/` in the workspace root

## Acceptance Criteria
- [ ] `projects/claude-agents-research/` exists (`test -d projects/claude-agents-research/`)

## Gates Satisfied
- DOC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
