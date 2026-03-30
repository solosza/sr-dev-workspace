# Build run_ssh_command.py

## Context
Layer 3 run_ssh_command function — wraps SSHInterface.execute with exit code checking. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 055

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tasks/run_ssh_command.py`
- Layer 3 run_ssh_command function — wraps SSHInterface.execute with exit code checking
- Must import cleanly: `python -c "import run_ssh_command"`

## Acceptance Criteria
- [ ] `run_ssh_command.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tasks/run_ssh_command.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
