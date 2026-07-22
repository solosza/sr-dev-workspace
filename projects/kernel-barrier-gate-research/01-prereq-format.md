# Prerequisite Declaration Format for Barrier Gates

## Research Question

Should run-task.sh enforce deliverable-based prerequisite barriers at the task level, and if so, where should prerequisites be declared — in the gate-contract.md (new Prerequisites section) or in per-task `## Prerequisites` blocks? What parse rules does run-task.sh need, and should prerequisites assert content or only existence?

## Analysis

### Option A: Gate Contract Prerequisites Section

Add a `## Prerequisites` section to `gate-contract.md`:

```markdown
## Prerequisites

| Prereq | Type | Target |
|--------|------|--------|
| PRE-01 | file_exists | projects/kernel-dag-wave-research/research-report.md |
| PRE-02 | grep | projects/kernel-dag-wave-research/research-report.md | Contains "Verdict" |
```

**Advantages:**
- Single source of truth — gate contracts already enumerate pass/fail criteria, adding prerequisites is a natural extension
- Machine-readable table format already proven parseable by the existing gate validation tooling
- The contract is per-pipeline, matching the granularity of inter-pipeline dependencies (backlog 240 depending on 237-239 outputs is a pipeline-to-pipeline relationship)
- Task-builder already reads gate-contract.md during atomization (step 6) — prerequisites would be visible at plan time

**Disadvantages:**
- Cross-cutting: a prerequisite applies to the pipeline's START, not to individual tasks — but gate-contract.md's table format is task-gate-level
- Mixing concerns: gates validate deliverables the pipeline produces; prerequisites validate deliverables OTHER pipelines produce
- run-task.sh would need to parse gate-contract.md before the first iteration, adding a pre-loop step

### Option B: Per-Task `## Prerequisites` Block

Add prerequisites to individual task files:

```markdown
## Prerequisites
- file_exists: projects/kernel-dag-wave-research/research-report.md
- grep: projects/kernel-dag-wave-research/research-report.md | Contains "Verdict"
```

**Advantages:**
- Fine-grained: task 005 depends on outputs from tasks 002-004 (intra-pipeline), and could also declare inter-pipeline prerequisites
- Self-contained: each task file declares everything needed to execute it
- run-task.sh already reads the task file to extract metadata (model routing uses `TASK_FILE_PATH`)

**Disadvantages:**
- Redundancy: if 3 tasks all need the same upstream output, the prerequisite is declared 3 times
- Intra-pipeline dependencies are ALREADY expressed via the `## Dependencies` section (task 005 depends on 002, 003, 004) — adding file-existence prerequisites for the same relationship duplicates the dependency graph
- Parse complexity: run-task.sh would need to extract prerequisites from each task file before spawning, adding per-iteration parsing

### Recommendation: Gate Contract for Inter-Pipeline, Dependencies Section for Intra-Pipeline

The two dependency types serve different purposes:

1. **Intra-pipeline** (task 005 needs task 002's output): Already handled by the `## Dependencies` field in task files. run-task.sh executes tasks sequentially within a pipeline, so task 005 runs after task 002 by natural ordering. No barrier gate needed.

2. **Inter-pipeline** (pipeline 242 needs pipeline 241's research-report.md): This is the actual gap. The gate-contract.md is the right location because:
   - The prerequisite is pipeline-scoped, not task-scoped
   - run-task.sh can parse it ONCE before the loop starts (not per-iteration)
   - The table format matches existing gate types

**Chosen format — gate-contract.md `## Prerequisites` section:**

```markdown
## Prerequisites

| Prereq | Type | Target | Description |
|--------|------|--------|-------------|
| PRE-01 | file_exists | projects/kernel-dag-wave-research/research-report.md | DAG wave verdict |
| PRE-02 | word_count | projects/kernel-dag-wave-research/research-report.md | >= 300 |
```

### Parse Rules for run-task.sh

Bash-parseable extraction using grep/sed (no new tooling):

```bash
# Extract prerequisites from gate-contract.md
GATE_CONTRACT="${TASK_DIR}/gate-contract.md"
if [ -f "$GATE_CONTRACT" ]; then
  # Find lines in the Prerequisites table (pipe-delimited, skip header/separator)
  PREREQS=$(grep -E '^\| PRE-' "$GATE_CONTRACT" | while IFS='|' read -r _ id type target desc _; do
    id=$(echo "$id" | xargs)
    type=$(echo "$type" | xargs)
    target=$(echo "$target" | xargs)
    echo "${id}:${type}:${target}"
  done)
fi
```

This reuses the same table format as the existing Gates section, making it parseable with the same grep/sed patterns. The `PRE-` prefix distinguishes prerequisites from gate entries (`BUILD-`, `DOC-`, etc.).

### Existence-Only vs Content Assertion

**Decision: Allow content assertion, reusing existing gate types.**

Rationale:
- `file_exists` alone proves presence but not correctness. A file from a prior run (stale artifact) would satisfy a file_exists prerequisite even if it contains outdated or incorrect content.
- The existing gate types (`grep`, `word_count`, `json_valid`) are already parseable by run-task.sh's verification tooling — reusing them for prerequisites adds no new parsing complexity.
- Content assertion is OPTIONAL — most prerequisites will use `file_exists` (the common case is "did the upstream pipeline finish?"), but `grep` catches cases like "does the report contain a verdict?" which prevents acting on incomplete upstream output.
- `word_count` catches truncated or empty files from partial upstream execution (task started, wrote headers, then was skipped).

**Guard against over-specification:** Prerequisites should assert COMPLETION signals, not content correctness. "File exists and contains 'Verdict'" is a valid prerequisite. "File exists and the verdict is YAH" is NOT — that's a design decision, not a dependency gate.

### Worked Example: Swarm 237-240

In the 2026-07-21 swarm run, backlog 240 (portfolio ranking) had a soft dependency on 237-239 outputs — it read sibling outputs "if present" and tolerated missing files. With barrier gates:

**Pipeline 240's gate-contract.md would add:**

```markdown
## Prerequisites

| Prereq | Type | Target | Description |
|--------|------|--------|-------------|
| PRE-01 | file_exists | projects/kernel-ephemeral-subagents-research/research-report.md | 237 verdict |
| PRE-02 | file_exists | projects/kernel-precompact-hook-research/research-report.md | 238 verdict |
| PRE-03 | file_exists | projects/kernel-jit-summarization-research/research-report.md | 239 verdict |
| PRE-04 | grep | projects/kernel-ephemeral-subagents-research/research-report.md | Verdict |
| PRE-05 | grep | projects/kernel-precompact-hook-research/research-report.md | Verdict |
| PRE-06 | grep | projects/kernel-jit-summarization-research/research-report.md | Verdict |
```

run-task.sh would check these BEFORE spawning the first claude -p for pipeline 240. If any are missing, it enters a wait/poll loop (design covered in task 003). The grep assertions ensure the upstream reports are complete (contain a verdict), not just file stubs.

This would have converted the 240 pipeline's "tolerate missing" soft dependency into a hard barrier — the portfolio ranking would only run after all three research reports were finalized, eliminating the risk of ranking based on partial data.

## Conclusion

**Gate-contract.md `## Prerequisites` section** is the right location. It keeps prerequisites at the pipeline scope (where inter-pipeline dependencies live), uses the existing pipe-delimited table format (bash-parseable), and allows content assertion via reused gate types (`file_exists`, `grep`, `word_count`). Intra-pipeline dependencies remain in task files' `## Dependencies` section — no change needed there.
