# Refactor A/B Testing Framework to 5-Layer Eval Architecture

## Status
Open

## Priority
High — the framework exists to enforce structure; if new components bypass it, the architecture is decorative

## Summary
The A/B testing framework (pipeline 171) works end-to-end but bypasses all 5 layers of the eval architecture defined in platform-deepeval. It calls DeepEval SDK directly (skips L1), has no Metric Objects (skips L2), no EvalTasks (skips L3), no EvalRole orchestrator (skips L4), and generates markdown instead of pytest tests (skips L5). Refactoring to conform proves the 5-layer framework scales to new eval modes and ensures the agent follows its own architecture when generating eval suites.

## Requirements

### L1: DeepEvalInterface
- `ABScorer` must use `DeepEvalInterface.measure_metric()` instead of raw `metric.measure()`
- Gets retry logic (3 retries, exponential backoff) and logging for free
- No direct DeepEval SDK imports in `ab_testing/` — all go through L1

### L2: Metric Objects
- Create `ABMetrics` class in `framework/metrics/ab_metrics.py`
- Thresholds as class constants (compliance=0.7, adherence=0.7, completeness=0.7, following=0.7, drift=0.7)
- `evaluate(test_case)` returns `self` (fluent chaining)
- `is_above_threshold(metric_name)` returns bool
- `get_score(metric_name)` returns float
- Move 5 criteria strings from `scorer.py` into this class

### L3: EvalTasks
- Create `run_ab_eval()` function in `framework/tasks/` (or `_reference/tasks/`)
- Composes ABMetrics, returns None
- One eval operation per function

### L4: EvalRoles
- Create `ABEvaluator` role class in `framework/roles/` (or `_reference/roles/`)
- Orchestrates full workflow: generate variants → run → score → report
- Composes L3 EvalTasks
- Replaces the current loose `VariantGenerator → Runner → Scorer → Reporter` pipeline

### L5: Tests
- Real pytest tests with `@pytest.mark.parametrize` over runs
- AAA pattern (Arrange/Act/Assert)
- Assert via `ABMetrics.is_above_threshold()` — not raw scores
- Conftest fixtures for experiment config, golden data, variant paths
- Runnable via `deepeval test run`

### Integration
- Update `ab_testing/__init__.py` exports
- Update eval skill step files if import paths change
- Existing `ExperimentConfig` and `VariantGenerator` stay — they're fine
- `ABScorer` gets gutted — scoring logic moves to L2/L3
- `ABReporter` stays for markdown output but L5 tests are the primary verification

## References
- `D:/my_ai_projects/project_test_repos/platform-deepeval/.claude/skills/deepeval-management-layer/references/architecture.md` — 5-layer spec
- `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/` — reference implementations per layer
- `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/` — current A/B code to refactor
- Backlog 171 — original A/B framework build

## Task Builder Input
- **Deliverable:** Refactored A/B testing framework conforming to 5-layer architecture
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-deepeval`
- **Scope:** REFACTOR
- **Constraints:** Must not break existing experiment output format (evals/eval-ab-*/). ExperimentConfig and VariantGenerator are fine as-is. Import direction must be strictly downward (Tests → Roles → Tasks → Metrics → Interface).
