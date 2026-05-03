# Add Intent Chain to Attestation Pipeline

## Status
Open

## Priority
High — closes the gap between "system spec produced code" and "human intent produced everything"

## Summary
When `/kernel/backlog` runs, it receives the user's raw natural language as its argument. That raw text is the actual human artifact — the proof that a person was steering. Today it disappears into the conversation. This enhancement captures it: hash the raw input, append to an intent log per backlog item, and include the full intent chain in the attestation bundle at pipeline completion. Three touch points: backlog command entry, attestation schema, attestation orchestrator.

## Requirements
- Before `/kernel/backlog` creates or updates a backlog file, hash the raw argument text (SHA-256) and append to `.claude/state/intents/NNN-intent-chain.jsonl`
- Each JSONL entry: `{"rev": N, "timestamp": "ISO", "raw_input_hash": "sha256hex", "backlog_hash_after": "sha256hex"}`
- `backlog_hash_after` is computed after the backlog file is written (captures the system's interpretation)
- `rev` auto-increments per backlog number (count existing lines + 1)
- Intent log directory `.claude/state/intents/` created on first use
- Attestation bundle schema (`lib/attestation/schema.py`) gains `intent_chain` array field inside `predicate.invocation`
- Attestation orchestrator (`lib/attestation/attest.py`) reads the intent JSONL for the relevant backlog number and includes it in the bundle
- If no intent log exists for a backlog item (legacy items created before this enhancement), `intent_chain` is `null` — not an error
- Raw input text stays private (only the hash is stored). The actual words live only in the conversation context.

## References
- Built by: `docs/backlog/done/046-kernel-build-sigstore-attestation-pipeline.md`
- Attestation modules: `lib/attestation/` (schema.py, collect.py, attest.py, sign.py, rekor.py)
- Backlog command: `.claude/commands/kernel/backlog.md`
- Execute pipeline step 5: `.claude/skills/execute-pipeline/references/step-05-validate-report.md`

## Task Builder Input
- **Deliverable:** Intent chain capture in backlog command + intent chain inclusion in attestation bundle
- **Location:** `workspace`
- **Scope:** BUILD
- **Constraints:** Must not break existing attestation dry-run flow. Must not store raw text (privacy). Backlog command is a markdown skill file — the hashing logic is instructions the agent follows, not executable code. The attestation modules are Python.
