# Research nono-attest and cosign

## Context
Before building, understand existing implementations. nono-attest is an existing Sigstore-based attestation tool. cosign is Sigstore's official CLI for signing.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Web search for nono-attest: how it signs artifacts, what attestation format it uses, how it integrates with Rekor
- Web search for cosign: installation on Windows, `cosign attest-blob` usage, keyless signing flow
- Determine: can cosign run locally on Windows without GitHub Actions? What OIDC providers are supported?
- Determine: is `sigstore-python` (Python SDK) a better fit than cosign CLI for integration into our Python-based pipeline?
- Document findings as comments in subsequent task files — no separate output file needed

## Acceptance Criteria
- [ ] nono-attest implementation understood (signing flow, format, Rekor integration)
- [ ] cosign vs sigstore-python decision made for this project
- [ ] Local Windows signing feasibility confirmed or alternative identified

## Gates Satisfied
None (research only)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
