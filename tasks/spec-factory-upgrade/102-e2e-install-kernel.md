# Install Kernel into E2E Workspace

## Context
Copy kernel files for full enforcement.

## Type
TEST

## Dependencies
- 101

## Phase Gate
- [ ] E2E workspace exists (task 101)

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/CLAUDE.md`, .claude/, run-task.sh to e2e workspace

## Acceptance Criteria
- [ ] `CLAUDE.md` exists in e2e workspace (verify: file_exists)

## Gates Satisfied
INT-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
