# Barrier Monitor + Failure Semantics

## 1. Barrier Mechanism Design: Notification-Driven with Timeout Backstop

The current swarm monitor polls per-agent state files every 10 seconds for up to 5 minutes (30 polls). For wave dispatch, the barrier must be **long-lived** — wave N+1 may not start for minutes or hours after wave N spawns.

### Recommended: Notification-Driven (Background Task Completion)

When spawn-agent-swarm dispatches agents via `Bash(run_in_background: true)` or `Agent(run_in_background: true)`, the Claude Code harness delivers a task-notification when the background process exits. This is the primary completion signal — no polling required for wave transitions.

**Wave dispatch loop:**

```
for each wave in sorted_waves:
  spawn all agents in this wave (parallel)
  wait for all task-notifications (harness-driven, not polling)
  read per-agent state files to confirm status
  if all COMPLETE → dispatch next wave
  if any FAILED/SKIPPED → apply failure policy (see §2)
  if timeout exceeded → apply timeout policy
```

**Why notification-driven over polling:**
- **Polling** wastes agent context window on repeated read cycles and risks missing completion between poll intervals
- **Notifications** are push-based: the orchestrator is dormant between waves, activated only when an agent exits
- The existing monitor's 5-minute cap is insufficient for multi-wave execution where a single wave may take 20+ minutes

### Timeout Policy

Each wave gets a configurable timeout (default: 30 minutes per wave, overridable in the task index):

- **At timeout:** Read per-agent state files for incomplete agents
- **If progress is advancing** (completed_tasks count increased since last check): extend by 10 minutes (once)
- **If stalled** (no progress in timeout window): mark stalled agents as TIMED_OUT
- **Total pipeline timeout:** Sum of all wave timeouts + 50% buffer. This prevents a single stalled wave from blocking the orchestrator indefinitely.

The timeout is a backstop, not the primary mechanism. Under normal operation, notifications drive all transitions.

## 2. Failure Semantics Decision Table

When a wave N agent fails, skips, or times out, the orchestrator must decide what happens to wave N+1. Three policies:

| Wave N Outcome | Block Entirely | Partial Dispatch | Abort Pipeline |
|----------------|---------------|-----------------|----------------|
| One agent FAILED (non-zero exit) | All N+1 blocked | Only children of failed task blocked; others dispatch | Entire pipeline stops |
| One agent SKIPPED (3 attempts) | All N+1 blocked | Only children of skipped task blocked | Entire pipeline stops |
| One agent TIMED_OUT | All N+1 blocked | Only children blocked | Entire pipeline stops |
| Multiple agents failed | All N+1 blocked | Each child checked independently | Entire pipeline stops |

### Recommended Policy: Partial Dispatch (Default)

**Rationale:** Partial dispatch maximizes useful work. If wave 1 has tasks A, B, C and task B fails, but wave 2's task D depends only on A and C (not B), task D should still run. Blocking D because of B wastes the successful work of A and C.

**Implementation:** After wave N completes, for each task in wave N+1:
1. Check its `depends_on` list
2. For each dependency, check the dependency's completion status in per-agent state
3. If ALL dependencies are COMPLETE → dispatch
4. If ANY dependency is FAILED/SKIPPED/TIMED_OUT → mark this task BLOCKED, skip it
5. Record blocked tasks and their blocking reason in the wave manifest

**Propagation:** Blocking cascades forward. If task D is blocked in wave 2, any wave 3 task depending on D is also blocked — the blocker propagates through the graph without needing to re-evaluate wave N.

**Override:** Users may set `failure_policy: "block_all"` or `failure_policy: "abort"` in the task index for strict pipelines where partial results are useless.

## 3. Orphaned Wave Cleanup

An orphaned wave occurs when all tasks in wave N+1 are blocked (every task depends on at least one failed wave N task). The orchestrator detects this by checking if the dispatched set for wave N+1 is empty:

- **If dispatched set is empty:** Log "Wave N+1 entirely blocked — no tasks to dispatch"
- **Skip to wave N+2** and re-evaluate (some N+2 tasks may depend on N-1 tasks that succeeded)
- **If all remaining waves are empty:** Pipeline terminates early with a "partial completion" report listing what completed and what was blocked

Cleanup actions:
- Per-agent state files for blocked tasks get `status: "blocked"` (not "failed" — distinguishes between agent-level failure and dependency-level blocking)
- The manifest records the blocking chain for diagnostics
- No orphaned processes to kill — blocked agents were never spawned

## 4. Resume After Orchestrator Restart

If the orchestrator session restarts mid-wave (context compaction, user restart, crash):

1. **Read the wave manifest** from `.claude/state/agent-swarm.json` — it records which wave is active and which agents were dispatched
2. **Read per-agent state files** for all dispatched agents — these survive the restart (file-based, not in-memory)
3. **Classify each dispatched agent:**
   - COMPLETE → already done, no action
   - RUNNING with recent `last_update` → still executing, re-attach to notification
   - RUNNING with stale `last_update` (> timeout) → mark TIMED_OUT
   - No state file → agent crashed before writing state, mark FAILED
4. **If all agents in current wave are terminal** (COMPLETE/FAILED/SKIPPED/TIMED_OUT): apply failure policy and dispatch next wave
5. **If some agents still running:** wait for their notifications (re-attach)

**Key principle:** All state is file-based. The orchestrator is stateless — it can reconstruct the full execution picture from per-agent state files and the wave manifest at any time. This is the same resume model the current session-start uses (read session_state.json, pick up where you left off), extended to wave-level granularity.

The wave manifest must record:
```json
{
  "waves": [
    {"wave": 0, "tasks": [1], "status": "complete"},
    {"wave": 1, "tasks": [2, 3, 4], "status": "active", "dispatched_at": "..."},
    {"wave": 2, "tasks": [5], "status": "pending"}
  ],
  "current_wave": 1,
  "failure_policy": "partial"
}
```

This is sufficient for any restart to determine: what's done, what's running, what's next.
