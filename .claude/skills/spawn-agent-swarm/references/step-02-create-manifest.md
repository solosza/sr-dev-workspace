# Step 2: Create/Update Agent Manifest

Create or update the shared agent manifest file that tracks all spawned agents.

## Manifest File Location

`.claude/state/agent-swarm.json`

## Manifest Structure

```json
{
  "wave_plan": [
    {
      "wave_id": 0,
      "backlog": 128,
      "task_folder": "tasks/reference-tests-db/",
      "tasks": [1, 2, 3]
    },
    {
      "wave_id": 1,
      "backlog": 128,
      "task_folder": "tasks/reference-tests-db/",
      "tasks": [4, 5]
    }
  ],
  "current_wave": 0,
  "waves_completed": [],
  "active_agents": [
    {
      "backlog": 128,
      "spawned_at": "2026-06-15T01:00:00Z",
      "status": "running",
      "progress": "0/8 tasks",
      "last_update": "2026-06-15T01:00:00Z",
      "last_completed": null,
      "deliverable": "Pulsia autonomous AI platform research",
      "wave_id": 0
    }
  ]
}
```

## Processing

1. **Read existing manifest** (if exists, preserve completed agents and wave plan)
2. **Input wave plan:** Accept `wave_plan` from step-01 (output of topological sort with cycle detection)
3. **Initialize wave tracking:**
   - Set `current_wave` = 0 (start with first wave)
   - Set `waves_completed` = [] (no waves completed yet)
   - Store full `wave_plan` from step-01 input
4. **For each agent in the current wave only:**
   - Resolve backlog number from wave entry
   - Check if already in manifest
   - If yes (already running): skip with warning
   - If no (new): add entry with status=`running` and `wave_id` from wave plan
5. **Initialize new agent entry:**
   ```json
   {
     "backlog": N,
     "spawned_at": "ISO_TIMESTAMP_NOW",
     "status": "running",
     "progress": "0/? tasks",
     "last_update": "ISO_TIMESTAMP_NOW",
     "last_completed": null,
     "deliverable": null,
     "wave_id": 0
   }
   ```
6. **Save manifest back** to `.claude/state/agent-swarm.json` with wave_plan and current_wave fields

## Per-Agent State Files (CRITICAL)

**Each agent gets its own isolated state file to prevent contention.**

For each new agent N, create:
```
.claude/state/agent-{N}-state.json
```

Initial content:
```json
{
  "backlog": N,
  "backlog_path": "docs/backlog/NNN-tag-verb-object.md",
  "spawned_at": "ISO_TIMESTAMP_NOW",
  "status": "running",
  "progress": "0/? tasks",
  "task_folder": null,
  "total_tasks": null,
  "completed_tasks": [],
  "deliverable": null,
  "log_file": "/tmp/execute-pipeline-{N}-*.log"
}
```

**Why per-agent files:**
- Prevents state overwrites when multiple agents run concurrently
- Each agent's state is independent, no contention with other agents
- Monitor aggregates by reading N separate files, not one shared file
- Preserves execution visibility even if agent crashes or completes
- Agent 132 won't lose state when agent 131 updates shared files

## Manifest Rules

- **Append only for new agents** — don't remove completed agents from history
- **Preserve completed entries** — `status: "complete"` agents stay in manifest (audit trail)
- **Status transitions:** `running` → `complete` or `running` → `failed` (never reverse)
- **Last_update:** Refreshed by monitor, not by this step
- **Deliverable field:** Populated by monitor after agent completes
- **Per-agent state is source of truth** — Monitor reads `agent-N-state.json`, not shared state files

## Validation

After writing manifest and per-agent files:
1. Read manifest back to verify format
2. Check that each per-agent file exists and is valid JSON
3. Count new vs existing agents
4. Report: "Manifest created with N agents (M new, K existing) + N per-agent state files"

## Example

**Input:** Backlog numbers [128, 131, 132]

**Action:**
1. Manifest doesn't exist, create it with 3 new entries
2. Create 3 per-agent state files:
   - `.claude/state/agent-128-state.json`
   - `.claude/state/agent-131-state.json`
   - `.claude/state/agent-132-state.json`
3. Save manifest to `.claude/state/agent-swarm.json`

**Output:** Manifest + per-agent state files ready for monitoring
