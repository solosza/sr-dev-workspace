# Subagent Output-Sandbox Hook — Confine Writes, Block Runner-Owned State

## Status
COMPLETE (2026-07-23) — built directly + orchestrator-verified (9/9), wired live.

## Completion
- **Hook:** `.claude/hooks/subagent-output-sandbox.py` — self-contained PreToolUse hook (no `lib.validators` dependency). For subagent sessions only (`KERNEL_AGENT_ID` set, or `KERNEL_SUBAGENT=1`): (a) blocks Write/Edit to `*_factory_state.json` (runner-owned state); (b) if `KERNEL_AGENT_OUTPUT_ROOT` is set, blocks any Write/Edit resolving outside it, naming the allowed root. Escape hatch: `KERNEL_SANDBOX_ALLOW=1`. Non-subagent (interactive/orchestrator) sessions are untouched — proven by test 1.
- **Wiring:** registered in `.claude/settings.local.json` PreToolUse (Edit|Write|Bash) after `sr_dev-gate-enforcer.py`. `run-task.sh` propagates `KERNEL_AGENT_OUTPUT_ROOT` into the spawned-agent env when set (confinement opt-in so a generic task with no single output dir is never wrongly blocked; the `factory_state` block is always on via `KERNEL_AGENT_ID`).
- **Tests:** `tests/test_290_output_sandbox.sh` — 9/9 (interactive passes; factory_state blocked; outside-root blocked; inside-root passes; escape hatch passes; non-Write passes; + wiring assertions: hook registered, runner propagates, syntax OK).
- **Prevents the two live failures:** the wrong-path `SKILL.md` write (blocked at the Write, not caught after 3 retries) and the `factory_state.json` clobber (hard-blocked).
- **Follow-up (parity requirement):** port to kernel-minimal (canonical) so every harness inherits it — deferred, not done here.

Product feature #2 of the reliability set: **"can't write outside its lane."** (291 = can't lie about finishing; 292 = can't clobber the repo.)

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
