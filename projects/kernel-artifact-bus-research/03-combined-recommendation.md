# Combined 241/242/243 Recommendation

## Sibling Verdicts Summary

### 241 — DAG Wave Execution Engine
**Verdict: YAH**

Adopt dependency-sorted dispatch with barrier monitoring. The design uses Kahn's algorithm (BFS topological sort) to extract execution waves from the task index's existing Dependencies column. Backward-compatible — task indexes with no dependencies produce a single wave identical to current flat-parallel behavior. Implementation cost is ~50 lines of sort logic plus a manifest extension to `agent-swarm.json`. Key design decisions: notification-driven barriers (not polling), partial dispatch on failure (only downstream dependents blocked, independent tasks proceed), 30-minute timeout per wave.

The critical insight: the latency trade-off is correctness. Flat dispatch is faster but produces race conditions when tasks have real dependencies. Wave dispatch adds wall-clock time equal to the critical path, but guarantees ordering.

### 242 — Deliverable-Based Barrier Gates
**Verdict: YAH (Conditional — Defense-in-Depth Under 241)**

Adopt barrier gates in run-task.sh as defense-in-depth, NOT as a standalone ordering mechanism. The design extends gate-contract.md with a `## Prerequisites` section using `PRE-*` entries and existing gate types (`file_exists`, `grep`). run-task.sh gains a `check_prerequisites()` function with a 15-second poll interval and 120-second timeout (short, because the wave engine should have ensured availability).

Key design decision: standalone adoption was explicitly disqualified. Without the wave engine, barrier gates have no global ordering (each pipeline sees only its own prerequisites), waste resources on idle polling processes, and require manual re-dispatch. The conditional verdict means 242 is contingent on 241 shipping.

### 243 — Inter-Agent Artifact Bus (This Research)
**Verdict emerging from overlap analysis: NAY (Deferred)**

The overlap analysis in 02-consumer-and-overlap.md found that the manifest is 80% re-serialization of existing information. Gate contracts already enumerate expected deliverables. Per-agent workflow state already tracks completion. Backlog archive status already signals pipeline done. The only genuinely new fields are artifact `kind` and `summary` — useful for human browsing but not required for the mechanical prerequisite checking that 242 barrier gates perform.

## Ranking Table

| Dimension | 241 DAG Waves | 242 Barrier Gates | 243 Artifact Bus |
|-----------|---------------|-------------------|------------------|
| **Implementation cost** | Moderate (~50 lines sort + manifest extension + barrier monitor changes) | Low (~50 lines bash + 1 state field) | Low (~30 lines bash in run-task.sh post-completion) |
| **Robustness** | High — topological sort with cycle detection; proven algorithm | High — reuses existing gate types; static validation | Medium — manifest is a cache that can drift from source of truth |
| **Coverage** | Primary — controls WHEN agents spawn based on dependency graph | Secondary — validates WHETHER a spawned agent's prerequisites exist | Tertiary — standardizes WHAT outputs exist, but duplicates gate-contract + workflow state |
| **Composition** | Standalone viable; enhanced by 242 | Dependent on 241 (conditional verdict) | Independent but largely redundant with existing mechanisms |
| **Overlap with existing** | Low — no current ordering mechanism exists | Low — no current prerequisite validation exists | High — gate contracts, workflow state, and file system already express 80% of manifest content |
| **Value-to-effort ratio** | Very High — solves a real ordering problem with moderate effort | High — small add-on that catches edge cases 241 misses | Low — significant overlap, modest new information |
| **Future scalability** | Scales naturally — more waves for deeper dependency graphs | Scales — more PRE-* entries as pipelines grow | Useful at scale (100+ pipelines, cross-repo) but premature at current scale (~150 completed, same workspace) |

## Recommended Build Order

### Build 241 First (Primary)

DAG wave execution solves the root problem: pipelines with dependencies currently require either manual sequencing (STRICTLY_SEQUENTIAL) or soft tolerance (agents read sibling outputs "if present"). Neither is correct — manual sequencing eliminates parallelism, soft tolerance produces race conditions. Wave dispatch is the only design that provides both ordering guarantees AND intra-wave parallelism.

Implementation sequence:
1. Wave sort in spawn-agent-swarm step-01 (parse Dependencies, Kahn's algorithm, store wave plan)
2. Wave dispatch in step-03 (scope spawning to current wave, barrier between waves)
3. Manifest extension in agent-swarm.json (wave metadata for monitoring)

**Prerequisite:** Per-agent session-state isolation (env-var agent_id routing) must ship before or alongside, per the swarm 237-240 evidence.

### Build 242 Second (Defense-in-Depth)

After 241 establishes wave ordering, 242 adds per-file validation as a safety net. The short timeout (120s vs 600s standalone) reflects trust in the wave engine — if the wave dispatched this agent, upstream outputs SHOULD exist. Barrier gates catch the edge cases: upstream completed but output file missing (bug), output exists but incomplete (skipped tasks), intra-wave dependency the DAG didn't model.

Implementation sequence:
1. Gate contract extension (add `## Prerequisites` section template)
2. run-task.sh `check_prerequisites()` function
3. Per-agent state `status` field (WAITING/RUNNING/BLOCKED/COMPLETE)
4. Static cycle detection at dispatch time

### Defer 243 (Reassess at Scale)

The artifact bus should NOT be built now. The overlap analysis shows it adds marginal new information (kind + summary fields) while introducing a fourth source of truth that can drift from the authoritative three (gate contracts, workflow state, file system). The maintenance cost of keeping the manifest synchronized outweighs the convenience benefit at current scale.

**Reassess when:**
- Cross-repo consumption becomes a real scenario (pipelines in different repositories need to discover each other's outputs)
- The workspace exceeds ~500 completed pipelines and grep-based discovery becomes impractical
- Non-file artifacts (APIs, deployed services) enter the pipeline output vocabulary

**What to preserve:** The manifest schema designed in 01-manifest-schema.md is sound. If the reassessment triggers fire, the schema and producer decision (run-task.sh post-completion) can be implemented without additional research. The design work is banked.

## Rationale for This Ordering

The three proposals operate at different layers of the dispatch stack:

```
Dispatch layer:    241 DAG Waves    → controls WHEN agents spawn (ordering)
Validation layer:  242 Barrier Gates → controls WHETHER agents proceed (prerequisites)  
Data layer:        243 Artifact Bus  → controls WHAT is discoverable (manifest)
```

The ordering layer must exist first because the validation layer is conditional on it (242's standalone adoption was disqualified). The data layer is deferred because the existing file-based discovery mechanisms are sufficient — the manifest would re-serialize what gate contracts and workflow state already express.

This mirrors the 237-240 portfolio ranking pattern: ship the highest-ROI items first (241 = primary ordering, 242 = defense-in-depth), defer high-overlap items until their unique value proposition materializes (243 = scale-dependent convenience).
