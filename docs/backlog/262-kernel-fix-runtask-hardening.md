# Fix: run-task.sh Hardening — Model Routing + Timeout/Signal Resilience

## Status
Open

## Priority
High — every inner task is paying Opus pricing because routing never resolves the task file; 3 batches tonight also burned iterations on empty-output timeouts and one died silently.

## Summary
The model switcher selects the default (Opus) on 13/13 sampled iterations because `CURRENT_TASK` comes from workflow-state `current_task`, which is null at every iteration start — `TASK_FILE_PATH` never resolves and `route_model` hits its file-missing fallback. Separately: `claude -p` sometimes produces zero output until the 600s kill (iteration burned, 0-byte log), and runner death is invisible to monitors. Fix the routing resolution, stop burning iterations on empty output, and add a heartbeat for liveness.

## Requirements
- Model routing: resolve the NEXT incomplete task file directly (task folder listing minus completed_tasks from the routed agent workflow file) instead of relying on `current_task`; `[MODEL] Selected` must show the real task filename; keyword tasks route to sonnet/haiku per config
- Empty-output resilience: when an iteration is killed at timeout with a 0-byte log, retry ONCE without consuming an iteration slot (bounded — a second empty output consumes the slot normally); log the event distinctly
- Liveness heartbeat: runner writes `.claude/state/{subfolder}_runner-heartbeat.json` (pid, iteration, ISO timestamp) each loop pass so monitors can detect death vs slow work reliably
- No behavior change for existing green paths; state writes UTF-8 no BOM (lesson #49)

## References
- Observed: 13/13 `[MODEL] Selected: claude-opus-4-6 (task: unknown)` across batches 215/216/250-254; 0-byte iteration logs in 214/215/216/252/253; silent death of both first parallel batches (214/246)
- `run-task.sh` (task resolution ~line 269 AGENT_ID block, route_model call, timeout handling), `lib/model-router.sh`, `lib/model-routing-config.json`
- Session ledger entries (failure kind) in session_state.json

## Task Builder Input
- **Deliverable:** Patched run-task.sh + heartbeat, L1-L3 tested (L3 = nested mini-batch proving non-default routing on a haiku-keyword task)
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** run-task.sh is in active use by parallel batches — ALL edits in the pipeline worktree only, merge after validation. Do not change lib/model-routing-config.json tiers. Keep retry_upgrade_order semantics intact.
