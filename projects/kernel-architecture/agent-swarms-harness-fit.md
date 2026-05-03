# Agent Swarms / Teams — Harness Fit Assessment

## Executive Summary

Isagawa is already a **governed sequential swarm**. The components map directly: run-task.sh is the orchestrator, skills are agent roles, gate contracts are handoff protocols, hooks are the governance layer, and lessons are the self-improvement loop. No competitor framework offers governance or self-improvement. The primary gaps are parallelism, agent persistence, and a visual dashboard — but these are enhancements, not prerequisites. The recommended path is to **build a visual dashboard first** (for demos/marketing), then add **agent persistence** (for quality improvement), and defer parallelism and inter-agent communication until task volume demands them.

---

## 1. What Are People Actually Shipping When They Say "Agent Teams"?

Four major frameworks dominate:

| Framework | Mental Model | Strengths | Weaknesses |
|-----------|-------------|-----------|------------|
| **CrewAI** | Org chart (roles) | Fastest setup, cheapest, intuitive | Least flexible, limited checkpointing |
| **AutoGen** | Group chat (conversation) | Natural for debate/review | Expensive (20+ LLM calls for 4-agent debate) |
| **LangGraph** | State machine (graph) | Best production readiness, error handling | Steepest learning curve |
| **OpenAI Agents SDK** | Routines + handoffs | Simplest model, official support | No persistence, no complex orchestration |

**What goes viral:** Role-based team narratives ("5 agents built my app"), self-correction demos, real revenue proof.
**What works in production:** LangGraph (checkpointing, observability) and OpenAI Agents SDK (guardrails).

→ Details: `swarms-competitor-analysis.md`

## 2. Does Isagawa Already Do This?

**Yes.** The mapping is clean:

| Swarm Concept | Isagawa Component |
|---------------|-------------------|
| Orchestrator | run-task.sh, execute-pipeline |
| Agent roles | Skills (website-cloner, audit-workflow, prod-test) |
| Handoff protocols | Gate contracts (mechanical verification between tasks) |
| Governance | Hook system (cannot be bypassed) |
| Self-improvement | Learn loop (failure → lesson → protocol update) |
| Coordination | File-based state (session_state.json, workflow.json) |

**The delta** between Isagawa and a purpose-built swarm:
- **Sequential vs parallel** — agents run one at a time
- **One-shot vs persistent** — agents die after each task
- **File-based vs direct comms** — agents read/write files, don't talk to each other
- **Terminal vs visual** — no dashboard showing activity

→ Details: `swarms-codebase-mapping.md`

## 3. What Would Dedicated-Job Agents Look Like?

Existing skills are already 80% of the way to dedicated-job agents:
- **website-cloner** → web intelligence agent (with persistent pattern library)
- **audit-workflow** → continuous auditor (with compliance history)
- **task-builder** → project planner (learning from past decompositions)
- **execute-pipeline** → pipeline coordinator (cross-pipeline optimization)

The missing 20%: persistent memory, named identity, direct communication. Skills are sufficient for the current use case; persistent agents become valuable when the system needs to learn per-role or coordinate in real-time.

→ Details: `swarms-dedicated-jobs.md`

## 4. What's the Moat?

**Real differentiator, not marketing fluff.**

Three unique properties no competitor has:
1. **Mechanical enforcement** — hooks physically block unauthorized actions. Not "trust the agent" — the agent literally cannot bypass governance.
2. **Self-improvement** — every failure makes the system stronger via the learn loop. Competitors start fresh every time.
3. **Self-extension** — the kernel creates new skills, commands, hooks from intent. The swarm grows new agent types recursively.

**Limitations:**
- Claude-specific (hooks are Claude Code hooks)
- Complexity barrier (steep onboarding)
- Speed cost (governance adds overhead)

**Positioning:** Don't sell "agent swarms." Sell "governed autonomous agents" — the only framework where agents can't go rogue, and every failure makes the system smarter.

→ Details: `swarms-moat-assessment.md`

## 5. What's the Viral Hook?

Five patterns that make agent demos go viral:
1. "I told it what I wanted and N agents built it" — ✅ Isagawa can do this today
2. Visible parallel agent activity — ❌ Requires parallel execution
3. "It caught its own mistake and fixed it" — ✅ Learn loop is better than competitors
4. Real revenue/results — ✅ Production deliverables, not toy demos
5. Open-source + actually works — ✅ Partial (kernel is public, onboarding needs work)

**Recommended demo:** Screen recording of execute-pipeline: natural language → decomposition → agents cycling → deliverable. Before/after transformation is the hook.

→ Details: `swarms-viral-hooks.md`

## 6. What Would Need to Change?

| Gap | Effort | Value | Priority |
|-----|--------|-------|----------|
| Visual dashboard | MEDIUM | HIGH | **1st** — essential for demos |
| Agent persistence | MEDIUM | HIGH | **2nd** — enables quality improvement |
| Inter-agent comms | HIGH | MEDIUM | **3rd** — defer (files work) |
| Parallel execution | HIGH | MEDIUM | **4th** — defer (sequential is fine) |

→ Details: `swarms-architectural-gaps.md`

---

## Recommendation: BUILD (Selective)

**Don't build a swarm framework.** Isagawa already IS a governed swarm. Instead:

1. **Build a visual dashboard** (1 pipeline) — web view of the loop running. This alone makes demos compelling and is the fastest path to viral content.

2. **Add agent persistence** (1 pipeline) — named agents with memory. This enables the "agent team" narrative and improves quality through per-role learning.

3. **Market the governance moat** — position as "the only autonomous agent framework with mechanical governance." This is genuinely unique and matters for enterprise/regulated use cases.

4. **Defer parallelism and inter-agent comms** — sequential execution with file-based communication works for all current and near-term use cases. Build when task volume demands it.

**Skip building:** A generic swarm framework to compete with CrewAI/LangGraph. The market is saturated with orchestration layers. Isagawa's moat is governance + self-improvement, not orchestration.
