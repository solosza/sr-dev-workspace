# Add Sanity Check for Identical Defaults

## Context
The website cloner uses `getComputedStyle()` to extract typography values. When a site renders via canvas, SVG text, or deferred-hydration React components, all elements return identical defaults (16px/24px/400 weight). This task adds a sanity check after typography extraction that detects this pattern and flags it.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add a new section "Step 4f: Sanity Check — Detect Non-DOM Rendering" to `.claude/skills/website-cloner/references/extraction.md`
- Place it after the existing Step 4e (Image & SVG Extraction)
- Include a `browser_evaluate` JavaScript snippet that:
  - Collects fontSize, lineHeight, fontWeight from h1, h2, h3, p, a, button, span
  - Checks if ALL values are identical (same fontSize, same lineHeight, same fontWeight)
  - Returns `{ flagged: true/false, reason: "..." , values: {...} }`
  - If flagged, the reason should say "All elements returned identical typography defaults — likely non-DOM rendering (canvas, SVG text, or deferred hydration)"
- Add guidance text: if flagged, the agent should proceed to fallback strategies (hydration wait, SVG text extraction, canvas detection)

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains section header "Sanity Check"
- [ ] Section includes a `browser_evaluate` JavaScript block that checks for uniform defaults
- [ ] Section includes guidance on next steps when flagged

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
