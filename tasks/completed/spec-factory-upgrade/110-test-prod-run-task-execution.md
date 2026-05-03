# Prod Test: run-task.sh Execution

## Context
Level 3: actually run run-task.sh with a test task.

## Type
TEST

## Dependencies
- 020, 022

## Phase Gate
- [ ] run-task.sh exists (020), settings updated (022)

## Requirements
- Create test task at `C:/Users/solos/my_ai_projects/domain-spec-factory/tasks/test/001-create-marker.md`
- Spawn run-task.sh in background
- Wait for completion

## Acceptance Criteria
- [ ] Task in completed_tasks (verify: read workflow JSON)

## Gates Satisfied
PROD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
