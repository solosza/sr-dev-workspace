# Competitor Framework Analysis — Agent Swarms/Teams

## CrewAI
- **Architecture:** Role-based agent teams inspired by real-world org structures
- **Roles:** Agents assigned roles (researcher, writer, analyst) with task delegation
- **Delegation:** Intuitive task handoff between roles, lowest learning curve (~20 lines to start)
- **Memory:** Shared memory via crew-level context
- **Handoffs:** Role-based delegation — agents can delegate subtasks to other agents
- **Production readiness:** Medium — growing ecosystem, limited checkpointing
- **Strengths:** Fastest setup, cheapest token usage, natural role metaphor
- **Weakness:** Least flexible/controllable of the three

## AutoGen (Microsoft)
- **Architecture:** Conversational collaboration — agents talk to each other in GroupChat
- **Roles:** Agents defined by system prompts, participate in multi-turn conversations
- **Delegation:** GroupChat pattern — agents take turns, coordinator picks next speaker
- **Memory:** Accumulated conversation history (expensive — every turn = full LLM call with history)
- **Handoffs:** Conversation-driven — agents respond in sequence
- **Production readiness:** Medium — no-code Studio option, .NET support
- **Strengths:** Most natural for debate/review patterns, diverse chat patterns
- **Weakness:** Expensive for high-volume (4 agents × 5 rounds = 20+ LLM calls minimum), latency

## LangGraph
- **Architecture:** Graph-based workflow — agents are nodes in a directed graph with shared state
- **Roles:** Nodes in a state machine, each with defined inputs/outputs
- **Delegation:** Graph edges define control flow, conditional routing
- **Memory:** Shared state object passed between nodes, checkpointing, persistence
- **Handoffs:** Edge-based — explicit graph transitions, human-in-the-loop support
- **Production readiness:** Highest — LangSmith observability, checkpointing, streaming, durable execution
- **Strengths:** Best error handling, highest success rate, most control
- **Weakness:** Steepest learning curve, most complex setup

## OpenAI Swarm → Agents SDK
- **Architecture:** Lightweight routines + handoffs. Agent = instructions (system prompt) + functions (Python callables)
- **Roles:** Agents are stateless — each encapsulates instructions + tools
- **Delegation:** Explicit handoff functions — agent returns another agent to transfer control
- **Memory:** Stateless by design — context passed via function arguments, not persistent
- **Handoffs:** Function-based — `transfer_to_agent_x()` returns the target agent
- **Production readiness:** Swarm was experimental (replaced March 2026). Agents SDK is production-grade with Guardrails primitive
- **Strengths:** Simplest mental model, maximum clarity/observability, official OpenAI support
- **Weakness:** No built-in persistence, no complex orchestration patterns

## Comparison Matrix

| Feature | CrewAI | AutoGen | LangGraph | OpenAI Agents SDK |
|---------|--------|---------|-----------|-------------------|
| Mental model | Org chart | Group chat | State machine | Routines + handoffs |
| Learning curve | Low | Medium | High | Low |
| Control/flexibility | Low | Medium | High | Medium |
| Production readiness | Medium | Medium | High | High (2026) |
| Token efficiency | High | Low | Medium | High |
| Governance/constraints | None built-in | None built-in | Conditional edges | Guardrails primitive |
| Persistence | Limited | Via conversation | Checkpointing | None (stateless) |
| Self-extension | No | No | No | No |

## Key Insight
None of these frameworks have built-in governance (hook-based enforcement), self-extension (agents creating new agent types), or protocol-driven development. They're all orchestration layers — they coordinate agents but don't constrain or improve them.
