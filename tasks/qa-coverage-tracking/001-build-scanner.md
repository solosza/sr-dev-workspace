# Write framework/coverage/scanner.py

## Context
Scans tests/, pages/, tasks/, roles/ directories. Builds coverage matrix by matching directory names across layers.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework/coverage/scanner.py`
- Function `scan_coverage(root_path)` that:
- Lists all subdirs in tests/, pages/, tasks/, roles/
- For each unique workflow name, checks which layers have it
- Returns dict: {workflow: {tests: bool, pages: bool, tasks: bool, roles: bool}}
- Excludes internal dirs (_audit, _reports, _state, __pycache__, common, guest, data)

## Acceptance Criteria
- [ ] `scanner.py` exists and has `scan_coverage` function (verify: file_exists + grep)

## Gates Satisfied
BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
