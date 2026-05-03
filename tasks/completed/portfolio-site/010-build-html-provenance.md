# Write Provenance Section HTML

## Context
The provenance section is a dedicated section (not just a footer link) showing real Sigstore attestation bundles. This is the proof that the loop is a system, not a stunt. Two attestation bundles displayed side by side — two proves a system, one proves a stunt. The component is modular so any bundle can be swapped.

## Type
BUILD

## Execution
inline

## Dependencies
- 009-build-css-section-detail

## Phase Gate
- [ ] All 4 anchor moment sections styled in `styles.css`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Replace provenance stub with content:
  - Section heading: "Provenance"
  - Intro text: "Every pipeline run is signed with Sigstore and logged to Rekor. These are real attestation bundles — verify them yourself."
  - Two `.attestation-card` containers, each with:
    - `.intent-text` — the human-readable intent string (this LEADS — visitor's eye hits this first)
    - `.attestation-meta` — backlog number, task count, timestamp
    - `.verification-badge` — placeholder div with class `verification-badge` (JS fills this)
    - `.attestation-actions` — two buttons: "View on Rekor" (link) and "View full bundle" (toggle)
    - `.bundle-viewer` — hidden div for expandable JSON display
  - First card: `data-bundle="attestation-bundle-1"` attribute
  - Second card: `data-bundle="attestation-bundle-2"` attribute
- Reference: `docs/backlog/047-market-build-portfolio-site-loop-theme/theme-and-narrative.md` (Provenance Component Spec)

## Acceptance Criteria
- [ ] `index.html` provenance section contains 2 `.attestation-card` elements
- [ ] `index.html` provenance section contains `.intent-text` elements
- [ ] `index.html` provenance section contains `.verification-badge` elements
- [ ] `index.html` provenance section contains "View on Rekor" text

## Gates Satisfied
- BUILD-08, FUNC-03 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
