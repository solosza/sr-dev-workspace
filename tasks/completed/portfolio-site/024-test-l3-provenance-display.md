# L3: Provenance Display Verification

## Context
Level 3 production test. Verify the provenance component actually works — attestation bundles parse correctly, intent text is displayed, metadata renders, and the "View full bundle" toggle functions. This is the critical component that proves the loop is real.

## Type
TEST

## Execution
agent

## Dependencies
- 021-test-l1-verify-structure

## Phase Gate
- [ ] L1 structural tests passed

## Requirements
- Use Playwright MCP to:
  1. Navigate to `file:///D:/my_ai_projects/isagawa-portfolio-site/index.html`
  2. Scroll to provenance section
  3. Verify two `.attestation-card` elements are visible
  4. For each card, verify:
     - `.intent-text` has non-empty text content (the human-readable intent)
     - `.attestation-meta` shows backlog number and timestamp
     - `.verification-badge` exists (content may say "pending" if offline)
     - "View on Rekor" link has href containing `search.sigstore.dev`
  5. Click "View full bundle" button on first card
  6. Verify `.bundle-viewer` becomes visible with JSON content
  7. Verify JSON content contains `invocation` key (attestation bundle structure)

## Acceptance Criteria
- [ ] 2 attestation cards visible in provenance section
- [ ] Intent text is displayed and non-empty in both cards
- [ ] "View on Rekor" links contain `search.sigstore.dev`
- [ ] "View full bundle" toggle works, shows JSON with `invocation` key

## Gates Satisfied
- FUNC-02, FUNC-03, TEST-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
