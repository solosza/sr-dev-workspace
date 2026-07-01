# Test Tier 3 observatory components

## Context
Validates the observatory repo's core components: aggregate.py processes sample metrics, evaluate_experiments.py handles experiments, and extension commands are well-formed.

## Type
TEST

## Execution
agent

## Dependencies
- 014 (evaluate_experiments.py), 016 (eval command), 017 (rollback command)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/lib/aggregate.py` exists
- [ ] `D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py` exists
- [ ] `D:/my_ai_projects/kernel-observatory/commands/kernel/eval.md` exists
- [ ] `D:/my_ai_projects/kernel-observatory/commands/kernel/rollback.md` exists

## Requirements
- Test aggregate.py with sample metrics data:
  - Create a temporary metrics.jsonl with 3 event types
  - Run `python aggregate.py --file <temp>` and verify output
- Test evaluate_experiments.py with sample experiment data:
  - Create temp experiments.jsonl + metrics.jsonl
  - Run `python evaluate_experiments.py --experiments <temp-exp> --metrics <temp-met>`
  - Verify it handles empty input gracefully
- Verify eval.md references correct paths and tools
- Verify rollback.md references correct paths and includes cascade detection

## Acceptance Criteria
- [ ] aggregate.py processes sample metrics and produces output
- [ ] evaluate_experiments.py handles empty input without error
- [ ] eval.md is a valid command document with correct references
- [ ] rollback.md includes cascade detection logic

## Gates Satisfied
- TEST-03, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
