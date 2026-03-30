# Production Test: Full Kernel Session in Spec Factory

## Context
Level 3 production test: spawn run-task.sh in the spec factory repo with a simple task. This exercises the FULL kernel loop (session-start, anchor, work, complete) under real enforcement. Implicitly tests: hooks fire (actions_since_anchor increments), commands load (session-start/anchor execute), skills are discoverable (SKILL.md readable), settings are valid (hooks registered and triggering).

## Type
TEST

## Dependencies
- 022, 023

## Phase Gate
- [ ] settings.local.json updated with all hooks (task 022)
- [ ] CLAUDE.md updated with all commands/skills (task 023)

## Requirements
- Initialize state files in `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/state/`:
  - Create `session_state.json` with `{"session_started": false, "domain": "spec_factory"}`
  - Create `spec_factory_workflow.json` with `{"domain": "spec_factory", "anchored": false, "actions_since_anchor": 0, "actions_limit": 10}`
- Create a simple test task at `C:/Users/solos/my_ai_projects/domain-spec-factory/tasks/kernel-test/001-create-marker.md` that writes a marker file
- Create `C:/Users/solos/my_ai_projects/domain-spec-factory/tasks/kernel-test/000-index.md` with task table
- Spawn `bash C:/Users/solos/my_ai_projects/domain-spec-factory/run-task.sh C:/Users/solos/my_ai_projects/domain-spec-factory 3` in background
- Wait for completion notification
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/state/spec_factory_workflow.json`
- Verify `actions_since_anchor` > 0 (hooks fired)
- Verify `anchored: true` (anchor ran)
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/state/session_state.json`
- Verify `session_started: true`

## Acceptance Criteria
- [ ] run-task.sh exited (verify: background task completed)
- [ ] `actions_since_anchor` > 0 in workflow state (verify: read JSON — proves hooks fire)
- [ ] `session_started: true` in session state (verify: read JSON — proves session-start ran)
- [ ] `anchored: true` in workflow state (verify: read JSON — proves anchor ran)

## Gates Satisfied
PROD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
