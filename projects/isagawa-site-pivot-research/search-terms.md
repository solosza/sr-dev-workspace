# Search Terms & Discoverability Research

**Date:** 2026-06-23
**Purpose:** Identify what developers actually search for when looking for agent governance, loop-based frameworks, and orchestration tools. Inform Isagawa Kernel positioning and GitHub discoverability.

---

## 1. Common Search Queries (What Developers Search)

### High-Volume Terms (established category)
- "ai agent framework"
- "multi-agent framework"
- "agent orchestration framework"
- "best ai agent framework 2026"
- "LangGraph vs CrewAI vs AutoGen"
- "agentic ai framework"
- "open source agent framework"

### Medium-Volume Terms (growing category)
- "loop engineering"
- "agent loop architecture"
- "agentic loop"
- "harness engineering"
- "agent runtime"
- "agent guardrails"
- "agent governance framework"
- "spec-driven development"

### Emerging Terms (June 2026 breakout)
- "loop engineering ai agents"
- "harness engineering ai"
- "agent harness"
- "context engineering"
- "agent memory systems"
- "agent evaluation harness"

### Job-Adjacent Terms (what hiring managers search)
- "agent infrastructure engineer"
- "agentic ai engineer"
- "ai agent architect"
- "multi-agent orchestration"
- "agent eval pipeline"

---

## 2. GitHub Topic Tags

### Tags Used by Top Frameworks

| Framework | GitHub Topics |
|-----------|-------------|
| LangGraph | `langgraph`, `ai-agents`, `agent-framework`, `multi-agent`, `llm` |
| CrewAI | `crewai`, `ai-agents`, `multi-agent`, `agent-orchestration`, `agentic-workflow` |
| AutoGen | `autogen`, `multi-agent`, `agent-framework`, `conversational-ai` |
| OpenAI Agents SDK | `openai`, `agents`, `multi-agent`, `guardrails`, `tracing` |
| awesome-harness-engineering | `mcp`, `ai-agents`, `agent-orchestration`, `agent-memory`, `context-engineering`, `agent-harness`, `harness-engineering` |

### Recommended Tags for Isagawa Kernel (ordered by discoverability)

**Tier 1 — High traffic, direct match:**
- `ai-agents`
- `agent-framework`
- `agent-orchestration`
- `agentic-ai`

**Tier 2 — Category-defining, growing:**
- `loop-engineering`
- `harness-engineering`
- `agent-harness`
- `agent-governance`
- `agent-runtime`

**Tier 3 — Niche but accurate:**
- `spec-driven-development`
- `agent-loop`
- `self-improving-agent`
- `claude-code`
- `mcp`
- `context-engineering`

---

## 3. Job Posting Language (Cross-Reference)

### Terminology from Major Companies

| Company | Role Title | Key Terms Used |
|---------|-----------|---------------|
| Google | Software Engineer, Agentic AI Infrastructure | "agent infrastructure", "autonomous agents", "orchestrate", "skills for LLMs", "domain knowledge" |
| OpenAI | Agent Infrastructure Engineer | "agent infrastructure", "tool calling", "multi-agent", "evaluation harnesses" |
| Anthropic | Various | "loop engineering", "harness", "agent loop", "tool use" |
| Scale AI | AI Infrastructure Engineer | "agent evaluation", "agent orchestration", "autonomous systems" |
| Enterprise (Deloitte, EY, Accenture) | Agentic AI Engineer | "agent loops", "sub-agent orchestration", "memory", "eval pipelines", "observability" |

### Most-Used Terms in Job Postings (280% YoY growth, ~90K US postings)
1. "agentic AI" — dominant umbrella term
2. "agent orchestration" — architectural layer
3. "agent infrastructure" — systems/platform layer
4. "multi-agent systems" — academic/research crossover
5. "evaluation harness" — testing/quality layer
6. "autonomous agents" — capability description
7. "tool calling" / "function calling" — implementation detail
8. "agent loops" — execution pattern

### Salary Signal (validates market demand)
- Agentic AI Engineer: $185K-$320K base + $40K-$120K equity
- 8 new job titles that didn't exist 3 years ago

---

## 4. Discoverability Gap Analysis

### "Spec-driven loop engineering" — VERDICT: Too Niche (but components are searchable)

| Term | Searchability | Notes |
|------|--------------|-------|
| "spec-driven loop engineering" | Very low | Compound term nobody searches for as a unit |
| "spec-driven development" | Medium-high | Has its own DeepLearning.AI course, GitHub blog coverage, 30+ framework map on Medium |
| "loop engineering" | High (breakout June 2026) | 6.5M views on the viral post. Addy Osmani, Boris Cherny (head of Claude Code) actively using this term |
| "agent governance framework" | Medium | Microsoft released "Agent Governance Toolkit" (April 2026). OWASP, NIST, Singapore IMDA all publishing in this space |
| "agent runtime" | Medium | Used by TrueFoundry, Amazon Bedrock AgentCore. Enterprise-oriented |
| "agent harness" | Medium-high | GitHub topic exists. awesome-harness-engineering repo (968 stars). AWS Bedrock calls their product "AgentCore harness" |

### Positioning Recommendations

**Best positioning terms (high search volume + accurate):**
1. **"Agent governance framework"** — differentiates from pure orchestration (LangGraph territory), aligns with Microsoft's Governance Toolkit framing, matches enterprise security/compliance buyer intent
2. **"Loop engineering framework"** — rides the June 2026 viral wave, accurately describes what the Kernel does (designs the loop that prompts agents)
3. **"Agent harness"** — AWS is using this term for Bedrock AgentCore, awesome-list exists, describes the scaffolding layer

**Terms to AVOID as primary positioning:**
- "Agent orchestration framework" — oversaturated, puts you in direct comparison with LangGraph/CrewAI/AutoGen
- "Multi-agent framework" — implies agent-to-agent communication, which isn't the Kernel's core value
- "Spec-driven loop engineering" — nobody searches for this compound phrase

**Recommended tagline formula:**
> "[Searchable category] for [differentiated value]"

Examples:
- "Agent governance framework for self-improving loops"
- "Loop engineering toolkit — spec-driven agent harnesses"
- "The agent harness that governs itself"

---

## 5. "Loop" as Search Term

### Verdict: YES — Developers Search for Loops (as of June 2026)

**Evidence:**
- "Loop engineering" went viral June 7, 2026 (Peter Steinberger / OpenClaw). 6.5M views in days.
- Oracle Developer Blog: "What Is the AI Agent Loop?" — dedicated explainer
- Data Science Dojo: "Agentic Loops: From ReAct to Loop Engineering (2026 Guide)"
- TechTalks (June 22, 2026): "Demystifying loop engineering"
- MindStudio: "What Is Loop Engineering?"
- Codersarts, Tosea.ai, Lushbinary all published loop engineering guides in June 2026
- TrueFoundry: "Loop Engineering at Enterprise Grade"
- Boris Cherny (Anthropic, head of Claude Code): "I don't write the prompt anymore... I'm talking to that new Claude that is kind of coordinating"

**Key Insight:** The shift is from "prompting your agent" to "designing the system that prompts your agent." This is EXACTLY what Isagawa Kernel does. The market language has caught up to the product.

### Search Terms People Actually Use:
- "loop engineering" (dominant)
- "agent loop" (architectural concept)
- "agentic loop" (pattern name)
- "AI agent loop architecture" (how-to searchers)
- "loop engineering vs prompt engineering" (comparison searchers)
- "how to build agent loop" (tutorial searchers)

### The Five-Block Loop Architecture (industry consensus per Addy Osmani):
1. Goal/trigger
2. Planning/reasoning
3. Tool execution
4. Verification/feedback
5. Memory/state persistence

Isagawa Kernel maps cleanly: session-start (trigger) -> anchor (planning/reasoning) -> WORK (tool execution) -> complete (verification) -> lessons (memory/persistence).

---

## 6. Competitive Landscape Summary

### Where Isagawa Kernel Fits

| Layer | Competitors | Isagawa Kernel Position |
|-------|-------------|------------------------|
| **Agent Orchestration** (multi-agent routing) | LangGraph, CrewAI, AutoGen, Google ADK | NOT competing here |
| **Agent Runtime** (single-agent execution) | OpenAI Agents SDK, Amazon Bedrock AgentCore | Adjacent — Kernel is the governance layer ON TOP of runtimes |
| **Agent Governance** (guardrails, compliance, audit) | Microsoft Agent Governance Toolkit, Superagent, AgentGuard | DIRECT competitor space |
| **Loop/Harness Engineering** (scaffolding design) | No dominant open-source player yet | OPPORTUNITY — this is the gap |

### The Gap
There is no dominant open-source framework specifically for **designing self-governing agent loops with spec-driven enforcement**. The closest are:
- Microsoft Agent Governance Toolkit (runtime security, not loop design)
- OpenAI Agents SDK guardrails (input/output validation, not protocol enforcement)
- LangGraph checkpoints (state management, not self-improvement)

Isagawa Kernel's differentiator: **the loop governs itself** (learns from failures, updates its own protocol, enforces its own rules via hooks). Nobody else does self-improving governance.

---

## 7. Actionable Recommendations

### GitHub Repository
1. Add topics: `ai-agents`, `agent-framework`, `loop-engineering`, `harness-engineering`, `agent-governance`, `agent-harness`, `spec-driven-development`, `claude-code`, `agentic-ai`, `self-improving-agent`
2. README first line should contain: "loop engineering", "agent governance", "self-improving"
3. Add to awesome-harness-engineering list (968 stars, actively maintained by ai-boost)

### Website (isagawa.co)
1. Primary H1: use "loop engineering" or "agent governance" (not "spec-driven loop engineering")
2. Meta description: include "agent harness", "loop engineering", "self-improving"
3. Create comparison pages: "Isagawa Kernel vs LangGraph", "Isagawa Kernel vs Agent Governance Toolkit"
4. Blog posts targeting: "what is loop engineering", "agent governance framework guide", "how to build self-improving agent loops"

### Naming/Branding
- "Isagawa Kernel" works as a product name (unique, memorable)
- Category descriptor should be: "self-governing agent harness" or "loop engineering framework"
- Avoid: "spec-driven loop engineering" as a category (too compound, not searchable)

---

## Sources

- [Best Open Source Agent Frameworks 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks)
- [AI Agent Frameworks (LangChain)](https://www.langchain.com/resources/ai-agent-frameworks)
- [10 AI Agent Frameworks 2026 (Medium)](https://medium.com/@atnoforgenai/10-ai-agent-frameworks-you-should-know-in-2026-langgraph-crewai-autogen-more-2e0be4055556)
- [Microsoft Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)
- [OWASP Agentic AI Security & Governance](https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/)
- [Agentic Loops: ReAct to Loop Engineering (Data Science Dojo)](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)
- [Loop Engineering Guide (Lushbinary)](https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/)
- [Demystifying Loop Engineering (TechTalks)](https://bdtechtalks.com/2026/06/22/ai-loop-engineering/amp/)
- [Loop Engineering Complete Guide (Tosea.ai)](https://tosea.ai/blog/loop-engineering-ai-agents-complete-guide-2026)
- [Loop Engineering at Enterprise Grade (TrueFoundry)](https://www.truefoundry.com/blog/loop-engineering-enterprise-agent-runtime)
- [AI Agent Loop Architecture (Oracle)](https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems)
- [awesome-harness-engineering (GitHub)](https://github.com/ai-boost/awesome-harness-engineering)
- [Amazon Bedrock AgentCore Harness](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/)
- [Agentic AI Engineer Roadmap 2026 (Medium)](https://medium.com/data-science-collective/the-agentic-ai-engineer-roadmap-for-2026-skills-stack-and-order-fc1dfa17948d)
- [Agentic AI Hiring Boom: 280% Growth](https://jobsbyculture.com/blog/agentic-ai-hiring-boom-2026)
- [Google Agentic AI Infrastructure Role](https://www.google.com/about/careers/applications/jobs/results/142497582013129414-software-engineer-agentic-ai-infrastructure)
- [Spec-Driven Development (Augment Code)](https://www.augmentcode.com/guides/what-is-spec-driven-development)
- [Spec-Driven Development Is Eating Software Engineering (Medium)](https://medium.com/@visrow/spec-driven-development-is-eating-software-engineering-a-map-of-30-agentic-coding-frameworks-6ac0b5e2b484)
- [Spec-Driven Development (DeepLearning.AI Course)](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents)
- [GitHub Blog: Agentic AI, MCP, Spec-Driven Development](https://github.blog/developer-skills/agentic-ai-mcp-and-spec-driven-development-top-blog-posts-of-2025/)
- [Top 20 GitHub Repos for AI Agents 2026 (Fungies)](https://fungies.io/top-github-repositories-ai-agent-frameworks-2026/)
- [LangGraph vs CrewAI vs AutoGen 2026 (DEV)](https://dev.to/cristian_iridon_286794874/langgraph-vs-crewai-vs-autogen-in-2026-pick-the-right-ai-agent-framework-or-skip-frameworks-4m2c)
- [Agentic AI Jobs Guide 2026 (AI Career Lab)](https://theaicareerlab.com/blog/agentic-ai-jobs-guide-2026)
- [Superagent Guardrails Framework](https://www.helpnetsecurity.com/2025/12/29/superagent-framework-guardrails-agentic-ai/)
