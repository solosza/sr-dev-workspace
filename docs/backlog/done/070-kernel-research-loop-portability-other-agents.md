# Research Loop Portability to Other AI Coding Agents

## Status
Open

## Priority
High — understanding portability determines whether the loop is a Claude-only product or a universal agent governance framework

## Summary
Research what it takes to port the loop (backlog → task-builder → run-task.sh → autonomous cycling) to other AI coding agents and frameworks. Specifically: building an AI agent using LangChain that implements the loop, and porting the kernel governance pattern to other coding agents like OpenAI Codex, Cursor, Windsurf, Aider, and other CLI/IDE-based agents. The goal is to understand the portability surface area — what's Claude-specific, what's universal, and what the porting effort looks like for each target.

## Requirements

### LangChain Port
- Build an AI agent using LangChain that implements the loop pattern
- What LangChain primitives map to the kernel? (chains = tasks? agents = skills? tools = hooks?)
- Can LangChain's agent executor replicate run-task.sh behavior (one-shot agents per task)?
- How does LangGraph's state machine model fit the pipeline pattern?
- What's the minimum viable port? (Just the loop, or full governance?)

### Other Coding Agent Targets
- **OpenAI Codex CLI** — does it support hooks/pre-post tool interceptors? Can it run headless one-shot like `claude -p`?
- **Cursor** — IDE-based, has rules files (.cursorrules). Can it run autonomous pipelines? What's the hook equivalent?
- **Windsurf (Codeium)** — similar to Cursor. Rules support? Headless execution?
- **Aider** — CLI-based, similar to Claude Code. Does it support hooks, one-shot mode, headless execution?
- **Cline/Continue** — VS Code extensions. Can they run autonomous loops?
- **Amazon Q Developer** — CLI agent. Headless support? Hook equivalent?

### Portability Analysis per Component
- **Hook system** — which agents support pre/post tool-use interceptors? This is the hardest part to port.
- **One-shot execution** — which agents can run headless with a prompt and exit? (equivalent to `claude -p`)
- **State management** — which agents can read/write JSON state files between invocations?
- **Task decomposition** — this is prompt-driven and LLM-agnostic, should port easily
- **Gate contracts** — mechanical verification is shell-based, should port to any agent with bash access
- **Lessons/protocol** — text-based, any agent can read markdown files

### Architecture Questions
- What's Claude-specific vs universal in the kernel?
- Can the loop be abstracted into an agent-agnostic SDK?
- What's the minimum hook layer needed for governance? (pre-write check, action counter, learn enforcement)
- Could the kernel be a wrapper around any coding agent? (kernel manages governance, inner agent does work)

## References
- The loop: `.claude/skills/execute-pipeline/`
- Kernel architecture: `projects/kernel-architecture/`
- Agent swarms research: `projects/kernel-architecture/agent-swarms-harness-fit.md` (backlog 045, done)
- Competitor frameworks: `projects/kernel-architecture/swarms-competitor-analysis.md`

## Task Builder Input
- **Deliverable:** Research report covering LangChain port feasibility, coding agent portability matrix, component-level portability analysis, and recommended porting strategy
- **Location:** `subproject:kernel-architecture`
- **Scope:** RESEARCH
- **Constraints:** Research only. Need to understand each target agent's hook/headless/state capabilities. The LangChain port is the deepest analysis (could it actually work?). Other agents are a portability matrix (what's possible vs what's blocked). Should identify the kernel's "portability surface" — which components are universal and which are Claude-specific.
