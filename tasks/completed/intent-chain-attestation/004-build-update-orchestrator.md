# Update attestation orchestrator to include intent chain

## Context
Wire the intent chain into `attest.py` so every attestation bundle includes the revision history.

## Type
BUILD

## Execution
inline

## Dependencies
- 001, 003

## Requirements
- Edit `lib/attestation/attest.py`:
  - Import `read_intent_chain` from `intent`
  - In `run_attestation()`, after collecting hashes (step 2):
    - Extract backlog number from `backlog_path` using existing `_extract_backlog_number()`
    - Call `read_intent_chain(backlog_number)`
    - Pass result as `intent_chain` to `create_bundle()`
  - If intent chain is empty list, pass `None` (no chain = legacy item)

## Acceptance Criteria
- [ ] `attest.py` imports from `intent`
- [ ] `run_attestation()` reads intent chain
- [ ] `create_bundle()` receives `intent_chain` parameter
- [ ] Dry-run still works (intent chain may be empty for test data)

## Gates Satisfied
BUILD-04
