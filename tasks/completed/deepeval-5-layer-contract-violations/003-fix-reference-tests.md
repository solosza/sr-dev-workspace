# Task 003: Fix _reference/ Tests

## What
Fix tests to call `evaluate()` instead of directly setting `_scores`. Mock at the GEval boundary, not by stuffing internal state.

## Design Doc
`docs/backlog/191-qa-refactor-deepeval-5-layer-contract-violations/phase-3-reference-tests.md`

## Canonical Reference
Read `platform-selenium/framework/_reference/tests/test_e2e_create_employee_and_assign_task.py` FIRST. Note:
- AAA pattern: Arrange, Act, Assert
- Act calls role workflow methods (no direct state manipulation)
- Assert uses page object state-check methods (`is_employee_displayed_in_list()`)
- Never directly sets internal page object state

## Files To Modify
All in `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tests/`:
1. `test_prompt_injection.py` — lines 27, 61: `metrics._scores["..."] = 0.95` → mock GEval.measure, call evaluate()
2. `test_rag_pipeline.py` — check for `_scores` direct access
3. `test_hook_bypass.py` — check for `_scores` direct access

## Changes
1. Replace `metrics._scores["X"] = 0.95` with proper mocking:
   - `unittest.mock.patch` on `GEval.measure`
   - Configure mock to set `.score` and `.reason` on the GEval instance
   - Call `metrics.evaluate(test_case)` — the CORRECT path
2. Keep all assertions on state-check methods (`is_above_threshold()`, `get_score()`)
3. Preserve AAA structure

## Gate
- [ ] `grep -r "_scores\[" platform-deepeval/framework/_reference/tests/` returns nothing
- [ ] All tests call `metrics.evaluate()` (with mocked GEval)
- [ ] All assertions use `is_above_threshold()` or `get_score()`
- [ ] `python -m pytest platform-deepeval/framework/_reference/tests/ --collect-only` succeeds
