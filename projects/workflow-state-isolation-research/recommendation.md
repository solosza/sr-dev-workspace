# Recommendation: Scoped Write Guard for Workflow State Isolation

## Recommendation

**Strategy E: Scoped Write Guard** — When `agent_id` is set, route per-agent fields to `agent-{id}-workflow.json`. Global fields stay in shared `sr_dev_workflow.json`.

## Why This Strategy

- Fewest files to change (4 vs 7 for alternatives)
- Builds on the proven actions-log-appender routing pattern
- Field classification is complete (15 per-agent, 12 global)
- No behavior change for single-agent execution
- No file locking, no context carrying, no major redesign

## Implementation Sketch

### Change 1: `/kernel/complete` command

**File:** `.claude/commands/kernel/complete.md`

**Current:** Reads and writes all fields to `sr_dev_workflow.json`

**Change:** Add routing logic:
```
1. Read session_state.json for agent_id
2. If agent_id is set:
   - Read agent-{id}-workflow.json (create if missing, seed from sr_dev_workflow.json global fields)
   - Write per-agent fields (completed_tasks, current_task, task_folder, total_tasks, cycling, cycling_complete, complete, complete_timestamp, attempts_on_current, timestamp) to agent-{id}-workflow.json
   - Do NOT write these fields to sr_dev_workflow.json
3. If agent_id is null:
   - Write everything to sr_dev_workflow.json (current behavior, unchanged)
```

### Change 2: Universal Gate Enforcer hook

**File:** `.claude/hooks/universal-gate-enforcer.py`

**Current:** Reads `anchored`, `actions_since_anchor`, `actions_limit` from `sr_dev_workflow.json`. Increments `actions_since_anchor`.

**Change:** Add routing logic:
```python
def get_workflow_state(session_state):
    agent_id = session_state.get('agent_id')
    if agent_id:
        agent_file = STATE_DIR / f'agent-{agent_id}-workflow.json'
        if agent_file.exists():
            return json.loads(agent_file.read_text()), agent_file
    return json.loads(WORKFLOW_FILE.read_text()), WORKFLOW_FILE

# Read from correct file
workflow, workflow_path = get_workflow_state(session_state)
# Write counter increment to correct file
```

### Change 3: `/kernel/anchor` command

**File:** `.claude/commands/kernel/anchor.md`

**Current:** Resets `actions_since_anchor` to 0, sets `anchored: true` in `sr_dev_workflow.json`

**Change:** Same routing — when agent_id set, write anchor fields to `agent-{id}-workflow.json`

### Change 4: run-task.sh and lib/common.sh

**File:** `run-task.sh` lines 251-268, `lib/common.sh` lines 94-191

**Current:** Reads `completed_tasks`, `skipped_tasks`, `current_task` from `sr_dev_workflow.json`

**Change:**
```bash
# In run-task.sh, after AGENT_ID is set:
WORKFLOW_FILE="$STATE_DIR/${DOMAIN}_workflow.json"
if [ -n "$AGENT_ID" ] && [ "$AGENT_ID" != "default" ]; then
    AGENT_WORKFLOW="$STATE_DIR/agent-${AGENT_ID}-workflow.json"
    if [ -f "$AGENT_WORKFLOW" ]; then
        WORKFLOW_FILE="$AGENT_WORKFLOW"
    fi
fi
# Use $WORKFLOW_FILE for all jq reads
```

Same pattern in lib/common.sh for `print_state` and `skip_current_task`.

### Change 5: Agent workflow file seeding

When an agent-specific workflow file doesn't exist yet, seed it:
```json
{
  "cycling": false,
  "cycling_complete": false,
  "task_folder": null,
  "total_tasks": null,
  "current_task": null,
  "completed_tasks": [],
  "skipped_tasks": [],
  "attempts_on_current": 0,
  "complete": false,
  "complete_timestamp": null,
  "anchored": true,
  "anchor_timestamp": null,
  "actions_since_anchor": 0,
  "last_anchor_token_confirmed": null,
  "timestamp": null
}
```

Global fields are NOT copied — the agent file only contains per-agent fields. Commands that need global fields (like `protocol_created`) still read from the shared file.

### Change 6: Parent merge on completion

After parallel agents complete, the parent (execute-pipeline step 5 or spawn-agent-swarm step 5) reads each `agent-{id}-workflow.json` to aggregate results:

```python
for agent_file in glob("agent-*-workflow.json"):
    state = json.loads(agent_file.read_text())
    report.append({
        "agent": agent_file.stem,
        "completed": state["completed_tasks"],
        "skipped": state["skipped_tasks"],
        "status": "complete" if state["complete"] else "incomplete"
    })
```

No merge INTO sr_dev_workflow.json — the parent reports from agent files directly. The shared workflow file retains its global-only state.

## Migration Path

1. Ship changes 1-4 (routing guards)
2. Sequential execution: no agent_id set, everything uses shared file (zero behavior change)
3. Parallel execution: agent_id set by run-task.sh, per-agent fields route to isolated files
4. Existing agent-{id}-actions.jsonl pattern already handles actions log (backlog 153)
5. No migration needed for existing state — new pattern activates only when agent_id is present

## Test Plan

Re-run the 150/151/152 parallel test:
1. Build task folders for backlogs 150, 151, 152
2. Spawn all 3 via `env -u CLAUDECODE bash run-task.sh` in parallel
3. Verify:
   - Each agent creates its own `agent-{subfolder}-workflow.json`
   - Shared `sr_dev_workflow.json` global fields unchanged
   - Each agent completes ALL its tasks (not just task 001)
   - No cross-agent task confusion
   - `completed_tasks` in each agent file contains only that agent's tasks
4. Verify sequential still works: run a single pipeline, confirm shared file behavior unchanged

## Rejected Alternatives

| Strategy | Reason for Rejection |
|----------|---------------------|
| B: File Locking | Doesn't solve semantic contention (agents still write conflicting values), cross-platform fragility, deadlock risk |
| C: Carry-and-Merge | Incompatible with run-task.sh one-shot-per-task model — no context persistence between claude -p invocations |
| D: Split File | More complex than E with similar benefits — splitting introduces two file schemas to maintain |
| A: Per-Agent Files (whole file) | Viable runner-up but routes global fields unnecessarily, requiring merge logic that E avoids |
