# Embed Attestation Bundle #050

## Context
The provenance component displays two real attestation bundles. This task embeds the first bundle — pipeline #050 (run-task.sh fix). The bundle JSON is embedded at build time as a `<script type="application/json">` block, NOT fetched at runtime. This keeps the site static while enabling live verification.

## Type
BUILD

## Execution
inline

## Dependencies
- 010-build-html-provenance

## Phase Gate
- [ ] Provenance section HTML exists with `.attestation-card` containers

## Requirements
- Read the attestation bundle: `.claude/state/attestations/050-20260425T221608Z.json`
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Add a `<script type="application/json" id="attestation-bundle-1">` block at the end of `<body>` (before closing `</body>`)
- Embed the full bundle JSON content inside the script tag
- The card with `data-bundle="attestation-bundle-1"` will reference this data

## Acceptance Criteria
- [ ] `index.html` contains `<script type="application/json" id="attestation-bundle-1">`
- [ ] The embedded JSON contains a valid attestation bundle structure

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
