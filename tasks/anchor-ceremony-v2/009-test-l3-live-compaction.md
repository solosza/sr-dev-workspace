# Task 009: L3 Test — Real Compaction Fires the Hook (GATE)

**Type:** TEST (L3 — real conditions?) — GATE TASK: a skip here NEVER waives the gate (lesson #39); orchestrator validates regardless.
**Gates Satisfied:** AC-08

## Action

Prove the hook fires on a REAL compaction event dispatched by Claude Code itself (not simulated stdin), and that the flipped state forces an anchor.

## Method

1. **Version preflight:** `claude --version`; compare against capability findings in `projects/kernel-precompact-reanchor-research/01-hook-capability.md` (PreCompact supported 2.1.207+). If the installed version predates PreCompact support, report ENV-BLOCKED with the version string — do not fake the gate.
2. **Test repo:** copy a minimal kernel state set (session_state with `domain: sr_dev`, workflow `anchored: true`, the hook, `state_io.py`, and a settings.local.json registering ONLY the PreCompact hook) into a scratch repo. Fresh `claude -p` processes load settings at startup, so the hook is active there without restarting the interactive session.
3. **Trigger:** run `env -u CLAUDECODE claude -p "/compact"` (manual compaction; matcher covers `manual`) in the scratch repo with a short seeded conversation (`--resume` a tiny session or open with enough preamble that /compact has something to do). Capture stderr/stdout.
4. **Assert:** after the run, scratch `sr_dev_workflow.json` has `anchored: false` AND session state has `compaction_anchor_reason` — written by the HOOK PROCESS (verify mtime changed during the run, not by the test script).
5. **Gate 3 follow-through:** in the same scratch repo, run a second `claude -p` one-shot instructed to attempt a Write — assert its output shows the Gate 3 anchor block (BLOCKED text referencing anchor).
6. **Ledger survival:** seed `context.ledger` with one entry before step 3 — assert it is intact (byte-equal entry) after compaction.

## Fallback (document honestly)

If `/compact` in `-p` mode does not execute in the installed version, document the exact behavior observed, then degrade to: interactive verification note for the user's next session + L2 evidence as the standing proof. Mark AC-08 residue explicitly — do NOT report the gate green on simulated evidence.

## Acceptance Criteria

- Hook fired on a real PreCompact event (or explicit documented ENV-BLOCKED/residue with version evidence)
- Gate 3 block observed on next tool call
- Ledger survived compaction
- Live workspace state untouched
