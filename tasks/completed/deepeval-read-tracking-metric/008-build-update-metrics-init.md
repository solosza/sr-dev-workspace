# Update Metrics __init__.py

## Context
Export ReadComplianceMetric from the metrics package so it can be imported as `from framework._reference.metrics import ReadComplianceMetric`.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-write-read-compliance-metric

## Phase Gate
- [ ] `framework/_reference/metrics/read_compliance_metrics.py` exists

## Requirements
- Edit: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/framework/_reference/metrics/__init__.py`
- Add import: `from .read_compliance_metrics import ReadComplianceMetric`
- Add import: `from .instrumentation import ReadTraceParser`

## Acceptance Criteria
- [ ] `grep -q "ReadComplianceMetric" framework/_reference/metrics/__init__.py` passes
- [ ] `grep -q "ReadTraceParser" framework/_reference/metrics/__init__.py` passes

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
