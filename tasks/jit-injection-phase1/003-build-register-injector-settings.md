# Task 003: Register Injector in settings.local.json

**Type:** BUILD | **Gates:** JIT-03

## Action

Edit `.claude/settings.local.json` (ONE edit): APPEND `python .claude/hooks/jit-rule-injector.py` to PreToolUse for the Edit|Write|Bash matcher — existing enforcer commands must remain, order preserved, injector AFTER enforcers.

**Worktree note:** settings.local.json is GITIGNORED. If missing in your repo copy, first copy it verbatim from `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/settings.local.json`, then apply the merge. The orchestrator reapplies the change to main at validation.

Edit via Python json.load → modify → json.dump, UTF-8 no BOM. Never PowerShell (lesson #49).

## Acceptance

Parse succeeds; enforcer entries unchanged; injector present after them.
