# Write /kernel/attest command

## Context
Standalone kernel command for manual attestation of any artifact outside the pipeline.

## Type
BUILD

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Attest orchestrator exists (task 008)

## Requirements
- Write `.claude/commands/kernel/attest.md`
- Command accepts a file or directory path as argument
- Instructions:
  1. Parse argument (file path or directory)
  2. Compute SHA-256 of target file(s)
  3. Create attestation bundle with minimal metadata (no pipeline_state, no task_folder)
  4. Run `python lib/attestation/attest.py <path> --manual`
  5. Report: attestation bundle path, Rekor entry URL (if signed), hash summary
- Include `--dry-run` passthrough
- Usage examples in the command file

## Acceptance Criteria
- [ ] `.claude/commands/kernel/attest.md` exists
- [ ] Command documents usage, arguments, and expected output
- [ ] References `lib/attestation/attest.py` for execution

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
