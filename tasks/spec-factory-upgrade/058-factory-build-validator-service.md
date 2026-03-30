# Build service_validator.py

## Context
Layer 2 ServiceValidator — verify systemd services running, enabled state. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 055

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/validators/service_validator.py`
- Layer 2 ServiceValidator — verify systemd services running, enabled state
- Must import cleanly: `python -c "import service_validator"`

## Acceptance Criteria
- [ ] `service_validator.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/validators/service_validator.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
