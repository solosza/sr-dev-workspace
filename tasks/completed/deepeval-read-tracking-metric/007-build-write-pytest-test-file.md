# Write Pytest Test File

## Context
Test file that validates ReadComplianceMetric and ReadTraceParser against the golden dataset. Uses @pytest.mark.parametrize to iterate over all test cases. Tests: perfect compliance, missing reads, empty reads, trace parsing.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-write-read-compliance-metric
- 003-build-write-instrumentation-module
- 004-build-write-read-compliance-task
- 005-build-write-golden-dataset
- 006-build-write-expected-results

## Phase Gate
- [ ] `framework/_reference/metrics/read_compliance_metrics.py` exists
- [ ] `framework/_reference/metrics/instrumentation.py` exists
- [ ] `framework/_reference/tasks/run_read_compliance_eval.py` exists
- [ ] `tests/fixtures/read-compliance/golden-dataset.json` exists
- [ ] `tests/fixtures/read-compliance/expected-results.json` exists

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/tests/test_read_compliance.py`
- Test functions:
  - `test_perfect_compliance` — all required files read, score = 1.0, passes threshold
  - `test_missing_reads` — some required files not read, score < 1.0, detects missed files
  - `test_empty_reads` — no files read when required, score = 0.0
  - `test_extra_reads_still_pass` — all required plus extras, compliance = 1.0
  - `test_empty_required` — nothing required, should pass trivially
  - `test_trace_parsing` — ReadTraceParser correctly extracts file paths from JSONL trace
  - `test_golden_dataset` — parametrized over all cases from golden-dataset.json, validates scores match expected-results.json
- Uses `@pytest.fixture` for loading golden dataset and expected results
- Imports from `framework._reference.metrics.read_compliance_metrics` and `framework._reference.metrics.instrumentation`
- All paths use `pathlib.Path` relative to test file location

## Acceptance Criteria
- [ ] File exists at `tests/test_read_compliance.py`
- [ ] `grep -q "def test_perfect_compliance" tests/test_read_compliance.py` passes
- [ ] `grep -q "def test_missing_reads" tests/test_read_compliance.py` passes
- [ ] `grep -q "def test_trace_parsing" tests/test_read_compliance.py` passes
- [ ] `grep -q "def test_golden_dataset" tests/test_read_compliance.py` passes

## Gates Satisfied
- BUILD-08, FUNC-01, FUNC-02, FUNC-03, FUNC-04, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
