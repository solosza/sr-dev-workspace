# 002 — Prune registry + remove stale

## Action
Run `git -C <workspace> worktree prune` (drops dead registry entries). Then for each PRUNE-ELIGIBLE worktree dir, `git -C <workspace> worktree remove <path>` (use --force only if a dir is dirty and confirmed finished). Never touch a KEEP worktree.

## Acceptance
- `git worktree prune` run; PRUNE-ELIGIBLE worktrees removed; KEEP worktrees untouched.
- `git worktree list` after shows only KEEP + main.
