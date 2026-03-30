# Test all hooks in kernel repo

## Context
L2: pipe test JSON, verify exits 0.

## Type
TEST

## Execution
agent

## Dependencies
- 015-018, 019

## Phase Gate
- [ ] All hooks + settings updated

## Requirements
- Pipe test JSON to each hook in C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/hooks/. Verify exits 0.

## Acceptance Criteria
- [ ] All hooks exit 0 (verify: run_code)

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
