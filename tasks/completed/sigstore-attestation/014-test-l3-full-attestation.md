# L3: Full attestation pipeline test

## Context
Run the complete attestation pipeline (dry-run mode) on a real artifact to verify the end-to-end flow.

## Type
TEST

## Execution
inline

## Dependencies
- 008

## Requirements
- Run `python lib/attestation/attest.py docs/backlog/046-kernel-build-sigstore-attestation-pipeline.md tasks/sigstore-attestation/ --dry-run`
- Verify:
  - Bundle JSON created in `.claude/state/attestations/`
  - Bundle filename matches pattern `046-<timestamp>.json`
  - Bundle contains correct backlog hash (SHA-256 of the 046 backlog file)
  - Bundle contains artifact hashes for all files in `tasks/sigstore-attestation/`
  - Bundle has valid timestamp bracket
  - Bundle has correct metadata (task_folder, task_count)
- Verify dry-run skipped signing and Rekor (no signature, no rekor fields)
- If cosign/sigstore is available, optionally test a real signing flow (non-dry-run)

## Acceptance Criteria
- [ ] `--dry-run` exits 0
- [ ] Attestation bundle saved to `.claude/state/attestations/046-*.json`
- [ ] Bundle has all required fields per schema
- [ ] Backlog hash matches actual SHA-256 of 046 backlog file
- [ ] Artifact list includes files from task folder

## Gates Satisfied
TEST-01, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
