# Sigstore Signing — Keyless Flow

## Status
NEW

## Location
`workspace` (script or post-pipeline hook)

## What It Does
Signs the attestation bundle using Sigstore's keyless signing flow. No key management — uses OIDC identity from GitHub.

## How It Works
1. Authenticate via GitHub OIDC (short-lived certificate issued per signing event)
2. Sign the attestation bundle JSON with the certificate
3. Certificate proves: this person (GitHub identity) signed this bundle at this time
4. Like a notary stamp — automated and free

## Implementation Options
- **cosign** CLI tool (Sigstore's official signer) — `cosign attest-blob`
- **nono-attest** — existing tool that already signs code artifacts (SKILL.md, CLAUDE.md) via Sigstore. Reference implementation to study before building.
- **GitHub Actions integration** — OIDC token is natively available in Actions, no extra auth needed

## Output
- Signed attestation bundle (signature + certificate embedded or detached)
- Ready for Rekor logging

## Dependencies
- Hash collection must be complete (attestation bundle must exist)
- GitHub OIDC identity must be available (local: browser flow; CI: native token)
- cosign or equivalent must be installed
