# Prod Test: Hooks Fire Live

## Context
Level 3: verify hooks fire during real work.

## Type
TEST

## Dependencies
- 109, 110

## Phase Gate
- [ ] Kernel session works (109), run-task works (110)

## Requirements
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/state/*_workflow.json`
- Verify actions_since_anchor > 0

## Acceptance Criteria
- [ ] actions_since_anchor > 0 (verify: read JSON)

## Gates Satisfied
PROD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
