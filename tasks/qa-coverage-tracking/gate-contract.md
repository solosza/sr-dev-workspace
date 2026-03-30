# Gate Contract — QA Coverage Tracking

## Verification Methods
→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Build Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | scanner.py has scan_coverage | grep | `grep -q 'scan_coverage' scanner.py` | Write |
| BUILD-02 | report.py has generate_report | grep | `grep -q 'generate_report' report.py` | Write |
| BUILD-03 | __init__.py exists | file_exists | `test -f __init__.py` | Write |
| BUILD-04 | generator.py has generate_skeleton_test | grep | `grep -q 'generate_skeleton' generator.py` | Write |
| BUILD-05 | test_template.py exists | file_exists | `test -f templates/test_template.py` | Write |
| BUILD-06 | cli.py has argparse/click | grep | `grep -q 'argparse\|click' cli.py` | Write |
| BUILD-07 | conftest has coverage hook | grep | `grep -q 'coverage' conftest.py` | Edit |
| BUILD-08 | MCP server uses scan_coverage | grep | `grep -q 'scan_coverage' server.py` | Edit |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | Scanner tests pass | run_test | pytest test_scanner.py exits 0 | Fix |
| FUNC-02 | Generator tests pass | run_test | pytest test_generator.py exits 0 | Fix |
| FUNC-03 | Real scan detects correct coverage | run_code | 7 fully mapped detected | Fix |
| FUNC-04 | Skeleton test created for gap | file_exists | test file created | Fix |

## Production Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PROD-01 | Full pipeline e2e | run_code | All 4 CLI commands work | Fix |

## Documentation Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Coverage docs written | file_exists | `test -f docs/coverage-tracking.md` | Write |

## Summary
- Build: 8, Functional: 4, Production: 1, Documentation: 1
- **Total: 14 gates**
