# Gap 2: Add Attestation Step to Execute-Pipeline

## Status
NEW

## Location
`.claude/skills/execute-pipeline/references/step-05-validate-report.md`

## Problem
Step 5 (validate + report) has no mention of running the attestation pipeline. Pipeline 050 required manual attestation. Every pipeline that ships should produce a signed bundle automatically.

## Fix
Add an attestation sub-step to step 5 after validation passes:

1. Run `python lib/attestation/attest.py [backlog_path] [task_folder]` (no `--dry-run`)
2. This triggers: hash collection → bundle creation → sigstore signing (OIDC browser flow) → Rekor submission
3. Record the bundle path and Rekor URL in `pipeline_state`
4. Include in the final report output

The attestation infra already exists (`lib/attestation/`). This is just wiring it into the pipeline flow.

If signing fails (no browser, offline), the pipeline should still complete — attestation failure is a warning, not a blocker. Save the unsigned bundle and note it in the report.

## Dependencies
- Backlog 046 (attestation infra) — DONE
- Backlog 048 (intent chain) — DONE
