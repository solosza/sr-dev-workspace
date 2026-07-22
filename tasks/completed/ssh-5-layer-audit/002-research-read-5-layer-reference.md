# Read 5-Layer Reference Architecture

## Context
Read the platform-deepeval 5-layer reference to establish the compliance baseline.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/interfaces/deepeval_interface.py` (L1)
- Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/` (L2) — at least ab_metrics.py and harness_metrics.py
- Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tasks/` (L3)
- Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/roles/` (L4)
- Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tests/` (L5)
- Write a reference checklist to `tasks/ssh-5-layer-audit/5-layer-reference-checklist.md` with:
  - Required patterns per layer (class names, method signatures, import style)
  - Banned patterns (direct SDK imports, wrong import direction)

## Acceptance Criteria
- [ ] Reference checklist exists at `tasks/ssh-5-layer-audit/5-layer-reference-checklist.md`
- [ ] Documents required patterns for each layer (L1-L5)
- [ ] Documents banned patterns

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
