# Harness Design Pattern — Agent-Driven Orchestration

**Version:** 1.1
**Date:** 2026-06-13
**Core Principle:** Agent reads specification, executes autonomously. No code. Pure specification + state.

---

## What is a Harness?

A **harness** is a domain-specific agent orchestration specification built on **loops, data contracts, and defense-in-depth gates**.

A harness:
- Has ONE or more **loops** (self-contained command → skill → steps structures)
- Each loop has a main **command** (markdown file describing what to do)
- Specifies a workflow via **steps** (numbered, sequential actions)
- Calls other **loops** as sub-orchestrators (when needed)
- Validates data at every boundary via **gate contracts** (JSON schemas)
- Enforces rules via **soft gates** (protocol, lessons) and **hard gates** (hooks)
- Produces **deliverables** as JSON + Markdown
- Runs **autonomously** (agent reads spec and executes, no pauses)

**The agent is the orchestrator.** The harness is the specification.

---

## File Index

| Section | File | Purpose |
|---------|------|---------|
| Loop Types | → [[references/loop-types.md]] | Orchestrator loops vs. Primitive loops |
| Architecture | → [[references/architecture-layers.md]] | 6 layers of harness architecture |
| Execution | → [[references/orchestration-flows.md]] | How agents execute specifications |
| Examples | → [[references/examples.md]] | Canonical examples: reddit-pain, spawn-subagent |
| Composition | → [[references/composability.md]] | How loops call other loops |
| Principles | → [[references/key-insights.md]] | Core principles and comparisons |

---

## Overview: Two Loop Types

A **loop** is a complete command → skill → steps → references structure.

### Orchestrator Loops

Calls multiple skills sequentially. Coordinates a domain workflow.

**Example:** `/reddit-pain/analyze` — Orchestrates: validate → fetch → analyze → generate results

**Structure:**
```
Command → [calls multiple skills in sequence] → Results
```

### Primitive Loops

Self-contained execution with own steps. Can be called by orchestrators or invoked directly.

**Canonical example:** `/spawn-subagent [description]` — Spawns a background agent autonomously

**Structure:**
```
Command → Skill → 4 Steps → Results
```

**Key difference:** Primitive loops are self-contained but composable (can be called by orchestrators).

---

## Architecture Overview

All harnesses follow the same 6-layer architecture:

1. **Commands** (markdown) — Entry point specifications
2. **Skills** (markdown + references) — Multi-step execution specifications
3. **Data Contracts** (JSON) — Validation rules at boundaries
4. **References** (markdown) — Pattern guidelines and domain knowledge
5. **Protocol** (markdown index) — Links to all files
6. **State** (JSON) — Runtime progress tracking

See → [[references/architecture-layers.md]] for detailed breakdown.

---

## No Code in the Harness

The harness contains **ZERO runtime code**:

❌ No Python files
❌ No JavaScript files
❌ No compiled code
❌ No libraries
❌ No dependencies

✅ Markdown (specifications)
✅ JSON (schemas, state)
✅ Wikilinks (connections)

---

## Defense in Depth: Soft + Hard Gates

### Soft Gates (Agent-Enforced)

Protocol and lessons that guide agent behavior. If violated, agent learns.

### Hard Gates (Hook-Enforced)

Mechanical enforcement rules that **block** operations if violated.

---

## State Management (Agent-Driven)

Three levels of state:
1. **Session state** — Current task, context, pending actions
2. **Workflow state** — Job progress, steps completed
3. **Phase state** — Input/output passed between loops, validated against gate contracts

---

## Key Insight

**The harness IS the specification. The agent IS the runtime.**

Loops are the fundamental building blocks:
- Orchestrator loops coordinate multiple skills
- Primitive loops are self-contained and composable
- Both follow: Command → Skill → Steps → References

This is fundamentally different from:
- Traditional apps (code-first)
- APIs (request-response)
- Microservices (distributed execution)

**Harness = Specification-first, agent-driven orchestration via loops.**

---

## How to Use This Guide

Start with **Loop Types** (→ [[references/loop-types.md]]) to understand the two patterns.

Then explore **Architecture Layers** (→ [[references/architecture-layers.md]]) to see how harnesses are structured.

Look at **Examples** (→ [[references/examples.md]]) to see concrete implementations:
- **Orchestrator:** `/reddit-pain/analyze` (harness backlog 127)
- **Primitive:** `/spawn-subagent` (kernel utility, non-blocking background execution)

Finally, read **Key Insights** (→ [[references/key-insights.md]]) for principles and comparisons to other architectures.

---

*This pattern is the foundation for all Isagawa harnesses.*
