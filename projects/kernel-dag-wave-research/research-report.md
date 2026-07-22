# DAG Wave Execution Engine — Research Report

## Verdict: YAH

Adopt DAG wave execution (dependency-sorted dispatch with barrier monitoring) in the kernel's spawn-agent-swarm and execute-pipeline dispatch layer. The design is backward-compatible, implementation cost is low (~50 lines of sort logic + manifest extension), and it solves a real ordering problem that currently requires manual sequencing or lucky timing.

## Findings Summary

### 01 — Dependency Metadata + Wave Sorting

Dependencies are declared in the task index (`000-index.md`) using the existing `Dependencies` column — already present in every task-builder output. Wave sorting uses Kahn's algorithm (BFS topological sort) with built-in cycle detection. The algorithm naturally extracts waves: each BFS level becomes a dispatch wave. Backward compatibility is guaranteed — a task index with no dependencies (or all `none`) produces a single wave, which is identical to current flat-parallel behavior.

The format is self-hosting: this research's own task index uses the exact dependency format proposed.

### 02 — Barrier Monitor + Failure Semantics

The barrier between waves should be notification-driven (harness task-notifications when background agents exit), not polling. The current 5-minute poll cap is insufficient for multi-wave pipelines. Timeout backstop: 30 minutes per wave, extendable once if progress is advancing.

Failure semantics: partial dispatch is the recommended default. When a wave N agent fails, only its downstream dependents are blocked — other wave N+1 tasks whose dependencies all completed still dispatch. This maximizes useful work while propagating real failures. Override to `block_all` or `abort` via the task index for strict pipelines.

Resume after restart is naturally supported — all state is file-based (per-agent state files + wave manifest in `agent-swarm.json`). The orchestrator can reconstruct the full execution picture at any time by reading these files.

### 03 — Lesson Reconciliation + Cross-Proposal Comparison

The STRICTLY-SEQUENTIAL lesson applies to inter-pipeline ordering (multiple independent `execute-pipeline` invocations). DAG waves operate intra-pipeline (within a single pipeline's task graph), which is a different scope. The lesson's root cause (shared mutable state contention) is addressed by per-agent state isolation — already implemented for workflow state, pending for session_state.json.

Cross-proposal comparison:
- **241 (DAG Waves):** Primary ordering mechanism — controls WHEN agents spawn. YAH.
- **242 (Barrier Gates):** Defense-in-depth — controls WHETHER a spawned agent proceeds. YAH, conditional on building alongside 241.
- **243 (Artifact Bus):** Data-layer structuring — controls WHAT downstream consumes. NAY for now; the existing gate contracts and per-agent state files already express the same information.

## Trade-Off Analysis: DAG Waves vs Current Flat-Parallel

| Dimension | Current (Flat-Parallel) | DAG Waves |
|-----------|------------------------|-----------|
| **Ordering** | None — all tasks spawn simultaneously | Topological — respects declared dependencies |
| **Wasted compute** | Zero — all agents start immediately | Zero — agents in later waves don't spawn until dependencies complete (no polling waste) |
| **Latency** | Minimal — everything starts at t=0 | Higher — serialized waves add wall-clock time equal to the critical path |
| **Failure isolation** | None — if task A fails, task B (which depends on A's output) runs anyway and fails with missing input | Partial dispatch — B is blocked, C (independent of A) still runs |
| **Backward compat** | N/A (status quo) | Full — no dependencies = single wave = current behavior |
| **Complexity** | Trivial — spawn all | Moderate — sort + barrier + failure propagation |
| **State contention** | Per-agent isolation handles it | Same per-agent isolation; wave manifest is append-only |

**The latency trade-off is real but acceptable.** A 5-task pipeline with 3 waves (e.g., [1], [2,3,4], [5]) takes longer than spawning all 5 simultaneously. But the current flat approach only works when tasks are truly independent. When they aren't (task 5 reads outputs of 2, 3, 4), flat dispatch produces race conditions — the output may not exist yet. The latency cost of waves is the correctness cost of ordering.

## Implementation Spec

### Phase 1: Wave Sort in step-01

1. After task folder resolution, read `000-index.md`
2. Parse Dependencies column into adjacency list
3. Run Kahn's algorithm → produce wave list
4. Store in agent manifest: `{"waves": [{"wave": 0, "tasks": [1]}, ...], "current_wave": 0}`
5. If cycle detected: abort with diagnostic, no agents spawn

### Phase 2: Wave Dispatch in step-03

1. Read wave plan from manifest
2. For wave 0: spawn all tasks (current behavior, just scoped to wave 0)
3. Wait for task-notifications
4. On all wave 0 complete: evaluate failure policy, dispatch wave 1
5. Repeat until all waves dispatched or pipeline terminates early

### Phase 3: Manifest Extension

Extend `agent-swarm.json` with wave metadata:
```json
{
  "waves": [
    {"wave": 0, "tasks": ["001"], "status": "complete"},
    {"wave": 1, "tasks": ["002", "003", "004"], "status": "active"},
    {"wave": 2, "tasks": ["005"], "status": "pending"}
  ],
  "current_wave": 1,
  "failure_policy": "partial"
}
```

### Prerequisites

- Per-agent session-state isolation (session_state.json scoping) must ship before or alongside this, per the swarm 237-240 evidence. Without it, intra-wave parallel agents will contend on session_state.json even though workflow state is isolated.

### What This Does NOT Change

- run-task.sh: unchanged — still spawns one `claude -p` per task
- Task files: unchanged — individual tasks don't need to know about waves
- Gate contracts: unchanged — gates validate deliverables, not ordering
- Per-agent state files: unchanged — same isolation pattern
- Kernel commands (session-start, anchor, complete): unchanged — each one-shot agent runs the full kernel loop independently

The wave engine is a dispatch-layer addition that sits between "resolve task folder" and "spawn agents." Everything above and below it stays the same.
