# Write signing wrapper module

## Context
Wraps cosign CLI or sigstore-python to sign attestation bundles using keyless (OIDC) flow.

## Type
BUILD

## Execution
inline

## Dependencies
- 002, 004

## Phase Gate
- [ ] Signing tool installed (task 002)
- [ ] Schema module exists (task 004)

## Requirements
- Write `lib/attestation/sign.py`
- Functions:
  - `sign_bundle(bundle_path) -> str` — signs the attestation bundle JSON, returns path to signed output
  - `verify_signature(signed_path) -> bool` — verifies a signed bundle
- If using cosign: shell out to `cosign attest-blob --predicate <bundle.json> --type custom`
- If using sigstore-python: use `sigstore.sign` module directly
- Handle keyless flow: OIDC via GitHub identity (browser flow for local, token for CI)
- If signing fails (no OIDC available), return gracefully with error message — don't crash
- Include `--dry-run` mode that skips actual signing but validates the flow

## Acceptance Criteria
- [ ] `lib/attestation/sign.py` exists
- [ ] `sign_bundle()` and `verify_signature()` functions defined
- [ ] `--dry-run` mode works without OIDC credentials

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
