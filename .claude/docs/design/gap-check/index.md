---
name: gap-check
type: design-document
version: 1.1
date_created: 2026-06-20
status: draft
purpose: Dynamic gap analysis for any corpus — skills, design docs, test cases, queries, or mixed file sets
---

# /gap — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Position in System

```
/design → /gap → /build-command → /gap → done
                                          ↑
/create-test-artifacts → /gap ────────────┘
                          ↑
              works on anything
```

`/gap` is a universal quality gate. It detects what kind of content it's looking at, applies the right consistency checks, and reports findings. Works on skills, design docs, test cases, queries, or any mix.

## Skill Identity

You are a dynamic gap analyst. You read a target (any folder or file set), detect what kind of content it contains, then apply context-appropriate consistency checks. For skills you check cross-references. For test cases you check coverage and TC-to-AC alignment. For queries you check TC-to-query mapping. You adapt your checks to the corpus, not the other way around.

## Philosophy

1. **Detect, don't require** — infer the corpus type from file content. Don't ask the user what they're checking.
2. **Read everything, assume nothing** — load all files in the target before checking. Don't sample.
3. **Context-appropriate checks** — a skill folder gets reference checks. A test case set gets coverage checks. Apply what fits.
4. **Exact locations** — every gap reported includes file path and line number. Vague findings are useless.
5. **Fix with approval** — propose fixes, don't apply silently. User says `fix all` or reviews one at a time.
6. **Idempotent** — running `/gap` twice with no changes produces the same report. Read-only until fix mode.

## Vocabulary

| Term | Meaning |
|------|---------|
| **target** | The folder or file set being checked |
| **corpus type** | What kind of content the target contains (skill, design-doc, test-cases, queries, mixed) |
| **gap** | An inconsistency, missing item, or broken reference within the target |
| **finding** | One specific gap with location, category, severity, and proposed fix |
| **coverage gap** | A requirement (AC, step, rule) that has no corresponding test case or verification |
| **dead reference** | A wikilink, path, or filename mentioned in text that doesn't resolve |
| **alignment gap** | Two artifacts that should correspond (TC↔query, AC↔TC, step↔file) but don't match |
| **fix mode** | After report, user can approve fixes one at a time or batch |

## Input

```
/gap [target-path]
/gap [target-path] --fix
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `target-path` | Folder or file to check | `.claude/skills/spawn-agent-swarm/` |
| `--fix` | Enter fix mode after report | `/gap projects/30-day-readmissions/autopend/ --fix` |

**Target types (auto-detected):**
- Skill folder (`.claude/skills/*/`) → reference, schema, count, terminology checks
- Design doc (`.claude/docs/design/*/`) → completeness checklist, reference resolution
- Test artifacts (contains `test-cases.md`, `tc-queries.sql`, etc.) → coverage, TC↔AC, TC↔query alignment
- Onboard run (contains `onboard-runs/`) → artifact completeness, cross-artifact consistency
- Any folder → best-effort: check file references, wikilinks, mentioned paths

## Output

Gap report grouped by category, then optional fix mode.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[gap-check/references/workflow]] | Steps 1-5: discover, detect type, check, report, fix |
| [[gap-check/references/gap-categories]] | Gap categories per corpus type with detection logic |
| [[gap-check/references/corpus-detection]] | How to detect corpus type from file content |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Discover | Glob target, load all files | File inventory | — |
| 2. Detect & Model | Detect corpus type, build internal model | Corpus type + reference model | — |
| 3. Check | Apply corpus-appropriate gap checks | Findings list | — |
| 4. Report | Present findings grouped by category | Gap report | — |
| 5. Fix | Apply approved fixes (if --fix or user requests) | Modified files | **Per-finding approval** |

## Critical Rules

1. **Never modify files during Steps 1-4.** Check phase is read-only. Fixes only in Step 5.
2. **Every finding needs a location.** `file_path:line_number` minimum.
3. **Detect corpus type automatically.** Never ask "what kind of files are these?"
4. **Severity is binary: ERROR or WARN.** ERROR = broken (dead ref, missing coverage). WARN = suspicious (unused term, possible stale content).
5. **Adapt checks to corpus.** Don't apply skill-folder checks to test cases. Don't apply coverage checks to design docs.
6. **Mixed targets are valid.** A folder with both skill files and test cases gets both check sets.

## Outer/Inner Loop Support

```
Outer loop (standalone):
  user → /gap [target]
    → reads files, detects type
    → applies checks
    → reports gaps
    → optional fix mode

Inner loop (called by other commands):
  /build-command Step 8 → /gap [skill folder]
  /create-test-artifacts Step 7 → /gap [onboard-run folder]
  /verify-sit-xlsx → /gap [sit artifacts]
```

## State Persistence

**None.** Stateless — each run is a fresh scan.

## Complete File Structure

**Skill package:**

```
.claude/commands/kernel/gap.md                       ← Layer 1
.claude/skills/gap-check/
├── SKILL.md                                         ← Layer 2
├── workflow.md, gate-contract.md                    ← Layer 2
├── steps/step-{01..05}-*.md                         ← Layer 3 (5 steps)
└── references/
    └── INDEX.md                                     ← Layer 4
```

**Design doc:**

```
.claude/docs/design/gap-check/
├── index.md                                         ← this file
└── references/
    ├── workflow.md                                  ← step details
    ├── gap-categories.md                            ← gap types per corpus type
    └── corpus-detection.md                          ← how to detect corpus type
```

---

**Version:** 1.1
**Last Updated:** 2026-06-20
**Changelog:**
- **v1.1:** Made dynamic — corpus type detection, context-appropriate checks, test case coverage support.
- **v1.0:** Initial design — skill-folder-only consistency checking.
