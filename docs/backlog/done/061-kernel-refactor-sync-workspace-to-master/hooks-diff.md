# Hooks Diff — sr_dev_workspace → isagawa-kernel

## Status
NEW

## Source
sr_dev: `.claude/hooks/` (6 Python files)
Master: `.claude/hooks/` (2 Python files)

## Hooks That Differ (2)

| Hook | Diff Size | Action |
|------|-----------|--------|
| `universal-gate-enforcer.py` | 240 lines | Replace (massive evolution — anchor tokens, protocol hash, action limits) |
| `test-failure-detector.py` | 56 lines | Replace |

## Missing from Master (4)

| Hook | Purpose | Action |
|------|---------|--------|
| `actions-log-appender.py` | Append-only action ledger (PostToolUse) | Copy |
| `agent-inline-execution-blocker.py` | Block inline agent execution (PreToolUse) | Copy |
| `auto-approve-claude-writes.py` | Auto-approve .claude/ writes (PreToolUse) | Copy |
| `sr_dev-gate-enforcer.py` | Domain gate enforcer — copy as **template** | Copy as `[domain]-gate-enforcer.template.py` |

## Domain Gate Enforcer Note
`sr_dev-gate-enforcer.py` is domain-specific (sr_dev). For the master kernel repo, copy it as a template file that domain-setup can adapt per-repo.

## Settings Registration
Master's `settings.local.json` only registers 2 hooks (PreToolUse: universal-gate-enforcer, PostToolUse: test-failure-detector). After sync, update to register all 6:

**PreToolUse (Edit|Write|Bash):**
- `universal-gate-enforcer.py`

**PreToolUse (Agent):**
- `agent-inline-execution-blocker.py`

**PreToolUse (Write|Edit):**
- `auto-approve-claude-writes.py`

**PostToolUse (Bash):**
- `test-failure-detector.py`

**PostToolUse (Edit|Write|Bash):**
- `actions-log-appender.py`
