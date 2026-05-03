# Preservation Rules — What to Keep vs Replace

## Status
NEW

## Core Principle

**Kernel infrastructure = replace with master. Domain content = preserve.**

## Always Replace (Kernel Infrastructure)

These files are kernel infrastructure. The master version is always authoritative:

- `.claude/commands/kernel/*.md` — all 15 commands
- `.claude/skills/autonomous-cycling/` — loop behavior spec
- `.claude/skills/kernel-domain-setup/` — protocol creation
- `.claude/skills/audit-workflow/` — gap scanning
- `.claude/skills/execute-pipeline/` — autonomous pipeline
- `.claude/skills/prod-test/` — production testing
- `.claude/skills/task-builder/` — goal decomposition
- `.claude/hooks/universal-gate-enforcer.py` — session/anchor gates
- `.claude/hooks/test-failure-detector.py` — learn enforcement
- `.claude/hooks/actions-log-appender.py` — action ledger
- `.claude/hooks/auto-approve-claude-writes.py` — permission bypass
- `.claude/hooks/agent-inline-execution-blocker.py` — inline agent block
- `run-task.sh`, `lib/common.sh`, `lib/attestation/intent.py`

## Always Preserve (Domain Content)

These are domain-specific and must not be overwritten:

- `.claude/commands/` (non-kernel) — e.g., `qa-workflow.md`, `game-build.md`, `eval-dev.md`
- `.claude/skills/[domain-specific]/` — e.g., `game-engine/`, `healthcare-qa/`, `qa-management-layer/`, `content-production/`, `website-cloner/`
- `.claude/protocols/[domain]-protocol.md` — domain protocol content (but UPDATE to add kernel command references)
- `.claude/lessons/` — domain-specific lessons
- `.claude/state/` — runtime state, never touch

## Evaluate Case-by-Case

- `.claude/hooks/[domain]-gate-enforcer.py` — keep if it has real domain-specific gates; replace pattern to match master's `sr_dev-gate-enforcer.py` structure
- `.claude/hooks/code-quality-enforcer.py` — evaluate: is this a domain concern or superseded by universal-gate-enforcer?
- `.claude/hooks/audit-trail-writer.py` — legacy, likely superseded by actions-log-appender
- `.claude/hooks/qa-gate-enforcer.py` — legacy, likely superseded by universal-gate-enforcer
- `.claude/hooks/playwright-gate-enforcer.py` — legacy, likely superseded by universal-gate-enforcer
