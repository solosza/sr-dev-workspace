# Tiered Index Architecture

**Status:** Core IP — Internal Design Document
**Introduced:** v5 (as "Three-Tier Indexing"), renamed and generalized in v5.1

---

## Definition

A file organization pattern where every file serves as either an **index** (pointing to smaller files) or a **payload** (focused content under 200 lines). No file contains both navigation and dense content.

**Core rule:** A file is either a pointer or a payload, never both.

---

## Why It Exists

AI agents skim or skip large files, causing drift. The longer a file, the more likely the agent misses critical sections or hallucinates details. Small indexed files force the agent to load exactly the context it needs — nothing more, nothing less.

**The problem it solves:**
- 500-line protocol files → agent skips sections → drift → violations
- Monolithic CLAUDE.md → agent loses track of rules → inconsistent behavior
- Combined index+content files → agent reads navigation but skims payload (or vice versa)

**The fix:** Separate concerns at the file level. Navigation files navigate. Content files contain content. Never mix.

---

## The Pattern

### Fractal Application

The pattern applies at every layer of the kernel and grows organically. There is no fixed depth — files split when they need to, not before.

```
CLAUDE.md (index)
  → commands/*.md (payload, each < 200 lines)
  → skills/SKILL.md (index)
      → references/step-*.md (payload, each < 200 lines)

protocols/[domain]-protocol.md (index)
  → references to source files (payload)
  → lessons/lessons.md (payload, splits when > 200 lines)

domain-packs/[pack]/SKILL.md (index)
  → workflow.md (index or payload, depending on size)
  → steps/step-*.md (payload)
  → _reference/*.md (payload, splits when > 200 lines)
```

### The 200-Line Threshold

When any file exceeds 200 lines:

1. Convert the file to a **folder** with the same name
2. Create an **index file** inside (`README.md`, `SKILL.md`, or `index.md`)
3. Split content into **focused sub-files** (each under 200 lines)
4. Update the **parent reference** to point to the new index

The threshold is a guideline, not a hard gate. A 210-line file that's cohesive is fine. A 180-line file that mixes two distinct topics should still split.

### Index Files

Index files contain:
- A title and brief description (1-3 lines)
- A table or list pointing to sub-files
- Execution rules or ordering constraints (if applicable)
- Nothing else

**Example — SKILL.md as index:**
```markdown
# Domain Setup Skill

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Verify prerequisites | references/step-01-prerequisites.md |
| 2 | Discover repo | references/step-02-discover.md |
...
```

### Payload Files

Payload files contain:
- Focused content on a single topic
- Under 200 lines
- Self-contained (readable without needing sibling files)
- No navigation tables pointing to other files at the same level

---

## How It Differs from "Three-Tier Indexing"

The original v5 design described three fixed tiers:

```
Level 1: CLAUDE.md → Commands
Level 2: SKILL.md → Step Files
Level 3: Protocol → Reference Files
```

**Tiered Index Architecture** generalizes this:
- No fixed number of tiers — depth grows as content grows
- Applies to **all** file types (design docs, domain packs, lessons, specs)
- The organizing principle is index vs payload, not level number
- New layers emerge naturally when a payload file crosses 200 lines

The three-tier pattern is one valid instance of the architecture, not the architecture itself.

---

## Application Across the Kernel

| Layer | Index File | Payload Files |
|-------|-----------|---------------|
| Entry point | `CLAUDE.md` | Command `.md` files |
| Skills | `SKILL.md` | `references/step-*.md` |
| Protocols | `[domain]-protocol.md` | Source files, lesson files |
| Domain packs | `SKILL.md` | `workflow.md`, `steps/*.md`, `_reference/*.md` |
| Design docs | `KERNEL_DESIGN.md` | Topic-specific docs (this file) |
| Lessons | `lessons.md` (until > 200 lines) | `lessons/[topic].md` (after split) |

---

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Index + dense content in same file | Agent reads one, skims the other |
| File over 200 lines with no split plan | Agent skips sections, causing drift |
| Deep nesting without index files | Agent can't navigate to the right payload |
| Premature splitting (< 50 lines per file) | Overhead without benefit, too many files to track |
| Duplicating content across tiers | Stale copies diverge, agent reads wrong version |

---

## Relationship to Spec-Driven Domain Packs

Domain packs are the primary consumer of this architecture. Every pack follows the index/payload split:

```
domain-pack/
├── SKILL.md              ← Index (entry point)
├── workflow.md           ← Index or payload (depends on complexity)
├── gate-contract.md      ← Payload (validation rules)
├── steps/
│   ├── step-01.md        ← Payload (step criteria)
│   └── ...
└── _reference/
    ├── README.md         ← Index (architecture + navigation)
    ├── component-spec.md ← Payload (build spec, splits if > 200)
    └── ...
```

The pack structure is domain-specific — the kernel doesn't dictate how many steps or what the reference specs contain. It only enforces that the agent reads and follows whatever the pack defines, using the tiered index pattern to keep everything navigable.

---

*This document is part of the Isagawa Kernel internal design documentation.*
