# WI-04 Live Evidence — L3 Worktree Isolation

**Date:** 2026-07-23
**Method:** Real `git worktree add` + real `run-task.sh` invocation (nested `claude -p`), no simulation.

## Setup

- Parent repo (isolation reference): this worktree `agent-a046b69c360dd46b5` (kept as the fixed reference point instead of the shared main checkout, which had concurrent agents actively mutating its state files at test time — using it as parent would have produced false-positive diffs unrelated to this test).
- Parent HEAD: `843e23cd7a82f9a9611fa42f9039c85bc907c7ed`
- Child worktree: `.claude/worktrees/wi04-live-test` on branch `wi04-live-test-branch`, created via `git worktree add <path> -b wi04-live-test-branch HEAD`
- 1-task test folder written directly into the child's `tasks/wi04-live-test-tasks/` (000-index.md + 001-write-marker.md — trivial BUILD task: write `wi04_marker.txt` with content `WI04_LIVE_OK`)
- Command: `env -u CLAUDECODE ... bash run-task.sh <child_path> 3 wi04-live-test-tasks`

## Command output (tail)

```
=== Iteration 1/3 ===
[SEED] Created agent-wi04-live-test-tasks-workflow.json
[SEED] Created agent-wi04-live-test-tasks-session-state.json
[TASK] Attempting: 001-write-marker.md
ALL_TASKS_COMPLETE
[MOVE] Moving task folder to completed: tasks/wi04-live-test-tasks
[COMMIT] Deliverable committed.
ALL TASKS COMPLETE — Tasks completed this run: 1 — Total iterations: 1
```

## Assertions

**(a) Fresh base — PASS**
```
CHILD_HEAD    = 843e23cd7a82f9a9611fa42f9039c85bc907c7ed
PARENT_HEAD   = 843e23cd7a82f9a9611fa42f9039c85bc907c7ed
MERGE_BASE    = 843e23cd7a82f9a9611fa42f9039c85bc907c7ed
merge-base == parent HEAD -> fresh base confirmed
```

**(b) Parent `sr_dev_workflow.json` unchanged during/after — PASS**
```
hash before: c187425aa82f31c7ac9b303f88c8ea0ef37a251031a8ea5700f011945b3c11b5
hash after:  c187425aa82f31c7ac9b303f88c8ea0ef37a251031a8ea5700f011945b3c11b5
anchored before: True
anchored after:  True
```

**(c) No stray artifacts in parent working tree — PASS**
```
.claude/state/ directory listing (197 entries): unchanged, diff empty
tasks/ directory listing: unchanged, diff empty
wi04_marker.txt at parent repo root: NOT FOUND (only in child, as expected)
git status --porcelain | grep wi04: only the child worktree dir itself (removed at cleanup)
```

Child worktree's own `.claude/state/` correctly received `agent-wi04-live-test-tasks-workflow.json` and
`agent-wi04-live-test-tasks-session-state.json` — proving isolation held both ways (child wrote its own
scoped files, parent's shared files were untouched).

## Cleanup

`git worktree remove --force` + `git branch -D wi04-live-test-branch` — parent git status confirmed clean
of all wi04-related entries after cleanup.

## Verdict

3/3 live asserts pass. WI-04 gate satisfied.
