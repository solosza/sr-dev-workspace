# Task 001: Fix _reference/ Roles

## What
Fix all 4 `_reference/` roles to match platform-selenium's 5-layer contract.

## Design Doc
`docs/backlog/191-qa-refactor-deepeval-5-layer-contract-violations/phase-1-reference-roles.md`

## Canonical Reference
Read `platform-selenium/framework/_reference/roles/employee_manager.py` FIRST. Note:
- `-> None` on all workflow methods
- `"""NO return values"""` in class docstring
- Composes Task modules, delegates to them
- No dict returns anywhere

## Files To Modify
All in `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/roles/`:
1. `rag_evaluator.py` — `evaluate_pipeline()` returns dict at line 40 → return None
2. `agent_evaluator.py` — `evaluate_pipeline()` returns dict at line 40 → return None
3. `security_evaluator.py` — `evaluate_pipeline()` returns dict at line 50 → return None
4. `compliance_evaluator.py` — `evaluate_pipeline()` returns dict at line 44 → return None

## Changes Per File
1. Add `-> None` type hint to all workflow methods
2. Add `"""NO return values"""` comment in class docstring
3. Add `self.metrics = {}` and `self.test_cases = []` to `__init__`
4. Remove `return {...}` — replace with storing on `self.test_cases`
5. Add state-check methods: `is_dimension_passing(dim)`, `get_score(dim)`, `get_count()`

## Gate
- [ ] No `return {` in any role file
- [ ] All workflow methods have `-> None`
- [ ] All roles have `self.metrics` and `self.test_cases`
- [ ] All roles have `is_dimension_passing()`, `get_score()`, `get_count()`
- [ ] `python -c "from _reference.roles.rag_evaluator import RAGEvaluator"` succeeds
