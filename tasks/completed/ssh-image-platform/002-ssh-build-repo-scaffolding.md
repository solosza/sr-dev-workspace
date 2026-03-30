# Build Repo Scaffolding

## Type
BUILD

## Context
Create the platform-ssh repo structure using platform-docker as the template. Replace Docker CLI references with SSH. Set up the 5-layer directory structure.

## Dependencies
- 001 (research — need CIQ product info for README)

## Phase Gate
- [ ] `docs/research/ciq-product-analysis.md` exists

## Requirements
- Create repo directory (local — not GitHub yet)
- Create directory structure matching 5-layer pattern:
  ```
  framework/_reference/
  framework/_reference/validators/
  framework/_reference/tasks/
  framework/_reference/roles/
  framework/_reference/tests/
  framework/_reference/fixtures/
  framework/resources/
  .claude/skills/ssh-management-layer/
  .claude/skills/ssh-management-layer/references/
  docs/research/
  ```
- Create `requirements.txt` with paramiko, pytest
- Create `FRAMEWORK.md` explaining the 5-layer SSH adaptation
- Create `README.md` with project overview, install flow, CIQ context
- Create `__init__.py` files for Python package imports

## Acceptance Criteria
- [ ] Repo directory exists with correct structure
- [ ] `requirements.txt` has `paramiko` and `pytest`
- [ ] `FRAMEWORK.md` exists and references 5 layers
- [ ] `README.md` exists with install instructions
- [ ] All `__init__.py` files present for Python imports

## Gates Satisfied
BUILD-03, BUILD-04, BUILD-08, DOC-01, DOC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
