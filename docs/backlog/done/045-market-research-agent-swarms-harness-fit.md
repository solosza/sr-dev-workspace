# Research: Agent Swarms/Teams via Self-Extending Harness

## Status
Open

## Priority
High — agent teams/swarms are the current viral category in AI builder circles. If the harness already supports this pattern (or is one skill away from it), that's the positioning story.

## Summary
Research how Isagawa's self-extending agent harness maps to the agent swarms/teams pattern that founders and builders keep going viral with. The kernel already spawns sub-agents (run-task.sh → `claude -p` per task), already has role-based execution (task types: BUILD, TEST, RESEARCH), and already coordinates via shared state. Is this already agent teams by another name? What's missing to frame it that way — or to actually build dedicated-job agents that persist and specialize? The research should answer: does Isagawa extend into swarms naturally, or does it require architectural changes?

## Research Questions

1. **What are people actually shipping when they say "agent teams"?**
   - CrewAI, AutoGen, LangGraph multi-agent, OpenAI Swarm — what patterns do they use?
   - Role assignment, task delegation, shared memory, handoff protocols
   - What goes viral vs what actually works in production

2. **Does Isagawa already do this?**
   - run-task.sh spawns independent agents per task — is that a swarm?
   - Task types (BUILD/TEST/RESEARCH) are role specialization — is that "dedicated jobs"?
   - Gate contracts are handoff protocols — each task's output feeds the next
   - The kernel governs all agents via hooks — is that the orchestration layer teams need?
   - What's the delta between "pipeline of one-shot agents" and "team of persistent agents"?

3. **What would dedicated-job agents look like in the harness?**
   - Agent that only does extraction (website-cloner is already this)
   - Agent that only does code review / audit (audit-workflow is close)
   - Agent that only does testing (prod-test spawns test-only sub-agents)
   - Would these be skills? Specs? Something new?

4. **What's the moat?**
   - Other swarm frameworks have no governance — agents can do anything
   - Isagawa's hook-based governance means every agent in the swarm is mechanically constrained
   - Self-extension means the swarm can grow new agent types from intent
   - Is governed self-extending swarm a real differentiator or marketing fluff?

5. **What's the viral hook?**
   - What specifically makes agent team demos go viral?
   - Visual: seeing multiple agents work in parallel with distinct roles?
   - Narrative: "I told it what I wanted and 5 agents built it"?
   - Can Isagawa produce that demo today with execute-pipeline?

6. **What would need to change?**
   - Parallel task execution (currently sequential via run-task.sh)
   - Agent identity/persistence (currently one-shot, no memory between tasks)
   - Inter-agent communication (currently via files/state, not direct)
   - Visual dashboard showing agent activity (currently terminal-only)

## References
- Backlog 043: `docs/backlog/043-kernel-research-skill-as-app-architecture.md` (skill-as-app findings)
- Skill-as-app research report: `projects/kernel-architecture/skill-as-app-research.md`
- Backlog 044: `docs/backlog/044-market-refactor-portfolio-site-theme.md` (harness positioning)
- CrewAI, AutoGen, LangGraph, OpenAI Swarm — public repos and docs
- Greylock / Saam Motamedi "harness" framing

## Task Builder Input
- **Deliverable:** Research report answering all 6 questions with concrete assessment of harness-to-swarm fit, gap analysis, and recommended next steps (build/skip/defer)
- **Location:** subproject:kernel-architecture
- **Scope:** RESEARCH
- **Constraints:** Web research required for competitive landscape. Existing codebase (run-task.sh, skills, hooks) is the test subject for "does it already do this" analysis.
