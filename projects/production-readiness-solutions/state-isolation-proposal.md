# State Isolation — Solution Proposal

**Backlog:** 146-kernel-research-state-isolation-and-ci-solutions
**Date:** 2026-06-22
**Source:** External review critique (backlog 145) + research

---

## Industry Patterns

### LangGraph: Reducer-Driven State with Thread Isolation
- State is a typed schema (TypedDict) with **reducer functions** per field
- Each field can be overwrite-on-update OR accumulate (append-only)
- **Thread isolation**: each conversation/task gets a unique `thread_id` — state, history, and checkpoints are scoped to the thread
- **Checkpointing**: state is checkpointed after each super-step (batch of concurrent node executions), enabling pause/resume and failure recovery
- **Subgraph encapsulation**: a team of agents becomes a single node in the parent graph — internal state is isolated from the parent
- **Key insight**: state keys have explicit merge semantics, not last-write-wins

### CrewAI: Namespace Separation + Memory Layering
- Default memory is machine-bound with no multi-user isolation (ChromaDB locking errors under concurrency)
- Community solution: **scoped namespaces** — each agent has its own namespace, downstream agents read when needed
- **Memory layering**: shared layer (read-only) + private layer (per-agent, full read-write)
- **Append-only log pattern**: each agent owns its section, only reads others' contributions — prevents write conflicts
- **Checkpoint-based recovery**: mark last successfully completed step, resume from there on failure
- **Failure mode**: stale reads — solved with MESI-style invalidation signals

### AutoGen: Message Passing Over Shared State
- **No shared mutable state** — agents communicate exclusively via asynchronous messages
- **Agent instance separation**: each agent is an independent instance with its own internal state
- **Topic-based routing**: messages published to topics, agents subscribe to topics they care about
- **Closure agents**: dedicated agents collect results from concurrent workers
- **Key insight**: eliminates shared state entirely — isolation is architectural, not bolted on

### RAFT Consensus (Academic)
- Distributed consensus for state synchronization across nodes
- Leader election, log replication, term-based conflict resolution
- **Overkill for file-based kernel** — designed for network-distributed systems, not local file I/O
- Relevant concept: **append-only log** as source of truth (matches kernel's actions.jsonl pattern)

---

## Current State — What Already Exists

| Mechanism | Where | What It Does | Gap |
|-----------|-------|-------------|-----|
| `one_shot` guard | `universal-gate-enforcer.py:196-252` | Skips Gates 3/4/5 for run-task.sh sub-agents | Only prevents hook contention, not state overwrites |
| Lock file | `run-task.sh:47-64` | Prevents concurrent run-task.sh on same task folder | Doesn't prevent concurrent writes to shared state files |
| Per-agent state files | `spawn-agent-swarm/step-02` | `agent-{N}-state.json` per agent, monitor aggregates | **Designed but not wired into execute-pipeline** |
| Agent manifest | `.claude/state/agent-swarm.json` | Tracks all spawned agents with status | Only used by spawn-agent-swarm skill |
| Actions log | `.claude/state/actions.jsonl` | Append-only ledger of all actions | Shared across all agents — no per-agent scoping |

**The gap**: Per-agent isolation exists in the `spawn-agent-swarm` skill but is NOT used during execute-pipeline's parallel agent workflow. Background agents spawned by direct `Agent` tool calls write to shared `session_state.json`.

---

## Gap Analysis

### What Goes Wrong Today

1. **Context field overwrites**: Background agent writes its `context` to `session_state.json`, overwriting the parent's context
2. **Actions log mixing**: All agents append to the same `actions.jsonl` — anchor reviews can't distinguish which agent performed which action
3. **Workflow state collision**: `sr_dev_workflow.json` fields (`completed_tasks`, `actions_since_anchor`) get updated by multiple agents

### What Doesn't Go Wrong (Already Mitigated)

1. **Anchor/counter corruption**: `one_shot` guard prevents sub-agents from resetting anchor state
2. **Concurrent task execution**: Lock file prevents two run-task.sh on the same folder
3. **Work product loss**: Agents build in separate repos/branches — deliverables are isolated by Git

---

## Proposed Solution

**Pattern: Per-Agent State Files + Protected Parent Context**

Combines LangGraph's thread isolation, CrewAI's namespace separation, and the existing `spawn-agent-swarm` per-agent file design. No external runtime required.

### Architecture

```
.claude/state/
├── session_state.json          ← PARENT ONLY (orchestrator writes, agents read-only)
├── sr_dev_workflow.json        ← PARENT ONLY (orchestrator writes)
├── actions.jsonl               ← PARENT ONLY (orchestrator's actions)
├── agent-swarm.json            ← Manifest (orchestrator writes)
├── agent-128-state.json        ← Agent 128's isolated state
├── agent-128-actions.jsonl     ← Agent 128's actions log
├── agent-131-state.json        ← Agent 131's isolated state
├── agent-131-actions.jsonl     ← Agent 131's actions log
└── anchor-logs/                ← Shared archive (append-only, no contention)
```

### Isolation Rules

1. **Parent session** writes to `session_state.json` and `{domain}_workflow.json`
2. **Spawned agents** write ONLY to `agent-{N}-state.json` and `agent-{N}-actions.jsonl`
3. **Agents read** `session_state.json` for initial context but never write to it
4. **Monitor** reads all `agent-{N}-state.json` files to aggregate status
5. **Actions log appender hook** detects agent context and routes to per-agent log

### How Agents Know Their Identity

The agent identity is passed via environment variable or `pre_init_state`:

```bash
# In execute-pipeline when spawning background agent:
pre_init_state "session_started=True,one_shot=True,agent_id=128"

# Or via environment variable:
AGENT_ID=128 bash run-task.sh ...
```

The universal-gate-enforcer reads `agent_id` from session state and routes actions log writes accordingly:

```python
# In actions-log-appender hook (PostToolUse):
agent_id = session_state.get('agent_id')
if agent_id:
    log_file = STATE_DIR / f'agent-{agent_id}-actions.jsonl'
else:
    log_file = STATE_DIR / 'actions.jsonl'
```

---

## Implementation

### Change 1: Hook — Route actions log by agent_id

**File:** `.claude/hooks/universal-gate-enforcer.py` (or actions-log-appender if separate)

```python
def get_actions_log_path(session_state):
    """Route actions to per-agent log if agent_id is set."""
    agent_id = session_state.get('agent_id')
    if agent_id:
        return STATE_DIR / f'agent-{agent_id}-actions.jsonl'
    return STATE_DIR / 'actions.jsonl'
```

### Change 2: Hook — Skip session_state writes for agents

**File:** `.claude/hooks/universal-gate-enforcer.py`

The `one_shot` guard already skips Gates 3/4/5. Extend it to also skip any writes to `session_state.json` context field. Currently the hook doesn't write context — agents do that themselves. The enforcement is in the agent prompt:

```
# In run-task.sh pre_init_state or agent prompt:
"You are agent-{N}. Write state ONLY to .claude/state/agent-{N}-state.json.
 Do NOT modify session_state.json or {domain}_workflow.json."
```

### Change 3: run-task.sh — Pass agent_id

**File:** `run-task.sh`

```bash
# Add agent_id to pre_init_state (line ~289):
pre_init_state "session_started=True,one_shot=True,agent_id=${BACKLOG_NUM}"
```

### Change 4: execute-pipeline — Use per-agent state for background agents

**File:** `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`

When spawning background agents via Agent tool, include agent identity:

```
Agent(
  prompt: "...AGENT_ID=128 env -u CLAUDECODE bash run-task.sh ...",
  run_in_background: true
)
```

### Change 5: Monitor — Aggregate per-agent state

**File:** `.claude/skills/spawn-agent-swarm/references/step-04-monitor.md` (already designed)

```python
def aggregate_status():
    """Read all agent-N-state.json files, return combined status."""
    agents = glob('.claude/state/agent-*-state.json')
    return [json.load(open(f)) for f in agents]
```

---

## Migration Path

1. **Phase 1** (immediate): Add `agent_id` to `pre_init_state` in run-task.sh. Add log routing to actions-log-appender hook. Zero breaking changes — agents without `agent_id` use existing shared state.
2. **Phase 2** (next sprint): Update execute-pipeline step 4 to pass agent identity when spawning background agents.
3. **Phase 3** (follow-up): Add monitor aggregation to execute-pipeline step 5 (validation) so it reads per-agent state for the completion report.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Agent ignores prompt instruction and writes to shared state | Hook enforcement: reject writes to session_state.json when agent_id is set |
| Per-agent files accumulate (no cleanup) | Anchor ceremony archives and cleans up per-agent logs alongside actions.jsonl |
| Monitor reads stale per-agent files from prior runs | Clear agent-*-state.json at pipeline start (same as clearing cycling state) |
| Windows file locking on concurrent reads | JSON reads are atomic on Windows when files are small (<4KB) — no issue at current scale |

---

## Effort Estimate

**Small** — 4-6 hours of implementation. The pattern exists in spawn-agent-swarm. Changes are:
- 1 hook modification (log routing by agent_id)
- 1 run-task.sh modification (pass agent_id)
- 1 execute-pipeline reference update (spawn with identity)
- 1 prompt modification (agent isolation instruction)

No new architecture. No external dependencies. Compatible with existing hooks and Windows+Unix.
