# Industry Survey — Orchestrator-Worker Patterns for AI Agent Systems

Research for backlog 230, task 002. Sourced survey of when single-responsibility subagents win vs when inline execution wins.

---

## 1. Anthropic's Multi-Agent Guidance

Anthropic's ["Building Effective Agents"](https://resources.anthropic.com/building-effective-ai-agents) framework defines five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. The orchestrator-workers pattern is described as: a central LLM decomposes tasks at runtime and dispatches dynamic subtasks to worker LLMs. Key distinction from parallelization: subtasks aren't pre-defined but determined by the orchestrator based on specific input.

Anthropic's core recommendation: **find the simplest solution possible and only increase complexity when needed.** Workflows (predefined control flow) offer lower cost/latency with high predictability. Agents (model-driven control flow) offer higher cost/latency with lower predictability. The tradeoff is explicit — agentic systems trade latency and cost for better task performance on complex, flexible tasks.

Anthropic shipped recursive subagent spawning in Claude Code (skills in October 2025, Agent Teams in February 2026). Agent Teams use a flat topology — multiple Claude instances coordinate through shared state without a single orchestrator. The [multi-agent coordination patterns](https://claude.com/blog/multi-agent-coordination-patterns) blog identifies five coordination patterns with distinct failure modes:

| Pattern | Failure Mode |
|---------|-------------|
| Generator-Verifier | Verifiers without explicit criteria become rubber-stamps |
| Orchestrator-Subagent | Orchestrator becomes information bottleneck; sequential execution limits throughput |
| Agent Teams | Independent work creates coordination blindness; shared resources cause conflicts |
| Message Bus | Silent routing failures; difficult cascade tracing |
| Shared State | Agents duplicate work or contradict each other; reactive loops consume tokens |

**Source:** [Anthropic Building Effective Agents](https://resources.anthropic.com/building-effective-ai-agents), [Multi-Agent Coordination Patterns](https://claude.com/blog/multi-agent-coordination-patterns)

---

## 2. LangGraph Supervisor / Orchestrator-Worker Pattern

LangGraph's [supervisor pattern](https://reference.langchain.com/python/langgraph-supervisor) uses a central orchestration agent that routes tasks to specialist workers via structured output. The [Send API](https://docs.langchain.com/oss/python/langgraph/workflows-agents) enables dynamic worker node creation with per-worker state that writes to a shared state key accessible by the orchestrator.

Decision criteria from LangGraph practitioners:
- **Use supervisor when:** agent has 10+ tools, tasks require multi-domain collaboration, or debugging single-agent becomes difficult
- **Cost:** roughly 3x the cost of a single mega-agent for an 18-point lift in success rate
- **Optimization:** swapping the supervisor (not workers) to a smaller model drops total cost ~35% with ~4 percentage points of routing accuracy lost
- **Recursion limit:** default to 25 for 4-specialist teams, 40 for hierarchical setups; hitting the limit >1% of runs indicates a looping bug

LangGraph dominates production multi-agent deployments at ~38% market share, with custom orchestration at ~28%. Framework choice is cited as "fourth at best" behind model selection, evaluation infrastructure, and human-checkpoint design.

**Source:** [LangGraph Supervisor Reference](https://reference.langchain.com/python/langgraph-supervisor), [LangGraph Workflows & Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Multi-Agent Orchestration Frameworks 2026](https://presenc.ai/research/multi-agent-orchestration-frameworks-2026)

---

## 3. OpenAI Swarm / Agents SDK

OpenAI's [Swarm framework](https://www.morphllm.com/openai-swarm) (October 2024, now archived) reduced multi-agent coordination to a single primitive: **handoff**. Each agent executes within its own context until it determines another agent is better suited, then transfers control via tool-call return. No central coordinator — execution path emerges from handoff decisions.

Key constraints: stateless (each `run()` starts from scratch), no session state between calls, explicitly experimental, no production observability. The [Agents SDK](https://presenc.ai/research/multi-agent-orchestration-frameworks-2026) (March 2025) is the production successor with the same conceptual model but production-grade error handling and tracing.

The handoff-only model is the simplest multi-agent primitive — no orchestrator overhead, no state management complexity. But it lacks the decomposition and synthesis capabilities of orchestrator-worker patterns. Best fit: narrow routing scenarios (customer service triage, specialist escalation).

**Source:** [OpenAI Swarm Guide](https://www.morphllm.com/openai-swarm), [Agent Orchestration Frameworks 2026](https://presenc.ai/research/multi-agent-orchestration-frameworks-2026)

---

## 4. Production Failure Modes

### 4a. Cost Compounding

[Augment Code's analysis](https://www.augmentcode.com/guides/multi-agent-cost-compounding) quantifies the cost multiplication:

| Configuration | Token Multiplier |
|--------------|-----------------|
| Single agent vs chat | 4x |
| Multi-agent research vs chat | 15x |
| Tool-schema overhead per agent | 10,000–60,000 tokens (60–80% of static toolsets) |
| 3-agent pipeline vs single agent | 29,000 vs 10,000 tokens |
| Cascade failure (hub retry) | 2–3x multiplier on baseline |

Cost at scale: workflows costing $0.50 in testing can hit $50,000/month at 100K executions because the orchestrator makes multiple LLM calls for decomposition and aggregation on top of every worker call. Adding a 6th or 7th specialist often incurs more coordination overhead than the specialization saves. Mesh architectures scale poorly: 10 agents create 45 communication channels vs a 5-agent mesh's 10.

**Source:** [Multi-Agent Cost Compounding](https://www.augmentcode.com/guides/multi-agent-cost-compounding)

### 4b. Coordination Overhead

[Getmaxim's reliability analysis](https://www.getmaxim.ai/articles/multi-agent-system-reliability-failure-patterns-root-causes-and-production-validation-strategies/) identifies three failure categories:

1. **State synchronization failures** — stale state propagation, race conditions from concurrent modifications, partial state visibility (information silos)
2. **Communication protocol breakdowns** — message ordering violations, timeout/retry ambiguity causing duplicates, schema evolution incompatibility
3. **Coordination overhead saturation** — each inter-agent handoff adds 100–500ms; 10 handoffs total 1–5 seconds; context reconstruction multiplies tokens across agents

Error amplification rates by architecture:
- Centralized orchestrator: 4.4x
- Hybrid: 7.8x (estimated from token overhead)
- Independent agents: 17.2x

**Source:** [Multi-Agent System Reliability](https://www.getmaxim.ai/articles/multi-agent-system-reliability-failure-patterns-root-causes-and-production-validation-strategies/)

### 4c. Production Failure Taxonomy

The [MAST taxonomy](https://www.augmentcode.com/guides/multi-agent-orchestration-architecture-guide) across 1,642 annotated execution traces reports failure rates of 41–86.7%, with dominant categories:
- System design issues: 44.2%
- Inter-agent misalignment: 32.3%
- Coordination failures: 36.94% of all failures

Five named failure modes with recovery patterns:

| Failure Mode | Root Cause | Recovery |
|-------------|-----------|----------|
| Error cascading | Upstream deviations consumed as valid | Schema validation gates at handoffs |
| Infinite loops | Feedback loops or tool-call spinning | Two-level turn caps + boolean exit gates |
| Context drift | Information loss over long sessions | Living specs as correctness anchor |
| Verifier false passes | Agreement bias in reviewing agents | Independent dual-agent verification |
| Parallel write conflicts | Uncoordinated simultaneous modifications | One-writer-per-module rule (isolated worktrees) |

**Source:** [Multi-Agent Orchestration Architecture Guide](https://www.augmentcode.com/guides/multi-agent-orchestration-architecture-guide), [6 Multi-Agent Orchestration Patterns](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)

---

## 5. The Single-Agent Counterargument

Princeton NLP found that a single agent **matched or outperformed multi-agent systems on 64% of benchmarked tasks** when given the same tools and context. Multi-agent adds only 2.1 percentage points of accuracy at roughly double the cost.

A [2025 study on multi-hop reasoning](https://arxiv.org/abs/2604.02460) (Qwen3, DeepSeek, Gemini 2.5) confirmed: single agents consistently match or exceed multi-agent performance when compute budgets are equalized.

Google Research found that on tasks requiring **strict sequential reasoning**, every multi-agent variant tested degraded performance by 39–70% because communication fragmented the reasoning process.

Quantified decision thresholds from a [synthesis study](https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d):
- **Capability saturation:** coordination yields diminishing returns once single-agent baselines exceed ~45% on the target benchmark
- **Token overhead:** centralized orchestrator adds 285% tokens; hybrid adds 515%
- **Minimum volume for ROI:** ~50,000 queries/month
- **Tasks with 2–4 tools:** insufficient parallelization opportunity to justify coordination

**Source:** [Single-Agent vs Multi-Agent](https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d), [Single-Agent LLMs Outperform Multi-Agent](https://arxiv.org/abs/2604.02460), [6 Orchestration Patterns](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)

---

## 6. Decision Criteria the Field Converges On

Across all sources, the field converges on five decision dimensions:

### 6a. Task Independence

The decisive test: **can subtasks proceed without tightly sharing mutable state?** Breadth-first research (many independent paths) is a good fit. Tightly interdependent work (one coherent codebase) is not.

### 6b. Context-Budget Pressure

When a task's full context exceeds one agent's window, decomposition is forced. But each sub-agent then reconstructs partial context from shared state, consuming tokens and adding latency. The tradeoff: context overflow in one agent vs context reconstruction overhead in many.

### 6c. Parallelism Value

Multi-agent provides wall-clock speedup only when subtasks are genuinely independent. Fan-out/fan-in patterns require 4+ independent tasks to justify the overhead. Sequential dependencies negate parallelism benefits entirely.

### 6d. Verification Needs

Generator-verifier and multi-agent debate patterns improve output quality when accuracy matters more than speed. Centralized verification contains error amplification to 4.4x vs 17.2x for independent agents. But verification agents without explicit criteria become rubber-stamps.

### 6e. State Isolation

Per-agent state isolation is a prerequisite for reliable multi-agent execution. Without it: shared mutable state causes visibility loss, write conflicts, and cascading failures. With it (per-agent state files, worktree isolation): concurrent agents can work reliably.

---

## 7. When-To / When-Not Table

| Criterion | Use Multi-Agent (Orchestrator-Worker) | Stay Single-Agent (Inline) |
|-----------|--------------------------------------|---------------------------|
| **Task structure** | Decomposes into 4+ independent subtasks | Sequential dependencies; each step needs prior output |
| **Context window** | Full context exceeds single agent's capacity | Task fits within one context window |
| **Wall-clock pressure** | Parallel execution provides meaningful speedup | Sequential is fast enough; latency budget is tight |
| **Quality requirements** | Benefits from independent verification/debate | Single-pass quality is sufficient |
| **State coupling** | Subtasks have isolated state; no shared mutable data | Subtasks share mutable state; tight coordination needed |
| **Tool count** | 10+ tools benefit from specialist routing | 2–4 tools; insufficient parallelization opportunity |
| **Error tolerance** | Can tolerate 4.4x error amplification (centralized) | Errors cascade; can't afford 2–3x retry multiplier |
| **Cost sensitivity** | Business value justifies 3–15x token multiplication | Cost ceiling is low; single-agent is already optimized |
| **Task type** | Research, auditing, testing, code review (breadth-first) | Reasoning chains, design, context-dependent writing |
| **Infrastructure** | Per-agent state isolation exists; observability in place | No isolation infrastructure; debugging is manual |
| **Existing baseline** | Single-agent baseline has plateaued below ~45% | Single-agent already performs above ~45% |
| **Volume** | ≥50K queries/month for economies of scale | Low volume; coordination overhead not amortized |

### The Four-Part Decision Rule

Adopt multi-agent orchestration only when ALL four conditions hold:
1. The task decomposes into semi-independent subproblems
2. The synthesis step adds value rather than overhead
3. The single-agent baseline is already well-optimized and has plateaued
4. The incremental business gain exceeds the full coordination, governance, and infrastructure cost

---

## Sources

1. [Anthropic — Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
2. [Anthropic — Multi-Agent Coordination Patterns](https://claude.com/blog/multi-agent-coordination-patterns)
3. [LangGraph — Supervisor Reference](https://reference.langchain.com/python/langgraph-supervisor)
4. [LangGraph — Workflows & Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
5. [Multi-Agent Orchestration Frameworks 2026](https://presenc.ai/research/multi-agent-orchestration-frameworks-2026)
6. [OpenAI Swarm Guide](https://www.morphllm.com/openai-swarm)
7. [Multi-Agent Cost Compounding](https://www.augmentcode.com/guides/multi-agent-cost-compounding)
8. [Multi-Agent Orchestration Architecture Guide](https://www.augmentcode.com/guides/multi-agent-orchestration-architecture-guide)
9. [Multi-Agent System Reliability](https://www.getmaxim.ai/articles/multi-agent-system-reliability-failure-patterns-root-causes-and-production-validation-strategies/)
10. [6 Multi-Agent Orchestration Patterns for Production](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
11. [Single-Agent vs Multi-Agent Systems](https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d)
12. [Single-Agent LLMs Outperform Multi-Agent on Multi-Hop Reasoning](https://arxiv.org/abs/2604.02460)
