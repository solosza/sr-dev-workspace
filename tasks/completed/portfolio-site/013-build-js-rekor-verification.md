# Build Rekor Verification JS

## Context
Client-side JavaScript that performs real cryptographic verification of the embedded attestation bundles. For each card: fetch the Rekor entry by logIndex, compute the bundle hash locally via SubtleCrypto, compare with the Rekor entry, and display a verified/mismatch badge. Also handles the "View full bundle" expandable JSON viewer.

## Type
BUILD

## Execution
inline

## Dependencies
- 012-build-embed-bundle-052

## Phase Gate
- [ ] Both attestation bundles embedded in `index.html`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Add a `<script>` block (before `</body>`, after the bundle JSON blocks) that:
  1. For each `.attestation-card`:
     - Read the `data-bundle` attribute to find the corresponding `<script type="application/json">` block
     - Parse the bundle JSON
     - Extract intent text from `invocation.intent_chain` or `invocation.raw_input_hash` — display in `.intent-text`
     - Extract metadata (backlog number, task count, timestamp) — display in `.attestation-meta`
     - Extract `rekor_log_index` from the bundle
  2. Verification flow:
     - Compute SHA-256 hash of the bundle JSON string using `crypto.subtle.digest`
     - Fetch `https://rekor.sigstore.dev/api/v1/log/entries?logIndex=${logIndex}`
     - Compare the computed hash against the Rekor entry body
     - Update `.verification-badge` with "✓ Verified on Rekor" (green) or "✗ Verification pending" (amber)
  3. "View on Rekor" link: set href to `https://search.sigstore.dev/?logIndex=${logIndex}`
  4. "View full bundle" toggle:
     - Click toggles visibility of `.bundle-viewer`
     - `.bundle-viewer` shows pretty-printed JSON (`JSON.stringify(bundle, null, 2)`)
- Graceful degradation: if fetch fails (CORS, offline), show "Verification unavailable — view on Rekor directly"
- This is the ONLY JavaScript on the page (besides mobile nav toggle)

## Acceptance Criteria
- [ ] `index.html` contains a `<script>` block with `crypto.subtle` usage
- [ ] `index.html` contains `rekor.sigstore.dev` URL
- [ ] `index.html` contains `search.sigstore.dev` URL
- [ ] JS handles fetch failure gracefully (try/catch)

## Gates Satisfied
- BUILD-11, TEST-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
