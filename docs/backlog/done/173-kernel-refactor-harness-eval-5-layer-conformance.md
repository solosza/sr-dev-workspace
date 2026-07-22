# Refactor Harness Eval Tests to 5-Layer Eval Architecture

## Status
Open

## Priority
High — harness_metrics.py exists at L2 but nothing uses it; test_eval_harness.py bypasses all layers

## Summary
The harness evaluation test suite (test_eval_harness.py) bypasses the 5-layer architecture the same way the A/B framework does. It creates GEval metrics inline with hardcoded criteria strings, calls assert_test() directly (skipping DeepEvalInterface retry/logging), and has no Metric Objects, EvalTasks, or EvalRole. Meanwhile harness_metrics.py already exists with make_geval_metric(), DIMENSION_CRITERIA, and DIMENSION_THRESHOLDS — but nothing calls it. The reference implementations (_reference/) follow the pattern correctly; the actual production code does not.

## Requirements

### L1: DeepEvalInterface
- test_eval_harness.py must use DeepEvalInterface.measure_metric() instead of raw metric.measure() / assert_test()
- Gets retry logic (3 retries, exponential backoff) and logging for free
- Remove direct `from deepeval import assert_test` and `from deepeval.metrics import GEval` — go through L1

### L2: Metric Objects — Wire Up harness_metrics.py
- Create HarnessMetrics class following the CustomMetrics pattern (evaluate() returns self, is_above_threshold(), get_score())
- Use the existing DIMENSION_CRITERIA and DIMENSION_THRESHOLDS from harness_metrics.py — don't duplicate
- Use make_geval_metric() factory — it already exists and handles context injection
- Wire in architecture_notes.py context via use_context=True where applicable
- Remove all inline criteria strings from test_eval_harness.py

### L3: EvalTasks
- Create run_harness_eval() function composing HarnessMetrics
- One function per eval operation (or one for all 5 dimensions)
- Returns None — results accessed via Metric Object state-checks

### L4: EvalRoles
- Create HarnessEvaluator role class orchestrating the 5 dimensions
- Composes L3 EvalTasks
- Handles harness discovery (commands, skills, hooks, CLAUDE.md)
- Replaces the current flat test file structure

### L5: Tests
- Refactor test_eval_harness.py to use AAA pattern
- Assert via HarnessMetrics.is_above_threshold() — not raw assert_test()
- Keep @pytest.mark.parametrize for command quality (already correct)
- Conftest fixtures already exist and are fine

### Cleanup
- harness_metrics.py stops being orphaned — HarnessMetrics class uses it
- architecture_notes.py gets wired into test cases via LLMTestCase.context
- Import direction strictly downward: Tests → HarnessEvaluator → run_harness_eval → HarnessMetrics → DeepEvalInterface

## References
- `D:/my_ai_projects/project_test_repos/platform-deepeval/.claude/skills/deepeval-management-layer/references/architecture.md` — 5-layer spec
- `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` — existing L2 code (orphaned)
- `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` — context injection (orphaned)
- `D:/my_ai_projects/project_test_repos/evals/eval-platform-selenium/tests/test_eval_harness.py` — current non-conforming test file
- `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/metrics/custom_metrics.py` — correct L2 pattern to follow
- Backlog 172 — parallel refactor for A/B testing conformance

## Task Builder Input
- **Deliverable:** Refactored harness eval test suite conforming to 5-layer architecture, wiring up orphaned harness_metrics.py and architecture_notes.py
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-deepeval`
- **Scope:** REFACTOR
- **Constraints:** Must not change eval output format or scoring behavior. harness_metrics.py criteria and thresholds are the source of truth — tests must use them, not redefine. Eval skill step files (in sr_dev_workspace) may need path updates if imports change.
