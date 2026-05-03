# Write attestation schema module

## Context
Define the natural-language-session/v1 attestation format as a Python module. This schema is used by all other modules to produce and validate bundles.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Research complete (task 001) — format decisions informed by nono-attest findings

## Requirements
- Write `lib/attestation/schema.py`
- Define the attestation bundle as a Python dataclass or dict factory:
  - `predicateType`: `"natural-language-session/v1"`
  - `predicate.invocation.configSource`: SHA-256 of session/backlog content
  - `predicate.invocation.parameters`: SHA-256 of input prompt/backlog
  - `predicate.output.artifacts[]`: list of `{path, sha256}` entries
  - `predicate.timestamp.start`: ISO-8601
  - `predicate.timestamp.end`: ISO-8601
  - `predicate.metadata`: pipeline_backlog, task_folder, task_count, completed_count, skipped_count
- Include `create_bundle()` function that takes inputs and returns the bundle dict
- Include `validate_bundle()` function that checks required fields
- Include `--validate` CLI mode: `python lib/attestation/schema.py --validate` reads a bundle from stdin and validates it

## Acceptance Criteria
- [ ] `lib/attestation/schema.py` exists
- [ ] `create_bundle()` function defined
- [ ] `validate_bundle()` function defined
- [ ] `python lib/attestation/schema.py --validate` with valid JSON exits 0

## Gates Satisfied
BUILD-02, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
