# Write hash collector module

## Context
Computes SHA-256 hashes of pipeline inputs and outputs to populate the attestation bundle.

## Type
BUILD

## Execution
inline

## Dependencies
- 004

## Phase Gate
- [ ] Schema module exists (task 004)

## Requirements
- Write `lib/attestation/collect.py`
- Functions:
  - `hash_file(path) -> str` — SHA-256 hex digest of a single file
  - `hash_directory(dir_path) -> list[dict]` — walk directory, return `[{path, sha256}]` for each file
  - `hash_string(content) -> str` — SHA-256 of string content (for prompt/session hashing)
  - `collect_pipeline_hashes(backlog_path, task_folder, output_paths) -> dict` — collects all hashes and returns data ready for `create_bundle()`
- Read backlog path from `pipeline_state.backlog_path` in session_state.json
- Use `hashlib.sha256` — no external dependencies
- Include `--test` CLI mode: `python lib/attestation/collect.py --test` hashes its own source file and prints the result

## Acceptance Criteria
- [ ] `lib/attestation/collect.py` exists
- [ ] `hash_file()`, `hash_directory()`, `hash_string()`, `collect_pipeline_hashes()` functions defined
- [ ] `python lib/attestation/collect.py --test` exits 0 with valid SHA-256 output

## Gates Satisfied
BUILD-03, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
