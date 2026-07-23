# Task 001: Fresh-Base Worktree Creation
**Type:** BUILD | **Gates:** WI-01
## Action
Edit run-task.sh so worktrees are created from the CURRENT main HEAD at spawn time, removing the correctness-dependence on the `git reset --hard main` workaround.
## Spec
READ the worktree-creation + step-0 baseline logic in run-task.sh first. Ensure `git worktree add` (or the equivalent spawn) branches from `main` at its current HEAD so the worktree starts on a fresh, correct base. Keep a GUARDED safety assertion (merge-base == main HEAD, or a warn-and-reset) so a stale base is detected, but the default path must be correct WITHOUT relying on a manual reset. Use `git -C <repo>` absolute paths, never bare `cd`.
## Acceptance
Worktree spawn branches from current main HEAD; reset-hard is a safety net, not a correctness requirement; assertion retained.
