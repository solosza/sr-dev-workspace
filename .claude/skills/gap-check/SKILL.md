---
name: gap-check
version: 1.0
status: draft
type: skill
design_doc: .claude/docs/design/gap-check/index.md
design_doc_hash: 0b72c152b8baa8157be5a21e1fe03d7f3eba7bed6135fbda3b58b73ebf398ab1
---

# Gap Check — Skill

## Identity

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
| **alignment gap** | Two artifacts that should correspond (TC-query, AC-TC, step-file) but don't match |
| **fix mode** | After report, user can approve fixes one at a time or batch |

## Workflow

> `workflow.md` for phase details and state schema.

| Step | What It Does |
|------|-------------|
| 1. Discover | Glob target, load all files, build file inventory |
| 2. Detect & Model | Detect corpus type, build internal reference model |
| 3. Check | Apply corpus-appropriate gap checks against the model |
| 4. Report | Present findings grouped by category (errors first, then warnings) |
| 5. Fix | Apply approved fixes (if --fix or user requests) |

## Critical Rules

1. **Never modify files during Steps 1-4.** Check phase is read-only. Fixes only in Step 5.
2. **Every finding needs a location.** `file_path:line_number` minimum.
3. **Detect corpus type automatically.** Never ask "what kind of files are these?"
4. **Severity is binary: ERROR or WARN.** ERROR = broken (dead ref, missing coverage). WARN = suspicious (unused term, possible stale content).
5. **Adapt checks to corpus.** Don't apply skill-folder checks to test cases. Don't apply coverage checks to design docs.
6. **Mixed targets are valid.** A folder with both skill files and test cases gets both check sets.

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestrator |
| `workflow.md` | Phase definitions, state schema, HITL stops |
| `gate-contract.md` | Phase gates, per-step output validation |
| `steps/step-01-discover.md` | Glob target, load all files |
| `steps/step-02-detect-and-model.md` | Detect corpus type, build reference model |
| `steps/step-03-check.md` | Apply corpus-appropriate gap checks |
| `steps/step-04-report.md` | Present findings grouped by category |
| `steps/step-05-fix.md` | Apply approved fixes |
| `references/INDEX.md` | Reference index — links to design doc |
