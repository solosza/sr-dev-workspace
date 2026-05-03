# Pipeline Integration — Automatic Attestation on Every Build

## Status
NEW

## Location
`workspace:.claude/skills/execute-pipeline/` (step 5 extension)

## What It Does
Wires the attestation pipeline into execute-pipeline so every build automatically produces a cryptographic receipt. No manual step — it just happens.

## Integration Point
- After execute-pipeline step 5 (validate + report), add attestation as step 5b
- Sequence: tasks complete → validation report → hash collection → sign → log to Rekor → done
- If signing/logging fails (no internet, no OIDC), warn but don't fail the pipeline — attestation is evidence, not a gate

## Standalone Command
- Also provide `/kernel/attest` command for manual attestation of any artifact
- Takes a file or directory path, computes hashes, signs, logs
- Useful for attesting artifacts produced outside the pipeline (manual builds, one-off scripts)

## State Updates
- After attestation: update `session_state.json` with `last_attestation` field
- Track attestation count in `sr_dev_workflow.json` for audit trail

## Dependencies
- All other components (format, hash collection, signing, Rekor logging)
- execute-pipeline skill must be updated to include attestation step
