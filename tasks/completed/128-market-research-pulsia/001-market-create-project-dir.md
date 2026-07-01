# Create Project Directory

## Context
This is the foundational task. It creates the directory structure that all subsequent research tasks will write to. The structure includes `_research/` for working notes and `_test/` for test artifacts.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create `projects/pulsia-research/` directory
- Create subdirectories: `_research/`, `_test/fixtures/`, `_test/expected/`
- Create README.md with project description

## Acceptance Criteria
- [ ] Directory `projects/pulsia-research/` exists
- [ ] Subdirectories `_research/`, `_test/fixtures/`, `_test/expected/` exist
- [ ] `projects/pulsia-research/README.md` exists with project overview

## Gates Satisfied
- STRUCT-01 (project dir exists)

## Completion Signal
When all acceptance criteria are met, invoke `/kernel/complete`.
