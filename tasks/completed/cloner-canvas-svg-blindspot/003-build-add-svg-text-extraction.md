# Add SVG Text Extraction Strategy

## Context
Some sites render headlines and text inside `<svg>` elements using `<text>` tags. `getComputedStyle()` on CSS selectors like `h1` won't capture these. This task adds a fallback that scans for `<text>` elements inside `<svg>` and extracts their font attributes.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add a new section "Fallback Strategy 2: SVG Text Extraction" to `.claude/skills/website-cloner/references/extraction.md`
- Place it after the Hydration Wait section
- Include a `browser_evaluate` JavaScript snippet that:
  - Finds all `<text>` elements inside `<svg>` elements
  - For each, extracts: textContent (truncated), font-size, font-family, font-weight, fill color, x/y position
  - Groups by likely role (largest = h1, second largest = h2, etc.)
  - Returns `{ svg_text_found: true/false, elements: [...] }`
- Add guidance: use SVG text attributes as the typography values when DOM extraction returned defaults

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains section header "SVG Text"
- [ ] Section includes a `browser_evaluate` JavaScript block scanning `<text>` in `<svg>`
- [ ] Section includes guidance on mapping SVG text to typography roles

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
