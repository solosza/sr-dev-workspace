# Manifest Schema + Producer Wiring

## The Question

Should one-shot agents export a structured `exports/manifest.json` that downstream agents ingest for output discovery? If so, what does the schema look like and who writes it?

## Manifest JSON Schema (v1)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["version", "producer", "artifacts", "status", "timestamp"],
  "properties": {
    "version": {
      "type": "string",
      "const": "1.0",
      "description": "Schema version for forward compatibility"
    },
    "producer": {
      "type": "object",
      "required": ["backlog", "task_folder", "agent_id"],
      "properties": {
        "backlog": {
          "type": "string",
          "description": "Backlog number, e.g. '241'"
        },
        "task_folder": {
          "type": "string",
          "description": "Task subfolder, e.g. 'kernel-dag-wave-research'"
        },
        "agent_id": {
          "type": "string",
          "description": "Agent ID used for state routing, e.g. 'kernel-dag-wave-research'"
        }
      }
    },
    "artifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path", "kind", "summary"],
        "properties": {
          "path": {
            "type": "string",
            "description": "Relative path from repo root"
          },
          "kind": {
            "type": "string",
            "enum": ["research-report", "research-output", "source-code", "config", "test", "design-doc"],
            "description": "Artifact classification"
          },
          "summary": {
            "type": "string",
            "description": "One-line description of what this file contains"
          },
          "word_count": {
            "type": "integer",
            "description": "Word count at manifest generation time"
          }
        }
      }
    },
    "status": {
      "type": "string",
      "enum": ["complete", "partial", "failed"],
      "description": "Pipeline completion status"
    },
    "completed_tasks": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of completed task filenames"
    },
    "skipped_tasks": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of skipped task filenames"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 timestamp of manifest generation"
    }
  }
}
```

### Filled Example

```json
{
  "version": "1.0",
  "producer": {
    "backlog": "241",
    "task_folder": "kernel-dag-wave-research",
    "agent_id": "kernel-dag-wave-research"
  },
  "artifacts": [
    {
      "path": "projects/kernel-dag-wave-research/01-dependency-metadata.md",
      "kind": "research-output",
      "summary": "Wave sort algorithm design using Kahn's BFS topological sort",
      "word_count": 842
    },
    {
      "path": "projects/kernel-dag-wave-research/02-barrier-monitor.md",
      "kind": "research-output",
      "summary": "Notification-driven barrier monitor with failure semantics",
      "word_count": 731
    },
    {
      "path": "projects/kernel-dag-wave-research/03-lesson-reconciliation.md",
      "kind": "research-output",
      "summary": "Cross-proposal comparison and STRICTLY-SEQUENTIAL lesson reconciliation",
      "word_count": 695
    },
    {
      "path": "projects/kernel-dag-wave-research/research-report.md",
      "kind": "research-report",
      "summary": "YAH verdict — adopt DAG wave execution in dispatch layer",
      "word_count": 1204
    }
  ],
  "status": "complete",
  "completed_tasks": [
    "001-build-create-project-dir.md",
    "002-research-dependency-metadata.md",
    "003-research-barrier-monitor.md",
    "004-research-lesson-reconciliation.md",
    "005-build-write-research-report.md"
  ],
  "skipped_tasks": [],
  "timestamp": "2026-07-21T19:30:00Z"
}
```

## Producer Decision

Three candidate producers were evaluated:

### Option A: Task-Builder Appended Final Task

The task-builder could auto-append a final "write manifest" BUILD task to every pipeline. The one-shot agent executing this task would enumerate deliverables from the gate-contract, check which exist, compute word counts, and write the manifest.

**Pros:** Runs inside the kernel loop, gets verification. One-shot agents already write JSON (state files). No changes to run-task.sh.
**Cons:** Adds a task to every pipeline. The manifest-writing agent may fail or be skipped (3-attempt cycling rule), leaving no manifest — the opposite of guaranteed output.

### Option B: run-task.sh Post-Completion Step

After detecting ALL_TASKS_COMPLETE, run-task.sh could enumerate the `projects/{name}/` directory, match files against the gate-contract, and write `exports/manifest.json` before the `move_to_done` step.

**Pros:** Guaranteed execution (runs in the bash harness, not in an agent). Atomic with pipeline completion. Cannot be skipped by cycling rules.
**Cons:** Requires bash changes to run-task.sh. The bash script would need to parse gate-contract.md to know what artifacts to expect — currently it doesn't read gate contracts at all.

### Option C: Gate-Validation Pass Reuse

The existing gate-validation pass (in task-builder step 9 and the validation-report.json output) already enumerates every deliverable and verifies its existence. This pass could be extended to also write a manifest alongside the validation report.

**Pros:** Zero new code paths — extends an existing mechanism. Already knows the artifact list from gate-contract.md. Already computes pass/fail per gate.
**Cons:** Gate validation runs inside the agent, so it has the same skip risk as Option A. Also, validation-report.json already contains most of this information — the manifest would be partially redundant.

### Decision: Option B (run-task.sh Post-Completion)

**Rationale:** The manifest must be guaranteed. Options A and C run inside agents, which can fail, timeout, or be skipped. Option B runs in the bash harness after confirmed completion — if run-task.sh reached ALL_TASKS_COMPLETE, the manifest is written unconditionally. The implementation is ~30 lines of bash: read the task index for the project name, glob the output directory, write a JSON manifest.

The gate-contract parsing concern is solvable: run-task.sh already knows the task folder, so it can glob `projects/{task_folder_stem}/` for actual files rather than parsing gate-contract expectations. The manifest records what EXISTS, not what was EXPECTED — consumers compare the manifest against their own prerequisites (barrier gates from 242) to decide if the output is sufficient.

## Stale-Manifest and Manifest/File-Drift Handling

### Re-Run Scenario

When a pipeline is re-run (task folder re-created, agents re-execute), the manifest must be regenerated. Since run-task.sh writes the manifest as a post-completion step, re-runs naturally overwrite the previous manifest. No explicit staleness check is needed — the manifest is always written at the moment of completion, reflecting current file state.

### File-Drift Scenario

If files are manually edited after the manifest was generated, the manifest becomes stale. Two mitigations:

1. **Consumer-side freshness check:** The consuming agent (barrier gate from 242 or a manual prerequisite check) should verify both manifest existence AND file existence. The manifest is a discovery index, not a content guarantee. If a consumer needs content freshness, it checks the file's mtime or re-reads it directly.

2. **Manifest timestamp comparison:** The consumer can compare the manifest's `timestamp` against the target file's mtime. If file mtime > manifest timestamp, the manifest is stale but the file is newer — this is benign (file was improved after pipeline completion). If manifest timestamp > file mtime, the file hasn't been touched since manifest generation — this is the normal case. If the file doesn't exist at all, the manifest is dangerously stale (file was deleted after manifest generation) — fail fast.

### Design Principle

The manifest is a discovery shortcut, not a source of truth. It answers "what did this pipeline produce and where is it?" — not "is this file still valid?" Content validation remains the consumer's responsibility, which aligns with the 242 barrier gate design (prerequisites check file existence and content, not manifest claims).
