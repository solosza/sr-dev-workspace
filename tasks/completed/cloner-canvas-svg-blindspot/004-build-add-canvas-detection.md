# Add Canvas Detection Strategy

## Context
Some sites render content via `<canvas>` elements (WebGL, Three.js, etc.). Canvas content cannot be extracted via DOM APIs — it's rendered pixels. This task adds detection for canvas-based rendering and logs it appropriately.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add a new section "Fallback Strategy 3: Canvas Detection" to `.claude/skills/website-cloner/references/extraction.md`
- Place it after the SVG Text Extraction section
- Include a `browser_evaluate` JavaScript snippet that:
  - Finds all `<canvas>` elements
  - For each, reports: width, height, whether it has a WebGL context (`canvas.getContext('webgl')` or `'webgl2'`)
  - Estimates visual dominance (canvas area / viewport area)
  - Returns `{ canvas_found: true/false, elements: [...], dominant: true/false }`
- Add guidance: if canvas is dominant (>50% viewport), note that typography extraction is unreliable and the agent should use screenshot-based estimation or skip typography for that section
- Mark canvas content as "unextractable" — don't attempt to clone the canvas rendering

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains section header "Canvas Detection"
- [ ] Section includes a `browser_evaluate` JavaScript block detecting `<canvas>` elements
- [ ] Section includes guidance on handling dominant canvas content

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
