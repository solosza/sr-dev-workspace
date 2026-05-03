# L2: Schema validates bundle with intent_chain

## Context
Test that `create_bundle()` correctly includes intent_chain and `validate_bundle()` accepts it.

## Type
TEST

## Execution
inline

## Dependencies
- 003

## Requirements
- Run a Python script that:
  1. Imports `create_bundle` and `validate_bundle` from `lib/attestation/schema`
  2. Creates a bundle WITH intent_chain:
     ```python
     bundle = create_bundle(
         config_source_hash="abc123",
         parameters_hash="def456",
         artifacts=[{"path": "test.py", "sha256": "aaa"}],
         start_time="2026-01-01T00:00:00Z",
         end_time="2026-01-01T00:01:00Z",
         pipeline_backlog="test.md",
         task_folder="tasks/test/",
         task_count=1, completed_count=1, skipped_count=0,
         intent_chain=[{"rev": 1, "timestamp": "...", "raw_input_hash": "xxx", "backlog_hash_after": "yyy"}]
     )
     ```
  3. Asserts `bundle["predicate"]["invocation"]["intent_chain"]` exists and has 1 entry
  4. Validates bundle — `validate_bundle(bundle)` returns no errors
  5. Creates a bundle WITHOUT intent_chain (None) — asserts field is absent
  6. Validates that bundle too — no errors
- Exit 0 on success

## Acceptance Criteria
- [ ] Bundle with intent_chain validates
- [ ] Bundle without intent_chain validates
- [ ] intent_chain appears in correct location in bundle JSON

## Gates Satisfied
TEST-03
