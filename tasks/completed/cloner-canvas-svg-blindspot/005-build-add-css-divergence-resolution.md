# Add CSS Custom Property Divergence Resolution

## Context
During the Shader extraction, `--background: #fff` (CSS custom property) conflicted with body computed bg `rgb(0, 0, 0)`. This suggests CSS custom properties and computed styles can diverge (e.g., dark mode toggle, media queries). This task adds a step that compares both sources and resolves the divergence.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add a new section "Step 4g: Custom Property vs Computed Style Divergence" to `.claude/skills/website-cloner/references/extraction.md`
- Place it after the Fallback Strategy sections
- Include a `browser_evaluate` JavaScript snippet that:
  - Reads all CSS custom properties from `:root` (already done in 4a)
  - For each color-related custom property, resolves it via `getComputedStyle(document.documentElement).getPropertyValue('--prop')`
  - Compares against the corresponding computed style on the element that uses it
  - Flags divergences where custom property value differs from computed value
  - Checks for `prefers-color-scheme` media queries that might explain the divergence
  - Returns `{ divergences: [...], likely_dark_mode: true/false }`
- Add guidance: when divergence detected, prefer the computed value (what the user actually sees) but note the custom property as the "light mode" or "alternate" value

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains section header "Custom Property"
- [ ] Section includes a `browser_evaluate` JavaScript block comparing custom properties vs computed values
- [ ] Section includes guidance on resolving divergences (prefer computed, note alternates)

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
