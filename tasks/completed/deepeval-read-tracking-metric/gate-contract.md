# Gate Contract — DeepEval Read-Tracking Metric

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | ReadComplianceMetric file exists | file_exists | `test -f framework/_reference/metrics/read_compliance_metrics.py` | Create file |
| BUILD-02 | ReadComplianceMetric has evaluate method | grep | `grep -q "def evaluate" framework/_reference/metrics/read_compliance_metrics.py` | Add method |
| BUILD-03 | ReadComplianceMetric returns self | grep | `grep -q "return self" framework/_reference/metrics/read_compliance_metrics.py` | Fix return |
| BUILD-04 | Instrumentation module exists | file_exists | `test -f framework/_reference/metrics/instrumentation.py` | Create file |
| BUILD-05 | ReadComplianceEvalTask exists | file_exists | `test -f framework/_reference/tasks/run_read_compliance_eval.py` | Create file |
| BUILD-06 | Golden dataset exists | file_exists | `test -f tests/fixtures/read-compliance/golden-dataset.json` | Create file |
| BUILD-07 | Expected results exists | file_exists | `test -f tests/fixtures/read-compliance/expected-results.json` | Create file |
| BUILD-08 | Test file exists | file_exists | `test -f tests/test_read_compliance.py` | Create file |
| BUILD-09 | Metrics __init__ exports ReadComplianceMetric | grep | `grep -q "ReadComplianceMetric" framework/_reference/metrics/__init__.py` | Add export |
| BUILD-10 | Tasks __init__ exports eval task | grep | `grep -q "run_read_compliance_eval" framework/_reference/tasks/__init__.py` | Add export |
| BUILD-11 | Metric catalog updated | grep | `grep -q "ReadComplianceMetric" .claude/skills/deepeval-management-layer/references/metric-catalog.md` | Add entry |
| FUNC-01 | Metric computes correct score | run_test | `pytest tests/test_read_compliance.py::test_perfect_compliance -v` exits 0 | Fix scoring |
| FUNC-02 | Metric detects missing reads | run_test | `pytest tests/test_read_compliance.py::test_missing_reads -v` exits 0 | Fix detection |
| FUNC-03 | Metric handles empty reads | run_test | `pytest tests/test_read_compliance.py::test_empty_reads -v` exits 0 | Fix edge case |
| FUNC-04 | Instrumentation parses trace | run_test | `pytest tests/test_read_compliance.py::test_trace_parsing -v` exits 0 | Fix parser |
| TEST-01 | All tests pass | run_test | `pytest tests/test_read_compliance.py -v` exits 0 | Fix failures |
