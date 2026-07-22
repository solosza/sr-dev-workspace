# DAG Wave Engine — Orchestration

**When used:** Automatically when backlogs or task folders declare `depends_on` dependencies.

**When NOT used:** Backlogs with no dependencies produce a single wave (current flat-parallel behavior).

## Design Principles

The wave engine provides **dependency-aware orchestration** for multi-backlog or multi-task scenarios:
- Parse `depends_on` metadata (backlog frontmatter or task index columns)
- Topologically sort into execution waves using Kahn's algorithm
- Detect cycles and error before any spawn
- Dispatch waves sequentially, coordinate via notification-driven barrier
- Partial dispatch on failure: only downstream dependents are blocked

See `projects/kernel-dag-wave-research/` for full design documentation.

## Metadata Format

Dependencies are declared in TWO places:

### 1. Task-Level Dependencies (Within a Backlog's Task Folder)

In `tasks/[subfolder]/000-index.md`, add a `Dependencies` column:

```markdown
| # | Task | Type | Dependencies |
|---|------|------|---|
| 001 | task1 | BUILD | none |
| 002 | task2 | BUILD | 001 |
| 003 | task3 | TEST | 001, 002 |
```

Parse rules:
- `none` or empty = no dependencies
- Comma-separated task numbers = list of dependencies
- Referenced tasks must exist in the same index

### 2. Backlog-Level Dependencies (Future Extension)

Backlogs may declare prerequisites in frontmatter (reserved for future use):
```yaml
depends_on: [241, 242]
```

## Wave Sorting Algorithm (Kahn's BFS)

1. Parse dependencies → build adjacency list
2. Compute in-degree for each node
3. Wave 0 = all nodes with in-degree 0 (roots)
4. While nodes remain:
   - Remove current wave from graph
   - Decrement in-degree of dependents
   - Next wave = newly zero-in-degree nodes
5. Cycle detection: if nodes remain with non-zero in-degree after all waves → error

**Example:**
- Input: Task 1→2,3,4; Task 5→2,3,4
- Waves: [1,5] → [2,3,4]

## Manifest Structure (Wave-Aware)

`.claude/state/agent-swarm.json`:

```json
{
  "wave_plan": [
    {"wave_id": 0, "backlog": 128, "tasks": [1, 2, 3]},
    {"wave_id": 1, "backlog": 128, "tasks": [4, 5]}
  ],
  "current_wave": 0,
  "waves_completed": [],
  "active_agents": [
    {"backlog": 128, "wave_id": 0, "status": "running", ...}
  ]
}
```

Fields added:
- `wave_plan`: Full DAG sorted into waves
- `current_wave`: Which wave is being dispatched
- `waves_completed`: History of completed waves
- `active_agents[].wave_id`: Which wave this agent belongs to

## Failure Decision Table (Partial Dispatch)

When wave N completes, apply this logic to decide which agents in wave N+1 dispatch:

| Scenario | Action |
|---|---|
| All wave N agents COMPLETE | Dispatch all wave N+1 agents |
| Some wave N agents FAILED | Block only wave N+1 agents depending on failed agents |
| Some wave N agents SKIPPED | Block only wave N+1 agents depending on skipped agents |
| Some wave N agents TIMED_OUT | Block only wave N+1 agents depending on timed-out agents |

**Dependency propagation:** If agent D in wave N+1 is blocked, any agent in wave N+2 depending on D is also blocked (cascading).

**Orphaned wave detection:** If all agents in wave N+1 are blocked, skip to next unblocked wave.

## Barrier Semantics (Wave Transitions)

The monitor becomes the wave orchestrator:

1. **Current wave active:** All agents in wave N dispatch and run
2. **Wave completes:** All agents reach terminal state (COMPLETE/FAILED/SKIPPED/TIMED_OUT)
3. **Failure analysis:** Apply partial dispatch policy
4. **Next wave dispatch:** Update manifest, invoke step-03 again for wave N+1
5. **Pipeline end:** When all waves processed or all remaining waves are blocked

**Timeout per wave:** 30 minutes (configurable). If wave stalls, mark incomplete agents as TIMED_OUT.

**Resume capability:** On orchestrator restart, read manifest to determine:
- Which wave is active
- Which agents are complete/failed/blocked
- Which agents need re-dispatch

## Integration with Execute-Pipeline

When execute-pipeline needs to spawn multiple backlogs, it can invoke the swarm with dependencies:

```
/spawn-agent-swarm 241 242 243
```

If backlogs 241 and 242 have no dependencies but 243 depends on both:
- Waves: [241, 242] → [243]
- Dispatch order: 241 and 242 in parallel, then 243 after both complete

This is backward-compatible: backlogs with no dependencies produce a single wave (current behavior).

## Libraries

Implementation code:

| File | Purpose |
|---|---|
| `lib/wave_sort.py` | Kahn's algorithm, topological sort, cycle detection |
| `lib/barrier_semantics.py` | Failure decision table, partial dispatch logic, wave transitions |
