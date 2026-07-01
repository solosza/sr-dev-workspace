# Write ReadComplianceMetric Class

## Context
Layer 2 Metric Object that scores whether an agent read the required files before generating output. Follows the same pattern as `custom_metrics.py` and `agent_metrics.py` — constants for thresholds, `evaluate()` returns self, `is_above_threshold()` and `get_score()` for state checks.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-feature-branch

## Phase Gate
- [ ] Branch `feature/143-read-tracking-metric` is checked out

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/framework/_reference/metrics/read_compliance_metrics.py`
- Class `ReadComplianceMetric` with:
  - `DEFAULT_THRESHOLD = 1.0` (all required files must be read)
  - `__init__(self, required_reads: list[str], actual_reads: list[str], threshold: float = None)`
  - `evaluate(self) -> "ReadComplianceMetric"` — computes compliance score: `|required ∩ actual| / |required|`, stores in `_scores["compliance"]`. Also computes coverage: `|required ∩ actual| / |actual|` (noise detection), stores in `_scores["coverage"]`. Returns self.
  - `is_above_threshold(self, metric_name: str = "compliance") -> bool`
  - `get_score(self, metric_name: str = "compliance") -> float`
  - `get_detail(self, metric_name: str = "compliance") -> dict` — returns missed reads, extra reads, score, reason
- No DeepEval LLM judge dependency — this is a deterministic metric (set comparison), not an LLM-as-judge metric
- Docstring: `"""ReadComplianceMetric — Layer 2: Measures whether required files were read before generation."""`

## Acceptance Criteria
- [ ] File exists at `framework/_reference/metrics/read_compliance_metrics.py`
- [ ] `grep -q "def evaluate" framework/_reference/metrics/read_compliance_metrics.py` passes
- [ ] `grep -q "return self" framework/_reference/metrics/read_compliance_metrics.py` passes
- [ ] `grep -q "DEFAULT_THRESHOLD" framework/_reference/metrics/read_compliance_metrics.py` passes

## Gates Satisfied
- BUILD-01, BUILD-02, BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
