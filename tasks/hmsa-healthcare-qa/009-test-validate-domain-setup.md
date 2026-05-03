# Validate Domain-Setup Output

## Type
TEST

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Domain-setup has been run in target workspace

## Requirements
- Verify all domain-setup artifacts in `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`:
  1. `.claude/state/session_state.json` exists with `domain` field
  2. `.claude/state/*_workflow.json` exists with `setup_complete: true`
  3. `.claude/protocols/*-protocol.md` exists
  4. `.claude/settings.local.json` has `hooks` key with nested array format
  5. Settings uses string matchers (`"Write|Edit|Bash"`), NOT object matchers
- Report pass/fail for each check

## Acceptance Criteria
- [ ] All 5 verification checks pass
- [ ] No Settings Error format (string matchers confirmed)

## Gates Satisfied
- FUNC-01, FUNC-02, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
