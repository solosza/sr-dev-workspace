# Run Sequential A/B Test (N=5)

## Context
Execute the sequential walkthrough task with both flat and tiered prompts, N=5 runs each. Total: 10 claude -p calls.

## Type
BUILD

## Execution
inline

## Dependencies
- 010-build-prompt-flat-sequential
- 011-build-prompt-tiered-sequential

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-flat-sequential.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-tiered-sequential.md` exists

## Requirements
- Run 5 iterations of each variant (10 total calls)
- For each run: `cat [prompt-file] | env -u CLAUDECODE claude -p > [output-file]`
- Output naming: `results/sequential-flat-run-N.txt` and `results/sequential-tiered-run-N.txt` (N=1..5)
- All output files in `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/`
- Run calls in background to parallelize where possible
- Wait for all 10 to complete before marking done
- Verify each output file is non-empty (>1000 bytes)

## Acceptance Criteria
- [ ] 5 files matching `results/sequential-flat-run-*.txt` exist and are non-empty
- [ ] 5 files matching `results/sequential-tiered-run-*.txt` exist and are non-empty

## Gates Satisfied
- FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
