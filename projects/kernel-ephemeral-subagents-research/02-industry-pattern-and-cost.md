# Industry Pattern + Cost Model — Ephemeral Sub-Agent Execution

## The Orchestrator-Worker Pattern

### Pattern Description

The orchestrator-worker (or coordinator-executor) pattern decomposes complex agent tasks into a hierarchy: a long-lived orchestrator that plans, decomposes, and assigns work, paired with short-lived worker agents that each execute a single unit of work in a fresh context window.

**Key implementations:**

1. **Anthropic's own Claude Agent SDK sub-agents:** The Agent tool spawns sub-agents with fresh context. Each sub-agent receives a prompt, executes, and returns a result string. The parent agent synthesizes results. Sub-agents have no shared state — they are stateless executors.

2. **Devin (Cognition):** Uses a planner-executor split where the planner maintains high-level context (task decomposition, progress tracking) and spawns short-lived executors for individual code changes. The executor operates within a single-file or single-function scope, eliminating cross-task context bleed.

3. **LangGraph multi-agent workflows:** State is managed externally (in a graph state object). Each agent node receives only the state relevant to its task, executes, and writes results back to the graph. Context window consumption per agent is bounded by the node's input, not the full conversation history.

4. **OpenAI Swarm / Agents SDK:** Lightweight agent handoff pattern where each agent has a narrow instruction set and tools. Agents hand off to each other rather than accumulating context. The "routines" pattern keeps each agent's context window focused.

### Why Short Contexts Prevent Attention Decay

Transformer attention degrades with context length due to:

- **Attention dilution:** As context grows, attention weights spread thinner across more tokens. Rules read 20K tokens ago compete with recent tool outputs for attention budget.
- **Positional decay:** Despite improvements (RoPE, ALiBi), information near the end of context receives disproportionate attention weight. Protocol rules at the beginning of a session gradually lose influence.
- **Instruction-following degradation:** Empirically, models follow system-level instructions less reliably as conversation length grows. The kernel's observation (quick-anchor violations recurring after rules were read) is a textbook example.

**Typical context ceilings:** Industry practitioners report reliable instruction-following up to approximately 8-15 turns of substantive work (roughly 30-50K tokens of conversation). Beyond this, the probability of rule violations increases measurably. The kernel's N-action anchor (currently every 30 actions) is a mitigation — it re-injects rules into the recent context — but does not eliminate the underlying attention dilution.

### Result-Handoff Conventions

| Convention | Description | Used By |
|-----------|-------------|---------|
| **String return** | Worker returns final text as its output | Claude Agent SDK, kernel run-task.sh (`ONE_SHOT_COMPLETE`) |
| **Structured output (JSON schema)** | Worker forced to return validated JSON | Claude Agent SDK `schema` option, LangGraph state |
| **File-based handoff** | Worker writes results to disk; orchestrator reads files | Kernel run-task.sh (deliverable files + state JSON), Devin |
| **State graph** | Shared external state object; worker reads/writes specific keys | LangGraph, CrewAI |

The kernel's current handoff is file-based: one-shot agents write deliverable files and update per-agent workflow state; the orchestrator (or next iteration of run-task.sh) reads `completed_tasks` from the workflow state to determine what remains.

## Cost Model

### Token Economics: Ephemeral vs Long-Lived

**Per-agent spawn overhead (one-shot via run-task.sh):**

| Component | Input Tokens (est.) | Output Tokens (est.) |
|-----------|-------------------|---------------------|
| CLAUDE.md + protocol read | ~3,000 | 0 |
| session-start command | ~1,500 | ~500 |
| Anchor ceremony (protocol + lessons + state) | ~8,000 | ~2,000 |
| Task file read | ~200 | 0 |
| Task execution (typical BUILD task) | ~1,000 | ~2,000 |
| /kernel/complete | ~1,000 | ~500 |
| **Total per one-shot iteration** | **~14,700** | **~5,000** |

**Anchor overhead in long-lived session (every 30 actions):**

| Component | Input Tokens (est.) | Output Tokens (est.) |
|-----------|-------------------|---------------------|
| Protocol re-read | ~3,000 | 0 |
| Lessons re-read | ~6,000 | 0 |
| State read + actions log review | ~2,000 | ~1,000 |
| Anchor confirmation output | 0 | ~500 |
| **Total per anchor** | **~11,000** | **~1,500** |

### Cost Comparison for a 10-Task Pipeline

**Ephemeral (current run-task.sh model):**
- 10 one-shot agents x ~20K tokens each = ~200K total tokens
- Each agent has fresh context — no decay, no accumulated conversation history
- Overhead: 10x anchor ceremonies = ~100K tokens of "re-centering tax"

**Long-lived single session:**
- 1 session, ~10 tasks x ~3K execution tokens = ~30K execution tokens
- BUT: context grows linearly. By task 10, the agent is carrying ~80-100K tokens of prior conversation
- 1-3 anchor ceremonies (every 30 actions) = ~15-40K tokens
- Total context consumption: ~120-170K tokens (growing window)
- Risk: degradation probability increases with each task

**Net cost difference:** Ephemeral costs ~20-30% more in raw token consumption due to repeated anchor/session-start overhead. However, ephemeral avoids the hidden cost of degradation-induced failures — each rule violation that triggers a learn cycle costs an additional ~10-15K tokens (fix + learn ceremony + re-execution).

### Failure Mode Cost

From kernel data: the 5 documented quick-anchor violation recurrences each required user intervention + `/kernel/learn` + fix + re-execution. Conservative estimate of failure cost per incident: ~15,000 tokens + user time. With 5 incidents across ~4 months of operation, the degradation-induced cost is non-trivial.

### Latency Considerations

- **Spawn latency:** Each `claude -p` invocation has cold-start overhead (~5-10 seconds for model initialization, API handshake, CLAUDE.md processing)
- **10-task pipeline:** ~50-100 seconds of spawn overhead vs near-zero for a long-lived session switching between tasks
- **Parallelism offset:** Ephemeral agents can run in parallel (spawn-agent-swarm). 10 agents spawned simultaneously complete in ~1 task duration, not 10x

## Failure Modes

### 1. Context Loss at Handoff

The primary risk: a one-shot agent completes a task but fails to capture critical context that the next agent needs. Current mitigation: per-agent workflow state with `completed_tasks`, but this is structural metadata (what was done), not semantic context (why this approach was chosen, what constraints were discovered).

### 2. Orchestrator Becoming the Long-Lived Bottleneck

If the orchestrator decomposes, dispatches, monitors, and synthesizes — it accumulates the same context-decay problems it was designed to avoid. The kernel's execute-pipeline parent is already this bottleneck: it runs session-start, anchor, task-builder, monitors run-task.sh, and validates results.

### 3. State Contention (Observed in Kernel)

Multiple concurrent one-shot agents writing to shared state files (`session_state.json`, `sr_dev_workflow.json`) caused visibility loss (agent 132 incident, 2026-06-14). Mitigation: per-agent state files (`agent-{N}-state.json`), but the shared `session_state.json` remains a single point of contention — as directly observed during this research task (4 concurrent research agents fighting over the same file).

### 4. Overhead Multiplication

For very small tasks (rename a variable, fix a typo), the anchor ceremony overhead (~14K tokens) dwarfs the actual work (~500 tokens). The one-shot model is optimal for medium-complexity tasks (write a file, run a test) where the ceremony is 30-50% of total cost, not 95%.

## Summary

The orchestrator-worker pattern is well-established in industry, with clear evidence that short contexts prevent attention decay. The kernel's run-task.sh already implements this pattern effectively. Cost overhead is real but offset by failure avoidance. The main open questions are orchestrator decay and state contention — both observed in the current kernel.
