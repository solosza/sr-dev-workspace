# L2: Test hash collection

## Context
Verify the hash collector produces valid SHA-256 output on real files.

## Type
TEST

## Execution
inline

## Dependencies
- 005

## Requirements
- Run `python lib/attestation/collect.py --test`
- Verify output is a valid 64-character hex string (SHA-256)
- Hash a known file (e.g., `CLAUDE.md`) and verify the hash is deterministic (run twice, compare)
- Test `hash_directory()` on a small directory (e.g., `lib/attestation/`)
- Verify output is a list of `{path, sha256}` dicts

## Acceptance Criteria
- [ ] `--test` mode exits 0
- [ ] Output is valid SHA-256 (64 hex chars)
- [ ] Same file produces same hash on repeated runs
- [ ] `hash_directory()` returns list of dicts with path and sha256 keys

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
