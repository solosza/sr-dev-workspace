# Tiered Index Architecture — Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

**Status:** Core design pattern — applies to all layers, all repos
**Source:** Isagawa Kernel v5.1

---

## The Three Layers

The architecture has three integrated layers. Each solves a different failure mode. All three are required — removing any one breaks the system.

```
┌─────────────────────────────────────────────┐
│  Layer 1: Tiered Index (Organization)       │
│  How files are organized — small, focused,  │
│  navigable. Index or payload, never both.   │
├─────────────────────────────────────────────┤
│  Layer 2: Pre-Generation Checkpoints        │
│  (Directed Reading)                         │
│  When to read which files — each step has   │
│  an explicit reading list before writing.   │
├─────────────────────────────────────────────┤
│  Layer 3: Contracts & Dual Gates            │
│  (Enforcement)                              │
│  Proof the agent read correctly — soft gate │
│  validates content, hard gate blocks writes. │
└─────────────────────────────────────────────┘
```

**Why all three:**
- Index without checkpoints → agent has a library but no reading list → reads wrong files
- Checkpoints without index → agent knows what to read but files are too large → skims and misses rules
- Both without contracts → agent reads correctly but no enforcement → drifts over time

---

## Layer Documents

| Layer | File | Contents |
|-------|------|----------|
| Layer 1 | `references/layer-1-organization.md` | Index vs payload rule, 200-line threshold, folder structure, file formats |
| Layer 2 | `references/layer-2-checkpoints.md` | Pre-generation checkpoints, directed reading lists, checkpoint format |
| Layer 3 | `references/layer-3-contracts.md` | Dual gate validation, contract structure, soft + hard gates |
| Reference | `references/reference-implementation.md` | Complete worked example showing all 3 layers in a multi-step skill |

---

## How the Three Layers Connect

```
Step N begins
    │
    ▼
Layer 1: Agent follows index to find step-N payloads
    │
    ▼
Layer 2: Checkpoint directs agent to read specific files
    │  ├── canonical reference (the correct pattern)
    │  ├── contract (the validation rules)
    │  └── domain lessons (patterns from prior runs)
    │
    ▼
Agent generates artifact matching reference pattern
    │
    ▼
Layer 3: Dual gate validates output
    │  ├── Soft gate: agent checks content against contract rules
    │  └── Hard gate: hook checks structure on write
    │
    ▼
Step N complete → proceed to Step N+1
```

---

## Core Rule (Summary)

**Every file is either an index or a payload. Never both.**

- **Index** = points to other files. No substantive content.
- **Payload** = contains the actual knowledge. Pointed to by an index.
- **200-line threshold** — any file exceeding 200 lines splits into index + sub-payloads. Recursive.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Do Instead |
|-------------|-------------|------------|
| File is both index AND payload | Grows unbounded, agent skims | Pick one role |
| Flat directory with 10+ files | Hard to scan | Group into topic folders |
| Duplicating content across files | Drift, contradictions | Single source of truth |
| Payload over 200 lines | Agent loses context | Split into sub-payloads |
| Index without checkpoints | Agent browses randomly | Add reading lists per step |
| Checkpoints without contracts | No enforcement | Add dual gate validation |

---

## Decision Record

- **Why 200 lines?** — Above that, agents lose context or skim.
- **Why folders?** — Flat directories with 10+ files are hard to scan.
- **Why recursive?** — Same rule at every level, no special cases.
- **Why three layers?** — Organization alone doesn't control agent attention. Checkpoints direct it. Contracts enforce it.
