# Fix Attestation Signing — Replace cosign CLI with sigstore-python

## Status
Open

## Priority
High — attestation pipeline is a skeleton without real signing; cosign is not installed and everything has only run in dry-run mode

## Summary
The attestation pipeline (046, 048) built Python modules that shell out to `cosign` for signing and Rekor logging. Cosign was never installed (`cosign version` returns exit 127). Every test ran `--dry-run`, so no real Sigstore signature or Rekor entry was ever produced. Rewrite `sign.py` and `rekor.py` to use `sigstore-python` (pure Python SDK) instead of the cosign CLI. This eliminates the external binary dependency, works natively on Windows, and handles the OIDC browser flow for GitHub identity. Then test end-to-end with a real signature and a real Rekor entry.

## Requirements
- `pip install sigstore` in the workspace
- Rewrite `lib/attestation/sign.py` to use `sigstore.sign` instead of `subprocess.run(["cosign", ...])`
- Rewrite `lib/attestation/rekor.py` to use sigstore-python's built-in Rekor integration instead of raw HTTP calls
- Preserve the existing function signatures (`sign_bundle()`, `verify_signature()`, `log_to_rekor()`, `update_bundle_with_rekor()`) so `attest.py` doesn't need changes
- `--dry-run` mode still works (skip actual signing)
- Non-dry-run mode: opens browser for GitHub OIDC, signs bundle, logs to Rekor, returns entry URL
- Test end-to-end: run `python lib/attestation/attest.py <backlog> <task_folder>` WITHOUT `--dry-run` and verify a real Rekor entry is produced
- Verify the Rekor entry URL resolves and contains the expected data
- Fix `run-task.sh` zombie process issue: `claude -p` output not captured on Windows, causing empty iteration logs and orphaned processes

## References
- Attestation modules: `lib/attestation/` (sign.py, rekor.py, attest.py, schema.py, collect.py, intent.py)
- Built by: `docs/backlog/done/046-kernel-build-sigstore-attestation-pipeline.md`
- Intent chain: `docs/backlog/done/048-kernel-add-intent-chain-attestation.md`
- sigstore-python: PyPI package `sigstore`
- run-task.sh defect: empty iteration logs, zombie `claude -p` processes on Windows

## Task Builder Input
- **Deliverable:** Working attestation signing with real Sigstore signatures and Rekor entries, plus run-task.sh fix
- **Location:** `workspace`
- **Scope:** BUILD
- **Constraints:** Requires internet access for OIDC flow and Rekor API. First real signing will pop a browser window for GitHub auth. sigstore-python must be compatible with Windows + Python 3.x.
