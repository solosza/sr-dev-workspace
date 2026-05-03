# Update execute-pipeline step-05 with attestation

## Context
Wire attestation into the pipeline so every build automatically gets a cryptographic receipt.

## Type
BUILD

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Attest orchestrator exists (task 008)

## Requirements
- Read `.claude/skills/execute-pipeline/references/step-05-validate-report.md`
- Add a new section after the validation report (step 5b):
  - "After validation, run attestation"
  - Call `python lib/attestation/attest.py <backlog_path> <task_folder>`
  - If attestation succeeds: include Rekor entry URL in pipeline report
  - If attestation fails: warn but don't fail the pipeline — attestation is evidence, not a gate
- Update the final report template to include attestation status
- Add `last_attestation` field to state update instructions

## Acceptance Criteria
- [ ] `step-05-validate-report.md` contains attestation instructions
- [ ] Attestation is documented as non-blocking (warn on failure, don't fail pipeline)
- [ ] Report template includes attestation status line

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
