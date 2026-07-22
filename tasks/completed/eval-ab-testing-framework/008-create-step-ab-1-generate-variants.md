# Task 008: Create step-ab-1-generate-variants.md

## Action
Create `.claude/skills/eval/steps/step-ab-1-generate-variants.md`.

## Content
Step file for A/B mode — generates flat and tiered variants using VariantGenerator from platform-deepeval.

Include:
- Input table (artifact path, output dir from step 0)
- Procedure: instantiate VariantGenerator, call generate(), verify both variants exist
- Verification gates (flat file exists, tiered dir copied, files_flattened > 0)
- Error handling (artifact not found, no .md files to flatten)

## Acceptance Criteria
- File exists at `.claude/skills/eval/steps/step-ab-1-generate-variants.md`
- References `platform-deepeval/framework/ab_testing/variant_generator.py`
- Under 100 lines
