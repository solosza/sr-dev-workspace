# Task 002: Heartbeat-Staleness Stall Detection
**Type:** BUILD | **Gates:** RH-02
## Action
Edit run-task.sh (or add a small companion checker it calls each loop pass) so that if the 262 HEARTBEAT_FILE is older than a threshold while tasks remain, the runner marks the run `stalled` in routed state and terminates with a NON-ZERO exit the orchestrator can observe — never a silent exit-0 with work remaining.
## Spec
READ the 262 HEARTBEAT_FILE write + cleanup_lock code first. Threshold configurable (env or constant, sensible default e.g. 2x expected iteration time). Write `stalled: true` + reason to routed state via Python/Write. Ensure normal completion still exits 0; only stall/abandon emits non-zero.
## Acceptance
Stale-heartbeat-with-work-remaining path sets stalled state + non-zero exit; healthy completion still exit 0.
