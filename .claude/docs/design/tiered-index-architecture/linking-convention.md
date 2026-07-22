# Linking Convention — Design Decision

**Status:** Accepted
**Date:** 2026-07-06
**Context:** Tiered Index Architecture

---

## Decision

Use a **layered convention** with two formats distinguished by intent:

| Intent | Format | Example |
|--------|--------|---------|
| Directive ("read this") | `→ [[path]]` | `→ [[references/step-01.md]]` |
| Informational ("this exists") | `` `path` `` | See `.claude/protocols/hmsa-protocol.md` |

---

## Rules (3)

### Rule 1: Arrow + Wikilink for Directives

When a reference means "the agent MUST read this file," use `→ [[path]]`.

Where this applies:
- SKILL.md step tables
- Step file cross-references
- Index files pointing to sub-files
- Lessons index → topic files

```markdown
| 1 | Parse goal | → [[references/step-01-parse-goal.md]] |
```

### Rule 2: Code Span for Informational Mentions

When a reference is contextual (not an instruction to read), use `` `path` ``.

Where this applies:
- Protocol reference tables (anchor ceremony provides the "read" instruction)
- CLAUDE.md reference lists
- Inline mentions in prose
- Examples and code blocks

```markdown
| Core Philosophy | `.claude/references/core-philosophy.md` |
```

### Rule 3: Never Use Plain Text Paths or @-imports

- Plain text paths (`references/step-01.md`) have no visual signal — agent misses them
- `@path` only works in CLAUDE.md (client-parsed at startup) — not a general convention

---

## Rationale

### Research Findings (Tasks 001-003)

**@-import testing (Task 001):** `@path` is CLAUDE.md-specific. The Claude Code client parses it at startup only. In skill files, protocols, and design docs, `@path` is inert plain text. Not viable as a general linking convention.

**Wikilink vs code span testing (Task 002):** Neither format triggers auto-reading. Both are agent-interpreted — the agent sees the text and decides whether to follow it. The `→` arrow prefix is the key signal that transforms a reference from informational to directive. With the arrow, both `[[]]` and `` ` ` `` work equally. Without the arrow, signal strength drops from "strong" to "medium."

**Current usage analysis (Task 003):** Code spans outnumber wikilinks 33:1 across both repos (7,453 code spans vs 222 wikilinks). But this reflects dual-duty — code spans serve both informational mentions and structural references. Wikilinks are used correctly where they appear (always directive, always with `→` prefix). The gap is under-use of wikilinks in CLAUDE.md, protocol, commands, and lessons index.

### Why Layered (Not Single Format)

A single format would mean using `→ [[]]` for everything — including inline path mentions in prose where the agent should NOT read the file. The two-format convention matches the two intents that actually exist:
1. "Go read this file now" → directive format
2. "This file exists for reference" → informational format

---

## Examples by Layer

### CLAUDE.md
```markdown
## References
| Reference | File |
|-----------|------|
| Core Philosophy | `.claude/references/core-philosophy.md` |
```
Uses code spans because the anchor ceremony (not CLAUDE.md itself) instructs reading.

### SKILL.md (Step Table)
```markdown
| Step | Action | Reference |
|------|--------|-----------|
| 1 | Parse goal | → [[references/step-01-parse-goal.md]] |
| 2 | Research | → [[references/step-02-research.md]] |
```
Uses wikilinks because each row is a directive — agent reads at execution time.

### Step Files (Cross-References)
```markdown
For verification methods, see:
→ [[references/verification-methods.md]]
```
Directive — agent must read the referenced file to complete the current step.

### Index Files (Tasks, Lessons)
```markdown
| Topic | File |
|-------|------|
| Kernel Compliance | → [[kernel-compliance.md]] |
| Git & Branching | → [[git-and-branching.md]] |
```
Directive — when the agent needs detail on a topic, follow the link.

---

## Trade-offs

| Trade-off | Accepted Because |
|-----------|-----------------|
| Two formats to remember instead of one | Maps 1:1 to two distinct intents — low cognitive load |
| Code spans are ambiguous (path vs code literal) | Context disambiguates; wrapping format (table cell, prose, code block) provides signal |
| Wikilinks don't render in GitHub | Kernel files are agent-consumed, not human-browsed; rendering is not a priority |
| Migration effort for existing files | Incremental — fix on touch, not bulk rewrite (see migration checklist) |
