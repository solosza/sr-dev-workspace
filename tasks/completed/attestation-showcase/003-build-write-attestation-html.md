# 003 — Write attestation.html

## Type
BUILD

## Requirements
Create `attestation.html` in `D:\my_ai_projects\isagawa-co.github.io\`. This is the product showcase page for the agent-attestation-spec.

### Content Structure

1. **Built by the loop** — one sentence: "This product was built by the same system described on the homepage." + link to index.html#self-extension

2. **Hero** — "Prove your AI agent did what it said it did." + subhead: "A drop-in spec that gives any AI coding agent cryptographic proof of every pipeline run. No private keys. No infrastructure. Just Sigstore."

3. **Problem** — "You tell your AI agent to build something. It says 'done.' But how do you know?" Three bullet points: no audit trail, no tamper evidence, no proof for teams/auditors.

4. **How It Works** — Flow diagram showing 5 steps:
   - User request → SHA-256 hash → Intent chain
   - Task execution → Output files → SHA-256 hashes
   - Attestation bundle created (JSON)
   - Sigstore keyless signing (OIDC)
   - Rekor transparency log entry
   Each step with a brief plain-text explanation.

5. **What's in a Bundle** — Show annotated attestation bundle JSON (use real example from README). Highlight: intent_chain, artifacts with hashes, timestamps, rekor entry.

6. **Drop-in Setup** — 3 steps:
   - `pip install sigstore`
   - `cp -r lib/ your-project/lib/`
   - `python lib/attest.py path/to/spec.md path/to/tasks/`

7. **Tech Stack** — Badges: Sigstore, Rekor, OIDC, Python, SHA-256

8. **Results** — Dynamic counter fetched from feed-count.txt, link to feed.html

### Technical
- Links stylesheet `attestation.css`
- Nav: ISAGAWA logo → index.html, Home, Feed, attestation counter
- Dynamic counter from feed-count.txt (same pattern as feed.html)
- Static HTML, no build step, GitHub Pages compatible
- Content from agent-attestation-spec README.md

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\attestation.html` exists
- [ ] Contains all 8 content sections
- [ ] Nav links back to index.html
- [ ] Dynamic counter fetches feed-count.txt
