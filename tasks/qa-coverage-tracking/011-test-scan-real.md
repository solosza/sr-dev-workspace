# Run scanner against actual framework

## Context
L2: verify scanner detects the correct coverage state.

## Type
TEST

## Execution
agent

## Dependencies
- 009

## Phase Gate
- [ ] Scanner tests pass (009)

## Requirements
- Run scanner against C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/
- Verify 7 fully mapped workflows detected (clawdbot, helios1, helios3, helios4, helios6, helios7, test10)
- Verify gaps detected (auth, catalog, helios2, parabank13)
- Report coverage percentage

## Acceptance Criteria
- [ ] Scanner detects correct fully-mapped count and gaps (verify: agent report)

## Gates Satisfied
FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
