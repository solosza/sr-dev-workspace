# Create runner.py — Pipeline Orchestrator + CLI

## Context
Chains all modules together: extract -> replace -> leak_detect -> (optional refine). CLI entry point for the tool.

## Type
BUILD

## Execution
inline

## Dependencies
- 007-build-extract
- 008-build-catalog-replace
- 009-build-leak-detector
- 010-build-refine
- 011-build-reverse

## Phase Gate
- [ ] All 5 core modules exist in `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/`

## Requirements
- Function `run_pipeline(input_path: str, output_dir: str, mapping_store_path: str | None = None, refine: bool = False) -> PipelineResult`
- Pipeline steps:
  1. Read input .sql file
  2. Extract identifiers (extract.py)
  3. Replace all identifiers (catalog_replace.py)
  4. Run leak detector (leak_detector.py)
  5. If refine=True, run refinement pass (refine.py)
  6. Write sanitized .sql to output_dir
  7. Write mapping JSON to output_dir
  8. Write leak report JSON to output_dir
- CLI via `if __name__ == "__main__"` and/or `main()` function:
  - `python -m sp_sanitizer.runner <input.sql> --output-dir <dir> [--mapping-store <path>] [--refine]`
  - Support single file or glob of .sql files
- Exit code: 0 if all files CLEAN, 1 if any FLAGGED
- Print summary to stdout

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/runner.py` exists
- [ ] Exports `run_pipeline` function
- [ ] Has `main()` function or `if __name__ == "__main__"` block
- [ ] Accepts `--output-dir` CLI argument

## Gates Satisfied
- BUILD-12, FUNC-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
