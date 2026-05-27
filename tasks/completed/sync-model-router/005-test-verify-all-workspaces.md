# Task 005: Verify all workspaces have model router

## Objective
Verify that model-router.sh, model-routing-config.json, and updated run-task.sh exist in all 4 target workspaces.

## Instructions

For each workspace, verify:
1. `lib/model-router.sh` exists and contains `route_model()` function
2. `lib/model-routing-config.json` exists and contains tier definitions
3. `run-task.sh` exists and sources `model-router.sh`

Workspaces:
- `D:\my_ai_projects\project_test_repos\game-dev`
- `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`
- `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh`
- `D:\my_ai_projects\project_test_repos\domain-spec-factory`

## Acceptance Criteria
- [ ] All 4 workspaces have lib/model-router.sh with route_model function
- [ ] All 4 workspaces have lib/model-routing-config.json with 3 tiers

## Gate
TEST-05
