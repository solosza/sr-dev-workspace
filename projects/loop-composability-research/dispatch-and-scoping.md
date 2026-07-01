# Dispatch Mechanism and State Scoping for Loop Composability

Research for backlog 155 — Loop Composability, Task 002.

---

## 1. Dispatch: How Does an Outer Loop Select an Inner Loop?

The core question: when execute-pipeline encounters a task like "build a new kernel command," how does it know to invoke the build-command primitive instead of executing the task inline?

### Option A: Explicit Task Tags

Each task file includes a `## Primitive` field that names the inner loop to invoke.

```markdown
# 003-build-filter-command.md
## Type
BUILD
## Primitive
build-command
## Arguments
name: filter-patients
description: Filter qualifying RT patients from census
```

**Pros:**
- Zero ambiguity — the task-builder decides dispatch at decomposition time
- No runtime pattern matching needed
- Extensible — new primitives just need a new tag value

**Cons:**
- Requires task-builder to know all available primitives
- Couples task format to primitive names

### Option B: Convention-Based (Deliverable Type Detection)

The outer loop inspects the task's deliverable path and type to infer which primitive to invoke.

| Deliverable Pattern | Inferred Primitive |
|--------------------|--------------------|
| `.claude/commands/kernel/*.md` | build-command |
| `.claude/skills/*/SKILL.md` | build-command (skill variant) |
| `*-test/` or validation report | prod-test |
| `.claude/protocols/*.md` | domain-setup |
| `projects/*/research-*.md` | none (inline research) |

**Pros:**
- No changes to task file format
- Works with existing tasks retroactively

**Cons:**
- Fragile — path conventions change, edge cases multiply
- Can't distinguish between "write a command file" (simple copy) and "build a command" (full primitive loop)
- Needs a mapping table that grows with every new primitive

### Option C: Hybrid — Tags with Convention Fallback

Task-builder tags tasks with `## Primitive` when it recognizes the pattern. If no tag is present, the outer loop falls back to inline execution (current behavior). Convention-based detection is NOT used as fallback — if it's not tagged, it's not a primitive invocation.

**This is the recommended approach.** Reasons:
1. Task-builder already has full context during decomposition (it reads the goal, researches the repo, checks conventions)
2. Explicit > implicit — a tag is a deliberate decision, not a guess
3. The fallback (inline execution) is safe and well-tested
4. No retrofit burden — existing tasks without tags work exactly as before

### Dispatch Implementation

The dispatch happens in run-task.sh or the one-shot agent's task execution logic:

```
1. Agent reads task file
2. If ## Primitive field exists:
   a. Look up primitive in registry (skill folder → entry point mapping)
   b. Invoke primitive with arguments from task file
   c. Check primitive's exit contract (artifacts exist, validation passed)
   d. Report result to outer loop
3. If no ## Primitive field:
   a. Execute task inline (current behavior)
```

The **primitive registry** is simply the existing skill folders:

| Primitive Name | Skill Location | Entry Point |
|---------------|----------------|-------------|
| `build-command` | `.claude/skills/build-command/` | Read SKILL.md, follow steps |
| `prod-test` | `.claude/skills/prod-test/` | `/kernel/prod-test <path>` |
| `audit-workflow` | `.claude/skills/audit-workflow/` | `/kernel/audit-workflow` |
| `domain-setup` | `.claude/skills/kernel-domain-setup/` | `/kernel/domain-setup` |

No new registry file needed — the skill folders ARE the registry.

---

## 2. State Scoping: Inner Loops Must Not Contaminate Outer State

### Current State Isolation (Already Shipped)

The per-agent workflow state isolation (backlog 155, shipped) already solves the primary contention problem:

| Mechanism | How It Works |
|-----------|-------------|
| `agent_id` in `session_state.json` | Routes workflow reads/writes to `agent-{id}-workflow.json` |
| Per-agent actions log | `agent-{id}-actions.jsonl` — each agent logs independently |
| Per-agent workflow file | `agent-{id}-workflow.json` — cycling state, completed_tasks, anchor counter |
| Shared `sr_dev_workflow.json` | Global fields only (domain, setup_complete, protocol_created) |

### What Inner Loops Need Beyond Current Isolation

Inner loops invoked by an outer loop introduce a **nesting** dimension that parallel agents don't have. The key difference:

| Dimension | Parallel Agents | Nested Inner Loops |
|-----------|----------------|-------------------|
| Lifecycle | Independent — spawned by run-task.sh, run to completion | Dependent — invoked mid-task by outer agent, must return control |
| State scope | Each gets own agent_id at spawn time | Inner loop needs a DERIVED agent_id (e.g., `{outer-id}--{primitive}`) |
| Session state | Each one-shot gets fresh session_state pre-init | Inner loop runs WITHIN outer agent's session — shared session_state.json |
| Anchor budget | Each agent has own anchor counter | Inner loop actions count against... whose anchor budget? |

### Scoping Strategy: Delegated Execution via run-task.sh

The simplest and most consistent approach: **inner loops execute as spawned one-shot agents**, exactly like current task execution.

When the outer loop's one-shot agent encounters a `## Primitive: build-command` task:

```
1. One-shot agent reads task file, sees ## Primitive: build-command
2. Agent writes inner task files to a NESTED task folder:
   tasks/{outer-folder}/_inner/{task-id}-{primitive}/
3. Agent invokes: env -u CLAUDECODE bash run-task.sh . 5 {nested-folder}
4. run-task.sh spawns one-shot agents for inner tasks with agent_id = "{nested-folder}"
5. Inner agents get their own agent-{nested-folder}-workflow.json
6. When run-task.sh returns, outer agent checks exit artifacts
7. Outer agent reports task complete/failed based on inner results
```

**Why this works:**
- Reuses the proven run-task.sh execution model — no new execution path
- State isolation is automatic (new agent_id = new workflow file)
- Anchor budget is independent (inner agents have their own counter)
- Session state contention is avoided (each one-shot gets pre-init)
- Error handling follows existing patterns (retry, skip after 3 attempts)

**Why NOT inline execution of inner primitives:**
- An inner primitive running inline shares the outer agent's anchor counter, actions log, and session state
- If the inner primitive triggers an anchor, it resets the outer agent's context
- If the inner primitive fails and needs /kernel/learn, it writes to the outer agent's lessons state
- The contamination risk is exactly the multi-agent state collision lesson (2026-06-14)

### session_state.json Contention

Even with delegated execution, `session_state.json` has contention risk:

| Field | Risk | Mitigation |
|-------|------|------------|
| `pipeline_state` | Inner loop's pipeline_state would overwrite outer | Inner loops don't use pipeline_state — they're not pipelines, they're primitive invocations |
| `pipeline_mode` | Same concern | Inner loops read but don't write pipeline_mode |
| `context` | Inner agent writes its own context | One-shot pre-init resets context per invocation — no cross-contamination |
| `agent_id` | Inner agent has different agent_id | Set by run-task.sh pre-init — isolated |
| `needs_learn` | Inner failure sets needs_learn | Scoped to inner agent's session — cleared on next pre-init |

**Verdict:** With delegated execution via run-task.sh, session_state.json contention is already mitigated by the one-shot pre-init pattern. Each `claude -p` invocation gets a fresh session_state merge with its own agent_id.

---

## 3. Error Propagation: When Inner Loops Fail

### Failure Modes

| Inner Loop Failure | Outer Loop Sees | Outer Loop Response |
|-------------------|-----------------|---------------------|
| Inner task fails, retried, succeeds | run-task.sh returns success | Continue |
| Inner task fails 3x, skipped | run-task.sh returns success (with skipped tasks) | Check `skipped_tasks` in inner workflow — partial success |
| run-task.sh hits max consecutive failures | run-task.sh returns exit 1 | Mark outer task as FAILED |
| Inner primitive produces wrong artifacts | Exit contract check fails | Mark outer task as FAILED |
| Inner primitive times out | run-task.sh timeout kills claude -p | Retry (standard run-task.sh behavior) |

### Error Handling Strategy: Fail-Fast with Context

```
1. Inner run-task.sh completes (success or failure)
2. Outer agent reads inner agent's workflow file:
   - completed_tasks: what succeeded
   - skipped_tasks: what was skipped (3x failures)
   - complete: whether all tasks finished
3. Outer agent checks exit contract:
   - Are the expected artifacts present?
   - If validation report exists, does it show passes?
4. Decision:
   - All artifacts present + validation passes → task COMPLETE
   - Partial artifacts + some skips → task FAILED (log which inner tasks failed)
   - No artifacts → task FAILED (inner loop didn't produce anything)
5. On failure: outer loop's standard retry logic applies
   - attempts_on_current increments
   - After 3 outer attempts, task is skipped
   - /kernel/learn records the compound failure
```

### Why NOT Retry Semantics at the Inner Level

The inner loop (run-task.sh) already has its own retry logic (resume attempts, model upgrade, skip after 3 failures). Adding another retry layer at the outer level for inner failures creates:
- Exponential retry explosion: 3 outer × 3 inner × 2 resume = 18 attempts for one task
- State accumulation: each retry leaves partial artifacts that may confuse subsequent attempts

**Keep it simple:** Inner loop retries internally. Outer loop treats inner loop as atomic — it either produced the artifacts or it didn't.

---

## 4. Recursive Composition: Can Inner Loops Invoke Their Own Inner Loops?

### Is It Needed?

Concrete scenario: execute-pipeline invokes build-command (inner loop), and build-command needs prod-test (inner-inner loop) to validate its output.

This is a real use case — the build-command primitive already calls prod-test as its final validation step. If build-command runs as an inner loop inside execute-pipeline, it would naturally want to invoke prod-test as an inner-inner loop.

### Depth Limit

With delegated execution via run-task.sh, recursion is technically unlimited — each level spawns new one-shot agents with their own state. But practical limits exist:

| Depth | Example | Latency | State Files |
|-------|---------|---------|-------------|
| 0 | execute-pipeline (outer) | baseline | 2 (session + workflow) |
| 1 | build-command (inner) | +run-task.sh overhead per task | +2 per inner agent |
| 2 | prod-test (inner-inner) | +run-task.sh × another set of tasks | +2 per inner-inner agent |
| 3 | ??? | minutes of overhead per level | state file proliferation |

**Recommendation: Cap at depth 2.**

Depth 0 = execute-pipeline (outer orchestrator)
Depth 1 = primitive invocation (build-command, prod-test, etc.)
Depth 2 = primitive's own sub-invocation (build-command → prod-test)

Beyond depth 2, the latency cost of spawning run-task.sh layers exceeds the benefit. If a primitive needs something at depth 3, it should either:
1. Inline it (simple enough to not need a separate loop)
2. Restructure the task decomposition to flatten the nesting

### Nested Task Folder Convention

```
tasks/
  my-project/                          ← outer task folder (depth 0)
    001-research-requirements.md
    002-build-filter-command.md         ← has ## Primitive: build-command
    _inner/
      002-build-command/                ← inner task folder (depth 1)
        001-read-spec.md
        002-write-command.md
        003-prod-test.md                ← has ## Primitive: prod-test
        _inner/
          003-prod-test/                ← inner-inner task folder (depth 2)
            001-assemble-master.md
            002-run-tests.md
```

Each `_inner/` folder is self-contained with its own index and gate contract. The nesting is visible in the filesystem, making debugging straightforward.

### Agent ID at Each Depth

```
Depth 0: agent_id = "my-project"
Depth 1: agent_id = "my-project--002-build-command"
Depth 2: agent_id = "my-project--002-build-command--003-prod-test"
```

The `--` separator creates a hierarchy that's parseable and unique. Each depth gets its own `agent-{id}-workflow.json`.

---

## 5. Summary of Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Dispatch mechanism | Explicit `## Primitive` tag in task files | Explicit > implicit, task-builder decides at decomposition |
| Fallback for untagged tasks | Inline execution (current behavior) | Safe, well-tested, no retrofit needed |
| State scoping | Delegated execution via run-task.sh | Reuses proven one-shot model, automatic state isolation |
| session_state.json | One-shot pre-init handles contention | No new mechanism needed |
| Error propagation | Fail-fast — inner loop is atomic to outer | Avoids retry explosion |
| Recursive depth | Cap at 2 (outer → inner → inner-inner) | Latency vs benefit tradeoff |
| Nested folder convention | `_inner/{task-id}-{primitive}/` | Filesystem-visible, self-contained |
| Agent ID nesting | `--` separator (e.g., `project--002-build-command`) | Unique, parseable, maps to workflow files |

### What Does NOT Change

- Primitive interfaces (entry/exit contracts remain as-is)
- run-task.sh (no changes needed — it already supports agent_id and nested folders)
- Kernel governance (anchor, learn, complete — all work the same at every depth)
- session_state.json schema (no new fields)
- Existing task execution (untagged tasks execute inline as before)

### What DOES Change (Implementation Required)

1. **Task-builder step-05 (decompose):** Add logic to emit `## Primitive` field when goal matches a known primitive's entry contract
2. **One-shot agent task execution:** Add dispatch logic — if `## Primitive` exists, write inner tasks and invoke run-task.sh instead of executing inline
3. **Convention:** Document `_inner/` folder pattern and `--` agent ID separator
