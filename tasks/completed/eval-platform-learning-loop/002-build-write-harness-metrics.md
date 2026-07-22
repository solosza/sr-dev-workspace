# Write harness_metrics.py

## Context
Universal GEval criteria for harness evaluation. Criteria are architecture-agnostic — they define WHAT to measure. Per-harness architecture notes are passed separately via LLMTestCase.context. The `make_geval_metric()` function accepts `use_context=True` to include CONTEXT in evaluation_params.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (metrics dir exists)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/` directory exists

## Requirements
- Copy from `D:/my_ai_projects/project_test_repos/eval-kernel-minimal-test/framework/metrics/harness_metrics.py`
- Write to `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py`
- Preserve v2 criteria, `use_context` parameter, `DIMENSION_THRESHOLDS`, `DIMENSION_CRITERIA`
- Do NOT modify the content — this is a direct copy

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` exists
- [ ] File contains `def make_geval_metric` function
- [ ] File contains `use_context` parameter

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
