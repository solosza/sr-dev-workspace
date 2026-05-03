# Fix Website Cloner Canvas/SVG/Hydration Blind Spot

## Status
Open

## Priority
Medium — the cloner skill works correctly for DOM-rendered sites but returns defaults for sites using canvas, SVG text, or deferred-hydration React components. Discovered during 044 Shader extraction.

## Summary
The website cloner skill uses `getComputedStyle()` on CSS selectors to extract design tokens. When a site renders its real visual content via canvas elements, SVG text, or deferred-hydration React components, the extracted values are defaults (16px/24px/400 weight for all elements). The skill honestly reports what the DOM returns — the problem is the extraction strategy, not the skill implementation. Need fallback extraction methods for non-DOM rendering.

## Evidence (from 044 Shader extraction)
- `shader-typography.json`: every element (h1, h2, p, a, button) returned identical 16px/24px/400 weight
- shader.se is aggressively typographic — h1s are NOT 16px in the visual rendering
- Root cause: headlines likely rendered as canvas, SVG text, or deferred-hydration components
- The skill did exactly what it was told — `getComputedStyle()` on those selectors returned the actual computed values at extraction time
- `shader-colors.json`: `--background: #fff` conflicts with body computed bg `rgb(0, 0, 0)` — suggests CSS custom properties and computed styles diverge (possibly dark mode toggle)

## Requirements
- Add a "sanity check" step after typography extraction: if all values are identical defaults, flag it as likely non-DOM rendering
- Add fallback extraction strategies:
  - Screenshot-based measurement (use Playwright screenshot + pixel analysis to estimate font sizes)
  - Wait for hydration (add configurable delay before extraction, or wait for specific DOM mutations)
  - SVG text extraction (scan for `<text>` elements inside `<svg>`, extract their font attributes)
  - Canvas inspection (check for `<canvas>` elements, log them as unextractable with a note)
- Add acceptance criteria guidance: extraction tasks should check for "all values identical" as a failure signal
- Resolve the CSS custom property vs computed style divergence (check both `getPropertyValue()` and `getComputedStyle()`)

## References
- Website cloner skill: `.claude/skills/website-cloner/`
- 044 extraction results: `data/portfolio-site/shader/`
- 051 extraction-evidence sub-doc: `docs/backlog/051-kernel-fix-execute-pipeline-gaps/extraction-evidence.md`

## Task Builder Input
- **Deliverable:** Updated website cloner skill with non-DOM rendering detection and fallback extraction strategies
- **Location:** workspace:.claude/skills/website-cloner/
- **Scope:** BUILD
- **Constraints:** Must not break existing DOM-based extraction. Fallback strategies are best-effort — some sites genuinely can't be extracted. The sanity check (identical defaults = flag) is the minimum viable fix.
