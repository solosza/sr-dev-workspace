# Update attestation schema with intent_chain

## Context
Add `intent_chain` field to the attestation bundle schema so bundles can carry the full revision history.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Requirements
- Edit `lib/attestation/schema.py`:
  - Add `intent_chain` parameter to `create_bundle()` (default `None`)
  - Place `intent_chain` inside `predicate.invocation` alongside `configSource` and `parameters`
  - If `intent_chain` is `None`, omit the field (backward compatible — old bundles without it stay valid)
  - If `intent_chain` is a list, include as-is: `"intent_chain": [{"rev": 1, ...}, ...]`
  - Do NOT add `intent_chain` to `REQUIRED_FIELDS` — it's optional for backward compatibility
  - `validate_bundle()` should accept bundles with or without `intent_chain`

## Acceptance Criteria
- [ ] `create_bundle()` accepts `intent_chain` parameter
- [ ] Bundle includes `intent_chain` in `predicate.invocation` when provided
- [ ] Bundle omits `intent_chain` when `None`
- [ ] Existing bundles without `intent_chain` still validate

## Gates Satisfied
BUILD-03
