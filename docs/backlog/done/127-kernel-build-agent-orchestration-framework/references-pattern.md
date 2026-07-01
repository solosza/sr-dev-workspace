# References Indexing Pattern — Documentation Library

## What Are References?

References are **pattern libraries and design guidelines** that inform how the system should behave. They are **not executable** — they document constraints, philosophies, anti-patterns, and design decisions.

References guide both:
1. **Agent behavior** — What the agent should do (soft constraints via lessons/protocol)
2. **Developer behavior** — How to build skills and commands (best practices)

## Directory Structure

```
.claude/references/
├── core-philosophy.md                ← Why the orchestration system exists
├── agent-autonomy.md                 ← Autonomy assumptions and contract
├── gate-contract-template.md         ← Schema for phase boundaries
├── state-schema-patterns.md          ← How to structure state files
├── cycling-behavior.md               ← Rules for autonomous task looping
├── error-recovery.md                 ← How to handle and recover from failures
├── skill-design-patterns.md          ← How to build modular skills
├── data-contract-patterns.md         ← Validation interfaces
└── [domain-specific references]
```

## Reference Document Template

Each reference follows this structure:

```markdown
# [Topic Name]

## Purpose

[1-2 sentences: What is this pattern? Why does it matter?]

## Principles

1. **[Principle 1]:** [Explanation]
2. **[Principle 2]:** [Explanation]

## Rules

| Rule | Rationale | Example |
|------|-----------|---------|
| Rule 1 | Why this rule exists | Concrete example |
| Rule 2 | Why this rule exists | Concrete example |

## Anti-Patterns

What NOT to do:

- ❌ **Anti-pattern 1:** [Why this is wrong]
- ❌ **Anti-pattern 2:** [Why this is wrong]

## Implementation

How to implement this pattern in practice:

1. Do this
2. Then this
3. Validate with this check

## Examples

Concrete examples from the kernel or framework:

- Example 1: [Link to file/skill/command]
- Example 2: [Link to file/skill/command]

## Related References

→ [[other-pattern.md]]
→ [[error-recovery.md]]
```

## Core References (Must Extract)

When building the framework, extract these key references from the kernel:

### 1. core-philosophy.md
**What:** Why autonomous agent orchestration matters, core design principles

**Topics:**
- Why orchestration matters (control flow for agents)
- Autonomy by default (no pauses, no user input during execution)
- Data-driven behavior (state files control logic, not code)
- Composable skills (skills can call other skills)
- Error recovery as design (failures don't halt)

### 2. agent-autonomy.md
**What:** The autonomy contract — what the agent must guarantee

**Topics:**
- Never pause during autonomous execution
- No user confirmation requests (except initial command)
- Errors are handled internally (retry, skip, record)
- State is authoritative (always read state before acting)
- Results are reported after completion

### 3. gate-contract-template.md
**What:** Schema for phase boundaries and validation

**Topics:**
- Input gates (what must be true before a step)
- Output gates (what must be true after a step)
- Recovery gates (what to preserve if step fails)
- JSON schema template
- Examples: task-builder step gates, execute-pipeline step gates

### 4. state-schema-patterns.md
**What:** How to structure state files for skills and commands

**Topics:**
- session_state.json structure
- domain_workflow.json structure
- Task-specific state schemas
- State field naming conventions
- Merging patterns (read → modify → write)

### 5. cycling-behavior.md
**What:** Rules for autonomous looping through tasks

**Topics:**
- When to cycle (task done, pick next task)
- When to stop (all done, or skip after 3 retries)
- State transitions (mark complete, set next_task)
- Error recovery during cycling (if task fails)
- Nesting rules (cycling within cycling)

### 6. error-recovery.md
**What:** How to handle failures without halting

**Topics:**
- Retry logic (attempt N times before giving up)
- Error categorization (transient vs. permanent)
- Recovery actions (rollback, skip, retry)
- Logging errors to state
- When to escalate (move to user for decision)

## The Indexing Pattern

References are **indexed, not duplicated**. The protocol and lessons files are indexes that **point to** reference documents.

**Example: protocol.md**
```markdown
# Sr Dev Protocol

## References

### Architecture Patterns
→ [[../references/core-philosophy.md]]
→ [[../references/agent-autonomy.md]]
→ [[../references/gate-contract-template.md]]

### Implementation Guides
→ [[../references/skill-design-patterns.md]]
→ [[../references/error-recovery.md]]
```

The protocol is **thin** (1-2 pages). It points to detailed references. This keeps the protocol readable while allowing deep dives.

## Lessons as Reference

The lessons.md file is a **special reference** — it records lessons learned from failures and violations. Structure:

```markdown
# Lessons Learned

## RULE ZERO

**NEVER ASSUME. ALWAYS VERIFY.**
[Explanation + examples of when this was violated]

## Specific Lesson Topics

| Topic | File | Lessons |
|-------|------|---------|
| Kernel Compliance | kernel-compliance.md | Hook bypass, quick anchor, ... |
| Testing | testing-completeness.md | L1/L2/L3, simulate != real, ... |
```

Lessons are lessons.md entry points that link to detailed topic files.

## Building the Reference Library

The framework should ship with reference **templates** showing what each reference should contain:

1. **Reference Template** — Blank template for creating new references
2. **Example References** — 3-5 complete references extracted from kernel
3. **Index Structure** — How to link references in protocol.md and lessons.md

Domains adopting the framework customize references (add domain-specific patterns) but keep the structure.

## Discovery and Usage

References are **not discovered automatically**. They're manually indexed in:

1. **protocol.md** — Links to foundational references
2. **lessons.md** — Links to domain-learned lessons
3. **SKILL.md files** — Links to skill-specific references (e.g., task-builder references step-06-verification.md)

The agent reads protocol/lessons/SKILL as part of anchor ceremony. References are loaded on-demand during execution.

## Examples to Extract

When building the framework, extract these reference implementations:

1. **core-philosophy.md** — Kernel's philosophy on orchestration
2. **agent-autonomy.md** — Autonomy contract (from CLAUDE.md)
3. **gate-contract-template.md** — From execute-pipeline skill
4. **cycling-behavior.md** — From autonomous-cycling skill reference
5. **error-recovery.md** — From step files handling failures

Each becomes a **reference implementation** showing how to structure and document patterns.
