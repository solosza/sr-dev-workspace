# Task 005: Fix framework/ Roles and Tasks

## What
Mirror the corrected `_reference/` pattern in `framework/`. Same fixes: return None, self.metrics, no _eval_results, generalize discover_harness().

## Design Doc
`docs/backlog/191-qa-refactor-deepeval-5-layer-contract-violations/phase-5-framework-roles-tasks.md`

## Files To Modify
All in `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/`:

### Roles
1. `roles/harness_evaluator.py`
   - Line 127: `evaluate_harness()` returns dict → return None
   - Line 33: `discover_harness()` hardcoded to `.claude/commands/kernel/` → accept parameter
   - Lines 123-124: reads `_eval_results` → read from `self.metrics`
   - Add `self.metrics`, `self.test_cases`, state-check methods
2. `roles/ab_evaluator.py`
   - Line 50: `evaluate_experiment()` returns dict → return None
   - Add `self.metrics`, `self.test_cases`, state-check methods

### Tasks
1. `tasks/run_harness_eval.py` — line 21: remove `test_case._eval_results`, add `metrics_out`
2. `tasks/run_ab_eval.py` — same pattern

### Tests
1. Any test in `tests/` asserting on return values or `_scores` → assert on state methods

## Gate
- [ ] `grep -r "return {" platform-deepeval/framework/roles/` returns nothing
- [ ] `grep -r "_eval_results" platform-deepeval/framework/tasks/` returns nothing
- [ ] `discover_harness()` accepts path parameter
- [ ] All roles have `self.metrics` + state-check methods
- [ ] Pattern matches corrected `_reference/`
