# Ephemeral Sub-Agent Execution — Research Report

## Verdict: YAH

Expand ephemeral sub-agent execution as a primary context-decay strategy, contingent on resolving session_state.json contention first.

---

## Findings Summary

### Current Surface (Task 002)

The kernel already operates a mature ephemeral execution surface: run-task.sh one-shot agents, prod-test sub-agents, spawn-subagent (BUILD and RESEARCH scopes), and spawn-agent-swarm. All five documented recurring rule violations in lessons.md (quick-anchor bypasses, state contention, rule-application decay) trace to long-lived sessions — interactive orchestrators and extended pipeline parents. Zero violations originated from one-shot agents. The one-shot contract (fresh context → single task → complete → exit) eliminates context decay by design: there is no opportunity for attention dilution, positional decay, or instruction-following degradation because the context window never accumulates multi-task history.

### Industry Patterns (Task 003)

The orchestrator-worker pattern is well-established: Anthropic's Agent SDK sub-agents, Devin's planner-executor split, LangGraph's state graph nodes, and OpenAI Swarm's agent handoff all use short-lived executors with external state management. Empirical evidence supports reliable instruction-following up to approximately 30-50K tokens of conversation; beyond that, rule-violation probability increases measurably. The kernel's N-action anchor mitigates this by re-injecting rules into recent context, but does not eliminate the underlying attention dilution — a fresh context does.

**Cost:** Ephemeral execution costs ~20-30% more in raw token consumption due to repeated anchor/session-start overhead (~14.7K input + ~5K output per one-shot agent). However, each degradation-induced failure costs ~15K tokens in fix + learn + re-execution, plus user intervention time. With 5 documented incidents over 4 months, the degradation cost offsets the overhead premium. Parallelism further reduces wall-clock time — 10 agents spawned simultaneously complete in ~1 task duration versus 10x sequential.

### Integration Design (Task 004)

The strongest candidate for ephemeral expansion is the vertical pipeline orchestrator (e.g., the 203-229 build series), which accumulated 28 actions between anchors and produced multiple rule violations. The execute-pipeline parent is a partial candidate — task-builder (Steps 1-3) needs full backlog context, but execution (Step 4) already spawns one-shot agents. Interactive sessions cannot be made ephemeral because users need conversation continuity.

A four-tier anchor policy emerges naturally:

| Tier | Role | Anchor Policy |
|------|------|---------------|
| 0 | Interactive user session | Full anchor every N actions (current) |
| 1 | Pipeline orchestrator | Anchor at start; delegate all execution to Tier 2 |
| 2 | One-shot executor (run-task.sh) | Inherit anchor from parent; single task |
| 3 | Inner test agent (prod-test) | Same as Tier 2; disposable test repo |

## Trade-Off Analysis vs Current N-Action Anchor

| Dimension | N-Action Anchor (Current) | Expanded Ephemeral |
|-----------|--------------------------|-------------------|
| Context decay prevention | Mitigates (re-injects rules) | Eliminates (fresh context per task) |
| Token cost | Lower per-task (shared context) | ~20-30% higher (repeated ceremony) |
| Failure cost | ~15K tokens per violation + user time | Near-zero (no accumulated decay) |
| Latency | Near-zero task switching | ~5-10s cold-start per agent |
| Parallelism | Limited (single session) | Full (concurrent agents) |
| Semantic continuity | Natural (same conversation) | Lost without explicit handoff |
| State contention | Single writer (safe) | Multiple writers (requires isolation) |

The N-action anchor is the right strategy for Tier 0 (interactive sessions) where conversation continuity is essential. For Tier 1-3 (autonomous execution), ephemeral agents are strictly superior: they eliminate the failure mode that the anchor was designed to mitigate.

## Integration Design

### Prerequisite: Fix session_state.json Contention (CRITICAL)

Directly observed during this research: four concurrent agents fought over `session_state.json`, overwriting each other's `agent_id`, `context`, and `timestamp` fields. The `agent_id` field — which routes reads/writes to per-agent workflow files — is itself in the shared file. When agent B overwrites agent A's `agent_id`, agent A's hook reads the wrong routing target.

**Required fix:** Pass `agent_id` via environment variable (`AGENT_ID=xyz claude -p ...`). run-task.sh already controls the `claude -p` invocation and can inject this. Hooks read `$AGENT_ID` instead of `session_state.json.agent_id`. Per-process, not per-file — no contention possible.

### Semantic Context Handoff

Current handoff transfers structural metadata (`completed_tasks`) but loses semantic context (constraints discovered mid-execution, approach decisions, environmental findings). Proposed: each one-shot agent writes a `handoff` block to its per-agent state file with `discoveries`, `constraints`, and `next_agent_should_know` fields. The next agent's session-start reads prior handoffs. Cost: ~700 tokens per task boundary. Value: prevents the "context loss at handoff" failure mode identified in task 003.

### Orchestrator Discipline

Moving more work to ephemeral agents does not eliminate the orchestrator — it constrains it. The orchestrator's role must stay minimal: decompose, dispatch, aggregate. It must not do actual work (writing files, running tests, editing code). execute-pipeline already approaches this discipline; the lesson is to enforce it: if an orchestrator finds itself writing deliverable files, it should be spawning an agent instead.

## Disqualifying Reasons (None)

No fundamental barriers exist. All blockers are engineering tasks:

1. **session_state.json contention** — solvable via env-var agent_id routing
2. **Orchestrator decay** — mitigated by keeping orchestrator thin (decompose, dispatch, aggregate only)
3. **Handoff quality** — solvable via semantic handoff schema extension to per-agent state
4. **Overhead for tiny tasks** — acceptable; the ceremony tax is ~30-50% for medium tasks, problematic only for trivial edits (rename, typo fix) that rarely appear in task-builder output

## Recommended Next Steps

1. **Backlog: env-var agent_id routing** — Modify run-task.sh to set `AGENT_ID` env var; update hooks to read from env instead of session_state.json. Eliminates the critical contention blocker.
2. **Backlog: semantic handoff schema** — Extend per-agent workflow state with `handoff` block; update session-start to read prior handoffs. Low cost, high impact on inter-agent context continuity.
3. **Backlog: orchestrator discipline rule** — Add to protocol/lessons: orchestrators must not write deliverable files directly. If an action creates output, it must be delegated to a Tier 2 agent.
