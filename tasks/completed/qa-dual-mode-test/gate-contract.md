# Gate Contract — QA Dual-Mode Test

## Verification Methods
→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Structural Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Testbed cloned | file_exists | `test -d .../qa-dual-mode-testbed/` | Clone |
| BUILD-02 | Deps installed | run_code | pip install exits 0 | Fix |
| BUILD-03 | conftest.py logic identified | manual | Line noted | Read |
| BUILD-04 | Test files in testbed | file_exists | Test subdirs exist | Copy |
| BUILD-05 | .env has QA_FRAMEWORK_PATH | grep | `grep -q 'QA_FRAMEWORK_PATH' .env` | Create |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | conftest.py has env var override | grep | `grep -q 'QA_FRAMEWORK_PATH' conftest.py` | Modify |
| FUNC-02 | Mode A and Mode B results match | run_code | Same pass/fail counts | Fix |

## Test Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| TEST-01 | Mode A pytest runs | run_test | Output produced | Fix |
| TEST-02 | Mode A results parsed | manual | Counts documented | Parse |
| TEST-03 | Mode B pytest runs | run_test | Output produced | Fix |
| TEST-04 | Mode B results parsed | manual | Counts documented | Parse |

## Documentation Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Report written | file_exists | `test -f docs/research/qa-dual-mode-test-report.md` | Write |

## Production Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PROD-01 | Dual-mode e2e diff | run_code | Identical results excluding paths/timestamps | Fix |

## Requirements Coverage
Each gate maps to a task acceptance criterion.

## Summary
- Structural: 5, Functional: 2, Test: 4, Documentation: 1, Production: 1
- **Total: 13 gates**
