# 289 — prune stale worktrees (TEST/cleanup)

Prune finished agent-* worktrees under sr_dev_workspace/.claude/worktrees/. Skip anything tied to an unmerged/pending-review branch.

| # | Task |
|---|------|
| 001 | Inventory worktrees + safety check |
| 002 | Prune registry + remove stale |
| 003 | Write prune report |
