# Build Sigstore Attestation Pipeline for Kernel-Produced Artifacts

## Status
Open

## Priority
High — transforms every "the harness built this" claim from a story into a cryptographic receipt. Applies to all builds going forward.

## Summary
Wire Sigstore signing and Rekor logging into the kernel's post-pipeline flow so that every artifact produced by the harness has a verifiable provenance chain. Every execute-pipeline run automatically produces a cryptographic receipt proving: natural language intent (hashed, content private) → governed execution → output artifact, signed by the builder's GitHub identity, timestamped permanently on a public ledger. Also provides a standalone `/kernel/attest` command for manual attestation of any artifact.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[046-kernel-build-sigstore-attestation-pipeline/attestation-format]] | JSON schema for natural-language-session/v1 attestation bundles |
| [[046-kernel-build-sigstore-attestation-pipeline/hash-collection]] | Post-pipeline SHA-256 computation of all inputs and outputs |
| [[046-kernel-build-sigstore-attestation-pipeline/sigstore-signing]] | Keyless signing via Sigstore OIDC (GitHub identity, no key management) |
| [[046-kernel-build-sigstore-attestation-pipeline/rekor-logging]] | Permanent logging to Rekor transparency ledger |
| [[046-kernel-build-sigstore-attestation-pipeline/pipeline-integration]] | Automatic attestation on every execute-pipeline completion + standalone command |

## Architecture

```
execute-pipeline completes
        |
        v
  Hash Collection
  (SHA-256 of outputs + backlog + prompt)
        |
        v
  Sigstore Keyless Sign
  (OIDC via GitHub identity)
        |
        v
  Rekor Log
  (permanent public entry)
        |
        v
  Attestation bundle saved locally
  + Rekor entry URL stored
```

## Use Cases

| Scenario | What the attestation provides |
|----------|------------------------------|
| Portfolio site (backlog 044) | Provenance page: "this site was built by the harness" — click to verify on Rekor |
| YC application | "Command /X was produced by session Y on date Z" — verifiable, not a claim |
| Job interview | "I described what I wanted, the system built it" — cryptographic proof attached |
| Platform-absorption defense | 27+ attested events with timestamps predating any competitor's feature launch |

## Requirements
- Attestation runs automatically after every execute-pipeline completion
- Hash-commits prompts (publish hash, keep content private)
- Signs via Sigstore keyless flow (no key management)
- Logs to Rekor (permanent, independently verifiable)
- Standalone `/kernel/attest` command for manual use
- Reference nono-attest as model implementation before building

## References
- nono-attest — existing Sigstore-based attestation tool for code artifacts
- Sigstore (sigstore.dev) — free signing infrastructure
- Rekor — public transparency log
- Backlog 044: portfolio site refactor (provenance page consumes attestation output)
- Backlog 045: agent swarms research (attestation strengthens differentiation story)

## Task Builder Input
- **Deliverable:** Post-pipeline attestation step that hashes outputs + inputs, signs via Sigstore keyless, logs to Rekor. Runs automatically on every execute-pipeline completion. Includes standalone `/kernel/attest` command for manual attestation.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Requires GitHub OIDC identity for Sigstore keyless flow. Research nono-attest first to understand existing implementation before building. Need to determine if signing happens locally or in GitHub Actions.
