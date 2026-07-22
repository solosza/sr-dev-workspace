# Verify Corpus Size ≥ 60K Tokens

## Context
Verify both corpora meet the 60K+ token minimum and that content matches between flat and tiered variants.

## Type
TEST

## Execution
agent

## Dependencies
- 003-build-assemble-flat-corpus
- 004-build-assemble-tiered-corpus

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md` exists

## Requirements
- Count characters in flat corpus, divide by 4 to estimate tokens — must be ≥ 60,000
- Count characters in tiered corpus — must be within 10% of flat
- Verify both contain content from all 5 skills (grep for skill-specific terms)
- Report exact token counts

## Acceptance Criteria
- [ ] Flat corpus ≥ 240,000 characters (60K tokens)
- [ ] Tiered corpus within ±10% of flat corpus size
- [ ] Both contain "check-data-engine" content (grep for "date registry" or "CLM-H")
- [ ] Both contain "healthcare-qa" content (grep for "readmission" or "30-day")
- [ ] Both contain "verify-sit-xlsx" content (grep for "SIT" or "verification")

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
