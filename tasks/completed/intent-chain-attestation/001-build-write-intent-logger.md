# Write intent logger module

## Context
Create `lib/attestation/intent.py` — the Python module that records and reads intent chains.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create `lib/attestation/intent.py` with:
  - `record_intent(backlog_number: str, raw_text: str, backlog_path: str) -> dict`
    - Compute SHA-256 of `raw_text`
    - Compute SHA-256 of backlog file at `backlog_path` (after it's been written)
    - Auto-increment `rev` by counting existing lines in the JSONL + 1
    - Append entry to `.claude/state/intents/{backlog_number}-intent-chain.jsonl`
    - Create `.claude/state/intents/` directory if it doesn't exist
    - Entry format: `{"rev": N, "timestamp": "ISO", "raw_input_hash": "sha256", "backlog_hash_after": "sha256"}`
    - Return the entry dict
  - `read_intent_chain(backlog_number: str) -> list`
    - Read `.claude/state/intents/{backlog_number}-intent-chain.jsonl`
    - Return list of entry dicts, or empty list if file doesn't exist
  - CLI interface:
    - `python intent.py record NNN "raw text" path/to/backlog.md`
    - `python intent.py read NNN`
    - `python intent.py --test` (self-test)
- Use same patterns as existing `collect.py` and `schema.py` (hash_string from collect, sys.path manipulation)
- Raw text is ONLY hashed — never stored. Privacy by design.

## Acceptance Criteria
- [ ] `lib/attestation/intent.py` exists
- [ ] `record_intent()` creates JSONL file and appends entry
- [ ] `read_intent_chain()` reads and returns entries
- [ ] CLI `--test` mode passes

## Gates Satisfied
BUILD-01
