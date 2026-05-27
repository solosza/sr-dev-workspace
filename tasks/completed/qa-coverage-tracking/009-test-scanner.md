# Write test for coverage scanner

## Context
Test scanner against known framework state.

## Type
TEST

## Execution
agent

## Dependencies
- 001

## Phase Gate
- [ ] scanner.py exists (001)

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/tests/coverage/test_scanner.py`
- Test scan_coverage() returns dict with known workflows
- Test that clawdbot has all 4 layers True
- Test that auth has tests=False
- Run pytest on this file

## Acceptance Criteria
- [ ] test_scanner.py exists and passes (verify: run_test)

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
