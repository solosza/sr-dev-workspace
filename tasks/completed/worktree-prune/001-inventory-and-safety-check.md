# 001 — Inventory worktrees + safety check

## Action
Run `git -C D:/my_ai_projects/project_test_repos/sr_dev_workspace worktree list`. Cross-reference `.claude/state/review-status.json` — mark any worktree whose branch is pending review/unmerged as KEEP. Everything else (finished agent-* runs) is PRUNE-ELIGIBLE.

## Acceptance
- A list of worktrees split into KEEP vs PRUNE-ELIGIBLE (saved to projects/worktree-prune/inventory.md).
- No worktree removed yet.
