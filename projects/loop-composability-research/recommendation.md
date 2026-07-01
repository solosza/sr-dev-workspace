# Loop Composability — Recommendation

Final synthesis for backlog 155. Based on primitive contract analysis (task 001) and dispatch/scoping research (task 002).

---

## Recommendation: Delegated Dispatch via Explicit Tags

### Dispatch Mechanism

**Choice: Explicit `## Primitive` tag in task files (Option C from task 002).**

Task-builder emits a `## Primitive` field when it recognizes that a task's deliverable matches a known primitive's entry contract. Untagged tasks execute inline (current behavior, no retrofit).

Why this over convention-based detection:
- Task-builder has full context at decomposition time — it already reads the goal, researches the repo, and checks conventions
- Explicit tags are auditable — `grep "## Primitive" tasks/*/` shows all dispatch points
- No fragile path-matching heuristics that break when conventions evolve
- The fallback (inline execution) is the proven default

### State Scoping

**Choice: Delegated execution via run-task.sh.**

When a one-shot agent encounters `## Primitive: X`, it writes inner task files to `tasks/{outer-folder}/_inner/{task-id}-{primitive}/` and invokes `env -u CLAUDECODE bash run-task.sh . N {nested-folder}`. Inner agents get their own `agent-{id}-workflow.json`, anchor counter, and actions log. No shared mutable state.

Why this over inline primitive execution:
- Reuses the proven one-shot execution model — no new code path
- State isolation is automatic (new agent_id = new workflow file per the shipped backlog 155 isolation)
- Anchor budget is independent — inner actions don't consume outer anchor counter
- session_state.json contention is avoided by one-shot pre-init
- The multi-agent state collision lesson (2026-06-14) proved shared mutable state fails at scale

### Error Propagation

**Choice: Fail-fast — inner loop is atomic to outer loop.**

The outer loop treats each inner primitive invocation as a black box:
1. Inner run-task.sh completes
2. Outer agent reads inner workflow file (`completed_tasks`, `skipped_tasks`, `complete`)
3. Outer agent checks exit contract (expected artifacts present?)
4. Result: COMPLETE (all artifacts) or FAILED (missing artifacts or skipped inner tasks)
5. On failure: outer loop's standard retry logic (3 attempts then skip)

No retry amplification — inner loop already retries internally (resume, model upgrade, skip after 3). Adding outer retries of inner retries creates exponential explosion (18 attempts for one task).

### Primitive Interface Changes

**Choice: None required.**

Primitives keep their current entry/exit contracts unchanged. Composability is purely an orchestration concern:
- Task-builder learns to emit `## Primitive` tags (new decomposition logic)
- One-shot agents learn to dispatch on `## Primitive` (new execution logic)
- Primitives themselves don't know or care whether they're invoked standalone or as inner loops

This preserves backward compatibility — every existing primitive works exactly as before.

---

## Concrete Example: "Build New Command" Task

Scenario: User runs `/kernel/execute-pipeline 200-build-filter-patients-command`.

```
Step 1: Execute-pipeline reads backlog, invokes task-builder
Step 2: Task-builder decomposes into tasks:

  tasks/filter-patients-command/
    000-index.md
    gate-contract.md
    001-research-requirements.md        ← Type: RESEARCH (inline)
    002-build-filter-command.md          ← Type: BUILD, Primitive: build-command
    003-test-filter-command.md           ← Type: TEST, Primitive: prod-test

Step 3: run-task.sh cycles through tasks

  Task 001: One-shot agent reads requirements, writes analysis → COMPLETE

  Task 002: One-shot agent reads task, sees ## Primitive: build-command
    → Writes inner tasks to tasks/filter-patients-command/_inner/002-build-command/
    → Invokes: env -u CLAUDECODE bash run-task.sh . 5 tasks/filter-patients-command/_inner/002-build-command
    → Inner run-task.sh spawns one-shot agents (agent_id: "filter-patients-command--002-build-command")
    → Inner agents build the command file, write SKILL.md, register in settings
    → Inner run-task.sh completes
    → Outer agent checks exit contract: .claude/commands/kernel/filter-patients.md exists? YES
    → Task 002: COMPLETE

  Task 003: One-shot agent reads task, sees ## Primitive: prod-test
    → Writes inner tasks to tasks/filter-patients-command/_inner/003-prod-test/
    → Invokes run-task.sh for inner tasks
    → Inner agents assemble master, copy to test repo, run L1/L2/L3
    → Outer agent checks exit contract: validation-report.json exists + all passes? YES
    → Task 003: COMPLETE

Step 4: Execute-pipeline reads validation report, archives backlog → DONE
```

### Agent ID Hierarchy

```
Depth 0: "filter-patients-command"                              → agent-filter-patients-command-workflow.json
Depth 1: "filter-patients-command--002-build-command"            → agent-filter-patients-command--002-build-command-workflow.json
Depth 1: "filter-patients-command--003-prod-test"                → agent-filter-patients-command--003-prod-test-workflow.json
```

### Folder Structure

```
tasks/filter-patients-command/
  000-index.md
  gate-contract.md
  001-research-requirements.md
  002-build-filter-command.md
  003-test-filter-command.md
  _inner/
    002-build-command/
      000-index.md
      gate-contract.md
      001-read-spec.md
      002-write-command.md
      003-register-command.md
    003-prod-test/
      000-index.md
      gate-contract.md
      001-assemble-master.md
      002-run-tests.md
      003-report.md
```

---

## What NOT to Do

| Anti-Pattern | Why Not |
|-------------|---------|
| Convention-based dispatch (infer primitive from deliverable path) | Fragile — path conventions change, edge cases multiply, can't distinguish "write a file" from "invoke a full primitive loop" |
| Inline primitive execution (run inner loop inside outer agent's session) | State contamination — inner actions count against outer anchor budget, inner anchor resets outer context, inner learn writes to outer lessons state. This is the exact failure mode from the 2026-06-14 multi-agent state collision lesson |
| New session_state.json fields for nesting | Unnecessary — one-shot pre-init already scopes all session state per invocation. Adding nesting fields creates schema debt |
| Retry amplification (outer retries of inner retries) | Exponential explosion — 3 outer x 3 inner x 2 resume = 18 attempts. Inner loop retries internally; outer treats inner as atomic |
| Depth > 2 nesting | Latency — each run-task.sh layer adds startup overhead per task. Beyond depth 2, restructure the task decomposition to flatten instead |
| Registry file for primitives | Unnecessary — skill folders ARE the registry. Adding a separate mapping file is one more thing to maintain and drift |
| Modifying primitive interfaces for composability | Composability is orchestration, not interface. Primitives work. Don't touch them |

---

## Implementation Priority

If this design were to be built, the implementation order:

### Phase 1: Dispatch Foundation (2 tasks)
1. **Add `## Primitive` field support to task-builder step-05 (decompose)** — Teach task-builder to recognize when a subtask maps to a known primitive and emit the tag. This is a single edit to the decomposition logic in `references/step-05-decompose.md`.
2. **Add dispatch logic to one-shot agent task execution** — When a one-shot agent reads a task with `## Primitive`, write inner tasks to `_inner/` and invoke run-task.sh instead of executing inline. This is the core behavior change.

### Phase 2: Inner Task Generation (2 tasks)
3. **Define inner task templates per primitive** — Each primitive needs a standard decomposition into inner tasks (e.g., build-command → read-spec, write-command, register, test). These could be static templates or dynamically generated by the primitive's own task-builder invocation.
4. **Document `_inner/` folder convention and `--` agent ID separator** — Add to kernel conventions so all future task-builder runs respect the nesting pattern.

### Phase 3: Validation (1 task)
5. **End-to-end test** — Run execute-pipeline with a goal that triggers inner loop dispatch. Verify: inner tasks created, inner agents spawned, inner artifacts produced, outer loop reads exit contract correctly, final validation report is clean.

### What Already Works (No Changes Needed)
- run-task.sh — already supports arbitrary task folders and agent_id
- Per-agent workflow state isolation — already shipped (backlog 155)
- One-shot pre-init — already scopes session_state.json per invocation
- Kernel governance (anchor, learn, complete) — works identically at every depth
- Existing task execution — untagged tasks continue to execute inline

---

## Key Insight

The kernel's existing primitives are already composable in contract — they have clear entry/exit boundaries and (mostly) isolated state. The gap is purely in orchestration: no mechanism exists for an outer loop to detect that a task should invoke a primitive and delegate execution. The `## Primitive` tag + delegated run-task.sh pattern closes this gap with minimal changes — two edits to existing code (task-builder decomposition + one-shot dispatch), zero changes to primitives, zero new state schemas.

The prod-test primitive is the proof this works: it already operates on external filesystem trees, returns results via artifacts, and doesn't mutate parent state. Every primitive should aspire to this level of isolation. The ones that don't (execute-pipeline's pipeline_state, autonomous-cycling's workflow fields) are scoped by the existing per-agent isolation — no new mechanism needed.
