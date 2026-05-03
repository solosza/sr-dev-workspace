# Build ssh_interface.py

## Context
Layer 1 paramiko wrapper — SSHInterface class with retry logic, auth handling, context manager. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 047

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/ssh_interface.py`
- Layer 1 paramiko wrapper — SSHInterface class with retry logic, auth handling, context manager
- Must import cleanly: `python -c "import ssh_interface"`

## Acceptance Criteria
- [ ] `ssh_interface.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/ssh_interface.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-08, FAC-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
