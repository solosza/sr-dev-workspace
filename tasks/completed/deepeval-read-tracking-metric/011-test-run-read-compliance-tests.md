# Run Read Compliance Tests

## Context
Execute the full pytest suite for the read compliance metric. Validates that the metric correctly scores perfect compliance, partial reads, missing reads, empty reads, trace parsing, and all golden dataset cases.

## Type
TEST

## Execution
agent

## Dependencies
- 007-build-write-pytest-test-file
- 008-build-update-metrics-init
- 009-build-update-tasks-init

## Phase Gate
- [ ] `tests/test_read_compliance.py` exists
- [ ] `framework/_reference/metrics/__init__.py` exports ReadComplianceMetric
- [ ] `framework/_reference/tasks/__init__.py` exports run_read_compliance_eval

## Requirements
- Run: `pytest tests/test_read_compliance.py -v --rootdir=D:/my_ai_projects/project_test_repos/test-platform-deepeval`
- All tests must pass
- If any test fails, read the failure output, identify root cause, fix the relevant source file, and re-run

## Acceptance Criteria
- [ ] `pytest tests/test_read_compliance.py -v` exits 0
- [ ] All test functions pass (test_perfect_compliance, test_missing_reads, test_empty_reads, test_extra_reads_still_pass, test_empty_required, test_trace_parsing, test_golden_dataset)

## Gates Satisfied
- FUNC-01, FUNC-02, FUNC-03, FUNC-04, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
