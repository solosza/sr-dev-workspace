# Step 4: Wave Barrier Monitor (Notification-Driven + Polling Fallback)

Start a continuous loop that monitors the current wave and transitions to the next wave when complete. Notification-driven (task-completion event), with polling as fallback.

## Wave Barrier Mechanism

**Primary Signal:** Task completion notification (push-based, harness-driven)
**Fallback:** 10-second polling loops if notification unavailable

**Per-Wave Timeout:** 30 minutes per wave (configurable in task index)

**Loop behavior:**
- For current wave: wait for all agents to reach terminal state (COMPLETE/FAILED/SKIPPED/TIMED_OUT)
- Read per-agent state files to assess outcomes
- Apply failure decision table (partial dispatch policy)
- Dispatch next wave OR conclude pipeline if all waves done/blocked

## State File Architecture (CRITICAL FIX)

**DO NOT read shared state files** (`session_state.json`, `sr_dev_workflow.json`)

**Instead read per-agent state files:**
```
.claude/state/agent-{N}-state.json  ← source of truth for each agent
```

**Why:**
- Shared state files are overwritten by concurrent agents
- Per-agent files are isolated, no contention
- Each agent updates only its own file
- Monitor reads all per-agent files, aggregates results

## Detection Methods

For each agent in manifest (status = `running`):

### Method 1: Per-Agent State File

Read the isolated per-agent state file:

```python
agent_state_file = Path(".claude/state/agent-{N}-state.json")

if agent_state_file.exists():
    state = read_json(agent_state_file)
    progress = state.get("progress")  # e.g., "5/7 tasks"
    completed_count = len(state.get("completed_tasks", []))
    total_tasks = state.get("total_tasks")

    agent["progress"] = progress
    agent["last_update"] = NOW

    if completed_count == total_tasks and total_tasks > 0:
        agent["status"] = "complete"
        agent["completed_at"] = NOW
```

### Method 2: Backlog Archive Status (Confirmation)

After per-agent state shows "complete", verify by checking backlog:

```python
done_files = glob("docs/backlog/done/{N}-*")
if done_files:
    agent["status"] = "complete"  # Confirmed
```

## Polling Sequence

```python
for poll_num in range(max_polls):
    print(f"[Poll {poll_num} @ {poll_num * 10}s]")

    for agent in manifest.active_agents:
        backlog_num = agent.backlog

        # Read per-agent state file (PRIMARY source)
        agent_state_file = Path(f".claude/state/agent-{backlog_num}-state.json")

        if agent_state_file.exists() and agent.status == "running":
            state = read_json(agent_state_file)

            # Update from per-agent file
            progress = state.get("progress", "running")
            agent["progress"] = progress
            agent["last_update"] = NOW

            completed = len(state.get("completed_tasks", []))
            total = state.get("total_tasks")

            # Check for completion
            if completed > 0 and completed == total:
                agent["status"] = "complete"
                agent["completed_at"] = NOW
                print(f"  Agent {backlog_num}: COMPLETE ({completed}/{total} tasks)")
            else:
                print(f"  Agent {backlog_num}: {progress}")

        # Secondary: Verify with backlog archive status
        elif backlog_archived(backlog_num):
            agent["status"] = "complete"
            agent["completed_at"] = NOW

    # Save updated manifest
    write_json(manifest, "agent-swarm.json")

    # Check exit condition
    all_done = all(a.status == "complete" for a in agents)
    if all_done:
        break

    sleep(10)
```

## Output Format

Print updates as polling happens:

```
[Poll 0 @ 0s]
  Agent 128: COMPLETE (archived)
  Agent 131: 3/7 tasks
  Agent 132: COMPLETE (archived)

[Poll 1 @ 10s]
  Agent 128: COMPLETE (archived)
  Agent 131: 4/7 tasks
  Agent 132: COMPLETE (archived)

...continues until all complete...
```

## Manifest & State Updates

On each poll:

**Update agent-swarm.json (aggregated view):**
```python
agent.last_update = timestamp_now()
agent.progress = current_progress
agent.status = new_status
write_json(manifest, "agent-swarm.json")
```

**DO NOT update agent-{N}-state.json** — only read it. The background agent updates its own state file.

This creates audit trail in manifest while preserving per-agent isolation.

## Early Exit Conditions

Stop monitoring if:

1. **All agents complete** — `all(status == "complete")`
2. **Timeout reached** — 30 polls × 10 seconds = 5 minutes
3. **No running agents detected** — all status not "running" for 2+ consecutive polls

## Error Detection

Mark agent as `failed` if:
- Per-agent state file missing for 3+ polls
- State file shows error markers
- Backlog not archived after 5+ minutes of "running"
- No state file updates for 3+ polls (agent crashed)

```python
if agent.status == "running" and agent_state_file.exists():
    # Check state file's last_update time
    state = read_json(agent_state_file)
    last_update = state.get("last_update", agent.spawned_at)
    elapsed = NOW - last_update

    if elapsed > 30 seconds:  # 3 polls × 10s
        agent["status"] = "failed"
        agent["error"] = "No state file updates (agent may have crashed)"
```

## Failure Decision Table (Partial Dispatch Policy)

After current wave completes, apply this table to determine which agents in the next wave can dispatch:

| Current Wave Status | Next Wave Action |
|---|---|
| All COMPLETE | Dispatch all agents in next wave |
| One/more FAILED | Block ONLY downstream dependents of failed agents; dispatch others |
| One/more SKIPPED | Block ONLY downstream dependents of skipped agents; dispatch others |
| One/more TIMED_OUT | Block ONLY downstream dependents of timed-out agents; dispatch others |

**Dependency lookup:** For each agent in next wave, check its `depends_on` list. If ANY dependency is in the FAILED/SKIPPED/TIMED_OUT set, mark that agent BLOCKED and skip dispatch.

**Cascade:** Blocking propagates forward — if agent D is blocked in wave N+1, any agent in wave N+2 that depends on D is also marked BLOCKED.

**Orphaned wave detection:** If all agents in next wave are blocked, log "Wave N+1 entirely blocked — no tasks to dispatch" and proceed to next unblocked wave.

## Wave Transition Logic

1. **Current wave completes:** All agents reach terminal state
2. **Read per-agent state files** for all agents in current wave
3. **Classify outcomes:** COMPLETE/FAILED/SKIPPED/TIMED_OUT per agent
4. **Update manifest:** Set current wave status to "complete", add to `waves_completed`
5. **Evaluate next wave:** Apply failure decision table
6. **Determine dispatched set:** Subset of next-wave agents that pass dependency checks
7. **If dispatched set is empty:** Continue to next unblocked wave
8. **If dispatched set is non-empty:** Increment `current_wave`, dispatch via step-03 again
9. **If all waves processed:** Conclude pipeline with summary

## Resume After Orchestrator Restart

1. **Read manifest** — contains `wave_plan`, `current_wave`, `waves_completed`
2. **Determine active wave state:**
   - Read per-agent state files for all agents in `current_wave`
   - Classify each: COMPLETE/FAILED/SKIPPED/TIMED_OUT/RUNNING
3. **If all agents terminal:** Apply failure policy and dispatch next wave
4. **If some agents still running:** Re-attach to notifications and continue monitoring

## Key Difference from Previous

**OLD (broken):**
- Monitor read shared `session_state.json`
- Agent 131 completed, overwrote agent 132's state
- Monitor lost visibility into agent 132
- Result: "still running" for hours

**NEW (fixed):**
- Monitor reads per-agent `.claude/state/agent-N-state.json`
- Agent 131 updates `agent-131-state.json` only
- Agent 132 updates `agent-132-state.json` only
- Monitor sees both agents independently
- No overwrites, no visibility loss

**Wave Barrier (NEW):**
- Monitor becomes orchestrator of wave transitions
- Manifest tracks wave state (current_wave, waves_completed, wave_plan)
- Failure decision table provides partial dispatch semantics
- Resume from manifest restores full execution picture after restart
