# Per-Command Recommendation Matrix

Research for backlog 230, task 003. Applies the industry survey's decision criteria to each workspace command.

---

## Decision Framework Applied

From the industry survey (02-industry-survey.md), the four-part decision rule: adopt orchestrator+subagents only when ALL four conditions hold:

1. The task decomposes into semi-independent subproblems
2. The synthesis step adds value rather than overhead
3. The single-agent baseline is already well-optimized and has plateaued
4. The incremental business gain exceeds the full coordination, governance, and infrastructure cost

Plus the five dimensions: task independence, context-budget pressure, parallelism value, verification needs, state isolation.

---

## Recommendation Matrix

### Candidates Evaluated

| Command/Skill | Verdict | Deciding Criterion | Cost Acknowledged | Kernel Governance |
|---------------|---------|-------------------|-------------------|-------------------|
| **gap-check** | Stay inline | Checks are small and fast; parallelism overhead > benefit | 14 subprocess startups + merge for checks that complete in seconds each. Anthropic's own guidance: "find the simplest solution possible." | N/A — no subagent state needed |
| **eval** | Hybrid (sequential steps, parallel metric execution) | Per-metric independence within step 6; LLM-as-judge calls take 30-60s each; 12+ metrics = significant wall-clock savings | Subprocess startup per metric (~200-500ms) amortized against 30-60s per metric. Net win at ≥4 metrics. Context loss acceptable because each metric has self-contained inputs (golden dataset + artifact output). | Per-metric agents use `one_shot: true`. No shared mutable state between metrics. Each metric writes its own score; step 6 aggregates. Existing `agent-{id}-workflow.json` pattern applies. |
| **audit-workflow** | Orchestrator + per-scan subagents | 7 independent scans = textbook fan-out/fan-in. Each scan is self-contained (reads files, produces findings list). No inter-scan state. | 7 subprocess startups + merge step. Each scan takes 1-3min sequential; parallel execution cuts wall-clock from ~15min to ~3min. | Per-scan agents write to `agent-{scan-id}-actions.jsonl`. Step 8 (report-fix) runs in parent session, reads all scan results. Hooks enforce anchor on each subagent independently. |
| **task-builder** (plan review) | Hybrid (already designed correctly) | Step 07 already specs an automated agent check — a spawned reviewer. Decomposition stays inline because it requires full conversation context. | One additional subprocess for the reviewer. Acceptable — plan review quality > latency. | Reviewer is a one-shot agent. Reads the plan, returns structured verdict. No state file writes needed — result goes back to parent. |
| **walkthrough** | Stay inline | User-paced, one section per turn. Blocking on user IS the design. Sequential by contract. Fails all four conditions of the decision rule. | No parallelism opportunity. User interaction is the core value. | N/A |
| **project-run** (outer loop) | Orchestrator — thin sequencing layer | Items in the same dependency tier are independent. Each item is already handled by execute-pipeline subagents. The outer loop just sequences tiers and calls existing commands. | Each item = full execute-pipeline run (5-30min). Parallelizing independent items in a tier = major wall-clock savings. Cost is orchestrator state management per item. | Per-item state via `agent-{component-id}-workflow.json`. Sequential constraint applies WITHIN a dependency chain, not across independent items. Manifest file (README status table) is the orchestrator's input — reads DESIGNED items, iterates in dependency order. |
| **vertical build chain** (validate-merge-launch loop) | Subsumed by project-run | The validate-merge-launch loop IS what project-run orchestrates. Steps 2-4 per component (backlog → execute-pipeline → validate) are the inner loop. project-run is the outer loop that iterates components. | Same as project-run — the chain is the unit of work per component. | Same as project-run. |

### Commands That Must Stay Inline (No Evaluation Needed)

These fail the decision rule at condition 1 (don't decompose into subproblems) and are session-lifecycle-bound:

| Command | Why Inline |
|---------|-----------|
| **session-start** | Sets up THIS session's state. No delegation possible. |
| **anchor** | Re-reads protocol into THIS agent's context window. Spawning defeats the purpose. |
| **learn** | Records what THIS agent learned from a failure. Subagent lacks the failure context. |
| **complete** | Validates THIS session's work against gate contracts. Must see current state. |
| **fix** | Assesses impact on current task. Requires current context. |
| **reset** | Resets state files. Trivial operation. |
| **backlog** | Intent chain hashes the user's raw words at invocation time. MUST run in the session that receives user input. |
| **summarize** | Single-pass text processing. No decomposition opportunity. |
| **human-check** | Single-pass text analysis. No decomposition opportunity. |
| **check-5-layer** | Architecture validation. Reads contract, checks structure, reports. One-pass. |
| **design** | Produces design documents. Requires full conversation context. |
| **build-command** | Constructs kernel commands. Requires full conversation context. |
| **review-queue** | State operations on feature branches. Trivial. |
| **attest** | Cryptographic attestation. Sequential by nature. |

---

## Per-Candidate Detail

### gap-check — Stay Inline

**Current state:** 5 steps (discover, detect & model, check, report, fix). 14 gap categories across different corpus types. Steps 1-2 must complete before step 3 (sequential dependency).

**Why not orchestrator:** The checks in step 3 are independent but each is fast — a grep + pattern match completing in under a second. Spawning 14 subagents (subprocess creation + session initialization + anchor ceremony per agent) adds ~3-5 seconds per agent. Sequential execution of all 14 checks takes ~5-10 seconds. Parallelizing adds overhead without meaningful wall-clock improvement.

**Decision rule check:**
1. Decomposes into subproblems? Technically yes (14 checks), but each is trivial.
2. Synthesis adds value? No — merge is just concatenation.
3. Single-agent baseline plateaued? No — gap-check works well inline.
4. Business gain exceeds cost? No — saving 5 seconds doesn't justify 14 subprocess startups.

**Verdict:** Stay inline. The Princeton NLP finding applies directly: single agent matches or outperforms when subtasks are trivial and context fits in one window.

### eval — Hybrid

**Current state:** 7 sequential steps. Step 6 (run and score) executes multiple DeepEval metrics, each involving an LLM-as-judge call (30-60s per metric).

**Why hybrid:** Steps 0-5 are sequential — each depends on the prior (can't generate tests before compiling the harness). But within step 6, each metric is independent: it takes the same artifact output and golden dataset, runs its own LLM-as-judge call, and produces a score. With 12+ metrics, sequential execution = 6-12 minutes. Parallel execution = 1-2 minutes.

**Decision rule check:**
1. Decomposes? Yes — N independent metric evaluations within step 6.
2. Synthesis adds value? Yes — aggregated score report across metrics.
3. Single-agent baseline plateaued? Yes — the bottleneck is LLM-as-judge API latency, not agent capability.
4. Business gain exceeds cost? Yes — 5-10x wall-clock improvement on the slowest step.

**Cost profile:**
- N subprocess startups (~200-500ms each) amortized against 30-60s per metric = negligible overhead ratio
- Token overhead: each metric agent needs the artifact output + golden dataset + metric definition. No context reconstruction needed — inputs are self-contained files.
- Augment Code's "3x cost at 18-point lift" applies to general orchestration. Here, the parallelism is purely wall-clock optimization with identical total tokens.

**Kernel governance:** Each metric agent runs with `one_shot: true`. No shared mutable state — each writes its own score file. Parent step 6 aggregates scores after all agents complete. Existing `agent-{id}-workflow.json` pattern provides state isolation. The OPENAI_API_KEY dependency (2026-06-25 lesson) means all metric agents need the same env var validated once at entry.

### audit-workflow — Orchestrator + Subagents

**Current state:** 8 steps. Steps 1-7 are independent scans (commands, skills, hooks, protocol, state, testing, atomicity). Step 8 aggregates findings and generates fix tasks.

**Why orchestrator:** This is the textbook fan-out/fan-in pattern from the industry survey. 7 scans, each self-contained (reads a specific set of files, produces a findings list), no inter-scan state dependencies. Getmaxim's reliability analysis rates centralized orchestrator error amplification at 4.4x (lowest of all architectures) — the parent runs step 8 with full visibility.

**Decision rule check:**
1. Decomposes? Yes — 7 independent scans.
2. Synthesis adds value? Yes — step 8 aggregates findings, deduplicates, prioritizes, generates fix tasks.
3. Single-agent baseline plateaued? Moderate — audit is already thorough but slow.
4. Business gain exceeds cost? Yes — audit wall-clock drops from ~15min to ~3min. Audit runs frequently during kernel development.

**Cost profile:**
- 7 subprocess startups. Each scan takes 1-3 minutes (file reads + pattern checks).
- Token overhead: each scan agent reads its own file subset. No cross-scan context needed.
- Cost multiplier is low (1.5-2x total tokens) because scans are read-heavy, not generation-heavy.

**Kernel governance:** Per-scan agents use `agent-{scan-step}-actions.jsonl`. Each agent anchors at session start, runs its scan, and exits. Step 8 runs in the parent session — reads all scan results, generates fix tasks, and executes them through the existing cycling mechanism. No change to hook enforcement; each subagent is a standard `one_shot: true` session.

### task-builder plan review — Hybrid (Already Correct)

**Current state:** Step 07 (plan-review) already specs an automated agent check. The decomposition (steps 1-6) stays inline because it requires full conversation context (user goal, repo structure, conventions, prior research).

**Why hybrid is correct:** The spawned reviewer in step 07 is a generator-verifier pattern. Anthropic's own guidance identifies this as effective when: the verifier has explicit criteria (the gate contract provides this) and independence from the generator (the reviewer hasn't seen the decomposition process, only the output).

**The lesson from Anthropic's failure mode analysis:** "Verifiers without explicit criteria become rubber-stamps." The task-builder's gate contract provides the explicit criteria — the reviewer checks against documented acceptance standards, not subjective quality.

**No change recommended.** The existing design is correct. The decomposition is context-dependent (inline). The review is independent verification (spawned). The 2026-04-28 lesson clarifies: plan REVIEW (automated agent check) is correct; plan APPROVAL (user pause) is the violation.

### walkthrough — Stay Inline

**Current state:** User-paced, one section per turn. The composability contract exists (designed for potential future orchestration with other commands like /design).

**Why inline:** Walkthrough is fundamentally interactive — the user reads an explanation, asks questions, makes decisions, and those decisions feed the next section. This is Google Research's "strict sequential reasoning" case: multi-agent degraded performance by 39-70% because communication fragmented the reasoning process. The user's conversation context IS the state.

**The composability contract:** The walkthrough produces a durable ledger that feeds downstream commands (/design). This is interface composability, not execution parallelism. The ledger is the handoff artifact — walkthrough stays inline, /design consumes the ledger later.

### project-run — Orchestrator (New Command)

**Current state:** Not yet built. The HMSA QA Platform README identifies the pattern: steps 2-4 (backlog → execute-pipeline → validate) are mechanical and repeatable. The README says: "All inner pieces exist — only the thin orchestrator is missing."

**Why orchestrator:** project-run reads a manifest (README status table), identifies DESIGNED items, resolves dependency order, and iterates. Each item is a full execute-pipeline invocation — already an orchestrator itself (Tier 1 from 01-current-state.md). project-run is a Tier 2 orchestrator wrapping Tier 1 pipelines.

**Decision rule check:**
1. Decomposes? Yes — each manifest item is an independent build unit (within a dependency tier).
2. Synthesis adds value? Yes — dependency ordering, status tracking, validation gates per component.
3. Single-agent baseline plateaued? Yes — manual iteration of backlog → execute-pipeline → validate is what the user does today.
4. Business gain exceeds cost? Yes — automating the outer loop for a 20+ component platform eliminates manual sequencing.

**Parallelism opportunity:** Items in the same dependency tier (no inter-item dependencies) can run concurrently via spawn-agent-swarm. Items with dependencies run sequentially. The HMSA platform has phases (Interfaces → Roles → Tasks → Metrics), with multiple items per phase.

**Kernel governance:**
- Per-item state via `agent-{component-id}-workflow.json`
- Sequential constraint applies WITHIN a dependency chain, not across independent items in a tier
- The sequential-pipeline lesson (2026-04-23) applies to items sharing state, which per-agent isolation resolves
- Manifest status updates are the orchestrator's responsibility — only project-run writes the status column

**Cost acknowledged:** Each item is a full pipeline run. Parallelizing 4 independent items in a tier = 4 full pipeline costs simultaneously. This is expensive but the alternative is 4x the wall-clock time. The MAST taxonomy's 41-86.7% failure rate is for general multi-agent systems; project-run delegates to the battle-tested execute-pipeline which already handles its own error recovery.

---

## Generic Decision Criterion

For future commands to self-classify:

```
IF the command:
  (a) has 4+ independent subtasks that share no mutable state, AND
  (b) each subtask takes >30 seconds (amortizes subprocess startup), AND
  (c) per-agent state isolation exists or is straightforward to add, AND
  (d) the synthesis/aggregation step is well-defined (not ad-hoc merging)
THEN → Orchestrator + subagents

IF the command:
  (a) has sequential steps where most depend on the prior, BUT
  (b) one or more steps contain internal parallelism (N independent items)
  (c) where each item takes >30 seconds
THEN → Hybrid (sequential steps, parallel within a step)

OTHERWISE → Stay inline
```

The 30-second threshold comes from the cost analysis: subprocess startup (200-500ms) + session initialization (~1-2s) + anchor ceremony (~2-3s) = ~5s minimum overhead per subagent. This overhead must be <15% of the subtask duration to justify spawning. At 30s per subtask, overhead is ~17% — the break-even point.

---

## Lesson Governance Implications

### Per-Agent State (Already Exists)

Every orchestrator recommendation above uses the existing `agent-{id}-workflow.json` pattern. No new state isolation infrastructure is needed. The 2026-06-14 lessons proved this pattern works in production.

### Hook Enforcement Per Subagent

Each subagent runs under `one_shot: true` with its own anchor ceremony at session start. The universal gate enforcer and domain gate enforcer apply to all sessions equally. No hook modifications needed for any recommendation in this matrix.

### Sequential Constraint Evolution

The 2026-04-23 sequential-pipeline lesson was recorded when per-agent state isolation didn't exist. With `agent-{id}-workflow.json`, the structural cause of state contention is resolved. The lesson should evolve:

- **Current rule:** Execute pipelines strictly sequentially.
- **Recommended rule:** Execute pipelines sequentially UNLESS per-agent state isolation is confirmed for all participants. audit-workflow and eval already use per-agent patterns. project-run would be designed with per-agent isolation from day one.

### Cost Budget

From the industry survey: multi-agent adds 3-15x token cost. For the three orchestrator/hybrid candidates:

| Command | Estimated Cost Multiplier | Justification |
|---------|--------------------------|---------------|
| eval (hybrid) | 1.3-1.5x | Only step 6 parallelizes; metric agents are small |
| audit-workflow | 1.5-2x | 7 read-heavy scan agents; low generation overhead |
| project-run | 1.0x (per item) | Each item costs the same as a manual pipeline run; orchestrator overhead is negligible state management |

None approach the 15x worst case because they don't involve orchestrator LLM calls for decomposition — the decomposition is static (predefined scans, predefined metrics, predefined manifest items).

---

## Summary

| Verdict | Commands |
|---------|----------|
| **Orchestrator + subagents** | audit-workflow, project-run |
| **Hybrid** | eval (parallel metrics), task-builder (spawned reviewer — already designed) |
| **Stay inline** | gap-check, walkthrough, session-start, anchor, learn, complete, fix, reset, backlog, summarize, human-check, check-5-layer, design, build-command, review-queue, attest |

Three commands should evolve. The rest are correctly inline. The 2026-04-04 lesson needs amendment — not removal, but scoped evolution. Task 004 (synthesis report) will state the final recommendation on that lesson.
