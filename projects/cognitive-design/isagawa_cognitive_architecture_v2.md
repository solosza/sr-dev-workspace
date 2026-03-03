# Isagawa Cognitive Architecture

**Author:** Alain Ignacio | **Date:** 2026-03-01 | **Status:** Architecture Design

---

## One-Line Summary

A cognitive architecture for autonomous AI agent execution where a human-authored spec generates the management infrastructure, execution discipline, and self-improvement loop for a session-cycling, self-governing agent that accumulates knowledge through the filesystem.

---

## The Problem

AI agents drift. After 10-15 actions without guidance, they lose coherence. Multi-turn conversations degrade performance — research shows accuracy drops from 90% (single-turn) to 65% (multi-turn), with unreliability increasing 112%. Every existing multi-agent system fights this by trying to make individual agents smarter, compressing context, or adding coordination layers between agents.

None of them solve the root problem: **agents don't need more intelligence. They need management.**

---

## The Architecture

Four components, one information flow:

```
SPEC (human-authored intent)
 │
 ▼
DOMAIN SETUP (comprehension — reads spec, builds everything)
 │
 ├── Protocol (rules, patterns, anti-patterns)
 ├── Reference Library (executable truth — code to copy)
 ├── Hooks (mechanical enforcement — can't bypass)
 ├── Task Queue (tasks/ — user-provided work items)
 └── Lessons (empty at start, grows with experience)
 │
 ▼
KERNEL (management + execution — enforces protocol, re-centers agent, cycles through tasks)
 │
 ▼
LEARN LOOP (growth — failures become lessons, lessons become enforcement)
```

The human writes one document and provides work items. Everything downstream is autonomous.

---

## Component Roles

### 1. The Spec (Intent)

The spec is the only human-authored artifact. It describes system boundaries, data flows, decision logic, architectural patterns, quality gates, and anti-patterns. The spec is not code. It is not a prompt. It is a description of what the system should be. Everything else is derived from it.

The spec is long-term memory. It persists unchanged across all sessions, all tasks. It is the single source of truth.

### 2. Domain Setup (Comprehension)

Domain setup reads the spec and builds the entire operational infrastructure:

- **Protocol:** Rules extracted from the spec — naming conventions, architecture patterns, quality gates, anti-patterns. Pure index file under 200 lines, pointing to reference files.
- **Reference Library:** Concrete, copy-worthy code examples for every architectural layer. Not documentation — executable truth. Agents that read references before writing code produce correct output on first attempt. Agents that skip references hallucinate patterns.
- **Hooks:** Python scripts that fire on every tool call (Write, Edit, Bash). Mechanical enforcement that physically blocks non-compliant work. The agent cannot bypass hooks — they run at the infrastructure level, not the prompt level.
- **Task Queue:** The `tasks/` directory — user-provided numbered work items. Domain setup creates the directory infrastructure; the user populates it with tasks before or after setup. Domain setup does NOT generate work items — that's user input, not generated output.
- **Lessons:** Empty file at initialization. Grows as the agent encounters failures and records what it learned. Persists across all sessions.

Domain setup is an 11-step skill: prerequisites, discover repo, read reference code, extract patterns, understand enforcement, read workflow, initialize task queue, build protocol, wrap commands, update state, report & restart. It runs once. Its output governs every subsequent session.

### 3. Autonomous Cycling (Execution Loop)

Cycling is not a separate component — it's a kernel capability. The execution loop is built into the kernel itself, activated by the user via `/kernel/autonomous-cycle`.

```
READ task queue → PICK next task → IMPLEMENT → VERIFY → COMPLETE → ADVANCE → REPEAT
```

The cycling agent does not plan. The task queue was populated by the user. The agent reads `tasks/` and picks the next incomplete task. Each task gets a fresh session context. State persists via the filesystem — `session_state.json` and `[domain]_workflow.json` track cycling progress, completed tasks, and skipped tasks.

Cycling's simplicity is the feature. The agent has full autonomy within the boundaries the kernel enforces. The human is out of the loop after authoring the spec and populating the task queue. HITL only fires on failure — not on planning, not on execution, not on task breakdown.

The cycling workflow is an 8-step loop: scan tasks, pick next, save state, implement, verify (mechanical — check filesystem against acceptance criteria), complete (via `/kernel/complete` skill invocation), commit, loop. Error handling: test failure → fix → learn → retry. Stuck after 3 attempts → skip task, record lesson, continue. All tasks done → report.

Each task gets a clean session. When the task completes, the agent advances to the next. Context resets at session boundaries. No accumulated drift. No performance degradation from multi-turn conversations.

### 4. The Kernel (Discipline)

The kernel governs each agent session through mechanical enforcement:

- **Smart Gates:** PreToolUse hook (`universal-gate-enforcer.py`) fires on every Write, Edit, and Bash command. Four gates check state before allowing any action: (1) Session started? (2) Needs learn? (3) Anchored? (4) Action limit reached?
- **Re-centering:** Every N actions (configurable via `actions_limit` in workflow state), the hook blocks and forces the agent to re-read its protocol, review lessons learned, and check recent work against anti-patterns. This is the core enforcement mechanism — the agent cannot drift because it is mechanically forced to re-read its instructions at regular intervals.
- **Test Failure Detector:** PostToolUse hook (`test-failure-detector.py`) fires after every Bash command. Detects non-zero exit codes on test commands (pytest, npm test, playwright test, etc.). Sets a `needs_learn` flag that blocks all further work until the agent records what it learned from the failure.
- **Learn Self-Enforcement:** Protocol rule (not hook-enforced) — if a test fails, the agent MUST invoke `/kernel/learn` after fixing, even if the hook didn't fire (e.g., hooks not yet restarted after setup). The hook is the safety net, not the only trigger.

The kernel is invisible when everything works. It only surfaces when something goes wrong — and when it does, it blocks the agent AND tells it exactly how to fix the situation.

### 5. The Learn Loop (Growth)

Every failure creates a lesson. Every lesson makes the system smarter. Two tiers of learning:

- **Soft enforcement:** Lessons added to protocol. Agent reads during anchor. Relies on agent compliance.
- **Hard enforcement:** Patterns added to hooks. Fires automatically on every tool call. Cannot be bypassed.

The learn loop is mandatory. The hook blocks all work until the lesson is recorded. This is not optional — the infrastructure enforces it.

```
FAILURE DETECTED
 → Agent diagnoses root cause
 → Agent records lesson in protocol (soft enforcement)
 → Agent updates hooks if pattern is mechanically detectable (hard enforcement)
 → Lesson persists to filesystem
 → Next session's agent reads lesson during anchor
 → Same mistake is now impossible
```

---

## The Session Cycling Insight

This is the key architectural decision that makes everything else work.

Traditional agent systems maintain long-running sessions. The agent accumulates context and degrades over time. The Isagawa architecture does the opposite: every task gets a fresh session. The agent is stateless. The system is stateful.

- **No context degradation.** Each session is effectively single-turn. The Microsoft Research finding (90% → 65% accuracy over multi-turn) is sidestepped entirely.
- **No drift.** A fresh agent with a fresh protocol read cannot have drifted from previous instructions.
- **State lives in files.** The kernel restores management state from `session_state.json` and `[domain]_workflow.json`. The agent reads the task queue. It knows exactly where the project left off without needing accumulated context.
- **Lessons compound across sessions.** Task 1's failure becomes Task 2's knowledge. By Task 50, the protocol is dense with hard-won lessons that no single session ever had to accumulate.

The agent doesn't know it's on Task #47. It just sees: here's my spec, here's my protocol, here's my lessons, here's my next task. Go.

---

## The Cognitive Architecture Mapping

What emerged from solving practical problems maps to a cognitive architecture:

| Component | Cognitive Function | Persistence |
|---|---|---|
| Spec | Long-term memory / Intent | Permanent (human-authored) |
| Domain Setup | Comprehension | Runs once, artifacts persist |
| Task Queue | Planning | User-provided, consumed sequentially |
| Autonomous Cycling | Working memory | One task, one session, then discarded |
| Kernel | Discipline / Executive function | Restored fresh each session from state |
| Learn Loop | Learning / Adaptation | Accumulates across all sessions |
| Lessons | Episodic memory | Grows indefinitely, compounds over time |
| Hooks | Reflexes | Automatic, cannot be overridden |
| Protocol | Procedural memory | Updated by learn loop, read at anchor |
| State Files | Short-term memory | Updated per session, read on resume |

This is not a metaphor. Each component performs the cognitive function described. The architecture was not designed top-down from cognitive science theory — it emerged bottom-up from solving real problems with real agents in real sessions.

---

## What Makes This Different

**vs. Traditional Multi-Agent Orchestration (CrewAI, AutoGen, etc.)**

These systems focus on agent coordination — message passing, role assignment, conversation management. They assume agents need to talk to each other. The Isagawa architecture eliminates the coordination problem entirely. Knowledge accumulates through the filesystem, not through messages.

**vs. Agent Frameworks (LangChain, LangGraph, etc.)**

These provide tools for building agents — chains, memory, tool use. They don't provide management. An agent built with LangChain can still drift, hallucinate, and repeat mistakes. The Isagawa kernel adds the management layer that these frameworks are missing.

**vs. Platform-Specific Solutions (Anthropic Agent Infrastructure, OpenAI Codex, etc.)**

These build management for their own agents on their own platforms. They're proprietary, platform-locked, and designed for their specific use cases. The Isagawa architecture is universal — it runs inside any agent (Claude Code, Cursor, Copilot) because it governs through the filesystem and hooks, not through platform APIs.

**vs. Prompt Engineering / Instruction-Based Approaches**

Prompt engineering relies on the agent choosing to follow instructions. The Isagawa architecture uses mechanical enforcement — hooks that physically block non-compliant work at the infrastructure level. The agent cannot choose to ignore management because management runs in the execution environment, not in the prompt.

---

## Authored Autonomy

The Isagawa architecture introduces a new paradigm: **authored autonomy**.

The human authors the boundaries once (the spec). The system operates freely within those boundaries. This is not controlled autonomy (human approves every action) and not uncontrolled autonomy (agent does whatever it wants). It is governed autonomy — the agent has full freedom to execute and learn, but cannot violate the mechanical enforcement the spec generated.

The human's role shifts from managing agents to authoring specs. One spec produces a fully governed agent that enforces its own quality and learns from its own failures.

---

## Proposed Monetization

The cognitive architecture produces a natural business model: **Authored Autonomy as a Service**. A company provides a spec (or co-authors one with the Isagawa team). The system turns that spec into a self-governing AI agent that executes, learns, and improves — starting with one agent doing one task, scaling as trust grows.

### The Core Product

AI agent setup for any domain in your company. The spec is the variable. The kernel is the constant. The customer decides the scope. The system handles the rest.

### Three Revenue Layers

**Layer 1: Domain Setup Engagements ($15-50K)**

Walk into a company, understand their domain, author (or co-author) the spec, run domain setup, validate the kernel is governing correctly, and hand them a working system. The deliverable is a governed AI agent for their specific vertical — not a tool, not a platform, a governed agent that follows their rules and gets smarter every day.

Pricing scales with complexity. A single-workflow setup is the low end. An enterprise with 15 interconnected workflows across engineering, ops, and compliance is the high end.

**Layer 2: Agent Capacity Pricing (Recurring)**

Once domain setup is complete, the company needs agents running. Pricing is based on agent-sessions — how many tasks per month, how many tasks they're burning through.

The unit of value is a **governed task completion**. An agent that finishes a task and records its lessons is one unit. The kernel's state tracking already provides perfect metering — every task completion, every lesson learned, every session is logged.

The margin structure is favorable: the customer runs their own compute (Claude Code, Cursor, whatever). They pay their own LLM costs. Isagawa licenses the management layer — the kernel, the protocol, the hooks, the learn loop. Cost per agent-session is near zero. The customer pays for the management layer that makes their LLM costs actually productive.

**Layer 3: Domain Spec Marketplace (Platform)**

Every domain setup engagement produces a domain spec — a spec + reference library + hooks that encode expertise for that vertical. Each spec is a reusable asset.

Companies buy domain specs to skip the engagement and self-serve. A startup that needs governed QA automation buys the QA spec ($500-2K), plugs it into their kernel, runs domain setup, and they're live. Vibe coders buy simpler specs ($50-200) for things like governed Next.js development or governed data pipeline construction.

Spec authors (including third parties eventually) receive a revenue share. Distribution through ecosystem partners (OpenClaw Skills/Plugins, MCP-native positioning) extends marketplace reach.

### Pricing Framework

| Tier | What They Get | Price Range | Margin |
|---|---|---|---|
| **Setup** | Domain spec + governed workspace | $15-50K one-time | High (services) |
| **Solo** | 1 agent, kernel license, learn loop | $500-2K/month | Very high (software) |
| **Team** | Multiple agents, shared lessons, task queue | $2-8K/month | Very high |
| **Specs** | Pre-built domain expertise | $50-2K per spec | Platform margin |

### The Scaling Story

Start with one agent on one workflow. See it learn, see it improve, see it stop making the same mistake twice. When you trust it, add more tasks. When you trust the system, expand to more domains. Each new vertical is a new spec — all running on the same management infrastructure.

The customer's cost per governed task goes down as lessons accumulate. Isagawa's margin stays constant because management is software, not headcount.

### Go-to-Market Wedge

QA automation services are the initial wedge — a proven Trojan Horse demo methodology that builds working tests on prospects' actual websites during sales calls. This demonstrates the architecture's capability while creating immediate value, supporting premium pricing.

From QA, the engagement expands: the same architecture governs any domain the customer needs. The kernel doesn't change. The spec changes. Each new vertical is a new spec, a new revenue stream — all running on the same management infrastructure.

### Self-Serve Path

Open source kernel release targets initial adoption through the vibe coder market — non-technical users building with AI who need management without understanding management. They buy a domain spec, install the kernel, and their AI agent is immediately governed. No configuration. No DevOps. Just files and discipline.

This market path builds community, generates spec marketplace demand, and creates a pipeline for enterprise upsells when vibe coders' companies discover what's running under the hood.

### Why This Pricing Works

- **No compute costs:** Customers run their own LLM infrastructure. Isagawa licenses management only.
- **Perfect metering:** The kernel's state tracking provides exact usage data — task completions, lessons learned, sessions run, hook enforcement events.
- **Value scales with usage:** More tasks = more governed work = more value delivered. Pricing naturally aligns with value.
- **Stickiness:** As the learn loop accumulates domain-specific lessons and the protocol encodes company-specific knowledge, switching costs increase organically.
- **Compound defensibility:** Each engagement produces a domain spec. Each spec is a reusable asset. The spec library grows with every customer, creating a compounding moat.

---

## The Meta-Spec: A Machine That Builds Products

The architecture produces a second-order capability that collapses the cost of vertical expansion to near zero.

### Domain Knowledge Is Public

80-90% of the knowledge needed to build a domain spec for any vertical already exists on the internet. How Selenium works, EDI 835 transaction formats, RAG chunking strategies, CI/CD pipeline patterns, compliance frameworks — all documented publicly. The remaining 10-20% is enterprise-specific customization: proprietary systems, internal APIs, undocumented business logic.

The insight: **the knowledge is commodity. The transformation of knowledge into mechanical enforcement is not.** Nobody else is feeding public domain knowledge into a system that converts it into self-building protocols, reference libraries, and self-improving hooks.

### The Cycling Agent Builds Domain Specs

One meta-spec instructs the cycling agent to: read public documentation for a target vertical, extract architectural patterns, anti-patterns, and quality gates, and produce a domain spec. The agent reads the meta-spec, picks the next vertical, builds the spec, completes the task. Next vertical. Next task. Next spec.

The kernel governs the cycling agent while it builds domain specs that are themselves governed by the kernel. The system builds copies of itself for every industry on earth, governed the whole way through.

50 domain specs at launch is not a grind. It's the cycling agent working through verticals the same way it works through any task queue. Each spec is a task. Each task is fresh. Each failure makes the next spec better.

### The Cycling Agent Tests Domain Specs

The testing bottleneck dissolves through the same architecture. The agent builds a spec from public documentation. Then a fresh session installs the spec into a clean repo, runs domain setup, and tries to execute tasks against the spec. The kernel governs the whole time.

If the protocol has a bad pattern, the agent hits it during execution and the learn loop captures the failure. If a reference file has wrong imports or broken composition, the agent's code won't work and the test failure detector flags it.

Every failure the agent hits while testing is a lesson written back into the spec itself. The spec improves through the same learn loop that governs everything else. By the time the agent finishes a testing cycle, the spec has been battle-tested by the same system that will use it in production.

Validation closes the loop through the source material: the spec was derived from authoritative documentation, the reference library was built from documented patterns, and the agent tests against those same patterns. If the output matches what the documentation says it should look like, the spec works. If it doesn't, the learn loop catches it.

### The Pipeline

```
META-SPEC (one document, written once)
 │
 ▼
CYCLING AGENT reads public documentation for vertical N
 │
 ▼
CYCLING AGENT authors domain spec from extracted knowledge
 │
 ▼
DOMAIN SETUP builds protocol, references, hooks
 │
 ▼
CYCLING AGENT tests the spec in a clean environment
 │
 ├── Pass → Spec validated, move to vertical N+1
 └── Fail → Learn loop improves the spec → Retest
 │
 ▼
REPEAT for every vertical
```

The human's only input: the meta-spec and choosing which verticals to target. The machine builds the products. The machine tests the products. The machine improves the products.

### Where Humans Stay in the Loop

The 10-20% that isn't public — proprietary systems, internal APIs, undocumented business logic — remains the domain of human-authored customization. This is the enterprise services layer ($15-50K engagements) where the spec is tuned to a specific company's codebase, naming conventions, edge cases, and compliance requirements.

The platform handles commodity knowledge at scale. Humans handle the premium customization that enterprises pay for. Both layers compound — the cycling agent builds more specs while services engagements produce more enterprise-grade specs that feed back into the marketplace.

---

## Implementation Status

| Component | Status | Implementation |
|---|---|---|
| Spec-Driven Development | ✅ Validated | Domain specs authored, agent self-builds from them |
| Kernel (management) | ✅ Shipped | Open source, MIT license, GitHub |
| Domain Setup | ✅ Implemented | 11-step skill, creates protocol + hooks + task queue |
| Learn Loop | ✅ Implemented | Soft (protocol) + hard (hooks) enforcement |
| Autonomous Cycling | ✅ Validated | First cycling run: 7 tasks, 28 tests, ~15 min. Kernel-native. |
| Session Cycling | ✅ Proven | State persistence across session boundaries |
| QA Domain Spec | ✅ Validated | Prescriptive spec, live client delivery, real bugs found |
| Meta-Spec Pipeline | ⬜ Designed | Architecture defined, implementation pending |
| Swarm Execution | ⬜ Theoretical | See "Future: Swarm Scaling" below |

---

## The Evolution

This architecture wasn't designed in one pass. It evolved through three stages, each solving real problems:

**Stage 1: MCP Foundation (Defense-in-Depth)** — Built 6 management primitives (Protocols, Smart Gates, Hooks, Audit, State, HITL) as MCP server infrastructure for QA automation. Discovered that agents need mechanical enforcement, not just instructions.

**Stage 2: The Kernel (Self-Building Management)** — Generalized the MCP layer into a universal, infrastructure-free management system. Discovered that agents produce better results when they build their own enforcement from specs rather than following hardcoded rules.

**Stage 3: Domain Specs + Autonomous Cycling (Scalable Expertise)** — Created modular domain specs with indexed references per architectural layer. Autonomous cycling built into the kernel as a native capability. Discovered that session cycling + filesystem-based knowledge sharing + mechanical enforcement = a cognitive architecture that gets smarter with every task.

Each stage was driven by observing real agent behavior over hundreds of hours of hands-on use — not by theory about how agents should work.

---

## Future: Swarm Scaling

> **Status: Theoretical.** Not implemented. The architecture is designed to support this, but current implementation is single-agent.

The architecture should scale to swarm execution without modification.

- Every agent would read from the same spec, same protocol, same lessons.
- Agents wouldn't need to communicate with each other. The filesystem is the shared brain.
- No message bus. No orchestration layer. No consensus protocols. Just files and management.
- The kernel ensures every agent follows identical management. Same hooks. Same re-centering. Same learn loop.

**Knowledge sharing without coordination:** Agent A fails on a task. The learn loop records the lesson to the protocol. Agent B reads that lesson during its anchor phase before starting its task. Agent B is smarter than Agent A, and they never exchanged a single message.

**Conflict prevention (to be solved):**

- Task queue assigns work. No two agents pick the same task.
- File-level state tracking prevents concurrent writes to the same resource.
- Each agent operates in its own session with its own workspace.
- Kernel management is identical across all agents — consistency is structural, not coordinated.

This is the long-term vision. Current focus is validating the single-agent loop end-to-end.

---

## Summary

**One spec in. Governed autonomous execution out.**

The human authors intent. The system comprehends, executes with discipline, and learns from experience. No context degradation. Just files, management, and a session-cycling agent that gets smarter every time it fails.

---

*Designed by Alain Ignacio. Built from the bottom up, one drift problem at a time.*
