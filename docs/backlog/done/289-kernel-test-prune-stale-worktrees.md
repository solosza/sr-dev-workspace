# Prune Stale Pipeline Worktrees in sr_dev_workspace

## Status
Open

## Priority
Medium — 42 finished-run worktrees clutter `.claude/worktrees/`; harmless but noise. Cleanup, not urgent.

## Summary
`sr_dev_workspace/.claude/worktrees/` holds ~42 `agent-*` git worktrees left over from completed pipeline runs. They are finished (not tied to any in-flight run) and just accumulate. Prune the git worktree registry and remove the stale directories, leaving any worktree that belongs to an active run untouched.

## Requirements
- List all worktrees: `git -C <workspace> worktree list`.
- Run `git -C <workspace> worktree prune` to drop registry entries whose dirs are already gone.
- For remaining stale `agent-*` worktree dirs (finished runs), `git worktree remove` each (or `--force` if needed), then confirm the dir is gone.
- **Safety:** do NOT remove any worktree referenced by a running pipeline / open feature branch under review — check `review-status.json` and skip anything still pending merge.
- Report: count before/after, list of removed worktrees, any skipped (and why).

## References
- Target: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/worktrees/`
- Surfaced during kernel-consolidation inventory (42 stale `agent-*` worktrees).

## Task Builder Input
- **Deliverable:** Stale worktrees pruned + a short report (`projects/worktree-prune/prune-report.md`) of what was removed vs. skipped.
- **Location:** workspace
- **Scope:** TEST
- **Constraints:** Operate ONLY on `.claude/worktrees/`. Skip any worktree tied to an unmerged/pending-review branch. Use `git worktree` commands (not raw rm on live worktrees). No worktree-based isolation for this task (it prunes worktrees) — run in-workspace via subfolder.
