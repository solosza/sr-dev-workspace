# Test: spawned agent executes one factory step

## Context
L3: spawn agent in factory context, have it run step 1 (decompose) for SSH domain using platform-docker as template.

## Type
TEST

## Execution
agent

## Dependencies
- 006, 007

## Phase Gate
- [ ] Agent can read factory + platform-docker (006, 007)

## Requirements
- Spawn agent with prompt:
- Read C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/steps/step-01.md for decomposition process
- Read C:/Users/solos/my_ai_projects/platform-docker/FRAMEWORK.md for the template platform architecture
- Read C:/Users/solos/my_ai_projects/platform-docker/framework/interfaces/image_interface.py for the foundation layer
- Produce a decomposition document for SSH image testing that maps platform-docker's 5-layer architecture
- Write to C:/Users/solos/my_ai_projects/domain-spec-factory/research/ssh-image-testing_decomposition_v2.md

## Acceptance Criteria
- [ ] Decomposition doc exists at factory research dir (verify: file_exists)

## Gates Satisfied
PROD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
