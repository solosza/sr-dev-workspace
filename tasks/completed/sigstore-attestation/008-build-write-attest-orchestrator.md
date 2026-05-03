# Write attestation orchestrator

## Context
Main entry point that chains: collect hashes → create bundle → sign → log to Rekor → save locally.

## Type
BUILD

## Execution
inline

## Dependencies
- 005, 006, 007

## Phase Gate
- [ ] Hash collector exists (task 005)
- [ ] Signer exists (task 006)
- [ ] Rekor logger exists (task 007)

## Requirements
- Write `lib/attestation/attest.py`
- Main function: `run_attestation(backlog_path, task_folder, output_paths, dry_run=False) -> str`
  1. Call `collect_pipeline_hashes()` to gather all input/output hashes
  2. Call `create_bundle()` to produce the attestation JSON
  3. Save bundle to `.claude/state/attestations/<backlog-number>-<timestamp>.json`
  4. Call `sign_bundle()` to sign it
  5. Call `log_to_rekor()` to submit to transparency log
  6. Call `update_bundle_with_rekor()` to store Rekor entry in local bundle
  7. Return path to final attestation bundle
- CLI interface: `python lib/attestation/attest.py <backlog_path> <task_folder> [--dry-run]`
- `--dry-run` mode: collect hashes and create bundle, skip signing and Rekor (for testing)
- If signing/Rekor fails, save the unsigned bundle anyway and warn — attestation is evidence, not a gate

## Acceptance Criteria
- [ ] `lib/attestation/attest.py` exists
- [ ] `run_attestation()` function chains all modules
- [ ] CLI interface works: `python lib/attestation/attest.py --dry-run` exits 0
- [ ] Bundle saved to `.claude/state/attestations/`

## Gates Satisfied
BUILD-06, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
