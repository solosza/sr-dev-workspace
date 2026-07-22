# Generalized Loop Pattern

## Purpose

Define a reusable loop template that any repo can use to build, integrate, and validate loops (outer or inner). The dnd-game-engine-test repo is the first application — but the pattern itself is repo-agnostic.

## The Pattern

Every loop in any repo follows the same structure. This is the generalization of what hmsa-healthcare-qa's loop-architecture, tiered-index-architecture, and command-skill-pattern already describe — but packaged as a buildable template.

### Loop = SKILL.md + Contracts + References + Gate + Tests

```
.claude/skills/[loop-name]/
├── SKILL.md                    # Identity + DDD workflow (Declare-Determine-Describe)
├── contracts/
│   ├── [loop-name]-input.json  # What this loop receives (DECLARE)
│   ├── [loop-name]-output.json # What this loop returns (DESCRIBE)
│   └── [loop-name]-rules.json  # Mechanics rules (DETERMINE)
├── references/
│   └── [reference-materials]   # Canonical examples, patterns
├── gate-contract.md            # Enforcement: what must be true before loop completes
└── _test/
    └── fixtures/               # Test scenarios with expected outcomes
```

### Contract Is Part of the Loop

This is the key insight the user identified: contracts are not a separate concern — they ARE part of the loop definition. A loop without its contracts is incomplete. The contract defines:

1. **Input contract** — what the loop receives from its caller (outer loop or user)
2. **Output contract** — what the loop returns to its caller
3. **Rules contract** — the mechanics the loop applies (deterministic, no improvisation)
4. **Gate contract** — enforcement rules that block completion if violated

### Outer/Inner Loop Composition

Any loop can become an orchestrator by integrating inner loops as steps:

```
Outer Loop (orchestrator)
  DECLARE: Load context, present options
  DETERMINE: Route to inner loop based on input
    └─ Inner Loop executes (own DDD cycle)
       └─ Returns output contract to outer loop
  DESCRIBE: Validate output, save state, narrate
```

**Integration contract:** The outer loop's DETERMINE phase invokes the inner loop. The inner loop's output contract must satisfy the outer loop's expected return format. This is the composition interface.

### Building a Loop (Execute-Pipeline Pattern)

To build a new loop, execute-pipeline decomposes into tasks:

1. **SKILL.md** — Define identity, DDD phases, integration points
2. **Input contract** — JSON schema for what the loop receives
3. **Output contract** — JSON schema for what the loop returns
4. **Rules contract** — Mechanics/logic the loop applies
5. **Gate contract** — Enforcement rules
6. **References** — Canonical examples
7. **Test fixtures** — Scenarios with expected outcomes
8. **Integration** — Wire into outer loop's DETERMINE routing

Each of these is one task. A loop = 8 atomic tasks.

### Building a Loop's Contracts (Same Pattern)

Contracts are built as part of the loop — not separately. Each contract task reads:
- The loop's SKILL.md (what does this loop do?)
- The outer loop's integration spec (what format does the caller expect?)
- The command-skill-pattern contract-schema (what JSON structure?)
- Domain-specific rules (D&D 5e PHB, or healthcare QA rules, etc.)

## Repo-Agnostic Application

| Repo | Outer Loop | Inner Loops | Domain Rules Source |
|------|-----------|-------------|---------------------|
| dnd-game-engine-test | orchestration-loop (DDD) | combat, social, challenge, travel, rest, item-use, ability-saves, env-hazards, downtime | D&D 5e PHB/DMG |
| hmsa-healthcare-qa | create-test-artifacts | create-sit-xlsx, verify-sit-xlsx | HMSA QA standards |
| Any future repo | [domain orchestrator] | [domain sub-loops] | [domain rules] |

The pattern is the same. Only the domain rules change.

## What Makes This Different from Existing Docs

The hmsa design docs (loop-architecture, command-skill-pattern, tiered-index) describe the WHAT. This pattern describes the HOW TO BUILD:
- Concrete task decomposition for building a loop
- Contract-as-part-of-loop (not separate concern)
- Integration contract template for outer/inner composition
- Execute-pipeline compatible (each loop = task folder)
