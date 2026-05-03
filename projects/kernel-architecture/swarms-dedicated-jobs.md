# Dedicated-Job Agent Analysis

## Existing Skills as Agent Roles

### website-cloner — Extraction Specialist
- **Role:** Navigate to URL, extract visual/structural patterns, produce local clone
- **Tools:** Playwright MCP (browser automation), screenshot, DOM analysis
- **Persistence:** None — each invocation is fresh
- **Could be a persistent agent?** Yes — a "web intelligence agent" that monitors sites, tracks changes, extracts patterns on demand. Would need: URL queue, change detection, pattern library.
- **Current gap:** One-shot only. No memory of previously cloned sites.

### audit-workflow — Code Review/Audit Specialist
- **Role:** Scan all kernel infrastructure for gaps, generate fix tasks, auto-execute
- **Tools:** File system scanning, pattern matching, gap detection
- **Persistence:** None — scans fresh each time
- **Could be a persistent agent?** Yes — a "continuous auditor" that runs after every pipeline, tracks drift over time, builds a compliance history.
- **Current gap:** No history. Same audit runs identically every time.

### prod-test — Testing Specialist
- **Role:** Take a deliverable repo, build master+test workspace, run L1/L2/L3 tests
- **Tools:** Docker, run-task.sh, bash scripts, test frameworks
- **Persistence:** None — disposable test workspaces
- **Could be a persistent agent?** Partially — test infrastructure could persist, but test isolation requires fresh state by design.
- **Current gap:** Correct for testing. Persistence would actually harm test integrity.

### task-builder — Decomposition Specialist
- **Role:** Take a goal, research context, decompose into atomic tasks, write task files
- **Tools:** File system, web search, template resolution
- **Persistence:** None — each decomposition is independent
- **Could be a persistent agent?** Yes — a "project planner" that learns from past decompositions, tracks which task patterns work, optimizes task count.
- **Current gap:** No learning from past decompositions. Same mistakes possible each time (until lessons catch them).

### execute-pipeline — Orchestration Specialist
- **Role:** End-to-end: backlog → task-builder → run-task.sh → validation
- **Tools:** All other skills as sub-components
- **Persistence:** Pipeline state survives across steps, but not across pipelines
- **Could be a persistent agent?** Yes — a "pipeline coordinator" that tracks cross-pipeline dependencies, optimizes scheduling, learns from execution patterns.
- **Current gap:** Each pipeline is independent. No cross-pipeline optimization.

## Skills vs Specs vs Agents — Taxonomy

| Abstraction | Current Example | What It Is | Persistence | Identity |
|-------------|----------------|------------|-------------|----------|
| **Skill** | website-cloner | Prescriptive instructions for a capability | None | Anonymous (any agent can run any skill) |
| **Spec** | Domain spec (QA, SSH) | Domain knowledge + conventions | In protocol files | Domain-specific but not agent-specific |
| **Agent** | (doesn't exist yet) | Persistent entity with memory, identity, specialization | Across invocations | Named, with accumulated context |

## What Would "Agents" Add Beyond Skills?

1. **Memory across invocations** — website-cloner remembers previously cloned sites, audit-workflow tracks compliance trends, task-builder learns optimal decomposition patterns
2. **Identity/personality** — "the auditor" has a skeptical disposition, "the builder" has a bias toward action, "the researcher" is thorough
3. **Specialization via fine-tuning** — each agent could have a custom system prompt optimized for its role
4. **Inter-agent communication** — auditor flags issues → builder receives them → tester verifies fixes, without file-based intermediation

## Assessment

Skills are already 80% of the way to dedicated-job agents. The missing 20% is:
- **Persistent memory** — skills forget everything between invocations
- **Named identity** — all agents are anonymous `claude -p` instances
- **Direct communication** — agents can't talk to each other, only write/read files

The question is whether that 20% matters enough to build. For most use cases, the skill model works fine. Persistent agents become valuable when:
1. The agent needs to learn from repeated execution (e.g., auditor tracking trends)
2. The agent needs to coordinate with other agents in real-time (e.g., parallel pipeline workers)
3. The agent needs to maintain state across many invocations (e.g., a customer-facing agent)

For the kernel's current use case (autonomous pipeline execution), skills are sufficient. For a product offering ("AI agent teams"), persistent agents would be the differentiator.
