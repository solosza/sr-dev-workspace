# Install Kernel into Validation Workspace

## Context
Copy kernel infrastructure for enforcement testing.

## Type
TEST

## Dependencies
- 081

## Phase Gate
- [ ] Validation workspace exists (task 081)

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/CLAUDE.md` to workspace
- Copy .claude/ commands, hooks, state templates

## Acceptance Criteria
- [ ] `CLAUDE.md` exists in workspace root (verify: file_exists)

## Gates Satisfied
VAL-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
