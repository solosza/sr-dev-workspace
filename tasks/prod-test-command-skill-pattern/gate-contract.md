# Gate Contract — Prod-Test Command-Skill-Pattern Refactor

## Phase 1: Create Missing Files

| Gate | Check | Method |
|------|-------|--------|
| G1.1 | `steps/` directory exists | `test -d .claude/skills/prod-test/steps/` |
| G1.2 | `workflow.md` exists | `test -f .claude/skills/prod-test/workflow.md` |
| G1.3 | `gate-contract.md` exists | `test -f .claude/skills/prod-test/gate-contract.md` |
| G1.4 | `references/INDEX.md` exists | `test -f .claude/skills/prod-test/references/INDEX.md` |

## Phase 2: Move Step Files

| Gate | Check | Method |
|------|-------|--------|
| G2.1 | All 8 step files in steps/ | `ls .claude/skills/prod-test/steps/step-*.md` returns 8 files |
| G2.2 | No step files in references/ | `ls .claude/skills/prod-test/references/step-*.md` returns 0 files |
| G2.3 | File content unchanged | Content identical before/after move |

## Phase 3: Update Pointers

| Gate | Check | Method |
|------|-------|--------|
| G3.1 | SKILL.md has Identity section | `grep "## Identity" SKILL.md` |
| G3.2 | SKILL.md has Vocabulary section | `grep "## Vocabulary" SKILL.md` |
| G3.3 | SKILL.md has File Index section | `grep "## File Index" SKILL.md` |
| G3.4 | SKILL.md step table points to steps/ | `grep "steps/step-" SKILL.md` returns 8 matches |
| G3.5 | SKILL.md has no references/step- pointers | `grep "references/step-" SKILL.md` returns 0 matches |
| G3.6 | CLAUDE.md step table points to steps/ | `grep "steps/step-" CLAUDE.md` returns 8 matches for prod-test section |
| G3.7 | CLAUDE.md has no references/step- for prod-test | prod-test section uses steps/ not references/ |

## Phase 4: Verification

| Gate | Check | Method |
|------|-------|--------|
| G4.1 | No behavioral changes | Step file content unchanged from original |
| G4.2 | All wikilinks resolve | Every `→` link in SKILL.md/workflow.md points to existing file |
| G4.3 | Structure matches eval skill | Same directory layout as `.claude/skills/eval/` |
