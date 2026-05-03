# Rekor Logging — Transparency Ledger

## Status
NEW

## Location
`workspace` (integrated into signing step)

## What It Does
Pushes the signed attestation to Rekor — a public, append-only transparency log. Creates a permanent, independently verifiable record that can't be backdated or edited.

## How It Works
1. After signing, submit the signed bundle to Rekor
2. Rekor returns an entry ID and URL
3. Store the Rekor entry ID/URL alongside the local attestation bundle
4. Anyone — ever — can look up the entry and verify:
   - The signature is valid
   - The hashes match the artifacts
   - The timestamp is authentic

## Verification (what others can do)
- Given a Rekor entry ID: `rekor-cli verify --uuid <entry-id>`
- Given output files: recompute SHA-256, compare against attestation hashes
- No need to trust the builder — trust the math

## Storage
- Rekor entry URL/ID appended to local attestation JSON: `rekor.entryUrl`, `rekor.entryId`
- Local attestation stored at `.claude/state/attestations/<backlog-number>-<timestamp>.json`

## Dependencies
- Signed attestation bundle must exist
- Internet access required for Rekor submission
