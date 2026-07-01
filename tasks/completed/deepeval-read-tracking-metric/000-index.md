# DeepEval Read-Tracking Metric — Task Index

## Goal
Build ReadComplianceMetric + instrumentation + test fixtures + integration into existing 5-layer DeepEval architecture.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-write-read-compliance-metric]] | BUILD | 001 | pending |
| 003 | [[003-build-write-instrumentation-module]] | BUILD | 001 | pending |
| 004 | [[004-build-write-read-compliance-task]] | BUILD | 002, 003 | pending |
| 005 | [[005-build-write-golden-dataset]] | BUILD | 001 | pending |
| 006 | [[006-build-write-expected-results]] | BUILD | 005 | pending |
| 007 | [[007-build-write-pytest-test-file]] | BUILD | 002, 003, 004, 005, 006 | pending |
| 008 | [[008-build-update-metrics-init]] | BUILD | 002 | pending |
| 009 | [[009-build-update-tasks-init]] | BUILD | 004 | pending |
| 010 | [[010-build-update-metric-catalog]] | BUILD | 002 | pending |
| 011 | [[011-test-run-read-compliance-tests]] | TEST | 007, 008, 009 | pending |
| 012 | [[012-build-commit-push-merge]] | BUILD | 011 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- ReadComplianceMetric class in `framework/_reference/metrics/read_compliance_metrics.py`
- Instrumentation module in `framework/_reference/metrics/instrumentation.py`
- ReadComplianceEvalTask in `framework/_reference/tasks/run_read_compliance_eval.py`
- Golden dataset in `tests/fixtures/read-compliance/golden-dataset.json`
- Expected results in `tests/fixtures/read-compliance/expected-results.json`
- pytest test file at `tests/test_read_compliance.py`
- Updated metric catalog and package exports
