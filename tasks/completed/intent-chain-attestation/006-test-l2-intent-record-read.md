# L2: Intent logger record + read unit test

## Context
Test that `intent.py` correctly records and reads intent chain entries.

## Type
TEST

## Execution
inline

## Dependencies
- 001

## Requirements
- Run `python lib/attestation/intent.py --test`
- Additionally, run a Python script that:
  1. Creates a temp directory
  2. Creates a fake backlog file in temp
  3. Calls `record_intent("999", "build something cool", temp_backlog_path)` with `intents_dir` overridden to temp
  4. Calls `record_intent("999", "also add tests", temp_backlog_path)` again
  5. Calls `read_intent_chain("999")` with same override
  6. Asserts: 2 entries returned
  7. Asserts: rev 1 and rev 2
  8. Asserts: `raw_input_hash` is SHA-256 of "build something cool" for entry 1
  9. Asserts: `raw_input_hash` differs between entries (different input text)
  10. Asserts: `backlog_hash_after` is same for both (same file, unchanged)
  11. Cleans up temp
- Exit 0 on success, non-zero on failure

## Acceptance Criteria
- [ ] `--test` exits 0
- [ ] Custom unit test exits 0
- [ ] Two entries with correct rev numbers
- [ ] Hashes are valid SHA-256 hex strings (64 chars)

## Gates Satisfied
TEST-02
