# Production test: run kernel session in updated repo

## Context
L3: spawn agent to start a session, anchor, verify state changes. Proves the full kernel loop works.

## Type
TEST

## Execution
agent

## Dependencies
- 021, 022

## Phase Gate
- [ ] CLAUDE.md updated (021), hooks tested (022)

## Requirements
- Spawn agent in C:/Users/solos/my_ai_projects/isagawa-kernel/. Create minimal state files, run session-start + anchor. Verify session_started: true and anchored: true in state.

## Acceptance Criteria
- [ ] session_started + anchored = true (verify: read JSON)

## Gates Satisfied
PROD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
