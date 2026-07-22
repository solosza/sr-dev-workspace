# Research Report: Deliverable-Based Barrier Gates in run-task.sh

## Verdict: YAH (Conditional — Defense-in-Depth Only)

Adopt barrier gates in run-task.sh as a defense-in-depth mechanism UNDER the wave engine (backlog 241). Do NOT adopt as a standalone ordering mechanism.

**Condition:** This verdict depends on backlog 241 (DAG wave execution) being adopted as the primary ordering layer. If 241 receives a NAY verdict, barrier gates should be reconsidered as standalone — but the standalone cost/complexity analysis in this report suggests that would be a weaker design.

---

## Findings Summary

### Task 002: Prerequisite Declaration Format

**Decision:** Gate-contract.md gains a `## Prerequisites` section using the existing pipe-delimited table format with `PRE-*` prefixed entries. This keeps prerequisites at the pipeline scope (where inter-pipeline dependencies live) and reuses bash-parseable table parsing already proven in gate validation.

**Content assertion:** Allowed, reusing existing gate types (`file_exists`, `grep`, `word_count`). Most prerequisites use `file_exists`; `grep` catches incomplete upstream outputs (e.g., a report that exists but lacks a verdict). Content assertion guards against stale partial artifacts.

**Intra-pipeline dependencies** remain in task files' `## Dependencies` section — no change needed, because run-task.sh executes tasks sequentially within a pipeline.

### Task 003: Wait/Poll Loop + Monitor Visibility

**Design:** 15-second poll interval, 600-second timeout (standalone) or 120-second timeout (under wave engine). On timeout, the pipeline exits with code 2 (BLOCKED), distinct from success (0) and failure (1).

**Monitor visibility:** Per-agent workflow state gains a `status` field with values: IDLE, RUNNING, WAITING, BLOCKED, COMPLETE. When an agent is WAITING, it writes `waiting_on` to its state file. The monitor uses this to distinguish waiting agents from stalled agents and to detect potential deadlocks.

**Cost comparison:** Polling holds one bash process (~10MB) per waiting pipeline. Wave-based non-spawning (241) holds zero processes — downstream agents don't exist until their wave dispatches. At current scale (<10 pipelines), polling cost is acceptable. At scale (50+), wave dispatch is clearly superior.

### Task 004: Deadlock + Staleness Analysis

**Deadlock prevention:** Static cycle detection at dispatch time (before any agents spawn). This mirrors 241's topological sort — cycles are rejected as configuration errors. Runtime timeout (600s) serves as a backstop for cross-swarm dependencies the static check can't see.

**Staleness mitigation:** Content-based prerequisites (`grep`/`word_count`) rather than timestamp comparison. A stale report from a successful prior run is acceptable (content is valid). A stale stub from a partial prior run is caught by content assertions. Upstream completion status (no skipped tasks) adds a soft health check.

**Partial outputs:** When an upstream pipeline has skipped tasks, its outputs may be incomplete. The downstream prerequisite check should verify both file existence AND upstream agent health (completion status with no skips).

---

## Trade-Off Analysis: Barrier Gates vs Current Flat-Parallel Dispatch

### Current Behavior (No Ordering)

Today, spawn-agent-swarm and execute-pipeline fire all agents simultaneously. Inter-pipeline dependencies are handled by:
1. The `STRICTLY_SEQUENTIAL` lesson — execute one pipeline at a time (no parallelism)
2. Soft tolerance — agents read sibling outputs "if present" and degrade gracefully (swarm 237-240 pattern)

**Problems with current behavior:**
- STRICTLY_SEQUENTIAL eliminates parallelism entirely — a 5-pipeline swarm takes 5x longer
- Soft tolerance works only when the consumer can produce a meaningful result WITHOUT the dependency (240's portfolio ranking worked, but would have been more accurate with all inputs guaranteed)
- No mechanism to express "pipeline B MUST NOT start until pipeline A's report exists"

### Barrier Gates (This Proposal)

**What it adds:**
- Declarative prerequisites in gate-contract.md
- Wait/poll loop in run-task.sh with configurable timeout
- BLOCKED status for monitor visibility
- Static cycle detection at dispatch time

**What it costs:**
- ~50 lines of bash in run-task.sh (`check_prerequisites` function)
- One new field in per-agent workflow state (`status`)
- Idle process per waiting pipeline (~10MB, acceptable at current scale)

### Wave Engine (Backlog 241)

**What it adds:**
- Topological sort of the dependency DAG into execution waves
- Wave barriers — downstream agents spawn only when their wave is dispatched
- Zero idle processes (agents don't exist until needed)
- Global ordering intelligence in the orchestrator

**What it costs:**
- Significant implementation: topological sort, wave dispatch logic, barrier monitor extension
- Changes to spawn-agent-swarm and execute-pipeline skills
- New dependency metadata in backlog files or task indexes

### Combined (241 + 242): Defense-in-Depth

The wave engine handles macro ordering (which pipelines run when). Barrier gates handle micro validation (does the specific file this pipeline needs actually exist and contain expected content before we start?).

The wave engine prevents the need for long polling — if the wave dispatched this pipeline, upstream outputs SHOULD exist. Barrier gates with a SHORT timeout (120s instead of 600s) catch the edge cases:
- Upstream completed but output file wasn't written (bug in upstream pipeline)
- Upstream output exists but is incomplete (task was skipped after 3 attempts)
- Intra-wave dependency that the DAG didn't model (two pipelines in the same wave where one actually reads the other's output)

---

## Implementation Spec (Conditional on 241 YAH)

### 1. Gate Contract Extension

Add `## Prerequisites` section to gate-contract.md template:

```markdown
## Prerequisites

| Prereq | Type | Target | Description |
|--------|------|--------|-------------|
| PRE-01 | file_exists | projects/{upstream}/research-report.md | Upstream verdict |
```

Types: `file_exists`, `grep`, `word_count` (reused from existing gate types).

### 2. run-task.sh Changes

Add `check_prerequisites()` function (see 02-wait-loop-design.md for full implementation). Call it once before the main iteration loop, not per-iteration.

Parameters (under wave engine):
- Poll interval: 15 seconds
- Timeout: 120 seconds (short — wave engine should have ensured availability)
- Exit code on timeout: 2 (BLOCKED)

### 3. Per-Agent State Extension

Add to `agent-{id}-workflow.json`:

```json
{
  "status": "WAITING|RUNNING|BLOCKED|COMPLETE",
  "waiting_on": ["PRE-01:path/to/file"],
  "waiting_since": "ISO-8601"
}
```

### 4. Monitor Rule Change

When `status == "WAITING"`: do not count toward stall detection. Log the waiting state. Check upstream agent status to detect true failures (upstream COMPLETE but prerequisite missing = upstream bug).

### 5. Static Cycle Detection

At swarm dispatch time (before spawning agents), read all gate-contract.md files, extract `PRE-*` entries, build the dependency graph, and feed to `tsort` (or equivalent). Reject cycles with a clear error listing the circular dependencies.

---

## Disqualifying Factors for Standalone Adoption

If 241 receives a NAY verdict, barrier gates as a standalone mechanism have these weaknesses:

1. **No global ordering:** Each pipeline sees only its own prerequisites. The orchestrator has no DAG view — it cannot predict which pipelines should start first.
2. **Idle process cost:** Each waiting pipeline holds a bash process open. For highly connected DAGs (many dependencies), most pipelines start in WAITING state, burning memory and doing nothing.
3. **Re-dispatch is manual:** When a BLOCKED pipeline's upstream finishes, the user must re-dispatch it. The monitor could automate this, but that essentially recreates the wave engine's dispatch logic.
4. **Timeout arbitrariness:** 600s timeout is a guess. If upstream takes 15 minutes, it times out. If upstream takes 2 minutes, it wastes 13 minutes of the next poll cycle. The wave engine's barrier is exact — dispatch when done, no timeout.

These weaknesses don't disqualify barrier gates entirely, but they make standalone adoption a strictly inferior design compared to wave-based dispatch with barrier-gate defense-in-depth.

---

## Cross-Proposal Interaction

| Proposal | Layer | Owns |
|----------|-------|------|
| 241 (Wave Engine) | Orchestrator (spawn-agent-swarm) | Global ordering, wave barriers |
| 242 (Barrier Gates) | Runner (run-task.sh) | Per-file validation, defense-in-depth |
| 243 (Artifact Bus) | Data (manifest.json) | Output discovery, freshness metadata |

These three proposals are complementary, not competing:
- 241 decides WHEN agents run (wave ordering)
- 242 validates WHAT they need before starting (file prerequisites)
- 243 standardizes HOW outputs are published and discovered (manifests)

The recommended adoption order: **241 first** (global ordering solves the primary problem), **242 second** (defense-in-depth is a small add-on), **243 only if needed** (existing file conventions may suffice — 243's overlap analysis should determine this).
