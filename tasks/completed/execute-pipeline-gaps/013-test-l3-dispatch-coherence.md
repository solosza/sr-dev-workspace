# 013 — L3: Verify Dispatch Logic Coherence

## Type
TEST

## Requirements
- Read the updated `step-04-execute-tasks.md` end-to-end
- Verify the classification heuristic is complete:
  - Has criteria for simple vs complex
  - Has default fallback (complex/run-task.sh)
  - References autonomous-cycle for simple tasks
  - References run-task.sh for complex tasks
- Read the updated `complete.md` and verify gate verification step is properly numbered and doesn't break the flow
- Read the updated `step-03-run-task-builder.md` and verify skip_plan_review is false and the description is consistent
- Read `granularity-reference.md` and verify it has all 4 examples and the decision test

## Acceptance Criteria
- [ ] step-04 dispatch logic has both simple (autonomous-cycle) and complex (run-task.sh) paths
- [ ] step-04 dispatch has a default fallback
- [ ] complete.md gate verification is between deliverable verification and completion mode
- [ ] step-03 is internally consistent (no contradictions between JSON and prose)
- [ ] granularity-reference has 4 examples and "If this task times out" test
