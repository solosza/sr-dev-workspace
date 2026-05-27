# Test: spawned agent can read platform-docker repo

## Context
L2: verify agent can access template platform.

## Type
TEST

## Execution
agent

## Dependencies
- None

## Requirements
- Spawn agent. Have it read C:/Users/solos/my_ai_projects/platform-docker/FRAMEWORK.md and C:/Users/solos/my_ai_projects/platform-docker/framework/interfaces/image_interface.py (first 20 lines). Report contents.

## Acceptance Criteria
- [ ] Agent successfully reads both files (verify: agent reports content)

## Gates Satisfied
FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
