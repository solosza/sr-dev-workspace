# Gap 3: Add Per-Task Timeout Feedback to run-task.sh

## Status
NEW

## Location
`run-task.sh`

## Problem
When a task times out, the log says `[TIMEOUT] claude -p exceeded 600s — killing process tree (PID N)` but doesn't record which task was being attempted. The workflow state's `current_task` is the only breadcrumb — if that's stale (e.g., the agent didn't reach the task-pick step), you lose traceability.

## Fix
Before spawning `claude -p`, read `current_task` from workflow state and log it:

```bash
# Before run_claude call
CURRENT_TASK=$($PYTHON_CMD -c "
import json, pathlib
sf = pathlib.Path('$STATE_FILE')
if not sf.exists(): print('unknown'); exit()
s = json.loads(sf.read_text())
d = s.get('domain', '')
if not d: print('unknown'); exit()
wf = sf.parent / (d + '_workflow.json')
if not wf.exists(): print('unknown'); exit()
w = json.loads(wf.read_text())
print(w.get('current_task', 'not-yet-picked'))
" 2>/dev/null || echo "unknown")

echo "[TASK] Attempting: $CURRENT_TASK"
```

Also include `$CURRENT_TASK` in the timeout message:
```bash
echo "[TIMEOUT] Task '$CURRENT_TASK' — claude -p exceeded ${TASK_TIMEOUT}s (PID $claude_pid)"
```

## Dependencies
- Backlog 050 (run-task.sh rewrite) — DONE, this builds on it
