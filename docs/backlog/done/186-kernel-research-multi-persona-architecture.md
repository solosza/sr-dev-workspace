# Research Multi-Persona Autonomous Company Architecture

## Status
Open

## Priority
High — validates whether the harness design pattern can scale from "one developer agent" to "autonomous company with multiple specialized personas," which is the Pulsia-scale vision

## Summary
Research two architectural approaches for running an autonomous AI company using Isagawa kernel infrastructure, where each business function (Developer, QA, PM, Sales, Marketing) operates as a specialized persona with its own commands, skills, references, contracts, and hooks. The goal is autonomous nightly operation where the system decides what the company needs and dispatches the right persona.

## Approaches to Compare

### Approach A: Multi-Harness (one harness per persona)
- Each persona gets its own repo with full domain spec
- Developer harness (already exists — the kernel)
- QA harness (partially exists — prod-test, gap-check)
- PM harness (new — backlog prioritization, roadmap, velocity tracking)
- Sales harness (partially exists — job-application-spec)
- Marketing harness (new — site updates, content, SEO)
- One orchestrator harness decides which persona to activate based on company needs
- Each harness is fully isolated with its own state, hooks, and contracts

### Approach B: Unified Harness (outer/inner loops per persona)
- Single repo with one domain spec
- Each persona is a workflow (outer loop) containing task-specific inner loops
- Shared state, shared hooks, shared protocol
- Persona selection happens at the workflow routing level, not the repo level
- Lighter weight — no repo proliferation, shared infrastructure

## Requirements
- Assess feasibility of both approaches using current kernel infrastructure
- Compare on: state isolation, complexity, scalability, maintenance burden
- Use Isagawa's current personas as test case:
  - Developer (exists as kernel)
  - QA (partially exists via prod-test, gap-check, review-queue)
  - PM (gap — no backlog prioritization, no "what to work on next" logic)
  - Sales (partially exists via job-application-spec)
  - Marketing (gap — manual site updates)
- Evaluate autonomous nightly operation: cron trigger → orchestrator → persona dispatch
- Determine which approach better supports adding new personas over time
- Address: how does the orchestrator know what the company needs? (metrics, triggers, schedules)
- Reference Pulsia research for scale/complexity benchmarks

## References
- Pulsia research: `projects/pulsia-research/`
- Harness design pattern: `docs/harness-design-pattern/`
- Loop composability research: `projects/loop-composability-research/`
- Agent orchestration framework: `docs/backlog/done/127-kernel-build-agent-orchestration-framework.md`
- Spawn agent swarm skill: `.claude/skills/spawn-agent-swarm/`
- Current personas: Developer (kernel), QA (prod-test/gap-check), Sales (job-application-spec)

## Task Builder Input
- **Deliverable:** Research report comparing both approaches with recommendation, architecture diagrams, and implementation roadmap for the winning approach
- **Location:** `subproject:multi-persona-architecture`
- **Scope:** RESEARCH
- **Constraints:** Must use existing kernel infrastructure as foundation. Must be concrete — not theoretical. Include specific file paths, command names, and state schemas for the recommended approach. Reference real Isagawa personas, not hypothetical ones.
