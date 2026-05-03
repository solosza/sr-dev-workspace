# Build eval_config.py

## Context
SSH test configuration schema — validator thresholds, timeouts, retry config. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 047

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/resources/eval_config.py`
- SSH test configuration schema — validator thresholds, timeouts, retry config
- Must import cleanly: `python -c "import eval_config"`

## Acceptance Criteria
- [ ] `eval_config.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/resources/eval_config.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
