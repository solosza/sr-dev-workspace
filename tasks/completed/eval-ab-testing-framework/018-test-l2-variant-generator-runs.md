# Task 018: L2 Test — Run VariantGenerator Against check-data-engine

## Action
Run `variant_generator.py` against the check-data-engine skill from hmsa-healthcare-qa and verify it produces valid output.

## Steps

1. Run the variant generator:
   ```python
   import sys
   sys.path.insert(0, "D:/my_ai_projects/project_test_repos/platform-deepeval")
   from framework.ab_testing import VariantGenerator
   from pathlib import Path

   vg = VariantGenerator(Path("D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/skills/check-data-engine"))
   result = vg.generate(Path("D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/variants"))
   print(result)
   ```

2. Verify output:
   - `variants/flat/artifact-flat.md` exists and is non-empty
   - `variants/tiered/` exists and contains SKILL.md + subdirectories
   - `result["files_flattened"]` > 0
   - Flat file contains content from multiple source files (not just the root)

## Acceptance Criteria
- VariantGenerator imports without error
- `generate()` completes without exception
- Both variant directories contain expected files
- Flat file line count > tiered SKILL.md line count (proves flattening worked)
