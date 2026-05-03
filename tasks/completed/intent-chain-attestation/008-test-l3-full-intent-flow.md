# L3: Full intent flow — record → attest → verify chain in bundle

## Context
End-to-end test: record intent entries for a test backlog, then run attestation dry-run and verify the bundle contains the intent chain.

## Type
TEST

## Execution
inline

## Dependencies
- 004

## Requirements
- Run a Python script that:
  1. Creates temp workspace structure (temp dir with `.claude/state/intents/`, a fake backlog file, a fake task folder with one task file)
  2. Records 2 intent entries for backlog number "999" using `record_intent()`
  3. Runs `run_attestation(backlog_path, task_folder, dry_run=True)` — but since `run_attestation` reads intent from `.claude/state/intents/` relative to workspace root, use the workspace override or set up paths correctly
  4. Reads the output bundle JSON
  5. Asserts `predicate.invocation.intent_chain` exists
  6. Asserts it has 2 entries with rev 1 and rev 2
  7. Asserts `raw_input_hash` values are valid SHA-256 (64 hex chars)
  8. Cleans up temp files and generated bundle
- If the workspace path resolution in `attest.py` makes this hard, an alternative approach: directly call the functions in sequence (record_intent → collect_pipeline_hashes → read_intent_chain → create_bundle) and verify the assembled bundle
- Exit 0 on success

## Acceptance Criteria
- [ ] Intent chain with 2 revisions appears in attestation bundle
- [ ] All hashes are valid 64-char hex strings
- [ ] Bundle passes `validate_bundle()`
- [ ] Dry-run exits 0

## Gates Satisfied
TEST-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
