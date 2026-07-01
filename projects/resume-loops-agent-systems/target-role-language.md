# Target Role Language — Loops and Agent Systems

## Keyword Extraction from Job Postings

### Job Title Keywords (most frequent terms in titles)

| Keyword/Phrase | Frequency | Example Titles |
|---------------|-----------|---------------|
| Agent Infrastructure | High | "Software Engineer, Agent Infrastructure" (OpenAI) |
| Agents Infrastructure | High | "Senior Staff SWE, ML Infrastructure, Agents Infrastructure" (Google) |
| Agentic AI | High | "Staff SWE, Agentic AI" (Google), "Senior Staff SWE, ML Quality, Agentic AI" (Google) |
| Agent Protocol | Medium | "Senior Staff SWE, Agent Protocol, Cloud AI" (Google) |
| Agentic Workflows | Medium | "Applied AI Engineer, Agentic Workflows" (Cohere) |
| Agentic Platform | Medium | "Engineering Manager, Agentic Platform" (Cohere) |
| Frontier Agents | Medium | "Senior Frontier Agents Engineer" (Scale AI) |
| Agent Quality | Medium | "Staff SWE, Agent Quality" (Databricks) |
| Coding Agents | Medium | "MTS - Coding Agents, Infrastructure" (xAI) |
| Agent Platform | Low | "Software Engineer, Agent Platform" (Letta) |
| AgentOps | Low | "Engineering Manager, AgentOps" (Scale AI) |
| Computer-Using Agent | Low | "Software Engineer, Computer-Using Agent" (OpenAI) |
| Agent Security | Low | "Security Engineer, Agent Security" (OpenAI) |

### Job Description Keywords (terms in requirements/descriptions)

| Keyword/Phrase | Context |
|---------------|---------|
| agent orchestration | Multi-step goal execution, workflow coordination |
| agent governance | Safety, compliance, policy enforcement at runtime |
| multi-agent systems | Coordinating multiple agents in production |
| autonomous tool-use | Agents calling tools without human intervention |
| agent evaluation / evals | Measuring agent performance, safety, correctness |
| agent observability | Monitoring, tracing, explainability for agentic actions |
| agent post-training | RL, RLHF, fine-tuning for agent behavior |
| agent deployment | Production deployment of autonomous agent systems |
| loop orchestration | Not used in postings — this is Isagawa-specific language |
| enforcement / enforcement layer | Not used in postings — industry says "guardrails" or "safety" |
| mechanical enforcement | Not used in postings — Isagawa-specific |
| hook-based governance | Not used in postings — Isagawa-specific |

### Industry-Standard Framing vs Current Resume Language

| Industry Says | Resume Currently Says | Gap |
|--------------|----------------------|-----|
| agent infrastructure | agent governance, enforcement | Partial overlap — missing "infrastructure" framing |
| agent orchestration | autonomous task cycling | Different term for overlapping concept |
| agentic workflows | autonomous delivery pipeline | Different term — "agentic" is the industry adjective |
| multi-agent systems | (not mentioned) | Gap — resume doesn't use this term despite having multi-agent capability |
| agent evaluation / evals | LLM Evaluation (DeepEval section) | Present but buried under QA framing, not agent framing |
| agent observability | anchor mechanism, audit trail | Present but described with custom terminology |
| agent safety | safety-first, compliance | Present but underweighted vs job posting emphasis |
| agent platform | (not used) | Gap — "platform" signals production-grade infrastructure |
| production agents | production repos, production QA | Present but QA-framed, not agent-framed |
| guardrails | enforcement, hooks | Same concept, different word — industry uses "guardrails" |
| agent runtime | kernel, governance system | Same concept — "runtime" is industry standard |

## Top 15 Target Keywords/Phrases

1. **agent infrastructure** — the dominant framing across OpenAI, Google, Scale AI
2. **agentic AI** — Google's preferred term for the category
3. **agent orchestration** — multi-step coordination, workflow management
4. **multi-agent systems** — coordinating multiple agents
5. **agent platform** — production-grade agent management
6. **agentic workflows** — Cohere's framing, increasingly common
7. **agent evaluation / evals** — measuring agent behavior
8. **agent observability** — monitoring and tracing agent actions
9. **agent governance** — safety and compliance at runtime
10. **agent safety** — preventing harmful or incorrect agent actions
11. **agent runtime** — the execution environment for agents
12. **autonomous agents** — agents operating without human intervention
13. **guardrails** — constraints on agent behavior (industry term for "enforcement")
14. **agent protocol** — Google's term for structured agent communication
15. **agent quality** — Databricks' framing for agent correctness

## Gap Analysis Summary

### What the resume does well
- Deep technical substance — the kernel IS agent infrastructure
- Concrete metrics (80+ pipeline runs, 800+ tasks, 14 harnesses)
- End-to-end delivery story (backlog to attested artifact)

### Critical gaps
1. **Missing industry vocabulary.** Resume uses Isagawa-specific terms (kernel, mechanical enforcement, anchor mechanism, hook-based governance) instead of industry-standard terms (agent infrastructure, agent runtime, guardrails, agent orchestration, agent observability). ATS systems and recruiters scan for the standard terms.

2. **"Loops" framing absent.** The resume describes autonomous cycling and delivery pipelines but never uses "loop" as a first-class concept. The kernel IS a loop system — session-start → anchor → work → learn → complete → repeat. This framing is missing from the resume entirely.

3. **"Agent systems" framing buried.** The resume leads with "AI Agent Architect" but describes individual tools/platforms rather than framing the work as building agent systems. The Agent Factory section comes closest but is positioned as a subsection, not the lead.

4. **Multi-agent not mentioned.** The kernel orchestrates multiple agents (run-task.sh spawning one-shot agents, background agents, agent swarms) but "multi-agent" never appears in the resume.

5. **"Infrastructure" framing weak.** The resume reads as "I built tools" rather than "I built infrastructure." Job postings want infrastructure engineers — people who build the platform that other engineers use. The kernel IS infrastructure.

6. **QA framing dominates.** Prior experience section is 100% QA-titled. The technical skills section lists QA before agent engineering. For agent infrastructure roles, QA should be repositioned as "quality systems" expertise that naturally led to agent governance.

### Recommended Language Shifts

| Current | Shift To |
|---------|----------|
| Isagawa Kernel | agent runtime / agent infrastructure |
| mechanical enforcement | guardrails, runtime enforcement |
| anchor mechanism | agent observability, drift detection |
| hook-based governance | tool-call interception, runtime safety |
| autonomous cycling | agent orchestration loop |
| Agent Factory | agent harness factory, multi-agent system |
| kernel-governed | runtime-governed, infrastructure-enforced |
| QA Platform | quality automation platform |
