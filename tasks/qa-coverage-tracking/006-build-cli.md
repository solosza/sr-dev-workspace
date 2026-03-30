# Write framework/coverage/cli.py

## Context
CLI commands: scan, report, generate, check. Can be run standalone or as pytest plugin.

## Type
BUILD

## Execution
inline

## Dependencies
- 002, 004

## Phase Gate
- [ ] report.py (002) and generator.py (004) exist

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework/coverage/cli.py`
- Uses argparse or click
- Commands: scan (show matrix), report (full report), generate (create skeleton tests), check (pass/fail against threshold)
- `check` returns exit 0 if coverage >= threshold (default 80%), exit 1 otherwise
- Callable as: `python -m framework.coverage.cli scan`

## Acceptance Criteria
- [ ] `cli.py` exists and has argparse/click setup (verify: file_exists + grep 'argparse\|click')

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
