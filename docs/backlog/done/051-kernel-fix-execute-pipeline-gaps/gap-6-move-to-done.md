# Gap 6: Enforce Move-to-Done for Completed Backlogs and Tasks

## Status
NEW

## Location
- `.claude/skills/execute-pipeline/references/step-05-validate-report.md` (steps 6-7 exist but aren't enforced)
- `run-task.sh` (could do the move itself after ALL_TASKS_COMPLETE)

## Problem
Execute-pipeline step 5 has steps 6 and 7 that specify moving completed backlogs to `docs/backlog/done/` and task folders to `tasks/completed/`. But in practice this never happens because:

1. **run-task.sh was broken on Windows** — most pipelines ended as FAIL (empty logs, zombie processes), never reaching PASS. The move only triggers on PASS. Fixed by backlog 050, but historical pipelines never moved anything.

2. **Outer agent context loss** — by the time the background run-task.sh agent returns, the outer agent may have lost context to compaction and skips steps 6-7, jumping straight to the report or stopping.

3. **No enforcement mechanism** — the move is documented but not enforced. There's no hook or gate that checks "did the backlog get moved?" The agent can skip it silently.

Evidence: multiple completed pipelines (046, 048, 049, 050) have their backlogs manually moved to `done/` and task folders manually moved to `completed/`. The pipeline never did it automatically.

## Fix

### Option A: Add move logic to run-task.sh (recommended)
After printing ALL_TASKS_COMPLETE, run-task.sh itself moves the files:

```bash
if [ "$LAST_STATUS" = "all_done" ]; then
  # Move backlog to done
  if [ -n "$BACKLOG_PATH" ] && [ -f "$BACKLOG_PATH" ]; then
    mkdir -p docs/backlog/done
    mv "$BACKLOG_PATH" docs/backlog/done/
    # If backlog has a companion folder, move that too
    BACKLOG_DIR="${BACKLOG_PATH%.md}"
    if [ -d "$BACKLOG_DIR" ]; then
      mv "$BACKLOG_DIR" docs/backlog/done/
    fi
  fi

  # Move task folder to completed
  if [ -n "$TASK_SUBFOLDER" ]; then
    mkdir -p tasks/completed
    mv "tasks/$TASK_SUBFOLDER" "tasks/completed/$TASK_SUBFOLDER"
  fi
fi
```

This requires passing `BACKLOG_PATH` as a new 4th argument to run-task.sh.

### Option B: Add post-execution check to step 5
Make the move a hard requirement with verification:
- After producing the report, check if backlog file still exists in `docs/backlog/`
- If it does and result is PASS, move it
- Verify the move happened (file exists in `done/`, doesn't exist in `docs/backlog/`)

### Why Option A is better
run-task.sh runs as a subprocess with full filesystem access. It knows the result immediately (ALL_TASKS_COMPLETE). The outer agent may lose context. Putting the move in run-task.sh makes it atomic with the completion signal — the files move in the same process that detected completion.

## Dependencies
- Backlog 050 (run-task.sh rewrite) — DONE
- New argument to run-task.sh: `BACKLOG_PATH` (4th positional arg)
- Execute-pipeline step 4 must pass the backlog path to run-task.sh
