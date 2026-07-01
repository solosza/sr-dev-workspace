# Write ReadComplianceEvalTask

## Context
Layer 3 EvalTask that composes ReadComplianceMetric. Loads required_reads from a task spec, loads actual_reads from instrumentation, runs the metric, returns None (per Layer 3 convention).

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-write-read-compliance-metric
- 003-build-write-instrumentation-module

## Phase Gate
- [ ] `framework/_reference/metrics/read_compliance_metrics.py` exists
- [ ] `framework/_reference/metrics/instrumentation.py` exists

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/framework/_reference/tasks/run_read_compliance_eval.py`
- Function `run_read_compliance_eval(required_reads: list[str], actual_reads: list[str], threshold: float = 1.0) -> None` that:
  - Creates `ReadComplianceMetric(required_reads, actual_reads, threshold)`
  - Calls `.evaluate()`
  - Checks `.is_above_threshold()`
  - Prints result summary (score, missed reads, extra reads)
  - Returns None (Layer 3 convention)
- Also: `run_read_compliance_from_trace(required_reads: list[str], trace_source: str, threshold: float = 1.0) -> None` that:
  - Uses `ReadTraceParser` to extract actual_reads from trace
  - Delegates to `run_read_compliance_eval`
- Docstring: `"""ReadComplianceEvalTask — Layer 3: Runs read compliance evaluation."""`

## Acceptance Criteria
- [ ] File exists at `framework/_reference/tasks/run_read_compliance_eval.py`
- [ ] `grep -q "def run_read_compliance_eval" framework/_reference/tasks/run_read_compliance_eval.py` passes
- [ ] `grep -q "return None" framework/_reference/tasks/run_read_compliance_eval.py` passes

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
