# Write Atomic State Helper

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- READ the hooks directory first — if a shared module exists (e.g. common.py) extend it; else create hooks/state_io.py
- atomic_write_json(path, obj, schema_key): validate against minimal schema (required keys + types per state file kind), write temp file in same dir, os.replace() onto target
- Validation failure -> raise with clear message; NEVER write the invalid payload; near-empty dicts rejected
- Schemas: session_state (session_started, domain, ...), workflow (domain, anchored, actions_since_anchor, ...) — derive required keys by READING current files, keep minimal

## Acceptance Criteria
- [ ] Helper in one shared module with schema validation + os.replace
- [ ] Unit-style check runs green (invoke module directly)

## Gates Satisfied
- SI-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
