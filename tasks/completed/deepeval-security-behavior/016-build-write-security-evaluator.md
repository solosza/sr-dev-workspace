# 016 — Write SecurityEvaluator L4 role

**Type:** BUILD
**Deliverable:** `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/roles/security_evaluator.py`

## Action
Write L4 EvalRole following `agent_evaluator.py` pattern. Orchestrates run_security_eval, run_hook_bypass_eval, run_tool_boundary_eval across a dataset.

## Acceptance Criteria
- [ ] File exists at target path
- [ ] Class follows EvalRole pattern with `evaluate_pipeline` method
- [ ] Orchestrates 3 security EvalTasks
