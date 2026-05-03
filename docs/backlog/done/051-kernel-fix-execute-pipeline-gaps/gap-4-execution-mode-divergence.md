# Gap 4: Reconcile Task-Builder Step 9 Execution Modes

## Status
NEW

## Location
`.claude/skills/task-builder/references/step-09-execute.md`

## Problem
Step 9 describes two execution modes:
1. **Inline cycling** — BUILD/RESEARCH tasks run via `/kernel/autonomous-cycle` in-session
2. **Spawned sub-agents** — TEST tasks run via `run-task.sh` in background

But when execute-pipeline calls task-builder, it sets `no_execute: true` and handles ALL execution itself via run-task.sh (step 4). run-task.sh doesn't distinguish BUILD vs TEST — it cycles all tasks sequentially through `claude -p`.

This means the sub-agent-for-TEST design in step 9 is dead code when running under execute-pipeline (the most common path).

## Fix
Two options (recommend option A):

**Option A: Simplify step 9 to match reality.**
- Document that under execute-pipeline, all tasks run sequentially via run-task.sh
- The inline cycling + spawned sub-agent mode is for standalone `/kernel/task-builder` only
- Add a clear mode switch at the top of step 9:
  - If `pipeline_mode.no_execute` → defer to caller (already implemented)
  - If standalone → use the dual-mode execution (inline BUILD + spawned TEST)
- This is already how it works — just document it honestly

**Option B: Make run-task.sh task-type-aware.**
- run-task.sh reads each task's type tag and adjusts behavior
- TEST tasks get isolation (clean state, fresh env)
- BUILD tasks run normally
- This is more correct but more complex — save for a future backlog

## Dependencies
None — documentation/clarification change for option A.
