# Orchestrator/Subagent Research -- Final Report

Backlog 230. Decision-ready synthesis of the current-state map, industry survey, and per-command recommendation matrix.

---

## Executive Summary

The workspace already runs an orchestrator/subagent architecture at three tiers: execute-pipeline spawns one-shot `claude -p` agents per task (Tier 1), prod-test nests inner run-task.sh loops (Tier 2), and spawn-agent-swarm parallelizes full pipelines (Tier 3). Per-agent state isolation, worktree isolation, and entry-only protocol validation are all production-tested. The infrastructure for safe multi-agent execution exists -- it did not when the 2026-04-04 lesson was recorded.

The industry survey confirms what the workspace failure history shows: multi-agent orchestration is justified only when tasks decompose into 4+ independent subtasks, each taking >30 seconds, with isolated state and a well-defined synthesis step. Princeton NLP found single agents match or outperform multi-agent on 64% of benchmarked tasks. Google Research found multi-agent degrades sequential reasoning by 39-70%. Cost compounds 3-15x. The bar is high.

Three commands clear that bar: **audit-workflow** (7 independent scans, orchestrator), **eval** (parallel metric execution within step 6, hybrid), and **project-run** (outer loop over manifest items, new orchestrator command). The remaining 18+ commands are correctly inline and should stay that way.

Supporting evidence: [01-current-state.md](01-current-state.md), [02-industry-survey.md](02-industry-survey.md), [03-recommendation-matrix.md](03-recommendation-matrix.md)

---

## The Verdict: AMEND the 2026-04-04 Lesson

**Position: Amend -- not remove, not keep as-is.**

The 2026-04-04 lesson ("NEVER SPAWN AGENTS UNLESS FOR PROD-TEST OR RUN-TASK.SH") was correct at the time it was recorded. It prevented casual delegation when per-agent state isolation did not exist, worktree isolation was not available, and protocol validation during execution caused deadlocks. Every cost it cited -- latency, context loss, user preference for direct work -- was real and unmitigated.

Since then, three structural changes invalidated the blanket prohibition:

1. **Per-agent state isolation** (2026-06-14) -- each agent writes to `agent-{id}-workflow.json`, eliminating the shared mutable state that caused visibility loss and write conflicts.
2. **Worktree isolation** -- `Agent(isolation: "worktree")` prevents file conflicts between concurrent BUILD agents.
3. **Protocol validation at entry only** (2026-06-14) -- removing Gate 6 from PreToolUse eliminated the deadlock cascade that made concurrent agents structurally impossible.

The core insight -- that spawning adds latency and loses context -- remains true. But it is now a cost to weigh, not a prohibition to enforce. The blanket "NEVER" should become a conditional with explicit triggers.

### Recommended Amendment

**Current text:**
> NEVER SPAWN AGENTS UNLESS FOR PROD-TEST OR RUN-TASK.SH. Do not use the Agent tool for research, exploration, or task delegation. If you can do the work yourself (read files, search, web fetch, analyze), do it yourself.

**Proposed replacement:**
> DEFAULT TO INLINE EXECUTION. Do not spawn agents for research, exploration, or ad-hoc task delegation -- do the work yourself. Exceptions: (1) prod-test (by design), (2) run-task.sh / autonomous cycling (the intended execution model), (3) commands whose skill files explicitly declare `## Execution: orchestrator` or `## Execution: hybrid` -- these have been evaluated against the decision criterion below and approved for subagent spawning. All other commands stay inline. When in doubt, inline wins.

### Conditions That Would Reverse This Verdict

- If per-agent state isolation breaks in production (concurrent agents overwrite each other again), revert to blanket prohibition until structural fix ships.
- If subagent spawning cost exceeds 3x for the approved commands, re-evaluate. The 1.3-2x estimates assume read-heavy scan/metric agents; if they become generation-heavy, the calculus changes.
- If the user explicitly requests a return to the blanket prohibition, honor immediately. The lesson originated from user preference, and user preference overrides analysis.

---

## Decision Criterion

A generic test any future command can self-apply to determine its execution model:

**Orchestrator + subagents** -- all four conditions must hold:
1. The command has 4+ independent subtasks that share no mutable state
2. Each subtask takes >30 seconds (amortizes ~5s subprocess startup overhead)
3. Per-agent state isolation exists or is straightforward to add (one `agent-{id}-workflow.json` per subagent)
4. The synthesis/aggregation step is well-defined -- not ad-hoc merging but a structured combine (scoring, dedup, reporting)

**Hybrid** (sequential steps with internal parallelism) -- conditions 1-4 apply to the parallelizable step:
1. The command has sequential steps where most depend on prior output
2. One or more steps contain N independent items (metrics, scans, manifest entries)
3. Each item takes >30 seconds
4. Results aggregate into a structured output

**Inline** -- everything else. If any of conditions 1-4 fail, stay inline. If uncertain, stay inline.

The 30-second threshold derives from: subprocess creation (~200-500ms) + session initialization (~1-2s) + anchor ceremony (~2-3s) = ~5s minimum overhead. At 30s per subtask, overhead is ~17% -- the break-even point. Below 30s, parallelization costs more than it saves.

---

## Recommendations (Ranked)

### 1. audit-workflow -- Orchestrator + Subagents

**Priority: High.** 7 independent scans, each self-contained, no inter-scan state. Textbook fan-out/fan-in. Wall-clock drops from ~15min to ~3min. Centralized orchestrator error amplification is 4.4x (lowest architecture). Cost multiplier: 1.5-2x (read-heavy agents).

**Implementation:** Steps 1-7 each become a one-shot subagent with `agent-{scan-step}-actions.jsonl`. Step 8 (report-fix) runs in the parent session, reads all scan results, generates and executes fix tasks. Declare `## Execution: orchestrator` in audit-workflow SKILL.md.

### 2. eval -- Hybrid (Parallel Metrics in Step 6)

**Priority: High.** Steps 0-5 stay sequential (each depends on prior). Step 6 parallelizes N metrics: each takes 30-60s (LLM-as-judge API latency), has self-contained inputs (golden dataset + artifact output), writes its own score file. Wall-clock for step 6 drops from 6-12min to 1-2min. Cost multiplier: 1.3-1.5x.

**Implementation:** Step 6 spawns per-metric agents with `one_shot: true`. Parent aggregates scores after all complete. Validate OPENAI_API_KEY once at entry (2026-06-25 lesson). Declare `## Execution: hybrid` in eval SKILL.md.

### 3. project-run -- New Orchestrator Command

**Priority: Medium.** Not yet built. Reads a manifest (README status table), identifies DESIGNED items, resolves dependency order, iterates. Each item is a full execute-pipeline invocation. Items in the same dependency tier run in parallel; items with dependencies run sequentially. Automates the outer loop the user currently performs manually.

**Implementation:** New command + skill. Per-item state via `agent-{component-id}-workflow.json`. Leverages spawn-agent-swarm for intra-tier parallelism. Declare `## Execution: orchestrator` in project-run SKILL.md.

### 4. task-builder plan review -- No Change (Already Correct)

**Priority: None.** Step 07 already specs a spawned reviewer (generator-verifier pattern). Decomposition stays inline. The 2026-04-28 lesson clarifies: plan REVIEW (automated agent check) is correct; plan APPROVAL (user pause) is the violation. No implementation change needed.

### 5. gap-check -- Stay Inline

**Priority: None.** 14 checks, each completing in <1 second. Parallelization overhead (14 subprocess startups) exceeds total sequential execution time. Princeton NLP single-agent finding applies directly.

### 6. walkthrough -- Stay Inline

**Priority: None.** User-paced, interactive, sequential by contract. Google Research finding: multi-agent degrades sequential reasoning by 39-70%.

---

## What Would Change the Answer

| Signal | Effect |
|--------|--------|
| Per-agent state isolation fails in production | Revert to blanket prohibition. The 2026-04-04 lesson was correct BECAUSE isolation did not exist. If it breaks, the same reasoning applies. |
| Subprocess startup drops to <1s (persistent agent pools) | Lower the 30-second threshold. More commands become viable for orchestration. gap-check might cross the line. |
| LLM-as-judge latency drops to <5s per metric | Eval hybrid pattern loses justification. Stay inline if total step-6 time is under 1 minute. |
| User explicitly prefers blanket prohibition | Honor immediately. The lesson originated from user preference, which overrides cost-benefit analysis. |
| A new command with 8+ independent >30s subtasks ships | Apply the decision criterion. If all four conditions hold, declare orchestrator. |
| Cost multiplier for approved commands exceeds 3x | Re-evaluate. The 1.3-2x estimates assume read-heavy agents. Generation-heavy agents would change the math. |
| Context window expands 10x+ | Reduces context-budget pressure, the second dimension in the decision framework. More work fits inline. Raises the bar for orchestration. |

---

## Reconciliation with Failure History

Every recommendation in this report was evaluated against the recorded lessons:

| Lesson | How Reconciled |
|--------|---------------|
| 2026-04-04 (no-spawn) | Amended, not removed. Inline remains default. Only commands with explicit `## Execution` declarations spawn. |
| 2026-06-14 (state contention) | All orchestrator recommendations use per-agent state files. No shared mutable state between concurrent agents. |
| 2026-06-14 (protocol deadlock) | Protocol validation at entry only. No concurrent agents checking protocol hash during execution. |
| 2026-04-23 (pipeline contention) | Sequential constraint relaxed only where per-agent isolation is confirmed. Parent never preps pipeline N+1 while N runs on shared state. |
| 2026-04-28 (plan review vs approval) | task-builder recommendation preserves the distinction. Automated review (spawned agent) is correct. User approval (pause) is the violation. |
| Princeton NLP (single-agent parity) | gap-check stays inline because subtasks are trivial. Only commands where single-agent baseline has plateaued AND parallelism provides wall-clock gains cross the threshold. |
| Google Research (sequential degradation) | walkthrough stays inline. anchor, learn, complete stay inline. No sequential-reasoning command is recommended for orchestration. |
| MAST taxonomy (41-86.7% failure rate) | Mitigated by: centralized orchestrator (4.4x amplification, lowest), per-agent state isolation, existing run-task.sh governance, one-shot session lifecycle. |
| Augment Code (3-15x cost) | Estimated multipliers for approved commands are 1.3-2x. Low because decomposition is static (predefined scans/metrics/manifest), not dynamic LLM decomposition. |
