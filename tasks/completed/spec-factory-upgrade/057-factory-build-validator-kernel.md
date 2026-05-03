# Build kernel_validator.py

## Context
Layer 2 KernelValidator — verify kernel version, modules, sysctl parameters. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 055

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/validators/kernel_validator.py`
- Layer 2 KernelValidator — verify kernel version, modules, sysctl parameters
- Must import cleanly: `python -c "import kernel_validator"`

## Acceptance Criteria
- [ ] `kernel_validator.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/validators/kernel_validator.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
