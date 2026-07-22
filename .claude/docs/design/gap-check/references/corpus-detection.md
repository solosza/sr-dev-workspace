# Corpus Detection

How to detect what kind of content the target contains, so the right gap checks are applied.

---

## Dependency Traversal (CRITICAL)

Never check a target in isolation. **Follow the dependency chain down** — any file can reference other files, and those references are in scope.

**Examples of dependency chains:**

```
Command → Skill → Steps → References → Design Doc → Payloads
SKILL.md → workflow.md → gate-contract.md → step files → INDEX.md
Design doc index → references/ payloads → canonical references
test-cases.md → tc-queries.sql → verification-dump.sql
Backlog item → task folder → task files → gate contract
Stories → traceability matrix → test cases → queries
```

**Rule:** The scope of a gap check is the target **plus everything it references, recursively**. Any file that points to another file or folder brings that dependency into scope.

**How to traverse:**
1. Read the target file(s)
2. Extract all path references: `→` links, wikilinks `[[...]]`, backtick-quoted paths, `Skill Reference`, `Design Reference`, `Source:`, any `.claude/` or relative path
3. For each reference that is a folder → glob it recursively, add all files to inventory
4. For each reference that is a file → add it to inventory
5. Read newly added files, extract their references (recursive traversal, max depth 3)
6. Stop at depth 3 to avoid unbounded expansion

**What this enables:** `/gap` on any single file checks the full downstream tree. A test-cases.md check includes the queries it maps to. A SKILL.md check includes every step file it lists. A backlog item check includes its task folder.

## Detection Rules

Scan file names and content. Multiple types can co-exist (mixed corpus).

| Signal | Corpus Type |
|--------|-------------|
| Path contains `.claude/skills/` | **skill** |
| Path contains `.claude/docs/design/` | **design-doc** |
| File named `SKILL.md` | **skill** |
| File named `test-cases.md` | **test-cases** |
| File named `traceability-matrix.md` | **test-cases** |
| File named `tc-queries.sql` | **test-cases** |
| File named `verification-dump.sql` | **test-cases** |
| File named `test-cases-sit.xlsx` or `test-cases.xlsx` | **test-cases** |
| File contains `## Skill Identity` | **design-doc** |
| File contains `## Workflow Summary` with Step/Responsibility columns | **design-doc** |
| File contains `### AC-` patterns | **stories** (treat as test-cases source) |
| File contains `CREATE PROCEDURE` or `ALTER PROCEDURE` | **stored-procedures** |
| Folder named `onboard-runs/` | **onboard-run** (superset of test-cases) |
| Folder named `steps/` with `step-NN-*.md` files | **skill** |
| Folder named `references/` with `INDEX.md` | **skill** or **design-doc** |
| File named `gate-contract.md` | **skill** |
| File contains contract JSON (`contract_metadata`, `validations`) | **contract** |

## Priority

When multiple signals match, use the most specific:
1. **onboard-run** (superset — includes test-cases + evidence + queries)
2. **skill** or **design-doc** (from path or SKILL.md presence)
3. **test-cases** (from filename patterns)
4. **stories** or **stored-procedures** (from content patterns)
5. **generic** (fallback — reference checking only)

## Mixed Corpus Handling

A folder can contain multiple corpus types. Example:
```
projects/30-day-readmissions/autopend/
├── stories/         → stories corpus
├── sps/             → stored-procedures corpus
└── onboard-runs/    → onboard-run corpus (includes test-cases)
```

**Action:** Build models for each detected type. Apply all relevant gap checks. A gap between corpus types (e.g., story AC not covered by any TC) is the most valuable kind of finding.

## What Each Corpus Type Enables

| Corpus Type | What Gets Checked |
|-------------|-------------------|
| **skill** | wikilinks, step counts, vocabulary, schema, flow continuity |
| **design-doc** | completeness checklist (7 required sections), payload resolution, depth |
| **test-cases** | AC↔TC coverage, TC↔query alignment, traceability, expected results |
| **onboard-run** | all test-case checks + artifact completeness (all 7 onboard artifacts present) |
| **stories** | AC completeness (Given/When/Then present), AC numbering continuity |
| **stored-procedures** | table/column references consistent, JOIN logic complete |
| **contract** | rule IDs unique, canonical_reference paths resolve, severity values valid |
| **generic** | file path references, wikilinks, mentioned filenames |
