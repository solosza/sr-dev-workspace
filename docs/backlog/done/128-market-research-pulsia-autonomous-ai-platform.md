# Research Pulsia Autonomous AI Platform

## Status
Open

## Priority
High — Understand autonomous AI platform market and assess harness design pattern applicability for similar product development

## Summary
Pulsia is an autonomous AI company builder operating at significant scale (1,000-2,000 companies, nightly autonomous decisions). This research analyzes their operational model, business architecture, and technical implementation to determine whether a similar product could be built using the harness design pattern. Success would validate the harness pattern's applicability to autonomous SaaS platforms.

## Deliverables

1. **Company Overview** — Pulsia's business model, market positioning, revenue structure ($50/month base + 20% revenue share), scale metrics, and customer segments
2. **Operational Architecture** — How Pulsia operates autonomously: task execution patterns, decision trees, feedback loops, scaling approach, infrastructure requirements
3. **Autonomous Execution Model** — Technical implementation: task distribution, state management, error recovery, human-in-the-loop patterns (if any)
4. **Harness Design Pattern Applicability** — Can the harness design pattern (specification-first, agent-driven orchestration, loop composition) support Pulsia-like autonomous operations? What would need to extend the pattern?
5. **Architectural Blueprint** — Proposed harness loops for a Pulsia equivalent:
   - Core autonomous orchestrator loop (coordinates all operations)
   - Autonomous deployment loop (code generation → testing → deployment)
   - Feature coding loop (specification → LLM generation → validation)
   - Marketing automation loop (content generation → publishing → analytics)
   - Ad management loop (performance analysis → optimization → bidding)
   - Human escalation loop (flagging decisions for human review)
6. **Scalability Assessment** — How would harness-based implementation scale from 10 companies to 1,000+ companies? What are the bottlenecks? Infrastructure, LLM token cost, hook/gate complexity?
7. **Comparison Analysis** — Harness pattern vs. traditional microservices/task-queue approaches. What are the advantages and trade-offs?

## Requirements

- Deep research into Pulsia's public information (website, blog, case studies, interviews, LinkedIn, Twitter)
- Understand autonomous AI platform market trends (other players, competitive landscape)
- Analyze how specification-first approach differs from traditional agent architectures
- Identify what extensions would be needed to the harness pattern for Pulsia-scale operations
- Propose concrete harness loop structures with example specifications

## References

- Harness Design Pattern documentation: `docs/harness-design-pattern/`
- Spawn-subagent skill: `.claude/skills/spawn-subagent/`
- Orchestration flows: `docs/harness-design-pattern/references/orchestration-flows.md`
- Composability model: `docs/harness-design-pattern/references/composability.md`
- Backlog 029: AI harness engineering jobs research (related market analysis)

## Task Builder Input

- **Deliverable:** Pulsia research report (markdown) with architectural blueprint and feasibility assessment
- **Location:** `subproject:pulsia-research`
- **Scope:** RESEARCH
- **Constraints:**
  - Use publicly available information only
  - Focus on autonomous execution patterns and scalability
  - Relate findings back to harness design pattern capabilities
  - Propose concrete loop structures with mock specifications
