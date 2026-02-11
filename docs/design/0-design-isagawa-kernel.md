# Phase 1: Design Discussion - Isagawa Kernel

**Project:** Isagawa Kernel (Universal AI Management Layer)
**Created:** 2026-02-06
**Status:** Design Complete — Ready for PRD

---

## 1. Purpose & Scope

### What This Is

A **self-building, self-improving, safety-first agent** that manages other AI agents.

Following Pi/OpenClaw's pattern: minimal kernel + self-extension. But with **defense in depth** — the agent self-builds its management layer with safety baked in.

### What Problems It Solves

Every company adopting AI agents hits the same wall:
- Agent can do the work
- No guarantee output is structured, compliant, maintainable, auditable
- Every team hand-rolls guardrails (CLAUDE.md files, custom prompts, review processes)
- It's all ad hoc

**Gap:** Nobody is building the "how do you make AI agents do enterprise-grade professional work with enforcement and auditability" layer.

### What Is Explicitly OUT of Scope (Weekend Build)

- Multiple domain packs
- Production-ready anything
- Full product polish
- Interface layers (Slack, web dashboard)

---

## 2. Reference Model: Pi/OpenClaw

### How Pi Works

| Component | Implementation |
|-----------|---------------|
| **System Prompt** | Built in `buildAgentSystemPrompt()` — assembles sections |
| **Session** | `AgentSession` via `createAgentSession()` — embedded directly |
| **Tools** | Base tools (read/write/edit/bash) + custom tools injected |
| **Extensions** | Added via session, not separate infrastructure |

**Key insight:** Pi is a session manager + system prompt builder + tool injector. That's the whole kernel.

### Our Equivalent

```
Pi                          →  Isagawa
─────────────────────────────────────────────────────
AgentSession                →  Claude Code session (already exists)
buildAgentSystemPrompt()    →  CLAUDE.md or skill
Base tools                  →  read/write/edit/bash (already in Claude Code)
Custom tools                →  MCP tools for defense in depth
```

**We don't build an agent framework. We write the brain that sits on top of one that already exists.**

---

## 3. The Six Primitives

Behaviors the kernel agent learns, implemented via self-created slash commands:

| Primitive | Purpose | Implementation |
|-----------|---------|----------------|
| **Protocols** | Define how work must be done | Stored in docs/files agent creates |
| **Smart Gates** | Validate AND teach (not just block) | Slash commands agent creates (e.g., `/validate`) |
| **Hooks** | Extensibility points for domain-specific logic | Additional slash commands for edge cases |
| **Audit** | Proof trail of what was done and why | Slash command that logs actions (e.g., `/audit`) |
| **State** | Track workflow position and completion | State file + slash command to check state |
| **HITL** | Human control without human bottleneck | Slash command that stops and asks (e.g., `/check-with-human`) |

**Defense in Depth:** No single primitive catches everything. All six together? Nothing gets through unchecked.

**Self-Creating Pattern:** Agent doesn't just follow these primitives — it creates the enforcement mechanisms (slash commands) for each one.

---

## 4. Design Options: Two Agents

### Option A: HITL-First (Managed Autonomy)

```
Self-builds defense in depth → Human approves the build
Operates within approved structure → Gates enforce automatically
Proposes improvements → Human approves changes
Safety first = HITL on structural changes, autonomy on execution
```

**Pros:**
- Enterprise-friendly (auditable, controllable)
- Trust builds over time
- Prevents "fox guarding henhouse" problem

**Cons:**
- Slower start
- HITL could bottleneck

### Option B: Pure Autonomy (Pi-Style)

```
Self-builds → Just does it
Self-improves → Just does it
No built-in HITL
Management layer as optional add-on (loaded when needed)
```

**Pros:**
- Maximum autonomy (like Pi/OpenClaw)
- Fastest execution
- Viral adoption potential

**Cons:**
- Could produce garbage without guardrails
- Enterprise-hostile initially

### Decision: Build Both

Ship both. Run in parallel. See what breaks. Let reality decide.

| Observation | Insight |
|-------------|---------|
| Agent A bottlenecked by approvals | HITL too heavy, need to loosen |
| Agent B produces garbage | Autonomy needs guardrails earlier |
| Agent A earns trust faster | Enterprise prefers managed model |
| Agent B gets viral adoption | Hackers prefer freedom |
| Both work for different audiences | Ship both as product tiers |

---

## 5. User Flow (Enterprise)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  1. INSTALL                                                             │
│     User adds Isagawa to their Claude Code environment                  │
│     $ claude --profile isagawa  OR  $ claude /kernel init               │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  2. POINT AT DOMAIN                                                     │
│     User: "I need QA test automation for my e-commerce app"             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  3. KERNEL SELF-BUILDS                                                  │
│     Agent analyzes domain, produces:                                    │
│     - Protocols (how to work)                                           │
│     - Gates (what's valid)                                              │
│     - HITL triggers (when to ask human)                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  4. HUMAN APPROVES (Agent A only)                                       │
│     Agent: "Review the protocols I created..."                          │
│     User: "Approved" or "Change X"                                      │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  5. AGENT OPERATES                                                      │
│     Works WITHIN approved/self-built structure                          │
│     Gates validate output, audit logs, HITL triggers when needed        │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  6. AGENT IMPROVES (ongoing)                                            │
│     Proposes structural changes based on friction/failure               │
│     Human approves (Agent A) or auto-applies (Agent B)                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Technical Implementation

### Enforcement Architecture

Claude Code has three enforcement layers:

```
LAYER 1: CLAUDE.md (Soft)
├── Instructions, guidance
├── Claude respects but CAN drift as context grows
└── Weakens over long sessions

LAYER 2: Slash Commands (Medium)
├── Re-anchors Claude to protocols when invoked
├── Agent can self-create these
├── Just .md files in .claude/commands/

LAYER 3: Hooks + Settings (Hard)
├── PreToolUse/PostToolUse hooks
├── Always enforced, cannot be bypassed
├── Static config (doesn't self-improve)
```

**Key Insight:** Slash commands are files. Agent can create files. Therefore agent can create its own enforcement mechanisms.

### Self-Creating Enforcement Model

```
Agent enters domain
    ↓
Self-builds defense in depth (protocols, gates)
    ↓
Self-creates slash commands for those rules
    ↓
Operates, invokes its own commands to stay anchored
    ↓
Improves → creates new slash commands
```

**Example - Agent creates its own commands:**
```
.claude/commands/
├── (kernel creates these dynamically)
├── qa-validate.md      → "Check against 4-layer architecture"
├── qa-no-locators.md   → "Verify no locators outside POM"
├── qa-audit.md         → "Log what was done"
├── qa-check.md         → "Re-anchor to QA protocols"
└── ...
```

**Safety-First Pattern:**
```
KERNEL INSTRUCTION:

When entering a domain:
1. Analyze the domain
2. Build your protocols (how work must be done)
3. BEFORE doing any work, create slash commands that enforce your protocols
4. Only then begin operating
5. Invoke your commands regularly to stay anchored
6. When you improve, create new commands for new rules
```

### What We Build This Weekend

| Component | Implementation |
|-----------|---------------|
| **Kernel CLAUDE.md** | Meta-instructions for self-build + self-create enforcement |
| **Agent A variant** | Self-build + HITL approval on structure/commands |
| **Agent B variant** | Self-build + pure autonomy |
| **Test Domain** | QA (should reproduce FRAMEWORK.md + create its own commands) |

### What We Don't Build

- Custom runtime (use Claude Code)
- Custom session manager (use Claude Code)
- Static hooks (agent creates its own enforcement via commands)
- Domain packs (kernel should work without them)

### The Kernel Is

1. A CLAUDE.md with meta-instructions:
   - How to analyze a domain
   - How to build protocols
   - How to self-create slash commands for enforcement
   - How to stay anchored (invoke own commands)
   - How to self-improve

2. Claude Code's existing infrastructure:
   - read/write/edit/bash tools
   - .claude/commands/ directory
   - Slash command invocation

3. Optional accelerators:
   - Domain packs (skills with expert knowledge)
   - MCP tools for hard enforcement

---

## 7. Domain Packs (Future, Not Weekend)

Optional accelerators. Agent works without them, just slower.

```
Kernel alone:
  → Agent reasons from first principles
  → Output is generic, maybe 60% of senior-level

Kernel + Domain Pack:
  → Agent loads expert knowledge
  → Starts at 90%+ of senior-level
  → Self-extends for project-specific needs
```

Your FRAMEWORK.md = first domain pack (QA).

---

## 8. Business Model (Placeholder)

| Component | Model |
|-----------|-------|
| **Kernel** | Free or cheap (distribution) |
| **Domain Packs** | The product (expert knowledge, premium) |
| **Deployments** | Services (custom implementations) |

**TODO - Discuss Later:**
- Outcome-based model (sell results, not tools)
- Relationship to AI-native test automation services

---

## 9. Open Questions

### Resolved

| Question | Resolution |
|----------|------------|
| What exactly goes in the system prompt? | Meta-instructions for self-build + self-create enforcement |
| How does agent "self-build" — files or in-memory? | Files: docs for protocols, .claude/commands/ for enforcement |
| How are gates enforced? | Agent self-creates slash commands, invokes them to stay anchored |
| Does this preserve autonomy? | Yes — agent is author of its own constraints |

### Test and Learn (Explore During Implementation)

| Question | Hypothesis | How We'll Learn |
|----------|------------|-----------------|
| Minimum commands before working? | Let agent decide | Observe what it creates naturally |
| Re-anchoring triggers? | Agent decides when to invoke | Watch for drift, note when it re-anchors |
| Session persistence? | Commands persist as files | Verify commands survive session restart |
| Domain pack detection? | Agent discovers via exploration | See if it finds existing skills |
| HITL approval granularity? | Approve structure, not each command | Test with Agent A, adjust if too heavy |
| Success criteria? | Agent reproduces FRAMEWORK.md patterns | Compare output to existing QA setup |

---

## 10. Weekend Deliverables

- [ ] Kernel CLAUDE.md (meta-instructions for self-build + self-create enforcement)
- [ ] Agent A variant: HITL approval on structure/commands created
- [ ] Agent B variant: Pure autonomy
- [ ] Test run: Point at QA domain
- [ ] Observe: What commands does agent create? Do they match FRAMEWORK.md patterns?
- [ ] Observe: Does agent invoke its own commands? Does it stay anchored?
- [ ] Compare: Agent-built enforcement vs existing QA workflow
- [ ] Document learnings: what broke, what worked, what surprised

---

## 11. Design Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Build on Claude Code | Yes | Already has session, tools, MCP — don't reinvent |
| Two agents (A/B) | Yes | Let reality decide which model works |
| Weekend scope | Kernel only | Domain packs come later |
| No custom runtime | Yes | Mimic Pi — minimal, not infrastructure |
| Self-creating enforcement | Slash commands | Agent creates .md files in .claude/commands/ for its own rules |
| Safety-first pattern | Create enforcement before working | Agent must create its slash commands BEFORE doing domain work |
| Re-anchoring mechanism | Invoke own commands | When context drifts, agent invokes its own commands to re-anchor |
| No static hooks for gates | Dynamic via commands | Hooks are static; slash commands can be created/evolved by agent |

---

## 12. Integration Points

| System | Integration |
|--------|------------|
| Claude Code | Runtime (session, tools) |
| Existing QA MCP | Optional enforcement layer |
| FRAMEWORK.md | Test comparison target |

---

## Next Phase

Proceed to Phase 2 (PRD) with:
- Kernel CLAUDE.md specification
- Agent A vs B differentiation
- Test protocol
- Success criteria
- Test-and-learn items to explore

---

*Status: Design complete. Approved to proceed to PRD.*
