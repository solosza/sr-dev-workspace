# Integration Design — Ephemeral Sub-Agents vs State-Contention Lessons

## Candidate Workflows to Move to Ephemeral Execution

### Currently Long-Lived Workflows

| Workflow | Current Model | Candidate for Ephemeral? | Rationale |
|----------|--------------|-------------------------|-----------|
| **Interactive orchestrator** | Single session, user-driven | No — user needs conversation continuity | Ephemeral agents lose conversation history; user would need to re-explain context every task |
| **execute-pipeline parent** | Single session, autonomous | Partial — task-builder runs inline, execution already ephemeral | Task-builder (Steps 1-3) needs full context of backlog + conventions; execution (Step 4) already spawns run-task.sh |
| **Vertical pipeline orchestrator** (e.g., 203-229 builds) | Long-lived session with multi-pipeline management | Yes — strongest candidate | Orchestrator accumulated 28 actions between anchors, multiple rule violations. Each vertical pipeline is independent |
| **Agent swarm orchestrator** | Long-lived monitor + spawn session | Partial — monitoring phase is lightweight | Spawn is already ephemeral; monitor is stateless polling |

### Anchor Policy Per Agent Tier

| Tier | Role | Anchor Policy | Rationale |
|------|------|--------------|-----------|
| **Tier 0: Interactive** | User conversation | Full anchor every N actions (current) | Cannot be ephemeral; user expects conversation continuity |
| **Tier 1: Pipeline orchestrator** | execute-pipeline parent | Full anchor at start; delegate all execution to Tier 2 | Keeps orchestrator context small; only plans and monitors |
| **Tier 2: One-shot executor** | run-task.sh agent | Inherit anchor from parent; execute one task | Current model; proven effective |
| **Tier 3: Inner test agent** | prod-test inner run-task.sh | Same as Tier 2; runs inside disposable test repo | Already fully isolated |

## State Handoff Schema Proposal

### Current Handoff: File-Based, Structural

```
Orchestrator writes:
  session_state.json → { agent_id, context, pipeline_state }
  {domain}_workflow.json → { completed_tasks, cycling, task_folder }

One-shot agent reads:
  session_state.json → finds agent_id, routes to per-agent workflow
  agent-{id}-workflow.json → reads completed_tasks, picks next

One-shot agent writes:
  agent-{id}-workflow.json → updates completed_tasks
  Deliverable files → actual work output
```

### Proposed Enhancement: Semantic Context Handoff

The current handoff transfers structural metadata (what was completed) but loses semantic context (why this approach was chosen, what constraints were discovered mid-execution, what the next agent should know). This is the primary weakness of the ephemeral model.

**Proposed schema extension:**

```json
{
  "handoff": {
    "completed_task": "003-build-write-something.md",
    "discoveries": [
      "Import paths must use _reference prefix (not bare module names)",
      "Docker container takes 15s to start, adjust timeout"
    ],
    "constraints": [
      "File X depends on Y being written first (not documented in task deps)"
    ],
    "next_agent_should_know": "The API response format changed from array to object in v2"
  }
}
```

Each one-shot agent would write a `handoff` block to its per-agent state file. The next agent's session-start would read prior handoffs from completed tasks to inherit discovered context. This is analogous to LangGraph's state annotations — structured context that survives agent boundaries.

**Cost:** ~500 tokens per handoff (write) + ~200 tokens per read (next agent reads all prior handoffs). For a 10-task pipeline: ~7,000 additional tokens. Acceptable given the ~200K total pipeline cost.

## Reconciliation with State-Contention Lessons

### Lesson: Shared Mutable State Causes Visibility Loss (2026-06-14)

**Problem:** Multiple concurrent agents wrote to `session_state.json` and `sr_dev_workflow.json`, causing overwrites and visibility loss.

**How ephemeral expansion interacts:** More ephemeral agents means MORE concurrent writers, not fewer. The per-agent state file pattern (`agent-{N}-state.json`, `agent-{N}-workflow.json`) already addresses this for execution state. BUT: `session_state.json` remains a shared contention point because every agent runs session-start which reads and writes it.

**Directly observed during this research:** Four concurrent research agents (backlogs 237-240) fought over `session_state.json` repeatedly. Agent_id was overwritten, context was lost, hooks blocked because the wrong agent's state was active. This is the exact same failure mode from the 2026-06-14 lesson, occurring in real-time.

**Resolution required:** `session_state.json` must either (a) be scoped per-agent (each agent reads/writes its own `agent-{id}-session.json`) or (b) become read-only after initial setup (agents read it for domain/protocol info but don't write to it).

### Lesson: Background Agents Reset Parent Anchor State (2026-04-23)

**Problem:** Sub-agent's session-start sets `anchored: false` on the shared workflow file, blocking the parent.

**Status:** Already mitigated for per-agent workflow files. The `agent_id` routing in anchor.md routes reads/writes to `agent-{id}-workflow.json`. BUT: session_state.json's `agent_id` field itself is the contention point — the field that routes to per-agent files is in the shared file.

**Hard blocker:** The routing mechanism depends on `session_state.json` containing the correct `agent_id`. With concurrent agents, this field is constantly overwritten. The hook reads session_state to find agent_id, but by the time it reads, another agent may have changed it. This is a fundamental design flaw in the current state routing.

### Lesson: Protocol Validation at Entry, Not Execution (2026-06-14)

**Compatibility:** Ephemeral agents validate protocol once at session-start (entry). This is already aligned with the lesson — no change needed for expanded ephemeral execution.

### Backlog 183: Worktree Isolation

**Status:** Research complete (projects/worktree-research/). Worktree isolation solves file-system contention (two agents writing the same source file) but does NOT solve state-file contention. State files live in `.claude/state/` which is NOT part of the worktree — it's in the main repo's `.claude/` directory.

**Interaction with ephemeral expansion:** Worktree isolation is complementary but insufficient. Both are needed: worktree for file isolation, per-agent state routing for state isolation.

## Hard Blockers for Expanded Ephemeral Execution

### Blocker 1: session_state.json Contention (CRITICAL)

The `agent_id` field in `session_state.json` is a single-writer field being used by multiple concurrent writers. Every agent sets it to its own ID during session-start, overwriting whatever the previous agent wrote. This breaks the routing mechanism that the entire per-agent isolation strategy depends on.

**Fix required:** Either:
- (a) Move agent_id into the per-agent state file (chicken-and-egg: how does the hook know which agent file to check without first reading session_state?)
- (b) Pass agent_id via environment variable (`AGENT_ID=xyz claude -p ...`) so it's per-process, not per-file
- (c) Use process-level isolation (PID-based routing) instead of file-based routing

Option (b) is the most practical: run-task.sh already controls the `claude -p` invocation and can set `AGENT_ID` in the environment. The hook reads `$AGENT_ID` instead of `session_state.json.agent_id`. No file contention.

### Blocker 2: Orchestrator Context Decay Remains

Moving more work to ephemeral agents doesn't eliminate the orchestrator. Someone needs to decompose tasks, monitor progress, synthesize results, and decide what to do next. If that role stays in a long-lived session, context decay remains for the orchestrator — just with less exposure per anchor cycle.

**Mitigation (not fix):** Keep the orchestrator's role minimal: decompose, dispatch, aggregate. Don't let it do actual work. The execute-pipeline skill already approaches this — the parent only plans and spawns.

### Blocker 3: Handoff Quality Gap

No mechanism exists to transfer semantic context between one-shot agents. The `completed_tasks` array tells the next agent WHAT was done, not HOW or WHY. If task 3 discovers a constraint that affects task 7, that context is lost unless explicitly written to a handoff file.

**Mitigation:** The semantic handoff schema proposed above. Low cost, high value. But requires changes to run-task.sh's prompt template and session-start's state reading logic.

## Summary

Expanded ephemeral execution is architecturally sound and well-aligned with industry patterns. The main blockers are all state-management issues, not conceptual ones: (1) session_state.json contention is critical and requires env-var-based agent_id routing, (2) orchestrator decay is inherent and can only be mitigated by keeping the orchestrator thin, (3) semantic handoff needs a schema extension. None of these are fundamental barriers — they are engineering tasks that fit the kernel's existing improvement loop.
