# Layer 1: Tiered Index (Organization)

<!-- Payload of: tiered-index-architecture.md -->

How files are organized. Small, focused, navigable. Every file is either an index or a payload.

---

## Why It Exists

AI agents skim or skip large files, causing drift. The longer a file, the more likely the agent misses critical sections or hallucinates details. Small indexed files force the agent to load exactly the context it needs — nothing more, nothing less.

**The problem it solves:**
- 500-line protocol files → agent skips sections → drift → violations
- Monolithic CLAUDE.md → agent loses track of rules → inconsistent behavior
- Combined index+content files → agent reads navigation but skims payload (or vice versa)

**The fix:** Separate concerns at the file level. Navigation files navigate. Content files contain content. Never mix.

---

## The 200-Line Threshold

Any file exceeding **200 lines** MUST be split:

1. The oversized file becomes an **index** pointing to new sub-payloads
2. Content is extracted into **sub-payload** files grouped by topic
3. The index retains only: topic table, cross-cutting summary
4. Sub-payloads are placed in a **sub-folder** named after the parent topic

This rule applies recursively. A sub-payload that exceeds 200 lines splits again.

The threshold is a guideline, not a hard gate. A 210-line file that's cohesive is fine. A 180-line file that mixes two distinct topics should still split.

---

## Canonical Folder Structure

Every topic folder follows the same structure regardless of layer:

```
[topic-name]/
├── index.md              ← INDEX (entry point, points to references)
└── references/
    ├── payload-a.md      ← PAYLOAD (focused content, under 200 lines)
    ├── payload-b.md      ← PAYLOAD
    └── payload-c.md      ← PAYLOAD
```

The index sits at the folder root. All payloads live in `references/`. This applies at every layer — skills, design docs, domain packs, protocols. The folder name and payload names change, the structure does not.

**Examples across layers:**

```
skills/[skill-name]/                    design/[topic-name]/
├── SKILL.md          ← INDEX          ├── index.md          ← INDEX
└── references/                        └── references/
    ├── step-01/...   ← PAYLOAD            ├── concept-a.md  ← PAYLOAD
    ├── step-02/...   ← PAYLOAD            └── concept-b.md  ← PAYLOAD
    └── test-types.md ← PAYLOAD

domain-packs/[pack]/                    protocols/
├── SKILL.md          ← INDEX          ├── [domain]-protocol.md  ← INDEX
└── references/                        └── [domain]-lessons.md   ← PAYLOAD
    ├── workflow.md   ← PAYLOAD
    └── steps/...     ← PAYLOAD
```

**Rules:**
- Index is always at the folder root (`index.md`, `SKILL.md`, or layer-canonical name)
- Payloads always live in `references/` (never alongside the index)
- Folder name = topic slug (lowercase, hyphens)
- Recursive — if a payload exceeds 200 lines, it becomes a subfolder with its own `index.md` + `references/`

---

## Index File Format

```markdown
# [Layer/Topic Name] — Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

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

---

## Payload File Format

```markdown
# [Title]

<!-- Payload of: [parent-index-path] -->

[Content here]
```

**Payload rules:**
- Focused content on a single topic
- Under 200 lines
- Self-contained (readable without needing sibling files)
- No navigation tables pointing to other files at the same level

---

## Fractal Application

The pattern applies at every layer and grows organically:

```
CLAUDE.md (index)
  → commands/*.md (payload, each < 200 lines)
  → skills/SKILL.md (index)
      → references/step-*.md (payload, each < 200 lines)

protocols/[domain]-protocol.md (index)
  → references to source files (payload)
  → lessons/lessons.md (payload, splits when > 200 lines)

skills/[skill]/SKILL.md (index)
  → workflow.md (index or payload, depending on size)
  → contracts/*.json (payload)
  → references/step-*/*.md (payload)
```

No fixed number of tiers — depth grows as content grows. New layers emerge naturally when a payload crosses 200 lines.
