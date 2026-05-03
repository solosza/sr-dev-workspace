# L2: Test attestation bundle schema validation

## Context
Verify the schema module correctly validates attestation bundles.

## Type
TEST

## Execution
inline

## Dependencies
- 004, 005

## Requirements
- Create a test bundle using `create_bundle()` with real data:
  - Hash CLAUDE.md as the backlog input
  - Hash lib/attestation/ as the output artifacts
  - Use current timestamp
- Validate the bundle using `validate_bundle()`
- Verify all required fields are present: predicateType, invocation.configSource, invocation.parameters, output.artifacts, timestamp.start, timestamp.end, metadata
- Test with a malformed bundle (missing fields) — verify validation fails
- Run `python lib/attestation/schema.py --validate` with piped JSON input

## Acceptance Criteria
- [ ] `create_bundle()` produces valid JSON with all required fields
- [ ] `validate_bundle()` returns True for valid bundles
- [ ] `validate_bundle()` returns False for bundles missing required fields
- [ ] `--validate` CLI mode exits 0 with valid input, exits 1 with invalid

## Gates Satisfied
FUNC-02, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
