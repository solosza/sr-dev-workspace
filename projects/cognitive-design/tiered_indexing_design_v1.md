# Tiered Indexing Design v1

**Status:** Active — applies to all kernel layers
**Created:** 2026-03-03
**Applies to:** Protocols, Lessons, References, Skills, Specs/Tasks

---

## Core Principle

**Every file is either an index or a payload. Never both.**

- **Index** = points to other files. Contains no substantive content itself.
- **Payload** = contains the actual knowledge. Pointed to by an index.

This separation enables indefinite scaling. When a payload exceeds the size threshold,
it becomes an index and splits into sub-payloads. The structure is recursive.

## The 200-Line Rule

Any file exceeding **200 lines** MUST be split:

1. The oversized file becomes an **index** pointing to new sub-payloads
2. Content is extracted into **sub-payload** files grouped by topic
3. The index retains only: topic table, cross-cutting summary, anti-patterns (if shared)
4. Sub-payloads are placed in a **sub-folder** named after the parent topic

This rule applies recursively. A sub-payload that exceeds 200 lines splits again.

## Folder Structure

Folders mirror the index hierarchy. Each index file lives alongside its payload folder:

```
[layer]/
├── index.md                    ← Root index (points to topic folders)
├── topic-a/
│   └── content.md              ← Payload (single file, under threshold)
├── topic-b/
│   ├── index.md                ← Sub-index (topic exceeded threshold)
│   ├── subtopic-1.md           ← Sub-payload
│   └── subtopic-2.md           ← Sub-payload
└── topic-c/
    └── content.md              ← Payload
```

**Rules:**
- One folder per topic in the root index
- Folder name = topic slug (lowercase, hyphens)
- If a topic is a single file (under threshold), it lives alone in its folder
- If a topic splits, its folder gets an `index.md` + sub-payload files
- Root index always named `index.md` or the layer's canonical name (e.g., `lessons.md`, `protocol.md`)

## Index File Format

Every index file follows this template:

```markdown
# [Layer/Topic Name] — Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## [Topic Table Header]

| Topic | File | Contents |
|-------|------|----------|
| Topic A | `topic-a/content.md` | Brief description |
| Topic B | `topic-b/` | **INDEX** → subtopic-1, subtopic-2 |
| — Subtopic 1 | `topic-b/subtopic-1.md` | Brief description |
| — Subtopic 2 | `topic-b/subtopic-2.md` | Brief description |
| Topic C | `topic-c/content.md` | Brief description |
```

**Conventions:**
- Sub-indexed topics marked with **INDEX** in the Contents column
- Sub-payloads indented with `—` prefix in the Topic column
- Paths are relative to the index file's directory

## Payload File Format

Every payload file includes a header comment linking back to its parent index:

```markdown
# [Title]

<!-- Payload of: [parent-index-path] -->

[Content here]
```

## Where This Applies

### Lessons (`.claude/lessons/`)

Root index: `lessons.md`
Topics: framework, locators, assertions, test-org, error-handling, advanced, mcp
Agent reads root index during `/kernel/anchor`. Anchor follows index links as needed.

### Protocols (`.claude/protocols/`)

Root index: `[domain]-protocol.md`
Topics: workspace/repos, references, kernel commands, skills
Protocol is already an index by design. This formalizes the structure.

### References (`.claude/references/`)

Root index: referenced from protocol
Topics: core-philosophy, ai-agent-development, code-quality, git-workflow, anti-patterns, quality-gates
Currently flat files. Apply folder structure when any reference exceeds threshold.

### Skills (`.claude/skills/`)

Each skill already uses `SKILL.md` as index with `references/step-*.md` as payloads.
This is the tiered design — skills were the first implementation of it.

### Tasks/Specs (`tasks/` or `specs/`)

Work queue files. These are typically short (under threshold) and don't need sub-folders.
If a task spec exceeds 200 lines, split into a folder with index + sub-files.

## Scaling Behavior

```
Level 0: Root index
         ├── points to →  Level 1: Topic folders
         │                         ├── points to →  Level 2: Sub-topic files
         │                         │                         ├── points to →  Level 3: ...
         │                         │                         └── (split again if >200)
         │                         └── single payload (under threshold)
         └── flat file count stays manageable at each level
```

At every level:
- The index stays small (just a topic table + brief summary)
- Payloads stay focused (one topic, under 200 lines)
- The agent reads only what it needs (follow index → topic → sub-topic)

## Anti-Patterns

| Anti-Pattern | Why | Do Instead |
|-------------|-----|------------|
| File is both index AND payload | Violates separation, grows unbounded | Pick one role. Split if needed. |
| Flat directory with 10+ files | Hard to scan, no grouping | Group into topic folders |
| Duplicating content across index and payload | Drift, contradictions | Index points only. Single source of truth. |
| Payload over 200 lines | Too large to scan quickly | Split into sub-payloads |
| Index over 200 lines | Too many topics at one level | Group related topics into sub-indexes |
| Deep nesting (>3 levels) | Diminishing returns, hard to navigate | Broaden categories instead |

## Decision Record

- **Why 200 lines?** — Empirically, files under 200 lines are quick to read and process.
  Above that, agents start losing context or skimming. The threshold is a practical
  heuristic, not a hard science number.
- **Why folders?** — Flat directories with 10+ files become hard to scan. Folders group
  related content and make the structure self-documenting.
- **Why not databases/JSON?** — Markdown files are human-readable, git-diffable, and
  work natively with agent Read tools. No parsing overhead.
- **Why recursive?** — The same rule at every level means no special cases. The agent
  applies one pattern regardless of depth.
