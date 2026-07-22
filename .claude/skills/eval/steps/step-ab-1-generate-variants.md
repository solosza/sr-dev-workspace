# Step AB-1: Generate Variants

Generate flat and tiered variants of the artifact under test using `VariantGenerator` from `platform-deepeval/framework/ab_testing/variant_generator.py`.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `source_path` | Output of Step 0 | `D:\my_ai_projects\project_test_repos\kernel-minimal` |
| `target` | Output of Step 0 | `domain-setup` |
| `test_repo_name` | Output of Step 0 | `eval-domain-setup` |

## Procedure

1. **Resolve artifact path:**
   ```
   artifact_path = source_path / ".claude/skills/{target}/"
   ```
   If not found under skills, check `.claude/commands/{target}/` and `.claude/commands/{target}.md`.

2. **Set output directory:**
   ```
   output_dir = evals/{test_repo_name}/variants/
   ```

3. **Instantiate and run VariantGenerator:**
   ```python
   from framework.ab_testing.variant_generator import VariantGenerator
   from pathlib import Path

   gen = VariantGenerator(artifact_path)
   result = gen.generate(output_dir)
   # result: {"flat_path": Path, "tiered_path": Path, "files_flattened": int}
   ```

4. **Verify outputs:**
   - `output_dir/flat/{artifact-name}-flat.md` exists and is non-empty
   - `output_dir/tiered/` exists and contains at least one .md file
   - `files_flattened > 0`

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| GAB1.1 | Flat variant exists | `test -f output_dir/flat/*-flat.md` | File present, size > 0 |
| GAB1.2 | Tiered variant exists | `test -d output_dir/tiered/` | Dir has .md files |
| GAB1.3 | Files flattened > 0 | Check `result["files_flattened"]` | Integer > 0 |

All checks must pass before transitioning to Step AB-2.

## Error Handling

| Failure | Action |
|---------|--------|
| Artifact path not found | Abort — target not in source repo. List available skills/commands. |
| No .md files to flatten | Abort — artifact has no markdown content to compare. |
| Write permission error | Check output_dir permissions. Retry once. |

## Output

- `flat_path`: path to the flattened single-file variant
- `tiered_path`: path to the copied tiered directory variant
- `files_flattened`: count of files merged into flat variant
- State transition: `resolving_source` -> `variants_generated` -> ready for Step AB-2
