# Current-State Map — Orchestrator/Subagent Architecture

Research for backlog 230. Honest accounting of what the workspace already runs, what lessons protect, and what has changed since each lesson was recorded.

---

## Command/Skill Inventory

Every kernel command and skill, classified by current execution model and why.

### Orchestrator-Shaped (Already Spawn Subagents)

| Command/Skill | Execution Model | Subagent Mechanism | Why Orchestrator |
|---------------|----------------|-------------------|------------------|
| **execute-pipeline** | Orchestrator session + one-shot agents | `env -u CLAUDECODE bash run-task.sh` spawns `claude -p` per task | Autonomous pipeline: backlog → task-builder → run-task.sh cycling. Each task is a single-responsibility subagent (one task file = one `claude -p` invocation). Parent orchestrates sequencing, state, and validation. |
| **spawn-agent-swarm** | Parallel orchestrator | Multiple `Agent(isolation: "worktree")` or `Bash(run_in_background)` per backlog | Parallel execution of independent backlogs. Each agent is a full execute-pipeline instance with per-agent state isolation (`agent-{N}-state.json`). |
| **spawn-subagent** | Single background agent | `Agent(isolation: "worktree")` for BUILD, `Bash(run_in_background)` for RESEARCH | Non-blocking delegation of a single backlog. Goes through execute-pipeline internally — backlog → task-builder → run-task.sh. |
| **prod-test** | Orchestrator + inner run-task.sh | Assembles master repo, copies to test repo, writes inner L1/L2/L3 tasks, runs inner `run-task.sh` | Live infrastructure testing requires isolation (disposable test repo). Inner agents run under kernel governance with their own anchor/learn cycle. |
| **run-task.sh** (not a command, but the execution engine) | One-shot `claude -p` per task | Each `claude -p` invocation is a single-task subagent with `one_shot: true` | The atomic execution unit. Every task file becomes a self-contained agent with its own session lifecycle. |

### Inline (Execute in Current Session)

| Command/Skill | Execution Model | Why Inline |
|---------------|----------------|-----------|
| **session-start** | Session lifecycle | Must run in the current session to set up state. No delegation possible — it IS the session. |
| **anchor** | Protocol refresh | Re-reads protocol + lessons into the current context. The entire point is to re-center THIS agent's context window, not a subagent's. |
| **learn** | Lesson recording | Records what THIS agent learned from a failure. A subagent wouldn't have the failure context. |
| **complete** | Completion gate | Validates THIS session's work against gate contracts. Must see the current state. |
| **fix** | Impact assessment | Assesses the impact of a fix on the current task. Requires current context. |
| **reset** | Dev tool | Resets state files. Trivial operation, no delegation value. |
| **backlog** | Backlog creation | Creates a structured backlog item from user input. Intent chain hashes the user's raw words — MUST run in the session that receives the user's input. |
| **gap-check** | Analysis | Scans codebase for gaps. Currently runs inline — reads files, produces report. Could theoretically parallelize per-check, but currently sequential. |
| **eval** | Test harness | Compiles harness, copies artifact, generates tests, runs scoring. Currently inline. Complex multi-step process. |
| **audit-workflow** | Infrastructure scan | Scans all kernel infrastructure (commands, skills, hooks, protocol, state, testing). Currently inline, produces fix tasks. |
| **task-builder** | Decomposition | Parses goal, researches repo, decomposes into atomic tasks. Currently inline (called by execute-pipeline). The `skip_plan_review: false` flag already specs an automated agent check (spawned reviewer), but this reviews the plan — it doesn't execute the decomposition. |
| **walkthrough** | Documentation | Generates walkthrough documents from codebase analysis. Inline. |
| **summarize** | Text processing | Summarizes content. Inline, trivial. |
| **human-check** | Text analysis | Scans text for AI tells. Inline, single-pass analysis. |
| **check-5-layer** | Architecture validation | Validates 5-layer architecture compliance. Inline. |
| **design** | Architecture design | Produces design documents. Inline, requires full context. |
| **build-command** | Command construction | Builds a new kernel command from a design spec. Inline. |
| **review-queue** | Review management | Manages feature branch review workflow. Inline state operations. |
| **attest** | Cryptographic attestation | Signs and attests backlogs to Sigstore/Rekor. Inline. |

### Hybrid (Inline with Orchestrator Potential)

| Command/Skill | Current | Potential | Notes |
|---------------|---------|-----------|-------|
| **eval** | Inline | Per-metric subagents | Each DeepEval metric could run in parallel. Currently sequential. The eval platform already has component isolation (metrics, tests, golden datasets). |
| **audit-workflow** | Inline | Per-scan subagents | 8 scan steps are independent. Could run scans 01-07 in parallel, merge in step 08 (report-fix). |
| **gap-check** | Inline | Per-check subagents | Individual gap checks are independent. Could parallelize. |
| **task-builder** | Inline | Plan review already specs a spawned reviewer | Step 07 (plan-review) is designed as an automated agent check — a spawned agent reviews the plan. The decomposition itself stays inline. |

---

## The Two-Tier Reality

The workspace already operates an orchestrator/subagent architecture at two tiers:

### Tier 1: Pipeline Level

```
execute-pipeline (orchestrator session)
  └─ run-task.sh (spawns N one-shot claude -p agents)
       └─ each agent: one task file, one_shot: true, own session lifecycle
```

This is the primary execution model. Every backlog that goes through "the loop" (execute-pipeline → task-builder → run-task.sh) uses single-task subagents. The orchestrator (execute-pipeline) handles sequencing, state management, and validation. Each subagent handles exactly one task.

### Tier 2: Production Testing

```
prod-test (orchestrator)
  └─ assembles master repo
  └─ copies to test repo
  └─ writes inner L1/L2/L3 tasks
  └─ runs inner run-task.sh
       └─ each inner agent: one test task
```

Prod-test is a nested orchestrator — it spawns its own inner run-task.sh loop inside a disposable test repo. This is orchestrator-within-orchestrator.

### Tier 3: Swarm Level (Parallel)

```
spawn-agent-swarm (orchestrator)
  └─ spawns N independent execute-pipeline instances
       └─ each runs its own Tier 1 pipeline
```

The swarm is a meta-orchestrator that parallelizes Tier 1 pipelines. Each agent gets per-agent state isolation (`agent-{N}-state.json`).

---

## What Each Recorded Lesson Protects Against

### 2026-04-04 — "NEVER SPAWN AGENTS UNLESS FOR PROD-TEST OR RUN-TASK.SH"

**What happened:** The user explicitly requested that agent spawning be restricted. The reasons cited:
1. **Latency** — agent spawning adds overhead (subprocess creation, session initialization, anchor ceremony)
2. **Context loss** — subagents don't share the parent's conversation context. Research findings, design decisions, and investigation state are lost when delegated to a subagent
3. **User preference** — the user wants direct work in the main conversation, not delegation to invisible background processes

**What it protects against:** Casual delegation of work that the main agent could do faster and better itself. The anti-pattern is: agent encounters a task → spawns a subagent instead of doing the work → subagent lacks context → produces lower-quality output → user has to re-do or debug.

**Exceptions carved out:** (1) prod-test, which requires sub-agents by design (disposable test repos, inner task loops), and (2) run-task.sh / autonomous cycling, which IS the intended execution model for task-builder output.

**What has changed since:**
- Per-agent state isolation landed (2026-06-14 lessons → `agent-{id}-workflow.json` pattern)
- Worktree isolation available (`Agent(isolation: "worktree")`)
- spawn-agent-swarm skill built with full per-agent state files
- spawn-subagent skill built with scope-routed isolation (BUILD→worktree, RESEARCH→subfolder)
- Loop composability research (backlog 155) designed `## Primitive` tag dispatch mechanism
- execute-pipeline gained worktree isolation mode for BUILD scope
- The workspace has successfully run 170+ pipelines, many with parallel agents

**Key tension:** The lesson was recorded when the infrastructure for safe agent spawning didn't exist. Now it does (per-agent state, worktree isolation, run-task.sh governance). But the lesson's core insight — that spawning adds latency and loses context — remains true regardless of infrastructure improvements. The question is whether the benefits (parallelism, context isolation, specialization) outweigh those costs for specific commands.

### 2026-06-14 — Multi-Agent Orchestration + State Isolation

Two related lessons recorded on the same date:

#### "MULTI-AGENT ORCHESTRATION: PROTOCOL VALIDATION AT ENTRY, NOT EXECUTION"

**What happened:** When spawning parallel background agents, protocol hash validation during execution created a deadlock cascade. One agent updated `protocol_hash: "pending"` → other agents' bash got blocked → parent orchestrator stalled.

**What it protects against:** Distributed state validation that creates circular dependencies between concurrent agents.

**Fix applied:** Removed Gate 6 from PreToolUse hook. Protocol hash now validated only at session entry (`/kernel/session-start`), allowing concurrent agents to work without deadlock.

**What has changed since:** The fix is in production. Concurrent agents can now anchor and execute in parallel without protocol hash deadlock. This removed a hard blocker for any multi-agent pattern.

#### "MULTI-AGENT STATE ISOLATION: SHARED MUTABLE STATE CAUSES VISIBILITY LOSS"

**What happened:** Three concurrent agents all wrote to the same `session_state.json` and `sr_dev_workflow.json`. Agent 132 completed but agent 131 overwrote the shared state with its own completion state. Result: orchestrator lost visibility into agent 132's execution.

**What it protects against:** State file contention between concurrent agents. The failure mode: later writes silently overwrite earlier writes, causing invisible data loss.

**Fix applied:** Per-agent state file pattern — each agent writes to `agent-{id}-workflow.json` instead of shared state. Monitor reads all per-agent files independently.

**What has changed since:** Per-agent state isolation is fully implemented and production-tested across spawn-agent-swarm runs. The `agent_id` routing in session-start and anchor commands correctly routes state reads/writes to per-agent files. This was the structural fix that made multi-agent execution reliable.

### 2026-04-23 — State Contention (Pipeline Level)

**What happened:** Parent session prepped tasks for pipeline 038/039 while background agent executed pipeline 037. Both wrote to shared `sr_dev_workflow.json`. Sub-agent's session-start set `anchored: false` on the shared file, triggering hook blocks on the parent.

**What it protects against:** Parent and sub-agent co-tenancy of the same state file.

**Fix applied:** (1) Execute pipelines strictly sequentially. (2) Per-agent state scoping via `agent_id` routing (structural fix).

**What has changed since:** The `agent_id` routing system fully resolves this. Each agent (identified by `agent_id` in `session_state.json`) reads/writes its own `agent-{agent_id}-workflow.json`. The parent's workflow state is never touched by sub-agents. Sequential execution is still the default for safety, but parallel execution is now structurally safe.

---

## Prior Research Overlap

### Loop Composability Research (Backlog 155)

**Overlap:** Directly relevant. This research designed the `## Primitive` tag dispatch mechanism and delegated execution via run-task.sh. Key findings:
- Primitives are already composable in contract (clear entry/exit boundaries)
- The gap is in orchestration (detecting when to delegate), not in the primitives themselves
- Inline primitive execution causes state contamination (inner actions count against outer anchor budget)
- Delegated execution via run-task.sh with per-agent state isolation is the recommended pattern
- Depth > 2 nesting should be avoided (startup overhead per layer)

**Not duplicated here:** The specific implementation design (tag format, inner task templates, folder conventions). This research builds on 155's findings to evaluate whether MORE commands should adopt the orchestrator pattern.

### Multi-Persona Architecture (Backlog — comparison report)

**Overlap:** Tangentially relevant. This research evaluated multi-harness vs unified-harness for persona routing. Key finding: Approach B (unified harness) won 9/12 dimensions. State isolation is solved by per-agent files, not repo separation.

**Relevant insight for this research:** The multi-persona architecture validates that multiple "agents" (personas) can coexist in one workspace with per-agent state isolation. The same pattern applies to orchestrator subagents — they don't need separate repos, just separate state files.

---

## Infrastructure Summary

What exists today that enables safe orchestrator/subagent patterns:

| Capability | Status | Mechanism |
|-----------|--------|-----------|
| Per-agent state isolation | Production | `agent-{id}-workflow.json` per agent |
| One-shot session lifecycle | Production | `one_shot: true` in session_state.json |
| Worktree isolation | Production | `Agent(isolation: "worktree")` |
| Protocol validation at entry only | Production | Gate 6 removed from PreToolUse hook |
| Scope-routed isolation | Production | BUILD→worktree, RESEARCH→subfolder |
| Per-agent actions log | Production | `agent-{id}-actions.jsonl` |
| Inner task loop nesting | Production (via prod-test) | Nested run-task.sh in test repo |
| Primitive dispatch (## Primitive tag) | Designed, not built | Loop composability recommendation |
| Sequential pipeline constraint | Active | Lesson-enforced, structurally resolved |

---

## Honest Assessment

The workspace is already an orchestrator/subagent system at the pipeline level. The 2026-04-04 lesson correctly prevented casual agent spawning when the infrastructure wasn't ready. Since then:

1. **Per-agent state isolation solved the contention problem** — the 2026-06-14 lesson's fix is in production
2. **Protocol validation at entry eliminated the deadlock** — concurrent agents work
3. **Worktree isolation prevents file conflicts** — BUILD tasks get their own working tree
4. **run-task.sh provides kernel governance** — every subagent runs under the full loop

The remaining costs of spawning (latency, context loss) are real but context-dependent. For a command like `anchor` (which must re-center THIS agent's context), spawning is nonsensical. For a command like `eval` (which runs 12 independent metrics), parallelism could cut wall-clock time significantly.

The question for tasks 002-004 is: which commands cross the threshold where spawning benefits exceed spawning costs?
