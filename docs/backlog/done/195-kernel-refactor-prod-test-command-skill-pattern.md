# Refactor prod-test Skill to Command-Skill-Pattern Compliance

## Status
Open

## Priority
Medium — prod-test works but its file structure predates the command-skill-pattern and tiered-index-architecture designs. Step files live in `references/` instead of `steps/`. Missing `workflow.md`, `gate-contract.md`, and `references/INDEX.md`. SKILL.md lacks Philosophy, Vocabulary, and File Index sections. Bringing it into compliance ensures consistency across all kernel skills and enables contract-based validation.

## Summary

The `.claude/skills/prod-test/` skill was built before the command-skill-pattern was formalized. It needs structural refactoring to match the canonical 6-layer architecture. No behavioral changes — same steps, same logic, same outcomes. Pure structural compliance refactor.

## Current State (Non-Compliant)

```
.claude/skills/prod-test/
|-- SKILL.md                        (missing Philosophy, Vocabulary, File Index)
|-- references/
|   |-- step-01-parse.md            (should be in steps/)
|   |-- step-02-master.md           (should be in steps/)
|   |-- step-03-validate.md         (should be in steps/)
|   |-- step-04-copy.md             (should be in steps/)
|   |-- step-05-infra.md            (should be in steps/)
|   |-- step-06-inner-tasks.md      (should be in steps/)
|   |-- step-07-execute.md          (should be in steps/)
|   +-- step-08-report.md           (should be in steps/)
```

**Missing:** `workflow.md`, `gate-contract.md`, `references/INDEX.md`

## Target State (Compliant)

```
.claude/skills/prod-test/
|-- SKILL.md                        (+ Identity, Philosophy, Vocabulary, File Index)
|-- workflow.md                     (NEW — phase definitions, state schema)
|-- gate-contract.md                (NEW — phase gates, verification criteria)
|-- steps/
|   |-- step-01-parse.md            (MOVED from references/)
|   |-- step-02-master.md           (MOVED from references/)
|   |-- step-03-validate.md         (MOVED from references/)
|   |-- step-04-copy.md             (MOVED from references/)
|   |-- step-05-infra.md            (MOVED from references/)
|   |-- step-06-inner-tasks.md      (MOVED from references/)
|   |-- step-07-execute.md          (MOVED from references/)
|   +-- step-08-report.md           (MOVED from references/)
+-- references/
    +-- INDEX.md                    (NEW — tiered index with wikilinks)
```

## Design Documents

| Document | Purpose |
|----------|---------|
| `.claude/docs/design/command-skill-pattern/index.md` | Canonical 6-layer architecture |
| `.claude/docs/design/command-skill-pattern/references/file-structure.md` | Target file tree |
| `.claude/docs/design/command-skill-pattern/references/layers.md` | Layer 2 SKILL.md structure template |
| `.claude/docs/design/command-skill-pattern/references/completeness-checklist.md` | Required sections checklist |
| `.claude/docs/design/tiered-index-architecture/index.md` | Index vs payload rule, 200-line threshold |

## Architecture

```
Phase 1: Create missing files
  |-- workflow.md (extract workflow from SKILL.md, add state schema)
  |-- gate-contract.md (define per-step acceptance criteria)
  +-- references/INDEX.md (tiered index with wikilinks by step)
         |
Phase 2: Move step files
  |-- references/step-01-parse.md -> steps/step-01-parse.md
  |-- references/step-02-master.md -> steps/step-02-master.md
  |-- references/step-03-validate.md -> steps/step-03-validate.md
  |-- references/step-04-copy.md -> steps/step-04-copy.md
  |-- references/step-05-infra.md -> steps/step-05-infra.md
  |-- references/step-06-inner-tasks.md -> steps/step-06-inner-tasks.md
  |-- references/step-07-execute.md -> steps/step-07-execute.md
  +-- references/step-08-report.md -> steps/step-08-report.md
         |
Phase 3: Update SKILL.md
  |-- Add Identity section (one-sentence role)
  |-- Add Philosophy section (3-5 guiding principles)
  |-- Add Vocabulary section (domain terms)
  |-- Add File Index section (all files in skill package)
  |-- Update step table pointers (references/ -> steps/)
  +-- Fix any stale examples or dead references
         |
Phase 4: Update CLAUDE.md
  +-- Update prod-test step table to point to steps/ instead of references/
```

## Requirements
- All 8 step files move from `references/` to `steps/` — file content unchanged
- `workflow.md` created with phase definitions matching existing SKILL.md workflow
- `gate-contract.md` created with per-step acceptance criteria
- `references/INDEX.md` created following tiered-index wikilink format
- SKILL.md gains Identity, Philosophy, Vocabulary, File Index sections per command-skill-pattern Layer 2 template
- SKILL.md step table updated: `references/step-NN-*.md` -> `steps/step-NN-*.md`
- CLAUDE.md prod-test section updated: `references/step-NN-*.md` -> `steps/step-NN-*.md`
- No behavioral changes — same steps, same logic, same outcomes
- Compliant skill `.claude/skills/eval/` is the canonical reference for structural compliance

## References
- **Canonical compliance example:** `.claude/skills/eval/` (already compliant with command-skill-pattern)
- **Command-skill-pattern:** `.claude/docs/design/command-skill-pattern/index.md`
- **Tiered-index-architecture:** `.claude/docs/design/tiered-index-architecture/index.md`
- **Current prod-test skill:** `.claude/skills/prod-test/`
- **Prod-test command:** `.claude/commands/kernel/prod-test.md`

## Task Builder Input
- **Deliverable:** Refactored `.claude/skills/prod-test/` directory matching command-skill-pattern canonical structure
- **Location:** `D:/my_ai_projects/project_test_repos/sr_dev_workspace`
- **Scope:** REFACTOR
- **Constraints:** No behavioral changes. Move files, create missing structural files, update pointers. Use `.claude/skills/eval/` as the canonical reference for what compliant structure looks like. Read each design document before writing its corresponding artifact.
