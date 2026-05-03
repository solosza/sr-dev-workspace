# Build test_ssh_batch.py

## Context
Layer 5 pytest test suite — tests all layers with mocked SSH connections. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 055-061

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tests/test_ssh_batch.py`
- Layer 5 pytest test suite — tests all layers with mocked SSH connections
- Must import cleanly: `python -c "import test_ssh_batch"`

## Acceptance Criteria
- [ ] `test_ssh_batch.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tests/test_ssh_batch.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
