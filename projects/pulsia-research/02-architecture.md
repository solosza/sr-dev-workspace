# Pulsia (Polsia) — Operational Architecture Analysis

## Multi-Agent System Structure

Pulsia employs a layered multi-agent architecture with three structural tiers:

1. **Chat Agent (CEO Layer)** — The strategic decision-maker and primary user interface. Powered by Claude Opus 4.6 (Anthropic's most advanced reasoning model), this agent functions as an AI CEO that evaluates business state, prioritizes actions, and delegates work to specialized agents. Each user company gets a dedicated CEO agent instance.

2. **Task System (Orchestration Layer)** — Translates high-level strategic decisions into discrete, actionable work units. The task system manages sequencing, dependency resolution, and handoff between specialized agents. Tasks flow through structured pipelines — for example, a bug-fix pipeline follows PM triage → Engineering fix → QA verification → Deploy, with each agent passing structured reports to the next.

3. **Specialized Agents (Execution Layer)** — Domain-specific agents execute the actual work:

| Agent Role | Function |
|-----------|----------|
| Engineering Agent | Code development, bug fixes, deployments |
| Marketing Agent | Twitter content, outreach campaigns |
| Ads Agent | Meta campaigns across 15+ countries, UGC video generation (via Sora 2) |
| Support Agent | Customer email responses, ticket triage |
| PM Agent | Bug/feature request triage, prioritization |
| QA Agent | Test execution, verification |
| Deploy Agent | Production deployments |

This separation serves both functional and cost-control purposes. The founder noted that the chat agent assigns tasks to specialized agents "mostly from a cost perspective" — preventing runaway API consumption by limiting each agent's available tools and defining explicit task boundaries.

---

## The Nightly Autonomous Execution Cycle

The core operational primitive is the **nightly CEO cycle** — the mechanism that distinguishes Pulsia from reactive AI tools. The cycle operates as follows:

**Trigger:** Every night, the CEO agent instance for each active company (2,000+ as of June 2026) wakes up autonomously.

**State Assessment:** The CEO agent evaluates the current state of the business across multiple dimensions:
- Are there active bugs or technical issues?
- How is revenue performing? Are there paying customers?
- What is the customer acquisition pipeline status?
- Are there pending user messages or direction changes?
- What competitive or market signals exist?

**Decision Making:** Based on this assessment, the CEO agent determines the highest-leverage action to take. This is not a simple priority queue — the agent applies strategic reasoning to weigh competing priorities (e.g., fixing a critical bug vs. launching a new marketing campaign vs. responding to customer feedback).

**Task Delegation & Execution:** The CEO agent creates tasks and delegates them to the appropriate specialized agents. Those agents execute independently within their domain boundaries.

**Reporting:** After execution, the system sends a structured morning email to the user summarizing:
- Actions taken overnight
- Results and metrics
- Plans for the next cycle
- Any decisions requiring user input

**Continuity:** If the user doesn't respond, the system continues operating the next night using its own judgment. The founder described this as: "If you forget about prompting it, it's going to wake up at night, do work and send you an update in the morning."

---

## Task Execution Patterns and Decision Trees

Task execution follows structured pipelines with agent-to-agent handoff. The platform completed **25,444 tasks and exchanged 16,325 messages** across active companies in a single monitored day, demonstrating significant operational throughput.

**Pipeline Coordination:** Rather than operating independently, agents function within structured pipelines. Each pipeline defines the sequence of agents involved, the handoff protocol (structured reports), and the success/failure criteria for each stage.

**Task Isolation:** Each task is scoped to a specific agent with limited tool access. This prevents agents from exceeding their authority and controls API costs. The task system enforces boundaries — an engineering agent cannot make marketing decisions, and a support agent cannot deploy code.

**On-Demand vs. Scheduled Execution:** The pricing model reveals two execution modes:
- **Nightly autonomous tasks** — the CEO cycle runs one strategic task per night (included in $49/month base)
- **On-demand credits** — users can request immediate task execution (5 credits/month included, 10 bonus credits first month)

---

## Feedback Loops and Error Recovery

### Cross-Company Learning ("Hive Mind")

Pulsia's most architecturally distinctive feature is its **cross-company knowledge sharing system**. When an agent discovers a successful strategy — for example, that emojis in email subject lines increase reply rates — it anonymously saves that finding to a **shared memory file**. Every agent of the same type across the entire platform (8,000+ companies) benefits from this discovery.

This creates a compounding intelligence effect: the more companies run on Pulsia, the smarter all agents become. The founder described this as "hive mind learning" — errors caught in one company instantly update guardrails across all companies.

### Agent-Initiated Feedback

An unusual feedback mechanism exists where agents can request infrastructure improvements. In one documented case, the cold outreach agent identified the need for a professional email database and "asked for the tool it needed to do its job better." This represents a bottom-up feedback loop where execution agents surface capability gaps to the platform.

### Memory and Consistency

Agents maintain persistent context through:
- **Company-specific background information** — business model, target audience, brand voice
- **Historical decision records** — what was tried, what worked, what failed
- **User personality/preferences** — communication style, risk tolerance, strategic priorities
- **Shared memory threads** — agents within a company share memory via MCP integrations so context is not lost between handoffs

### Error Recovery Gaps

Specific error recovery mechanisms are not publicly documented. The platform likely relies on:
- Task-level retry logic within each agent
- QA agent verification before deployment
- The nightly cycle as a natural recovery point (failures get re-evaluated the next night)
- Cross-company guardrail updates to prevent error recurrence across the platform

However, detailed state rollback, transaction safety, or formal error escalation protocols have not been disclosed.

---

## Scaling Approach and Infrastructure

### Per-Company Infrastructure Provisioning

Each user company receives automatically provisioned infrastructure:

| Component | Provider | Purpose |
|-----------|----------|---------|
| Web server | Render | Application hosting |
| Database | Neon | Agent-friendly, cost-effective data management |
| Email | AgentMail | Outbound/inbound email operations |
| Payments | Stripe | Payment processing integration |
| Code repository | GitHub | Source code management |
| Ad accounts | Meta | Advertising campaign management |
| Sandbox | Blackcell | Isolated execution environment |
| Browser automation | Anchor Browser | Web interaction capabilities |

This automated provisioning eliminates manual onboarding friction — users go from "idea" to "live infrastructure" without wiring technical services.

### Platform-Level Scaling

- **Model infrastructure:** Three Anthropic Max subscriptions (~$600/month) plus one Codex Max subscription (~$200/month) — approximately $800/month total operational cost for managing 5,900+ companies
- **LLM-agnostic design:** The infrastructure is designed to reduce dependence on a single model provider, suggesting abstraction layers that allow model swapping
- **Cost challenge:** The founder reported $1.5M in API bills in a single month at scale, driving investment in GPU infrastructure buildout and cheaper model tiers
- **MCP integrations:** Agents access live data and external tools through Model Context Protocol integrations, maintaining context across tasks and companies
- **Multi-tenant architecture:** Centralized learning and safety systems operate across the full tenant base, with anonymized knowledge sharing

### Human-in-the-Loop Patterns

Pulsia's HITL model is deliberately minimal — "action before permission" is the default:
- **Email summaries** — the primary engagement mechanism; users receive morning reports of overnight actions
- **Dashboard** — real-time visibility into company operations and agent decisions
- **Chat interface** — users can message their AI CEO directly (~15 messages/day average across platform)
- **Direction changes** — users can redirect strategy through email replies or dashboard messages
- **No blocking approval** — the system does not wait for user confirmation before acting; it acts and reports

This positions the user as a "strategic investor" rather than an "operational manager" — providing guidance but not blocking execution.

---

## Sources

- [Tim Frin — How Polsia Builds and Runs Companies with AI Agents](https://timfrin.substack.com/p/how-polsia-builds-and-runs-companies)
- [Henry the 9th — How a Solo Founder Cloned Himself With AI](https://henrythe9th.substack.com/p/how-a-solo-founder-cloned-himself)
- [Context Studios — Polsia: How a Solo Founder Hit $1M ARR in 30 Days](https://www.contextstudios.ai/blog/polsia-how-a-solo-founder-hit-1m-arr-in-30-days-with-ai-agents)
- [Andrew.ooo — Polsia: Solo Founder Hits $1.5M ARR in 30 Days](https://andrew.ooo/posts/polsia-1m-arr-30-days-zero-employees/)
- [Summify — Polsia: 0 to 1M ARR in 1 Month](https://summify.io/discover/polsia-solo-founder-tiny-team-from-0-to-1m-arr-in-1-month-the-future-of-self-run)
- [Toolify — Polsia Overview](https://www.toolify.ai/tool/polsia)
