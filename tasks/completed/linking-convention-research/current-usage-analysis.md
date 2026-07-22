# Current Linking Convention Usage Analysis

## Summary

Three linking conventions are used across the kernel ecosystem: **wikilinks** (`→ [[path]]`), **code spans** (`` `path` ``), and **@-imports** (`@path`). Code spans dominate by volume (5,738 sr_dev + 1,715 hmsa = 7,453 total), wikilinks are concentrated in skills and task indexes (144 sr_dev + 78 hmsa = 222 total), and @-imports are rare/incidental (102 sr_dev + 86 hmsa = 188 total, mostly false positives from email addresses and social media handles).

## Per-Convention Counts by Layer

### sr_dev_workspace

| Layer | Wikilinks (`→ [[`) | Code Spans (`` `file.ext` ``) | @-imports |
|-------|--------------------:|------------------------------:|----------:|
| CLAUDE.md | 0 | 46 | 0 |
| .claude/skills/ | 15 | 542 | 8 |
| .claude/commands/ | 0 | 89 | 3 |
| .claude/protocols/ | 0 | 19 | 0 |
| .claude/lessons/ | 1 | 133 | 8 |
| docs/ | 38 | 900 | 46 |
| tasks/ | 89 | 4,009 | 37 |
| **Total** | **143** | **5,738** | **102** |

### hmsa-healthcare-qa

| Layer | Wikilinks (`→ [[`) | Code Spans (`` `file.ext` ``) | @-imports |
|-------|--------------------:|------------------------------:|----------:|
| CLAUDE.md | 0 | 13 | 0 |
| .claude/skills/ | 59 | 851 | 0 |
| .claude/commands/ | 0 | 150 | 0 |
| .claude/protocols/ | 0 | 8 | 0 |
| .claude/lessons/ | 1 | 27 | 0 |
| docs/ | 0 | 266 | 0 |
| tasks/ | 2 | 400 | 0 |
| **Total** | **62** | **1,715** | **0** |

## Convention Distribution Analysis

### Wikilinks (`→ [[path]]`)
- **Primary use:** Skill step files (cross-references to other references), task 000-index files (gate-contract links), HARNESS-DESIGN-PATTERN docs
- **Absent from:** CLAUDE.md, commands, protocols — these layers use code spans exclusively
- **Concentrated in:** .claude/skills/ (both repos) and task indexes
- **Purpose:** Directive references ("go read this file")

### Code Spans (`` `path/to/file.ext` ``)
- **Dominant convention** — 97% of all file references by volume
- **Used everywhere:** Every layer, both repos, all file types
- **Dual purpose:** Both informational mentions ("see `config.json`") and structural references in tables (protocol, CLAUDE.md, SKILL.md step tables)
- **Note:** Count includes both directive (with `→` prefix) and non-directive uses

### @-imports
- **sr_dev only:** 102 matches, but most are false positives (@anthropic, @isagawa, @reviewer-style mentions)
- **Not a linking convention** — per task 001 results, `@path` only works in CLAUDE.md (client-parsed), not in other files

## Inconsistencies Found

### Files Using BOTH Wikilinks AND Code Spans (Mixed Convention)

**sr_dev_workspace:** 30+ files use both conventions in the same file. Key examples:

| File | Pattern |
|------|---------|
| `.claude/lessons/lessons.md` | Wikilink in index table, code spans in rule text |
| `.claude/skills/task-builder/references/step-*.md` (6 files) | Wikilinks for cross-refs, code spans for inline paths |
| `docs/HARNESS-DESIGN-PATTERN.md` | Wikilinks for architecture refs, code spans for file paths |
| Task 000-index files (30+) | Gate-contract wikilink + code span paths in tables |

**hmsa-healthcare-qa:** 12 files with mixed conventions, same pattern — task-builder references and validate-tc skill files.

### The Mixed Pattern is Intentional (Partially)

Per task 002 findings, the mixed usage follows a consistent rule in skill files:
- **Wikilinks (`→ [[]]`)** = directive ("follow this link, read the file")
- **Code spans (`` `path` ``)** = informational ("this path exists, for reference")

This is documented in the task 002 results as the **Proposed Convention** and matches the lessons RULE ZERO ("ALWAYS USE WIKILINK TIERED INDEXING" for structural cross-references).

### True Inconsistencies (Unintentional)

1. **CLAUDE.md uses only code spans** — even for structural references in the Reference Tables (`.claude/references/core-philosophy.md`). These are "read this file" directives during `/kernel/anchor` but use code spans instead of wikilinks.

2. **Protocol uses only code spans** — same issue. The protocol's reference table points to files the agent must read, but uses code spans instead of the wikilink directive convention.

3. **Commands use only code spans** — no wikilinks in any command file. Some command cross-references (e.g., "see `/kernel/anchor`") are plain text, not linked.

4. **Lessons index uses code spans for topic file links** — the `| Topic | File |` table in lessons.md uses code spans for the file column, but these are "follow this link" references that should be wikilinks per the convention.

## Key Findings

1. **Code spans outnumber wikilinks 33:1** — but this is expected since code spans serve dual duty (informational + paths in code blocks/examples)
2. **Wikilinks are used correctly** where they appear — always with `→` prefix, always for directive cross-references
3. **The gap is under-use of wikilinks**, not misuse — CLAUDE.md, protocol, commands, and lessons index should use `→ [[]]` for structural "read this" references but currently use code spans
4. **@-imports are not a linking convention** — confirmed by task 001, only functional in CLAUDE.md via client parsing
5. **Both repos share the same pattern** — task-builder skill files have identical mixed conventions in both sr_dev and hmsa, confirming this is a kernel-level convention (not repo-specific drift)
