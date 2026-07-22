# Task 007: L1 Test — Files Exist + Registration + Constraint Gates

**Type:** TEST (L1 — does it exist?)
**Gates Satisfied:** AC-09 (+ structural halves of AC-01, AC-02, AC-05, AC-06)

## Action

Run ONE verification script (Python, absolute paths, no cd) that checks:

1. `.claude/hooks/precompact-reanchor.py` exists and `py_compile`s
2. `settings.local.json` parses; `hooks.PreCompact` present with matcher `auto|manual` and command referencing `precompact-reanchor.py`; PreToolUse/PostToolUse arrays intact
3. anchor.md: ledger schema greps (Step 10), read-back grep (Step 5), `compaction_anchor_reason` (Step 14), 244 routing section intact
4. step-10-state.md: `"actions_limit": 50` present, `"actions_limit": 10` absent
5. Constraint gates (AC-09): `git diff HEAD -- .claude/hooks/universal-gate-enforcer.py` empty; no `rolling-summary` / periodic-summarizer hook file exists in `.claude/hooks/`

## Acceptance Criteria

- Script exits 0 with per-check PASS lines
- Any FAIL → fix the corresponding build task output → re-run → /kernel/learn after fix
