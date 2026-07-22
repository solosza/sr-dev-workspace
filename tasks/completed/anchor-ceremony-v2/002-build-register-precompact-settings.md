# Task 002: Register PreCompact Hook in settings.local.json

**Type:** BUILD
**Gates Satisfied:** AC-02

## Action

Add a `PreCompact` entry to the `hooks` object in `.claude/settings.local.json` (ONE file edit).

## Spec

READ `.claude/settings.local.json` fully first (RULE ZERO). It already has `PreToolUse` and `PostToolUse` arrays — MERGE the new key, do not clobber anything.

**Worktree note:** settings.local.json is GITIGNORED. If it is missing from the repo you are executing in (fresh worktree), first copy it verbatim from the main repo: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/settings.local.json`, then apply the merge to the copy. The orchestrator applies the same change to main's copy at validation (a gitignored file cannot merge back via git).

Add:

```json
"PreCompact": [
  {
    "matcher": "auto|manual",
    "hooks": [
      { "type": "command", "command": "python .claude/hooks/precompact-reanchor.py" }
    ]
  }
]
```

Write the file via Python `json.dump` (indent 2, UTF-8 no BOM) or the Write tool after reading — NEVER PowerShell cmdlets (lesson #49).

## Acceptance Criteria (mechanical)

- `json.load` on settings.local.json succeeds
- `hooks.PreCompact[0].matcher == "auto|manual"`
- `hooks.PreCompact[0].hooks[0].command` contains `precompact-reanchor.py`
- Existing PreToolUse/PostToolUse entries unchanged (same count and commands as before edit)
