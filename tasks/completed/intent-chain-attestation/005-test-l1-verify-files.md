# L1: Verify all files exist and modified

## Context
Structural verification that all build tasks produced their artifacts.

## Type
TEST

## Execution
inline

## Dependencies
- 001, 002, 003, 004

## Requirements
- Verify `lib/attestation/intent.py` exists
- Verify `lib/attestation/intent.py` contains `record_intent` and `read_intent_chain`
- Verify `.claude/commands/kernel/backlog.md` contains "intent" (the new step)
- Verify `lib/attestation/schema.py` contains `intent_chain`
- Verify `lib/attestation/attest.py` contains `intent_chain`

## Acceptance Criteria
- [ ] All 4 files exist/contain expected strings
- [ ] No missing artifacts

## Gates Satisfied
TEST-01
