# Harness Design Pattern Applicability to Pulsia-Scale Autonomous Operations

## Assessment Summary

The harness design pattern — specification-first, agent-driven orchestration via composable loops — provides a strong architectural foundation for Pulsia-like autonomous operations. The core primitives (commands, skills, steps, gate contracts, state files) map naturally to Pulsia's layered agent structure. However, Pulsia operates at a scale and with operational patterns that require several significant extensions to the current harness model. This document assesses the fit, identifies gaps, and proposes concrete solutions.

---

## Pattern Strengths That Map to Pulsia

### 1. Specification-Driven Agent Orchestration

The harness principle that "the harness IS the specification, the agent IS the runtime" directly mirrors Pulsia's architecture. Pulsia's CEO agent reads business state and delegates to specialized agents — this is functionally identical to an orchestrator loop reading a command specification and calling skills sequentially. Both systems treat the agent as an interpreter of structured instructions rather than as hardcoded logic.

### 2. Loop Composition Matches Agent Hierarchy

Pulsia's three-tier structure (CEO → Task System → Specialized Agents) maps cleanly to harness loop types:

| Pulsia Layer | Harness Equivalent |
|-------------|-------------------|
| CEO Agent | Orchestrator loop (coordinates skills sequentially) |
| Task System | Command → Skill routing with gate contracts |
| Specialized Agents | Primitive loops (self-contained, composable, non-blocking) |

The harness composability model — orchestrators calling primitive loops with non-blocking returns — directly supports Pulsia's pattern of the CEO agent delegating to Engineering, Marketing, and Support agents that execute independently.

### 3. Gate Contracts Enable Task Isolation

Pulsia enforces strict task isolation: an engineering agent cannot make marketing decisions, a support agent cannot deploy code. The harness gate contract system (JSON schemas validated at every step boundary) provides exactly this mechanism. Input gates ensure an agent receives only data it should act on; output gates validate that results conform to expected structure before handoff.

### 4. Autonomous Execution Without Pauses

Both systems share the "action before permission" philosophy. Harness specifications run autonomously without user confirmation. Pulsia's nightly cycle operates identically — the CEO agent acts and reports, never blocks waiting for approval. The harness anti-pattern of pausing for user input is already a documented violation.

### 5. Defense-in-Depth Enforcement

Pulsia's cross-company guardrail updates (errors caught in one company update rules for all) parallel the harness two-tier enforcement model. Soft gates (protocol, lessons) guide behavior; hard gates (hooks) block violations mechanically. The lesson-learning loop (`/kernel/learn` after failures) is a single-tenant version of Pulsia's hive mind error propagation.

---

## Required Pattern Extensions

### Extension 1: Multi-Tenant State Isolation

**Gap:** The harness manages state for a single agent session — one `session_state.json`, one `workflow.json`. Pulsia manages 5,900+ company instances simultaneously, each with independent state, memory, and context.

**Proposed Solution:** Introduce a **tenant-scoped state layer** that namespaces all state files by company ID. The harness architecture already separates state into session, workflow, and phase levels (Layer 6). Extending this with a tenant prefix (`state/{tenant_id}/session_state.json`) preserves the existing state management pattern while enabling multi-tenant isolation. Each CEO agent instance reads only its tenant's state directory. A tenant registry file maps company IDs to their state paths and configuration.

### Extension 2: Scheduled Execution Engine (Cron Loops)

**Gap:** Harness loops are invocation-triggered — a user or orchestrator calls a command, and it executes. Pulsia's nightly CEO cycle is schedule-triggered — it wakes up autonomously at a configured time without any invocation.

**Proposed Solution:** Introduce a **cron loop** type alongside orchestrator and primitive loops. A cron loop specification includes a schedule expression, a trigger condition (e.g., "run if last_execution > 24h"), and an entry command. The execution engine reads cron loop specs at startup and invokes them on schedule. This preserves the "specification is the harness" principle — the schedule is declared in markdown, not in code. Implementation would use a lightweight scheduler process that reads cron loop specs and invokes the corresponding harness command at the specified time.

### Extension 3: Cross-Tenant Knowledge Sharing (Hive Mind)

**Gap:** Harness lessons are local — recorded in `.claude/lessons/lessons.md` within a single workspace. Pulsia's hive mind shares discoveries across 8,000+ companies: a successful marketing strategy found by one company's agent is anonymized and propagated to all marketing agents platform-wide.

**Proposed Solution:** Introduce a **shared lessons layer** that operates above tenant-scoped lessons. Each agent writes discoveries to a local `lessons.md` as usual. A separate aggregation loop periodically scans tenant lessons, anonymizes company-specific details, extracts generalizable patterns, and appends them to a global `shared-lessons.md` that all agents read during anchor. Gate contracts ensure anonymization before promotion — no company names, no specific revenue figures, no customer data. The existing anchor mechanism (re-read lessons every N actions) naturally picks up new shared lessons without architectural changes.

### Extension 4: Cost-Aware Gate Contracts

**Gap:** Harness gate contracts validate data correctness (field presence, type, format) but not operational cost. Pulsia faces $1.5M/month API bills and uses per-agent tool limitations specifically to control costs. The CEO agent assigns tasks to specialized agents "mostly from a cost perspective."

**Proposed Solution:** Add a **cost dimension** to gate contracts. Each skill specification declares an estimated token budget. Input gates include a `max_cost` field; the agent checks remaining budget before executing. If a step would exceed budget, the gate blocks execution and escalates to a higher-level loop for reallocation. This mirrors Pulsia's approach of limiting each agent's available tools — but enforced structurally through gates rather than through hardcoded tool restrictions.

### Extension 5: Infrastructure Provisioning Loops

**Gap:** Harness loops operate within an existing environment — they read files, call tools, and produce deliverables. Pulsia automatically provisions per-company infrastructure (Render, Neon, GitHub, Stripe, Meta, AgentMail) as part of onboarding.

**Proposed Solution:** Create **provisioning primitive loops** — self-contained loops that call infrastructure APIs to create resources. For example, a `provision-company` orchestrator loop would call primitive loops for each service: `create-render-instance`, `create-neon-database`, `create-github-repo`, `configure-stripe`, etc. Each primitive loop has its own gate contract (input: company config, output: provisioned resource URL + credentials). The credential outputs are stored in tenant-scoped state files, never in shared state. This fits naturally within the existing loop composition model — provisioning is just another orchestrator calling primitive loops.

---

## Architectural Alignment Summary

| Pulsia Capability | Harness Support | Extension Needed |
|------------------|----------------|-----------------|
| Multi-agent delegation | Orchestrator → primitive loop composition | None |
| Task isolation | Gate contracts at step boundaries | None |
| Autonomous execution | Built-in (no-pause philosophy) | None |
| Defense-in-depth | Soft gates + hard gates (hooks) | None |
| Specification-driven | Core principle (markdown specs) | None |
| Multi-tenant state | Single-tenant only | Tenant-scoped state layer |
| Scheduled execution | Invocation-triggered only | Cron loop type |
| Cross-company learning | Local lessons only | Shared lessons aggregation |
| Cost control | No cost awareness | Cost-aware gate contracts |
| Infrastructure provisioning | No provisioning loops | Provisioning primitive loops |

---

## Conclusion

The harness design pattern provides approximately 60% of the architectural surface area needed for Pulsia-scale operations out of the box. The core execution model (specification → agent → autonomous execution → state persistence) is architecturally identical to how Pulsia's agents operate. The five extensions identified above address the gaps between single-session orchestration and multi-tenant platform operations. Crucially, all five extensions follow the harness's own design principles — they are specification-driven (declared in markdown), gate-validated (JSON schemas at boundaries), and composable (new loop types that plug into existing orchestration flows). The harness pattern does not need to be replaced or fundamentally redesigned to support Pulsia-scale autonomy — it needs to be extended along its own grain.

---

## Sources

- Harness Design Pattern documentation (`docs/harness-design-pattern/`)
- Pulsia architecture analysis (`projects/pulsia-research/02-architecture.md`)
- Pulsia company overview (`projects/pulsia-research/01-company-overview.md`)
