# Assemble Flat Corpus (60K+ Tokens)

## Context
Concatenate multiple hmsa-healthcare-qa domain skills into a single flat markdown document with no tiered indexing structure. This is Variant A of the A/B test.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Read ALL markdown files from these hmsa-healthcare-qa skills (in order):
  1. `healthcare-qa` (~38K tokens — the main QA skill with all rules)
  2. `check-data-engine` (~12K tokens — the agent workflow skill)
  3. `verify-sit-xlsx` (~20K tokens — SIT verification skill)
  4. `create-sit-xlsx` (~17K tokens — SIT creation skill)
  5. `create-test-artifacts` (~18K tokens — test artifact creation)
- Skills are at `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/skills/[name]/`
- For each skill, find all .md files recursively and concatenate them
- Separate each skill's content with a simple `---` divider and skill name header
- NO wikilinks, NO index, NO `→ [[reference]]` markers — just one continuous flat document
- The flat corpus should be a direct wall of text with simple section headers only
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md`
- Target: 60K+ tokens (≈240K+ characters)

## Acceptance Criteria
- [ ] `corpus-flat.md` exists at the specified path
- [ ] File contains content from all 5 skills
- [ ] No wikilinks or `→ [[` markers in the file
- [ ] File size ≥ 240,000 characters (60K tokens)

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
