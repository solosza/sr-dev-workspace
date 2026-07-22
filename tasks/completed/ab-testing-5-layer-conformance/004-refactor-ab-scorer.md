# Task 004: Refactor ABScorer to Use L1+L2

## Action
Gut ABScorer's inline scoring logic — it should delegate to ABEvaluator (L4) or at minimum use ABMetrics (L2) via DeepEvalInterface (L1).

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/scorer.py` (current code)
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/ab_metrics.py` (task 001 output)
3. Refactor `scorer.py`:
   - Remove `DEFAULT_METRIC_CRITERIA` dict (now lives in ABMetrics)
   - Remove `_build_metrics()` (now handled by ABMetrics.evaluate())
   - Remove direct `from deepeval.metrics import GEval` and `from deepeval.test_case import ...`
   - `score_pair()` should create LLMTestCases via DeepEvalInterface, then call ABMetrics.evaluate()
   - `score_all_runs()` should use ABEvaluator.evaluate_experiment() or compose ABMetrics directly
   - Keep the file reading and directory iteration logic — that's I/O, not scoring

4. Import DeepEvalInterface in `__init__` of ABScorer, pass it through

## Acceptance Criteria
- No `from deepeval` imports in scorer.py
- `DEFAULT_METRIC_CRITERIA` removed (lives in ab_metrics.py)
- `_build_metrics()` removed
- Scoring delegates to ABMetrics.evaluate() via DeepEvalInterface
- `score_pair()` and `score_all_runs()` still produce the same output format (dict with run_id, scores)
- Existing experiment output format preserved (evals/eval-ab-*/results/scores.json)
