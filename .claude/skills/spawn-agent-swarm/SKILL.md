# Spawn Agent Swarm — Skill

**Type:** Orchestration
**Style:** Indexed — SKILL.md + references/

## What

Spawns multiple background agents in parallel, monitors their progress in real-time using isolated per-agent state files, and reports completion. Uses a shared agent manifest (`agent-swarm.json`) for aggregated view plus per-agent state files to prevent contention.

## Usage

```
/spawn-agent-swarm 128 131 132
/spawn-agent-swarm 125 126 127 129
/spawn-agent-swarm backlog-list.txt
```

**Arguments:**
- Backlog numbers (space-separated) → spawns one agent per backlog
- File path → reads backlog numbers from file (one per line)

## Steps

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Parse input (detect backlog numbers) | → `[[references/step-01-parse-input]]` |
| 2 | Create manifest + per-agent state files | → `[[references/step-02-create-manifest]]` |
| 3 | Spawn agents in parallel | → `[[references/step-03-spawn-agents]]` |
| 4 | Monitor agents continuously (per-agent isolation) | → `[[references/step-04-monitor]]` |
| 5 | Report final status | → `[[references/step-05-report]]` |

## Execution

1. **Parse input** to extract backlog numbers
2. **Create manifest** in `.claude/state/agent-swarm.json` (shared, aggregated view)
3. **Create per-agent state files** in `.claude/state/agent-{N}-state.json` (isolated per agent)
4. **Spawn all agents** via `Bash(run_in_background: true)` with `env -u CLAUDECODE bash run-task.sh [repo] [iterations] [subfolder]` — all in parallel, returns immediately
5. **Start continuous monitor** that polls per-agent state files every 10 seconds
6. **Report results** when all agents complete or timeout reached

**run-task.sh invocation:** `run-task.sh [REPO_ROOT] [MAX_ITERATIONS] [TASK_SUBFOLDER]`
- First arg = repo root (must have CLAUDE.md), NOT the task folder path
- Second arg = task count + 2 buffer
- Third arg = subfolder name under `tasks/` (just the name)

## Key Principles

- **Parallel execution** — all agents spawn simultaneously, no sequential wait
- **Non-blocking spawn** — returns after agents are spawned, doesn't wait for completion
- **Per-agent state isolation** — each agent writes to `agent-{N}-state.json`, preventing contention
- **Automatic monitoring** — monitor reads per-agent files, updates manifest in real-time
- **Generic tracking** — works with any number of agents (1 to N)
- **Real-time visibility** — user sees progress updates without manual checking
- **Eventual completion** — monitor detects completion via per-agent state files + backlog archive status
- **Composable** — can be chained or called standalone

## Agent Manifest (Shared)

File: `.claude/state/agent-swarm.json`

```json
{
  "active_agents": [
    {
      "backlog": 128,
      "spawned_at": "2026-06-15T01:00:00Z",
      "status": "complete | running | failed",
      "progress": "N/M tasks",
      "last_update": "ISO timestamp",
      "completed_at": "ISO timestamp",
      "deliverable": "human-readable description"
    }
  ]
}
```

**Status values:**
- `running` — agent spawned, tasks executing
- `complete` — all tasks done, backlog archived
- `failed` — agent errored out (detected after timeout)

## Per-Agent State Files (CRITICAL)

Files: `.claude/state/agent-{N}-state.json` (one per agent)

```json
{
  "backlog": 128,
  "spawned_at": "2026-06-15T01:00:00Z",
  "status": "running | complete | failed",
  "progress": "N/M tasks",
  "total_tasks": M,
  "completed_tasks": ["001-task.md", "002-task.md"],
  "last_update": "ISO timestamp",
  "task_folder": "tasks/project-name/",
  "deliverable": "description"
}
```

**Why per-agent files:**
- Prevents state overwrites when multiple agents run concurrently
- Each agent updates only its own file, no contention
- Monitor reads all files independently
- Preserves execution visibility even if other agents complete/crash
- Solves state contention issue from lesson 2026-06-14

## Monitor Behavior

Runs for max 30 polls (5 minutes with 10-second intervals):

- **Every 10 seconds:** Poll per-agent state files
- **Detection method:** Read `agent-{N}-state.json`, check `completed_tasks` count vs `total_tasks`
- **Real-time output:** Prints progress as agents complete
- **Stops early:** If all agents done OR no updates for 2+ polls

**CRITICAL: Read per-agent files, NOT shared state files**
- Monitor uses `agent-{N}-state.json` as source of truth
- Never reads `session_state.json` or `sr_dev_workflow.json` for agent status
- This prevents visibility loss from state file overwrites

## Outcome

After completion:
- `agent-swarm.json` updated with final status for all agents (aggregated)
- Per-agent state files show independent completion for each agent
- All spawned agents completed their pipelines
- User notified with final report (deliverables per agent)
- Backlog items moved to done/ as each agent finishes
