# Build conftest.py

## Context
Pytest fixtures — mock_ssh_interface, sample_host_config, mock_validator_results. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 055-061

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tests/conftest.py`
- Pytest fixtures — mock_ssh_interface, sample_host_config, mock_validator_results
- Must import cleanly: `python -c "import conftest"`

## Acceptance Criteria
- [ ] `conftest.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tests/conftest.py` (verify: file_exists)
- [ ] Imports without error (verify: run_code)

## Gates Satisfied
FAC-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
