# Write Rekor logging wrapper module

## Context
Pushes signed attestation to Rekor transparency log and stores the entry URL locally.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Signing wrapper exists (task 006)

## Requirements
- Write `lib/attestation/rekor.py`
- Functions:
  - `log_to_rekor(signed_bundle_path) -> dict` — submits to Rekor, returns `{entryUrl, entryId}`
  - `verify_rekor_entry(entry_id) -> bool` — verifies an existing Rekor entry
  - `update_bundle_with_rekor(bundle_path, rekor_response)` — adds rekor.entryUrl and rekor.entryId to the local bundle JSON
- If using cosign: Rekor logging happens automatically during signing (cosign uploads to Rekor by default)
- If using sigstore-python: use `sigstore.transparency` module
- Handle network failure gracefully — warn but don't crash if Rekor is unreachable
- Include `--dry-run` mode that skips Rekor submission

## Acceptance Criteria
- [ ] `lib/attestation/rekor.py` exists
- [ ] `log_to_rekor()`, `verify_rekor_entry()`, `update_bundle_with_rekor()` functions defined
- [ ] `--dry-run` mode works without network

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
