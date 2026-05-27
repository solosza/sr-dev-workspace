# Implement get_test_coverage() in MCP server

## Context
The MCP server has an unimplemented get_test_coverage() method. Wire it to the scanner.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] scanner.py exists (001)

## Requirements
- Edit `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/mcp_server/server.py`
- Find the `get_test_coverage()` method (currently returns 'not_implemented')
- Import scanner module
- Return coverage data as JSON from scan_coverage()

## Acceptance Criteria
- [ ] get_test_coverage returns real data (verify: grep 'scan_coverage' in server.py)

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
