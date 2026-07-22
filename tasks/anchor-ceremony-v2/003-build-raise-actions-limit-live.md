# Task 003: Raise actions_limit to 50 in Live Workflow State

**Type:** BUILD
**Gates Satisfied:** AC-03

## Action

Set `actions_limit: 50` in `.claude/state/sr_dev_workflow.json` (ONE field change).

## Spec

Hybrid policy (Policy C, 238 verdict): the PreCompact hook covers compaction, so the drift timer relaxes 30 → 50.

MERGE pattern (mandatory): read the full JSON (utf-8-sig tolerant), change ONLY `actions_limit` to `50`, write back the full object via Python json.dump (UTF-8, no BOM). Preserve every other key including `completed_tasks`, `anchored`, counters.

Note: when running in a worktree, the LIVE file is the MAIN repo's `.claude/state/sr_dev_workflow.json` — but a worktree-isolated task edits its own copy and the change reaches main via merge. Edit the workflow state file at the repo root you are executing in; the orchestrator reconciles at merge (state files resolve to main's live values, so the orchestrator applies this field to main's live state during validation if the merge drops it).

## Acceptance Criteria (mechanical)

- `json.load(open('.claude/state/sr_dev_workflow.json'))['actions_limit'] == 50`
- All pre-existing keys still present (compare key set before/after)
