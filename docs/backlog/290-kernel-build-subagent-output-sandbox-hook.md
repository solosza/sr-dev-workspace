# Subagent Output-Sandbox Hook — Confine Writes, Block Runner-Owned State

## Status
Open

## Priority
High — subagents mis-write and clobber even when the prompt forbids it. Prevention-by-hook is the hard fix; this converts two failure modes observed live this session into "impossible."

## Summary
A PostToolUse (and/or PreToolUse) hook that **confines a subagent's Write/Edit to its assigned output directory** and **blocks writes to runner-owned state files**. Mechanical prevention, not prompt hope — the same reason the gate-enforcer's `cd`/`intent.py` blocks work: an agent cannot bypass a hook. Reframes the reliability lesson from this session: you don't make the agent obedient, you make the forbidden action impossible.

## Evidence (this session)
- **Wrong-path write:** the gdpr-compliance factory step-6 agent wrote `SKILL.md` to the kernel's own `.claude/skills/gdpr-compliance/SKILL.md` instead of `output/gdpr-compliance/.claude/skills/...`. The runner's completion-truth *caught* it after 3 retries — a hook would have *prevented* it on the first Write.
- **State clobber:** agents wrote `factory_state.json` (a full template with `step_7..12:false`) that wiped the runner's `step_1..4` flags — despite the runner prompt saying "don't." Prose didn't hold; only the runner's re-derive/self-heal + a hard block will.

## Requirements
- **Output confinement:** given an agent's assigned output root (e.g. `AGENT_OUTPUT_DIR` / `output/{domain}/` / a task subfolder), reject any Write/Edit whose target resolves outside it — with a clear message naming the allowed root. Allow reads anywhere.
- **Runner-owned-state block:** block agent Write/Edit to files the runner owns (`*_factory_state.json`, and configurably other orchestrator state) so only the runner writes them.
- **Scoped activation:** only active for subagent/one-shot sessions (keyed off `one_shot`/`KERNEL_AGENT_ID`/an env flag), so the interactive session and the orchestrator are unaffected.
- **Escape hatch:** a documented, marked env var (like `KERNEL_BACKLOG_INTENT`) for the rare legitimate cross-dir write, so the sanctioned path exists but casual bypass doesn't.
- **Parity + portability:** ship in `sr_dev` hooks first, then fold into kernel-minimal (canonical) so every harness inherits it.

## References
- The reliability framework discussed 2026-07-23 (verify-at-boundary + isolation + hooks + checkable contracts). This is the "hooks for prevention of the forbidden" lever.
- Existing prevention hooks: `.claude/hooks/sr_dev-gate-enforcer.py` (cd block, intent.py block) — same pattern.
- Pairs with [[291-kernel-build-per-step-postcondition-contract]] (verification) and the worktree-isolation work (123/271, isolation).

## Task Builder Input
- **Deliverable:** A PostToolUse (+PreToolUse where needed) hook enforcing output-dir confinement + runner-owned-state blocking for subagent sessions, wired into settings, with tests (an out-of-sandbox write is blocked; an in-sandbox write passes; a factory_state write by an agent is blocked).
- **Location:** workspace:.claude/hooks/
- **Scope:** BUILD
- **Constraints:** Must not break the interactive/orchestrator session (scope to one-shot/agent sessions). Provide a marked escape hatch. Port to kernel-minimal after it proves out.
