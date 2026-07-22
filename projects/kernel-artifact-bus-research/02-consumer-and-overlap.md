# Consumer Design + Overlap Analysis

## Consumer Ingestion Step Design

### How a Downstream Agent Would Consume a Manifest

When a downstream pipeline depends on an upstream pipeline's output (e.g., pipeline 243 depends on 241's research-report.md), the consumer needs to:

1. **Discover** what the upstream produced and where it lives
2. **Validate** that the expected artifact exists and is complete
3. **Fail fast** if the dependency is missing or incomplete

Under the manifest schema from 01-manifest-schema.md, the consumer's ingestion step would be:

```
1. Read exports/manifest-{upstream-agent-id}.json
2. Parse artifacts array, find the entry matching the needed path
3. Verify the file exists at the declared path
4. If manifest missing → BLOCKED (upstream hasn't completed)
5. If manifest exists but artifact missing → FAIL (upstream bug — manifest claims it, file absent)
6. If artifact exists but no manifest → WARN, proceed (legacy/pre-manifest pipeline)
```

### Integration with 242 Barrier Gates

The 242 barrier gate design already defines a `## Prerequisites` section in gate-contract.md with `PRE-*` entries using `file_exists` and `grep` checks. The manifest adds a layer between the prerequisite and the raw file:

**Without manifest (current 242 design):**
```
PRE-01 | file_exists | projects/kernel-dag-wave-research/research-report.md
```
The barrier gate checks the file directly. Simple, reliable, no intermediary.

**With manifest:**
```
PRE-01 | manifest_check | kernel-dag-wave-research | research-report.md
```
The barrier gate reads the manifest, finds the artifact entry, then checks the file. Two reads instead of one, with the manifest as a discovery index.

**Verdict on integration:** The manifest adds indirection without adding information. The 242 barrier gate's `file_exists` check already validates exactly what the consumer needs — does the file exist? The manifest tells the consumer WHERE to look, but the consumer already knows where to look because the prerequisite declares the path explicitly. The manifest is useful only when the consumer does NOT know the path — which is not the case in the kernel's declarative prerequisite model.

### Unification with 237 Handoff Schema

The 237 ephemeral sub-agents research proposed a semantic handoff schema:

```json
{
  "handoff": {
    "completed_task": "003-build-write-something.md",
    "discoveries": ["Import paths must use _reference prefix"],
    "constraints": ["File X depends on Y being written first"],
    "next_agent_should_know": "API response format changed in v2"
  }
}
```

This schema transfers SEMANTIC context (discoveries, constraints, advice). The artifact bus manifest transfers STRUCTURAL context (file paths, kinds, word counts). These are different concerns:

| Dimension | 237 Handoff | 243 Manifest |
|-----------|-------------|--------------|
| **What it transfers** | Semantic — why, how, gotchas | Structural — what files, where |
| **Scope** | Intra-pipeline (task N → task N+1) | Inter-pipeline (pipeline A → pipeline B) |
| **Consumer** | Next one-shot agent in same pipeline | Different pipeline's barrier gate |
| **Written by** | Each one-shot agent after task completion | run-task.sh after ALL_TASKS_COMPLETE |

**Unification verdict:** These should NOT be merged into one schema. The handoff is per-task, written during execution, consumed by the next task in sequence. The manifest is per-pipeline, written after completion, consumed by dependent pipelines. Merging them would force the per-task handoff to carry pipeline-level metadata it doesn't need, and the pipeline manifest to carry per-task semantic context that's irrelevant to downstream pipelines. Two schemas, two concerns, two lifecycles.

## Overlap Analysis: Is the Manifest NEW Information?

### Existing Mechanisms That Already Express Artifact Information

**1. Gate Contracts (gate-contract.md)**

Every pipeline already has a machine-readable list of expected deliverables:

```markdown
| Gate | Type | Target | Pass Criteria |
|------|------|--------|---------------|
| DOC-01 | file_exists | projects/kernel-dag-wave-research/01-dependency-metadata.md | File exists |
| DOC-02 | word_count | projects/kernel-dag-wave-research/01-dependency-metadata.md | >= 300 words |
```

The gate contract declares what SHOULD exist. A downstream consumer can read the upstream's gate-contract.md to discover expected artifacts. This is already machine-parseable (pipe-delimited table) and already contains paths, types, and pass criteria.

**2. Per-Agent Workflow State (agent-{id}-workflow.json)**

Already tracks:
- `completed_tasks` — which tasks finished
- `skipped_tasks` — which tasks were skipped
- `complete` — whether the pipeline finished
- `task_folder` — where to find the task definitions

A downstream consumer can check `complete: true` and `skipped_tasks: []` to confirm upstream health.

**3. Backlog Archive Status (docs/backlog/done/)**

When run-task.sh detects ALL_TASKS_COMPLETE, it moves the backlog file to `docs/backlog/done/`. A downstream consumer can check `test -f docs/backlog/done/241-*.md` to confirm the upstream pipeline completed.

**4. Validation Report (_test/validation-report.json)**

The task-builder's step 9 execution produces a validation report with per-gate pass/fail results. This is the closest existing analog to the manifest — it enumerates every deliverable and records whether it passes its gate.

### What the Manifest Would Add

| Information | Already Available? | Source |
|-------------|-------------------|--------|
| List of produced files | YES | gate-contract.md (expected) + file system (actual) |
| File paths | YES | gate-contract.md Target column |
| Completion status | YES | agent-{id}-workflow.json `complete` field |
| Skipped tasks | YES | agent-{id}-workflow.json `skipped_tasks` field |
| Timestamp | PARTIAL | agent-{id}-workflow.json `timestamp` (not per-artifact) |
| Artifact kind | NO | Not tracked anywhere |
| Per-artifact summary | NO | Not tracked anywhere |
| Per-artifact word count | PARTIAL | gate-contract.md has word_count gates, but not all artifacts |
| Producer metadata | YES | Derivable from task folder name and backlog path |

### Overlap Verdict

**The manifest is 80% re-serialization of existing information.** The only genuinely new fields are `kind` (artifact classification) and `summary` (one-line description). These are useful for human browsing and for LLM-based consumers (an agent asked to "find all research reports" could filter by kind), but they are not required for the mechanical prerequisite checking that 242 barrier gates perform.

The manifest's value proposition is convenience — one file to read instead of three (gate-contract + workflow state + file system). But this convenience comes at the cost of maintaining a fourth source of truth that can drift from the other three. The gate contract is authoritative for expected artifacts. The file system is authoritative for actual artifacts. The workflow state is authoritative for completion status. A manifest that re-states all three is a cache, not a source of truth — and caches require invalidation strategies, which is overhead the kernel doesn't currently need.

### Conditional Value: When a Manifest WOULD Be Useful

1. **Cross-repo consumption:** If pipeline B runs in a different repository than pipeline A, the gate-contract.md and workflow state of A are not accessible from B's file system. A manifest in a shared location (or published via an API) would bridge this gap. But the kernel currently runs all pipelines in the same workspace — cross-repo is a future scenario.

2. **Non-file artifacts:** If pipelines produce artifacts that aren't files (API endpoints, database records, deployed services), the file-based discovery mechanisms break. A manifest could register these. But the kernel's current scope is file-based deliverables.

3. **Artifact registry / search:** If the workspace had hundreds of completed pipelines and someone needed to find "all research reports that mention DAG," a manifest index would enable that search. The current scale (~150 completed pipelines) is manageable with grep.

These are all future-scale justifications, not current-pain justifications.
