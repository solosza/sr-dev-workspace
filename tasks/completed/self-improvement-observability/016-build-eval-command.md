# Create /kernel/eval extension command

## Context
The /kernel/eval command runs the full eval suite on demand — invokes platform-deepeval with --harness-root, logs results to eval-results.jsonl, compares to historical trends, and checks active experiments.

## Type
BUILD

## Execution
inline

## Dependencies
- 005 (aggregate.py), 014 (evaluate_experiments.py)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/lib/aggregate.py` exists
- [ ] `D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py` exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/commands/kernel/eval.md`
- Command instructions:
  1. Check for platform-deepeval availability (graceful skip if missing)
  2. Check OPENAI_API_KEY for GEval tests (structural tests always run, GEval only with valid key)
  3. Run structural tests: `python -m pytest "[platform-deepeval]/tests/" --harness-root "[workspace-root]" --rootdir "[platform-deepeval]" -k "structural" --tb=short -q`
  4. If OPENAI_API_KEY valid: run GEval tests (warn about ~$0.10 cost)
  5. Log results to `.claude/state/eval-results.jsonl`
  6. Run aggregate.py to compare current results to historical trend
  7. Run evaluate_experiments.py to check active experiments
  8. Report summary: tests passed/failed, trend direction, experiment verdicts
- Installable: copied to workspace `.claude/commands/kernel/eval.md`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/commands/kernel/eval.md` exists
- [ ] Command references platform-deepeval with --harness-root
- [ ] Command includes eval-results.jsonl logging
- [ ] Command references aggregate.py and evaluate_experiments.py
- [ ] Command handles missing platform-deepeval gracefully

## Gates Satisfied
- BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
