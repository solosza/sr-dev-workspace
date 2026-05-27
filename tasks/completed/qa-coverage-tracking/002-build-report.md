# Write framework/coverage/report.py

## Context
Generates coverage report from scanner output. JSON + markdown formats.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] scanner.py exists (001)

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework/coverage/report.py`
- Function `generate_report(coverage_data, format='markdown')` that:
- Calculates: total workflows, fully covered count, gap count, coverage percentage
- Markdown format: table with workflow | pages | tasks | roles | tests columns
- JSON format: structured dict with same data
- Returns formatted string (markdown) or dict (JSON)

## Acceptance Criteria
- [ ] `report.py` exists and has `generate_report` function (verify: file_exists + grep)

## Gates Satisfied
BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
