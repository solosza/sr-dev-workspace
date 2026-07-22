# Task 002: Build variant_generator.py

## Action
Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/variant_generator.py`.

## Requirements

Implements the `VariantGenerator` class with:

1. `__init__(self, artifact_path: Path)` — accepts path to a tiered artifact directory (containing SKILL.md or a command .md)
2. `generate(self, output_dir: Path) -> dict` — produces both variants:
   - `output_dir/flat/artifact-flat.md` — all content flattened into one file
   - `output_dir/tiered/` — original structure copied as-is
   - Returns `{"flat_path": Path, "tiered_path": Path, "files_flattened": int}`

### Flattening Algorithm
1. Find root file (SKILL.md or first .md in directory)
2. Parse internal references: `→` links, wikilinks `[[...]]`, "Read and follow:" directives
3. Topological sort by dependency (parent before child)
4. For each file in order:
   - Strip index-only content (file tables, "Reading Order" sections, navigation headers)
   - Keep payload content (rules, steps, criteria, examples, code blocks)
   - Append with `## [filename]` section headers
5. Remove checkpoint directives ("Pre-Generation Checkpoint", "Directed Reading")
6. Remove contract references (gate-contract, dual gate sections)
7. Write single concatenated file

### Key Rules
- Deterministic — no LLM calls, pure file processing
- Preserve ALL payload content — same knowledge, different structure
- External references (URLs, absolute paths) stay as-is
- Handle circular references gracefully (detect and break cycles)

## Acceptance Criteria
- File exists at the specified path
- `VariantGenerator` class with `generate()` method
- Handles SKILL.md-based skills and command .md-based commands
- No external dependencies beyond stdlib + pathlib
