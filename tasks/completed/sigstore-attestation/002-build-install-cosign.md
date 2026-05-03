# Install cosign or sigstore-python

## Context
Install the signing tool determined by research in task 001. Either cosign CLI or sigstore-python package.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Research complete (task 001) — tool choice made

## Requirements
- If cosign CLI: install via appropriate method for Windows (scoop, winget, or direct download)
- If sigstore-python: `pip install sigstore` (or add to requirements.txt if one exists)
- Verify installation: `cosign version` or `python -c "import sigstore"` exits 0

## Acceptance Criteria
- [ ] Signing tool installed and available on PATH or importable
- [ ] Version/import check exits 0

## Gates Satisfied
FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
