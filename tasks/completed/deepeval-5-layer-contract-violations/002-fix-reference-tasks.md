# Task 002: Fix _reference/ Tasks

## What
Remove `test_case._eval_results` from all 7 tasks. Metrics store state internally. Tasks accept `metrics_out` dict to pass metric references back to role.

## Design Doc
`docs/backlog/191-qa-refactor-deepeval-5-layer-contract-violations/phase-2-reference-tasks.md`

## Canonical Reference
Read `platform-selenium/framework/_reference/tasks/employee_management_tasks.py` FIRST. Note:
- `-> None` on all methods
- `"""NO return values"""` in class docstring
- Operates on page objects (state holders), doesn't return results
- Page objects hold state — tasks just orchestrate

## Files To Modify
All in `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tasks/`:
1. `run_rag_eval.py` — line 25: remove `test_case._eval_results = {...}`
2. `run_agent_eval.py` — same pattern
3. `run_security_eval.py` — same pattern
4. `run_compliance_eval.py` — same pattern
5. `run_hook_bypass_eval.py` — same pattern
6. `run_tool_boundary_eval.py` — same pattern
7. `run_protocol_eval.py` — same pattern

## Changes Per File
1. Add `metrics_out: dict = None` parameter to function signature
2. Remove `test_case._eval_results = {...}` line
3. Add: `if metrics_out is not None: metrics_out[key] = metric_obj` for each metric
4. Keep `-> None` return type (already present in most)

## Gate
- [ ] `grep -r "_eval_results" platform-deepeval/framework/_reference/tasks/` returns nothing
- [ ] All tasks accept `metrics_out` parameter
- [ ] All tasks return `None`
- [ ] Imports still work
