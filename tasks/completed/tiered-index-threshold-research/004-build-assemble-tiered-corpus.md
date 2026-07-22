# Assemble Tiered Corpus (60K+ Tokens)

## Context
Organize the same hmsa-healthcare-qa domain skills using the tiered index pattern — a master index with wikilinks pointing to organized sections, preserving the natural skill file hierarchy. This is Variant B of the A/B test.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Read ALL markdown files from the SAME 5 skills as the flat corpus:
  1. healthcare-qa, 2. check-data-engine, 3. verify-sit-xlsx, 4. create-sit-xlsx, 5. create-test-artifacts
- Organize with a TIERED INDEX at the top:
  - Master index listing all skills with `→ [[section-name]]` wikilinks
  - Each skill's SKILL.md content preserved as a section with its own sub-index
  - Reference files organized under their parent skill with proper headings
  - Cross-references between skills use wikilinks
- The content is the SAME as flat — just organized differently
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md`
- Must be a single file (will be piped to claude -p), but internally organized with tiered structure

## Acceptance Criteria
- [ ] `corpus-tiered.md` exists at the specified path
- [ ] File contains a master index section at the top with wikilinks
- [ ] File contains content from all 5 skills (same content as flat)
- [ ] Contains `→ [[` or `→ [` markers for tiered organization
- [ ] File size approximately matches flat corpus (±10%)

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
