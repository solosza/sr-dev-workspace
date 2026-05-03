# Build host_configs.json

## Context
CIQ image configs — RLC Pro + RLC Pro AI variants with realistic package/service data. This is part of the SSH spec reference code produced by the factory.

## Type
BUILD

## Dependencies
- 045, 047

## Phase Gate
- [ ] Design doc exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/step-04-design.md`

## Requirements
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/fixtures/host_configs.json`
- CIQ image configs — RLC Pro + RLC Pro AI variants with realistic package/service data


## Acceptance Criteria
- [ ] `host_configs.json` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/fixtures/host_configs.json` (verify: file_exists)


## Gates Satisfied
FAC-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
