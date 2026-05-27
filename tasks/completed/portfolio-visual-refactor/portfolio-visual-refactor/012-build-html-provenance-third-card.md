# HTML Provenance Third Card + Bundle Embed

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
index.html

## Acceptance Criteria
1. Add third `.attestation-card` div with `data-bundle="attestation-bundle-3"` after the existing two cards, using the same HTML structure (intent-text, attestation-meta, verification-badge, attestation-actions, bundle-viewer)
2. Add `<script type="application/json" id="attestation-bundle-3">` containing the #047 attestation bundle JSON
3. Read the bundle from: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\state\attestations\047-20260426T071022Z.json`
4. The existing JS will auto-populate the card from the embedded JSON (no JS changes needed)

## Gates
HTML-11, HTML-12

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/provenance-upgrade.md
