# Task 003: Commit-on-Complete Gate
**Type:** BUILD | **Gates:** RH-03
## Action
Edit run-task.sh so that immediately before it prints the ALL_TASKS_COMPLETE banner, it runs `git status --porcelain` scoped to the task output dir; if the tree is dirty it either commits the deliverable (preferred, with a clear message) or fails loudly naming the uncommitted files. Complete must never leave an uncommitted deliverable on the branch.
## Spec
READ the ALL_TASKS_COMPLETE banner section first. Scope the porcelain check to the deliverable/output path, not the whole repo (avoid sweeping unrelated state). Use `git -C <repo>` absolute paths, never cd. Preserve existing merge-hint output.
## Acceptance
A dirty deliverable tree at complete triggers commit-or-loud-fail; clean tree completes normally.
