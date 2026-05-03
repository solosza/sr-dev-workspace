# Anchor Integrity — Verifiable Protocol Read

## Status
Open

## Priority
High — anchor is the core enforcement mechanism; if it can be faked, the entire governance loop is hollow

## Summary
The anchor is currently a state-file operation that an agent can satisfy by updating two booleans (`anchored: true`, `anchor_token_confirmed: true`). The hook checks that an anchor *happened* (via the token), not *what happened* during the anchor (protocol re-read, action review, drift check). A real anchor should produce an artifact that only a genuine protocol read can generate. Without this, "anchored: true" is a self-reported field.

## Finding Source
Dogfooding — discovered while running the system against itself on real work (backlog 009 execution).

## Requirements

1. **The gap:** `anchored: true` is self-reported. An agent can write the boolean without actually reading protocol, reviewing actions, or checking for drift.

2. **Options to fix (pick one or combine):**
   - **Protocol hash:** Write a protocol-read timestamp plus content hash to state. Hook verifies the hash matches the current protocol file content.
   - **Passage quoting:** Require the agent to quote a specific passage from the protocol file in the anchor report. Hook validates the quote exists in the protocol.
   - **Skill invocation verification:** PostToolUse hook verifies the anchor skill was invoked via the Skill tool rather than direct state file edits.

3. **Whichever mechanism:**
   - Must be machine-verifiable (hook can check it)
   - Must not be fakeable by a simple state file write
   - Must survive context compaction (the proof artifact persists)
   - Should not add excessive latency to the anchor cycle

## References
- `.claude/commands/kernel/anchor.md` — current anchor implementation
- `.claude/hooks/universal-gate-enforcer.py` — current hook that checks anchor state
- Backlog 009 — where this gap was discovered

## Task Builder Input
- **Deliverable:** Updated anchor command + hook enforcement that verifies genuine protocol read
- **Location:** workspace:.claude/commands/kernel/ and .claude/hooks/
- **Scope:** REFACTOR
- **Constraints:** Must not break existing anchor flow. Must work with current hook architecture. Agent must still be able to anchor successfully — the goal is verification, not friction.
