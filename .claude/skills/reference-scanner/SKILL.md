# Reference Scanner

**Type:** Kernel Skill
**Location:** `.claude/skills/reference-scanner/`

---

## Purpose

Discovers and catalogs payload files from tiered-index structures, then matches them to command steps by topic. Commands invoke the scanner as their Step 0 to load just-in-time knowledge — each step reads only the payloads mapped to it, not the entire reference corpus.

## File Index

| File | Purpose |
|------|---------|
| `scanner.py` | Core scanning engine: `scan_index()`, `parse_step_topics()`, `match_payloads_to_steps()` |
| `state-schema.md` | JSON schema for the `references` key in command state files, caching rules, invalidation, step usage |

## Usage: Step 0 Integration

Commands invoke the scanner as their Step 0 before executing domain steps:

1. Locate the project's root `index.md` (or reference index)
2. Call `scan_index(index_path)` to build a payload catalog
3. Call `match_payloads_to_steps(catalog, step_files)` to map payloads to steps
4. Write the result to the command's state file under the `references` key (see `state-schema.md`)
5. Each subsequent step reads `state.references.by_step["all"]` + `state.references.by_step[N]` and loads those payloads before proceeding

Cache check: skip re-scan if `references` exists and the index file mtime <= `scan_timestamp`.

## /build-command Integration

When `/build-command` scaffolds a new skill, it auto-generates topic declarations in step files so the scanner works out of the box.

### How It Works

1. `/build-command` parses the design doc's step definitions for checkpoint keywords
2. Keywords map to topics via the keyword-to-topic map below
3. Each generated step file gets a YAML frontmatter `topics:` field

### Generated Step Template

```markdown
---
topics: [rules, drg-mapping]
---

# Step N: [Name]

## Purpose
...
```

### Fallback

If no keywords match, generate `topics: [general]` and flag for manual review.

## Keyword-to-Topic Map

| Keyword in checkpoint | Generated topic |
|----------------------|-----------------|
| mapping, lookup | `drg-mapping` |
| exclusion | `drg-exclusion` |
| rules, validation | `rules` |
| SP, stored procedure | `sp-logic` |
| dates, DOS, registry | `dates` |
| QRS, Col Q, Col R, Col S | `qrs-columns` |
| xlsx, excel, format | `xlsx-format` |
| 837, QNXT, DynamicClaims | `tools` |

Projects extend this map freely. Matching is string equality — any new topic "just works."

## Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Pull model over push | Steps declare interests; index files don't annotate consumers. Lighter to maintain. |
| 2 | Scan once at startup | Per-step scanning is expensive. Reference docs rarely change mid-session. |
| 3 | Topic tags over paths | Paths break on refactor. Topics are stable and enable cross-project reuse. |
| 4 | Agent reasoning, not code | Scanner instructions live in skill files. Agent reads indexes and reasons about topics. Flexible across any index format. |
| 5 | Kernel skill (standalone) | Lives in `.claude/skills/reference-scanner/`. Any command invokes it as Step 0. |
| 6 | Graceful degradation | No index found → scanner returns empty catalog, steps use corpus-only fallback. |
| 7 | Hybrid taxonomy | Core topics defined here. Projects add domain-specific topics freely. |

## Topic Sources (How Steps Declare Interests)

The scanner reads three sources from each step file (merged, deduplicated):

1. **YAML frontmatter:** `topics: [rules, drg-mapping]`
2. **## Topics section:** bullet list of topic strings
3. **## References section:** infer topics from linked filenames
