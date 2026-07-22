# Run Cross-Reference A/B Test (N=5)

## Context
Execute the cross-reference task with both flat and tiered prompts, N=5 runs each. Total: 10 claude -p calls.

## Type
BUILD

## Execution
inline

## Dependencies
- 014-build-prompt-flat-crossref
- 015-build-prompt-tiered-crossref

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-flat-crossref.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-tiered-crossref.md` exists

## Requirements
- Run 5 iterations of each variant (10 total calls)
- For each run: `cat [prompt-file] | env -u CLAUDECODE claude -p > [output-file]`
- Output naming: `results/crossref-flat-run-N.txt` and `results/crossref-tiered-run-N.txt` (N=1..5)
- All output files in `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/`
- Run calls in background to parallelize where possible
- Wait for all 10 to complete before marking done
- Verify each output file is non-empty (>1000 bytes)

## Acceptance Criteria
- [ ] 5 files matching `results/crossref-flat-run-*.txt` exist and are non-empty
- [ ] 5 files matching `results/crossref-tiered-run-*.txt` exist and are non-empty

## Gates Satisfied
- FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
