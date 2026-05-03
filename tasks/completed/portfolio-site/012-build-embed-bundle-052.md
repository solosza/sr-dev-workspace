# Embed Attestation Bundle #052

## Context
Second attestation bundle — pipeline #052 (cloner canvas/SVG blind spot fix). Two bundles from different pipeline runs prove the attestation is a system, not a one-off. The modularity requirement means swapping a bundle is a config change, not a code change.

## Type
BUILD

## Execution
inline

## Dependencies
- 011-build-embed-bundle-050

## Phase Gate
- [ ] First attestation bundle embedded in `index.html`

## Requirements
- Read the attestation bundle: `.claude/state/attestations/052-20260426T061644Z.json`
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Add a `<script type="application/json" id="attestation-bundle-2">` block (after the first bundle, before `</body>`)
- Embed the full bundle JSON content inside the script tag
- The card with `data-bundle="attestation-bundle-2"` will reference this data

## Acceptance Criteria
- [ ] `index.html` contains `<script type="application/json" id="attestation-bundle-2">`
- [ ] The embedded JSON contains a valid attestation bundle structure

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
