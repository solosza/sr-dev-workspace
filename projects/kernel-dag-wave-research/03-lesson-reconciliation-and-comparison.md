# Lesson Reconciliation + Cross-Proposal Comparison

## 1. STRICTLY-SEQUENTIAL Lesson Analysis

The lessons.md rule reads: "When `/kernel/execute-pipeline` receives multiple backlog numbers, execute each pipeline to completion before starting the next. Both write to shared state files and create contention that blocks the parent via hook enforcement."

The root cause was **shared mutable state** — `session_state.json` and `sr_dev_workflow.json` are single files that every agent reads and writes. When pipelines overlap, later writes overwrite earlier state, and hooks (which read the same shared files) block the parent incorrectly.

### Does Per-Agent State Isolation Satisfy the Lesson?

**Yes, conditionally.** The per-agent state file pattern (`agent-{id}-workflow.json`, `agent-{id}-actions.jsonl`) was introduced specifically to solve this contention. Each agent writes only to its own files; the orchestrator reads all of them independently.

**However:** `session_state.json` remains a shared contention point. Evidence from the 2026-07-21 swarm 237-240 run (observed live in `kernel-ephemeral-subagents-research/03-integration-design.md`):

> "Four concurrent research agents (backlogs 237-240) fought over session_state.json repeatedly. Agent_id was overwritten, context was lost, hooks blocked because the wrong agent's state was active."

This means intra-wave parallelism (multiple agents in the same wave running simultaneously) is safe **only if** each agent's session-start writes to its own `agent-{id}-session.json` instead of the shared `session_state.json`. The per-agent workflow isolation is already there; the session-state isolation is not.

### Verdict on the Lesson

The STRICTLY-SEQUENTIAL rule remains valid for the **inter-pipeline** case (multiple independent `execute-pipeline` invocations against different backlogs). But the DAG wave engine operates **intra-pipeline** — within a single pipeline's task set, parallelizing independent tasks. These are different scopes:

- **Inter-pipeline** (lesson scope): pipelines 037, 038, 039 run independently with no shared task graph. Sequential is the only safe option until session-state isolation ships.
- **Intra-pipeline** (wave scope): tasks 002, 003, 004 within a single pipeline share a task graph, and per-agent workflow isolation already prevents the documented contention. The remaining gap is session_state.json, which needs per-agent scoping.

**Conclusion:** DAG waves within a single pipeline do NOT violate the sequential lesson, provided session_state.json contention is resolved. The lesson's rationale (shared mutable state) is satisfied by per-agent isolation at both the workflow and session layers.

## 2. Layer-Ownership Comparison: 241 vs 242 vs 243

Three proposals address ordering at different layers:

| Proposal | Layer | Mechanism | When It Acts |
|----------|-------|-----------|-------------|
| **241 (DAG Waves)** | Orchestrator dispatch | Topological sort of task index; barrier between waves | Before agent spawn — downstream agents never start until upstream completes |
| **242 (Barrier Gates)** | Task execution (run-task.sh) | File-existence prerequisites in gate contracts; wait/poll loop | At task start — agent spawns but waits for prerequisite files before executing |
| **243 (Artifact Bus)** | Data layer | Structured manifest exports; consumer ingestion step | At data handoff — downstream task reads manifest to discover what upstream produced |

### Key Differences

**241 controls WHEN agents run.** The orchestrator never spawns a wave N+1 agent until all of wave N exits. This is the cheapest approach — no wasted compute on agents that can't proceed. But it's coarse-grained: if wave 1 has tasks A and B, and wave 2 has tasks C (depends on A) and D (depends on B), ALL of wave 1 must complete before ANY of wave 2 starts (unless partial dispatch is implemented, as proposed in `02-barrier-monitor-and-failures.md`).

**242 controls WHETHER an agent proceeds.** The agent is spawned but checks prerequisites before doing work. This is finer-grained — agent C starts immediately and polls for A's output, while D polls for B's output independently. But it has a cost: polling agents hold a run-task.sh process open doing nothing (resource waste), and a waiting agent looks identical to a stalled agent from the monitor's perspective.

**243 controls WHAT data is consumed.** It doesn't enforce ordering at all — it structures the handoff so that when downstream runs, it knows exactly what upstream produced. Without 241 or 242, downstream could run before upstream and get an empty manifest. The bus is an enabler, not an enforcer.

## 3. Composition Proposal

### Primary: 241 (DAG Waves at the Orchestrator)

DAG wave dispatch should be the **primary ordering mechanism**. It is:
- **Cheapest:** No wasted compute — downstream agents don't spawn until upstream completes
- **Simplest to implement:** ~50 lines of Python for Kahn's algorithm, reading the existing task index format
- **Already backward-compatible:** No dependencies = single wave = current behavior
- **Aligned with the kernel's existing pattern:** The orchestrator already controls spawn timing; this refines it from "all at once" to "in dependency order"

### Defense-in-Depth: 242 (Barrier Gates in run-task.sh)

Barrier gates serve as a **safety net** under 241, not a replacement. If the orchestrator dispatches a wave correctly, barrier gates are never triggered (prerequisites are already satisfied). But if:
- The orchestrator has a bug and dispatches too early
- A manual `run-task.sh` invocation bypasses the orchestrator
- An agent crashes and is re-run independently

...then the barrier gate catches the premature execution and waits. This is the same "two-tier enforcement" pattern the kernel already uses (hooks as hard enforcement, protocol as soft enforcement).

**Recommendation for 242:** YAH, but only as defense-in-depth. Not worth building standalone — it's a ~20-line file-existence check in run-task.sh's pre-execution phase. Build it alongside or after 241.

### Deferred: 243 (Artifact Bus)

The artifact bus is **not needed yet**. The current per-agent state file pattern (`agent-{id}-state.json` with `completed_tasks` array) plus the gate contract (which already enumerates deliverables) provide enough information for downstream agents to locate upstream outputs.

Evidence: swarm 237-240's portfolio task (240) located sibling research outputs by convention (`projects/kernel-*-research/`). It worked because naming was uniform. An artifact bus would formalize this, but the formalization has no value until naming stops being uniform — which won't happen until the kernel manages cross-project dependencies (not currently on the roadmap).

**Recommendation for 243:** NAY for now. Revisit when (a) cross-project dependencies appear, or (b) the naming convention proves insufficient for more than 4-agent swarms. The overlap analysis in 243's backlog requirements ("is the bus new information or a re-serialization?") correctly identifies the risk: the bus re-serializes what gate contracts and per-agent state already express.

### Composition Summary

| Proposal | Verdict | Role | Build Order |
|----------|---------|------|-------------|
| 241 (DAG Waves) | **YAH** | Primary ordering mechanism | First |
| 242 (Barrier Gates) | **YAH** (conditional) | Defense-in-depth under 241 | Second, alongside or after 241 |
| 243 (Artifact Bus) | **NAY** (deferred) | Not needed yet | Revisit when cross-project deps appear |

The three compose cleanly because they operate at different layers: 241 decides WHEN to spawn, 242 guards against premature execution, 243 would structure WHAT is consumed. Only the first is needed now; the second is cheap insurance; the third solves a problem that doesn't exist yet.
