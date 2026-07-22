# Research Report: Inter-Agent Artifact Bus

## Verdict: NAY

Do NOT adopt an inter-agent shared artifact bus (structured export manifests) in the kernel's swarm/pipeline dispatch layer at this time. The existing mechanisms — gate contracts, per-agent workflow state, and file-system conventions — already provide the artifact discovery and validation capabilities that a manifest would re-serialize. The artifact bus becomes valuable only at a scale the kernel has not yet reached.

---

## Findings Summary

### Manifest Schema (01-manifest-schema.md)

A versioned JSON schema was designed covering producer identity (backlog number, task folder, agent ID), artifact list (path, kind, summary, word count), completion status, and timestamp. The producer decision favored run-task.sh post-completion (Option B) over task-builder appended tasks or gate-validation pass reuse, because the bash harness guarantees execution — it cannot be skipped by the cycling contract's 3-attempt rule, unlike agent-produced manifests.

The schema itself is sound. The design work is banked for future use if the reassessment triggers fire.

### Consumer Design + Overlap Analysis (02-consumer-and-overlap.md)

The consumer ingestion step was designed: read manifest, find artifact entry, verify file exists, fail fast if missing. Integration with 242 barrier gates showed that the manifest adds indirection without adding information — the barrier gate's `file_exists` check already validates exactly what the consumer needs, and the consumer already knows where to look because the prerequisite declares the path explicitly.

The overlap analysis is the decisive finding: **the manifest is 80% re-serialization of existing information.**

| Information | Already Available | Source |
|-------------|-------------------|--------|
| List of produced files | YES | gate-contract.md + file system |
| File paths | YES | gate-contract.md Target column |
| Completion status | YES | agent-{id}-workflow.json |
| Skipped tasks | YES | agent-{id}-workflow.json |
| Timestamp | PARTIAL | workflow state (not per-artifact) |
| Artifact kind | NO | Not tracked |
| Per-artifact summary | NO | Not tracked |

The only genuinely new fields — `kind` and `summary` — are useful for human browsing and LLM-based search but not required for mechanical prerequisite validation.

The 237 handoff schema (semantic context transfer between one-shot agents) was evaluated for unification and determined to be a separate concern: different scope (intra-pipeline vs inter-pipeline), different lifecycle (per-task vs per-pipeline), different consumer (next task vs dependent pipeline). Two schemas, not one.

### Combined 241/242/243 Recommendation (03-combined-recommendation.md)

The three proposals operate at different layers of the dispatch stack:

| Proposal | Layer | Controls | Verdict |
|----------|-------|----------|---------|
| 241 DAG Waves | Dispatch | WHEN agents spawn | YAH |
| 242 Barrier Gates | Validation | WHETHER agents proceed | YAH (conditional on 241) |
| 243 Artifact Bus | Data | WHAT is discoverable | NAY (deferred) |

Recommended build order: 241 first (primary ordering), 242 second (defense-in-depth), 243 deferred (reassess at scale).

---

## Trade-Off Analysis: Artifact Bus vs Current Discovery

### Current Behavior (Convention-Based Discovery)

Today, downstream agents discover upstream outputs by:
1. **Convention:** Output paths follow a predictable pattern (`projects/{pipeline-name}/research-report.md`)
2. **Gate contracts:** The upstream's gate-contract.md declares expected deliverables with exact paths
3. **File system:** `test -f` confirms existence
4. **Workflow state:** `agent-{id}-workflow.json` confirms completion status

This works because the kernel's pipeline structure is highly regular. Every pipeline produces output in `projects/{name}/`, every gate contract enumerates expected files, and every agent workflow tracks completion. The conventions are stable and machine-readable.

### What the Artifact Bus Would Change

The artifact bus adds a manifest file (`exports/manifest-{agent-id}.json`) that indexes all outputs from a completed pipeline. Consumers read the manifest instead of (or in addition to) checking gate contracts and the file system.

**What improves:**
- Single-file discovery: one read instead of three (gate-contract + workflow state + file system)
- Artifact metadata: `kind` and `summary` fields enable filtering and search
- Explicit producer identity: backlog number, task folder, agent ID in one place

**What degrades:**
- Fourth source of truth: manifest can drift from gate contracts (expected), file system (actual), and workflow state (completion)
- Maintenance overhead: run-task.sh must generate manifests; consumers must handle manifest-absent (legacy pipeline) and manifest-stale (file edited post-generation) cases
- Indirection cost: consumers now check manifest → file instead of just file, with fallback to direct check when manifest is missing

### Why the Degradation Outweighs the Improvement

The kernel's pipeline count is ~150 completed, all in the same workspace. At this scale:
- Convention-based discovery is reliable (patterns are consistent)
- Grep-based search is fast (`grep -r "YAH\|NAY" projects/*/research-report.md`)
- The three existing sources of truth agree (gate contracts declare it, file system has it, workflow state confirms it)

The manifest becomes a cache of these three sources. Caches require invalidation strategies. At 150 pipelines, the invalidation overhead exceeds the discovery convenience.

---

## Disqualifying Reasons

1. **80% overlap with existing mechanisms.** Gate contracts, workflow state, and file-system conventions already express the artifact information that the manifest would re-serialize. The two genuinely new fields (kind, summary) don't justify a fourth source of truth.

2. **Cache invalidation overhead.** The manifest is a snapshot at completion time. If files are edited, deleted, or regenerated after the manifest was written, the manifest becomes stale. Consumers must implement freshness checks (timestamp comparison, file existence verification), which is the same work they'd do without the manifest.

3. **Barrier gates (242) supersede the consumer use case.** The primary consumer of artifact discovery is the downstream pipeline's prerequisite check. Barrier gates perform this check directly against the file system — they don't need a manifest intermediary. The manifest would add a layer between the barrier gate and the file, increasing indirection without increasing reliability.

4. **Current scale doesn't justify the abstraction.** The artifact bus is a scale solution for a pre-scale system. At 500+ pipelines or with cross-repo consumption, the calculus changes. At 150 pipelines in one workspace, convention-based discovery is sufficient.

## What Covers the Need Instead

| Need | Covered By |
|------|-----------|
| Artifact discovery (what did pipeline X produce?) | gate-contract.md Target column |
| Artifact validation (does the file exist and is it complete?) | 242 barrier gates (`file_exists`, `grep`, `word_count`) |
| Completion status (did pipeline X finish?) | agent-{id}-workflow.json `complete` field |
| Ordering (don't start B until A finishes) | 241 DAG wave engine |
| Semantic context transfer (what should the next agent know?) | 237 handoff schema (separate concern) |

The combination of 241 (ordering) + 242 (validation) + existing conventions (discovery) provides complete coverage of the artifact bus's intended capabilities without introducing a redundant data layer.

## Reassessment Triggers

Revisit this verdict when any of the following become true:
- **Cross-repo consumption:** Pipelines in different repositories need to discover each other's outputs (gate contracts and workflow state are local to the workspace)
- **Scale threshold:** Workspace exceeds ~500 completed pipelines and grep-based discovery becomes impractical
- **Non-file artifacts:** Pipeline outputs include APIs, deployed services, or database records that the file-based discovery mechanisms cannot express
- **Artifact search:** Users need to query "find all research reports about X" across the entire pipeline history (the `kind` and `summary` fields enable this)

The manifest schema from 01-manifest-schema.md and the producer decision (run-task.sh post-completion) are preserved as design artifacts. If the triggers fire, implementation can proceed without additional research.
