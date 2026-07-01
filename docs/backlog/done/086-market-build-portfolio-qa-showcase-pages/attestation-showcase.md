# Attestation Pipeline Showcase Page

## Status
NEW — most differentiated offering, build first

## Location
`D:\my_ai_projects\isagawa-co.github.io\projects\attestation\index.html`

## What It Does
Showcases the Sigstore attestation pipeline — the unique agent governance capability that no competitor offers. Every task executed by the AI agent gets cryptographically signed and logged to a public transparency ledger (Rekor).

## Content Sections

1. **Hero** — "Every task I build is cryptographically attested" + live feed counter
2. **Problem** — AI agents produce output but there's no way to verify what happened, when, or whether it was governed
3. **How It Works** — Pipeline diagram: collect hashes → create bundle → sign (OIDC) → log to Rekor → verify
4. **Live Feed** — Embed or link to the live attestation feed (already on isagawa.co)
5. **Tech Stack** — Sigstore, Rekor, OIDC, Python, GitHub Pages
6. **Verification** — How anyone can verify an attestation via Rekor search
7. **Results** — 63+ attestations, 3 repos tracked, all publicly verifiable

## Dependencies
- Live attestation feed already exists on isagawa.co
- Attestation code in `lib/attestation/`
- Feed generator at `generate-feed.py` in isagawa-co.github.io
