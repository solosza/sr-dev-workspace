# Sync Model Router + run-task.sh to Child Workspaces

## Status
Open

## Priority
High — child workspaces are running stale run-task.sh without model routing, costing more per pipeline run

## Summary
Sync the updated `run-task.sh`, `lib/model-router.sh`, and `lib/model-routing-config.json` from sr_dev_workspace to all child workspaces that have their own copy of run-task.sh. Additionally, the domain spec factory needs the universal hook validator system (backlog 089) plus this model router added to its template so all future workspaces get both automatically.

## Target Workspaces

| Workspace | Path | Has run-task.sh | Has lib/ | Needs |
|-----------|------|----------------|----------|-------|
| game-dev | `D:\my_ai_projects\project_test_repos\game-dev` | Yes | Yes (common.sh) | model-router.sh, model-routing-config.json, updated run-task.sh |
| hmsa-healthcare-qa | `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` | Yes | Yes (common.sh) | model-router.sh, model-routing-config.json, updated run-task.sh |
| platform-ssh | `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh` | No | No | Full kernel infra: run-task.sh, run-task-batch.sh, lib/, model-router, universal hook validator |

## Requirements

### game-dev + hmsa-healthcare-qa (sync existing infra)
- Copy `lib/model-router.sh` to each target workspace's `lib/`
- Copy `lib/model-routing-config.json` to each target workspace's `lib/`
- Replace `run-task.sh` in each target with the current version from sr_dev_workspace
- Replace `lib/common.sh` in each target (ensure latest version)
- Verify each workspace's run-task.sh sources model-router.sh correctly
- Commit changes in each target workspace

### platform-ssh (full kernel infra bootstrap)
- Copy `run-task.sh` and `run-task-batch.sh` to platform-ssh root
- Create `lib/` directory with `common.sh`, `model-router.sh`, `model-routing-config.json`
- Copy `lib/attestation/` directory
- Copy universal hook validator (from backlog 089) to `.claude/hooks/`
- Verify run-task.sh works (sources lib correctly, no path issues)
- Commit changes in platform-ssh

### Domain spec factory (template update)
- Add `model-router.sh` + `model-routing-config.json` to template files list
- Add universal hook validator to template hooks list
- Ensures all future workspaces get both automatically

## References
- Backlog 087 (done): Multi-model routing implementation
- Backlog 089 (done): Universal hook validator system
- Source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\run-task.sh`
- Source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\lib\model-router.sh`
- Source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\lib\model-routing-config.json`

## Task Builder Input
- **Deliverable:** All child workspaces running updated run-task.sh with model routing
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not break existing task execution in any workspace. Platform-ssh needs full infra bootstrap (no existing run-task.sh). Each workspace commit should be atomic. Domain spec factory template update included.
