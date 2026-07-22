# Task 004: Raise actions_limit Seed Default to 50 in Domain-Setup Template

**Type:** BUILD
**Gates Satisfied:** AC-04

## Action

Update the workflow-state seed template in `.claude/skills/kernel-domain-setup/references/step-10-state.md`: `"actions_limit": 10` → `"actions_limit": 50` (ONE edit).

## Spec

READ the file first (RULE ZERO). Backlog 245 requires "actions_limit 30 → 50 in workflow state seeding + anywhere hardcoded" — the seed template is the seeding site (currently seeds 10). New domains created by `/kernel/domain-setup` get the hybrid-policy default.

Do NOT change the fallback default `10` inside `universal-gate-enforcer.py` — that is the no-config safety fallback, not a seeding site, and Gate 3 must not be modified.

Add one sentence near the seed noting the hybrid policy: timer at 50 is paired with the PreCompact re-anchor hook (backlog 245).

## Acceptance Criteria (mechanical)

- grep `"actions_limit": 50` hits in step-10-state.md
- grep `"actions_limit": 10` has zero hits in step-10-state.md
- `git diff HEAD -- .claude/hooks/universal-gate-enforcer.py` is empty
