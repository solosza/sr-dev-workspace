# Domain Spec Template

**Author:** Alain Ignacio | **Date:** 2026-03-02 | **Status:** Template Design

---

## One-Line Summary

The domain spec is the single input to the Isagawa Cognitive Architecture. It teaches the agent what a domain IS, how work flows through it, and what quality looks like — then the agent self-builds its own management system from it.

---

## What Is a Domain Spec?

A domain spec is a skill folder that lives at `.claude/skills/[domain]-guidance/`. It describes a domain — its workflow, quality gates, decision logic, and artifact templates — in enough detail that an agent can read it, understand it, and self-build the operational infrastructure needed to execute work in that domain.

The agent always self-builds. In every style — prescriptive or generative — the agent reads the spec and creates its own protocol, commands, hooks, lessons, and state following the tiered index design. The spec provides knowledge. The agent builds management.

A domain spec is NOT:
- A finished protocol (the agent builds that)
- A set of commands (the agent wraps those)
- Configuration (domain-setup generates that)
- Code to run (it's knowledge to internalize)

---

## The Three Layers

```
LAYER 1: VANILLA KERNEL + RALPH (constant — ships with isagawa-cognitive)

  commands/kernel/*              ← 6 kernel commands
  hooks/*                        ← gate enforcer + test failure detector
  skills/kernel-domain-setup/*   ← 10-step tool that reads specs
  scripts/ralph-loop.sh          ← outer execution loop
  CLAUDE.md                      ← kernel governance rules


LAYER 2: DOMAIN SPEC (variable — user or meta-spec provides this)

  skills/[domain]-guidance/      ← the spec itself (standard anatomy)
  commands/[domain]/*            ← domain entry points
  [reference code]               ← (prescriptive) executable truth
  [architecture docs]            ← (prescriptive) pre-authored system description


LAYER 3: DOMAIN-SETUP OUTPUT (generated — agent self-builds from spec)

  protocols/[domain]-protocol.md ← indexed protocol
  lessons/lessons.md             ← empty, grows with execution
  state/session_state.json       ← session tracking
  state/[domain]_workflow.json   ← domain state
  specs/*.md                     ← numbered task specs (Ralph's work queue)
  _generated/*                   ← domain artifacts (architecture, roadmap, etc.)
```

Layer 1 never changes. Layer 2 is what this document defines. Layer 3 is what the agent produces.

---

## Anatomy of a Domain Spec

Every domain spec follows this structure. All components are required unless marked optional.

```
.claude/skills/[domain]-guidance/
├── SKILL.md                 ← Identity: what, who, why, philosophy
├── workflow.md              ← Flow: phase index, data flow, artifact locations
├── gate-contract.md         ← Quality: validation rules per phase transition
├── phases/                  ← Execution: what the agent does per phase
│   ├── phase-01-*.md
│   ├── phase-02-*.md
│   └── ...
├── checkpoints/             ← HITL: gates between phases
│   ├── pre-build.md
│   ├── on-failure.md
│   └── ...
├── _decision-trees/         ← (optional) Domain-specific choice frameworks
│   └── *.md
└── _templates/              ← (optional) Shapes for generated artifacts
    └── *.md
```

Plus domain commands:
```
.claude/commands/[domain]/
├── [domain].md              ← Main entry point (Phases 1-N)
├── [domain]-feature.md      ← Repeating work unit
├── [domain]-fix.md          ← Fix with domain context
├── [domain]-test.md         ← Run tests with domain output
└── pr.md                    ← Architecture compliance review
```

---

### SKILL.md — Identity

Tells the agent what this domain is and how to think about it.

| Section | Purpose |
|---------|---------|
| Description | One-line: what this spec does |
| Target user | Who uses this (vibe coders, QA engineers, enterprise teams) |
| Philosophy | Principles that guide agent behavior in this domain |
| Phase flow | Table: phase → command → output → repeats? |
| Key files | Index of every file in the spec |
| Entry points | Command → what it invokes |

The philosophy section is critical. It shapes how the agent approaches every decision in the domain. "Educate, don't gatekeep" produces different agent behavior than "Follow the reference exactly."

### workflow.md — Flow

How phases connect, what data flows between them, where artifacts land.

| Section | Purpose |
|---------|---------|
| Phase index | Table: phase → spec file → input → output |
| Data flow | Visual: how artifacts cascade through phases |
| Artifact locations | Table: artifact → path → created by |
| Gate checkpoints | Table: between → checkpoint → purpose |
| Kernel integration | How/when domain-setup runs, what protocol indexes |

### gate-contract.md — Quality

Validation rules for every phase transition. A phase cannot advance until its gate passes.

Each gate defines:

| Element | Description |
|---------|-------------|
| Artifact | What must exist |
| Validation | Checklist of conditions (checkboxes) |
| Blocked if | What prevents advancement |

The gate contract is the quality backbone. Without it, the agent has no structured way to validate its own work between phases.

### phases/ — Execution

One file per phase. Each phase spec defines:

| Section | Purpose |
|---------|---------|
| Input | What this phase reads (artifacts from prior phases) |
| Process | Numbered steps the agent follows |
| Output | What this phase creates (artifacts for next phases) |
| Gate | Checkpoint or validation before advancing |
| Error handling | What to do when things fail |

Phases are sequential. Phase N's output feeds Phase N+1's input.

### checkpoints/ — HITL Gates

Quality gates that fire between phases or on failure. Each checkpoint defines:

| Section | Purpose |
|---------|---------|
| When | What triggers this checkpoint |
| Format | How to present information to the user |
| Rules | What the agent must/must not do |
| Validation | Checklist of conditions |

Checkpoints are where human judgment enters the loop. The spec defines WHEN to stop and ask, WHAT to show, and HOW to proceed based on the response.

### _decision-trees/ — Choice Logic (optional)

Domain-specific branching logic for decisions with multiple valid paths. Each decision tree defines entry conditions, branches, and recommendations with tradeoff explanations.

Used when the domain requires the agent to guide the user through choices (stack selection, architecture patterns, deployment strategies).

### _templates/ — Artifact Shapes (optional)

Markdown templates that define the structure of generated artifacts. The agent fills these during phase execution. Templates ensure consistent artifact format across all executions.

---

## Spec Styles

Domain specs fall into styles based on how much the agent discovers vs follows. Both styles use the same anatomy. The difference is in the phase content and what ships with the spec.

### Style 1: Prescriptive

**When:** The architecture is known. The patterns are established. The system must be exact.

**Examples:** QA test automation, EDI 835 claims, compliance workflows, enterprise integrations.

**Characteristics:**
- Reference code ships with the spec (executable truth the agent must follow)
- Architecture docs are pre-authored (the spec ships with the truth)
- Phases are tighter — less discovery, more execution
- Gate contracts enforce exact pattern matching
- The agent self-builds management, but with much stricter guidelines
- Philosophy: "Follow the reference. Extend, don't invent."

**What ships with a prescriptive spec:**
```
skills/[domain]-guidance/       ← standard anatomy
commands/[domain]/*             ← domain commands
framework/_reference/           ← canonical code per layer (the key differentiator)
FRAMEWORK.md                    ← architecture description
```

The reference library is the prescriptive spec's power. Agents that read references before writing code produce correct output on first attempt. Agents that skip references hallucinate patterns.

**Phases (typical):**

| Phase | Purpose |
|-------|---------|
| 1. Input | Gather what to build (user story, test case, transaction spec) |
| 2. Pre-flight | Verify environment, credentials, dependencies |
| 3. Processing | Analyze input against reference patterns |
| 4. Roadmap | Derive task order from reference architecture |
| 5. Construction | Build following reference code exactly |
| 6. Execution | Run, validate, HITL on failure |

**Roadmap in prescriptive specs:**
Derived from the reference architecture — what modules need building, in dependency order. Each module becomes a numbered spec in `specs/` for Ralph.

### Style 2: Generative

**When:** The system doesn't exist yet. The agent must discover what to build, then build it.

**Examples:** Vibe coding (app from plain English), greenfield projects, prototyping.

**Characteristics:**
- No reference code ships (the agent generates the architecture)
- Discovery phases are conversational
- Decision trees guide agent through choices
- Templates shape generated artifacts
- Self-binding: agent generates architecture → domain-setup indexes it → agent enforces it on itself
- Philosophy: "Educate, recommend, self-bind."

**What ships with a generative spec:**
```
skills/[domain]-guidance/       ← standard anatomy
commands/[domain]/*             ← domain commands
_decision-trees/                ← choice frameworks
_templates/                     ← artifact shapes
```

No reference code, no pre-authored architecture. The agent discovers and generates everything.

**Phases (typical):**

| Phase | Purpose |
|-------|---------|
| 1. Discovery | Conversational intake — what are you building? |
| 2. Decisions | Present options, guide choices, generate architecture |
| 3. Roadmap | Prioritize features, recommend build order |
| 4. Scaffold | Create project, verify toolchain, run domain-setup |
| 5. Feature Dev | Build features from roadmap (repeats per feature) |

**Self-binding pattern:**
1. Agent generates `_generated/architecture.md` during Phase 2
2. Agent runs `/kernel/domain-setup` during Phase 4
3. Protocol indexes `_generated/architecture.md` as the reference
4. Agent enforces its own generated architecture on all subsequent code
5. Failures feed through `/kernel/learn` back into the architecture doc

The agent creates its own constraints, then enforces them on itself.

### Future Styles

These two are the validated patterns. Others will emerge as new domains demand them:

- **Hybrid** — pre-authored architecture + agent-generated implementation plan (enterprise with known systems but unknown scope)
- **Diagnostic** — agent analyzes existing codebase, generates spec from what it finds (legacy modernization)
- **Compositional** — multiple specs compose into a single system (microservices, multi-team)

The anatomy stays the same. The phase content and what ships with the spec changes.

---

## The Roadmap Phase

Every domain spec MUST include a roadmap phase. The roadmap connects the spec to Ralph's execution loop.

### What the Roadmap Phase Produces

A structured task plan stored as a generated artifact (e.g., `_generated/product-roadmap.md`). Features/tasks are:
- Prioritized (P1 core, P2 essential, P3 nice-to-have)
- Ordered by dependency (earlier tasks don't depend on later tasks)
- Scoped (each task is implementable in a single Ralph session)

### How Roadmap Connects to Ralph

```
Domain Spec Phase (Roadmap)
 │
 └──► _generated/product-roadmap.md (or equivalent)
          │
          ▼
Domain-Setup Step 6b (Build Roadmap)
 │
 └──► Converts roadmap into numbered specs
          │
          ▼
specs/
├── 001-[first-task].md
├── 002-[second-task].md
└── ...
          │
          ▼
Ralph picks next incomplete spec → executes → closes session → repeats
```

The spec generates the roadmap in its own format. Domain-setup step 6b converts it into Ralph's queue format (`specs/*.md`). The spec doesn't need to know about Ralph. Ralph doesn't need to know about the spec.

### Roadmap by Style

| Style | Roadmap Source | Task Granularity |
|-------|---------------|------------------|
| Prescriptive | Derived from reference architecture (modules to build) | One module per spec |
| Generative | Generated from discovery phases (features to implement) | One feature per spec |

---

## How Domain-Setup Consumes the Spec

Domain-setup is the 10-step skill that reads whatever domain spec exists and builds governance around it.

```
Step 1:  Prerequisites     ← install deps, configure MCP
Step 2:  Discover          ← scan repo structure
Step 3:  Read references   ← read code patterns (prescriptive) or generated docs (generative)
Step 4:  Extract patterns  ← identify architecture, naming, anti-patterns
Step 5:  Enforcement       ← understand hook + protocol two-tier enforcement
Step 6:  Read workflow     ← READ THE DOMAIN SPEC (skills/[domain]-guidance/*)
Step 6b: Build roadmap     ← convert spec's roadmap artifact into specs/*.md for Ralph
Step 7:  Build protocol    ← create indexed protocol pointing to all discovered content
Step 8:  Wrap commands     ← wrap domain commands in kernel loop (anchor → execute → complete)
Step 9:  Update state      ← create session_state, workflow_state, register hooks
Step 10: Report & restart  ← hooks need Claude Code restart to load
```

Step 6 is where the domain spec enters the system. Domain-setup reads the skill folder — SKILL.md, workflow.md, gate-contract.md, phases, checkpoints — and uses that knowledge to build the protocol (step 7) and wrap commands (step 8).

The protocol is a **pure index** under 200 lines that points to:
- The domain spec's workflow and gate contracts
- Reference code (prescriptive) or generated architecture (generative)
- Lessons learned (grows with execution)
- Entry point commands

The agent reads this index during `/kernel/anchor`, then reads the actual files. Protocol stays small, never drifts.

---

## Tiered Index Design

All domain spec content follows the 200-line threshold rule:

1. **Under 200 lines** — single file
2. **Over 200 lines** — split into indexed folder

```
# Before (single file)
gate-contract.md (250 lines)

# After (indexed folder)
gate-contract/
├── index.md              ← points to sub-files
├── phase-transitions.md
├── failure-gates.md
└── feature-gates.md
```

This applies recursively. Protocol indexes spec files. Spec files index phase files. Phase files index sub-sections if they grow. Every parent is a table of contents pointing to its children.

---

## Domain Commands

Every domain spec ships with thin command wrappers that connect user intent to the kernel loop.

### Command Pattern

```
User types /[command]
  │
  ▼
Command wrapper:
  1. /kernel/anchor (re-read protocol)
  2. Execute workflow from spec
  3. /kernel/complete (final gate)
```

The command is a thin invocation layer. All workflow logic lives in the spec. All enforcement happens via the kernel loop.

### Standard Commands

| Command | Purpose | Maps To |
|---------|---------|---------|
| `/[domain]` | Main entry point (phases 1-N) | Full workflow |
| `/[domain]-feature` | Repeating work unit | Last phase (feature dev) |
| `/[domain]-fix` | Fix with domain context + /kernel/learn | on-failure checkpoint |
| `/[domain]-test` | Run tests with domain-specific output | Test execution step |
| `/[domain]-explain` | Explain code/decisions in domain terms | Read + explain |
| `/pr` | Architecture compliance review | Protocol + gate validation |

Not every domain needs all commands. The spec defines which entry points make sense.

---

## The Self-Build Pipeline

### Human-Authored Spec

```
1. AUTHOR THE SPEC
   └── Create skills/[domain]-guidance/ with standard anatomy
   └── Create commands/[domain]/ with entry points
   └── (Prescriptive) Add reference code + architecture docs
   └── (Generative) Add decision trees + templates

2. RUN DOMAIN-SETUP
   └── Agent reads the spec (step 6)
   └── Agent self-builds protocol, lessons, state, roadmap (steps 6b-9)
   └── Restart required (hooks load at startup)

3. EXECUTE
   └── Human: invoke /[domain] or /[domain]-feature
   └── Ralph: pick next spec from specs/, execute in governed session
   └── Kernel governs every session (hooks, anchor, learn loop)
   └── Lessons compound across sessions
```

### Meta-Spec Pipeline (Autonomous Domain Spec Creation)

The cognitive architecture's meta-spec instructs Ralph to self-build domain specs:

```
META-SPEC (one document, written once)
 │
 ▼
Ralph reads public documentation for vertical N
 │
 ▼
Ralph authors domain spec following THIS template:
 ├── SKILL.md (identity)
 ├── workflow.md (flow)
 ├── gate-contract.md (quality)
 ├── phases/ (execution)
 ├── checkpoints/ (HITL)
 └── commands/ (entry points)
 │
 ▼
Domain-setup builds governance from the spec
 │
 ▼
Ralph tests the spec in a clean environment
 │
 ├── Pass → spec validated, move to vertical N+1
 └── Fail → learn loop improves the spec → retest
```

This template is what Ralph reads when building domain specs. It defines the format. Ralph fills in the content from domain knowledge.

---

## Validated Examples

| Domain Spec | Style | Repo | Version |
|-------------|-------|------|---------|
| QA Test Automation (Playwright) | Prescriptive | `platform-playwright` | v1 — validated, missing roadmap phase |
| Vibe Coder Guidance | Generative | `vibe-coder-spec` | v2 — validated, full template |

### What v2 Added Over v1

| Feature | v1 (QA/Playwright) | v2 (Vibe Coder) |
|---------|---------------------|-----------------|
| Roadmap phase | Missing | Phase 3 generates product-roadmap.md |
| Self-binding | No — references pre-authored | Yes — agent generates then enforces own docs |
| Decision trees | No — stack is fixed | Yes — guides user through choices |
| Templates | No | Yes — shapes for all generated artifacts |
| HITL checkpoints | Implicit in workflow | Explicit checkpoint files per gate |
| Gate contract | Present | More structured (per-phase validation checklists) |

---

## Summary

The domain spec is the input. The kernel is the constant. The agent self-builds everything in between.

One template, multiple styles. Prescriptive for exact systems. Generative for open-ended systems. Both follow the same anatomy — SKILL.md (identity), workflow.md (flow), gate-contract.md (quality), phases (execution), checkpoints (HITL). Both run on the same kernel. Both produce the same output: governed, autonomous execution that learns from its own failures.

The meta-spec reads this template to self-build domain specs at scale. Every domain spec this template produces feeds back into the system that produced it.

---

*Template derived from two validated implementations (platform-playwright v1, vibe-coder-spec v2). Designed by Alain Ignacio.*
