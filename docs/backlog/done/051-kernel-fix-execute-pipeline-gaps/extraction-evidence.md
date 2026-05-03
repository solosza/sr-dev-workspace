# Real-World Evidence: 044 Extraction Gaps Prove Granularity Matters

## Status
NEW — supporting evidence for the granularity reference

## What Happened (Backlog 044 Execution)

Pipeline 044 ran 14 extraction tasks against two reference sites (ethansuero.com, shader.se). Results:

### Suero extraction: thorough
- `suero-structure.md` — complete 17-section audit with heading hierarchy, nav items, content blocks
- `suero-sections.json` — CSS selectors, computed dimensions, display properties for all 17 sections
- `suero-spacing.json` — body/main/footer/16 sections + 20 containers + 7 wrappers + 16 grids with padding/margin/gap/max-width/grid-template
- `suero-nav.json` — nav component with letter-by-letter animation notes and CTA details
- `suero-breakpoints.json` — six breakpoints extracted
- `suero-components.json` — possibly missing or empty (needs verification)

### Shader extraction: thin
- `shader-colors.json` — body bg + text color + 2 custom properties. **Conflict:** `--background: #fff` but body computed bg is `rgb(0, 0, 0)`
- `shader-typography.json` — STIX Two Text font loaded correctly, but every typography sample (h1, h2, p, a, button) returned **16px/24px/400 weight**. All identical. shader.se has aggressively different typography — these are defaults, not real values.

### Root cause
The cloner skill uses `getComputedStyle()` on CSS selectors. Shader likely renders headlines as canvas elements, SVG text, or deferred-hydration React components. The typography extractor hit DOM nodes that were invisible, not yet hydrated, or semantically headings but visually something else. The skill honestly reported what the DOM returned — the task didn't account for non-DOM rendering.

## How This Proves the Granularity Point

The extraction tasks were atomic (one file per task) — that part was correct. But the **acceptance criteria** were too loose:

```markdown
# BAD acceptance criteria (what happened)
## Acceptance Criteria
- [ ] `shader-typography.json` exists
- [ ] File contains typography data
```

The file existed. It contained data. But the data was wrong (all defaults). The acceptance criteria passed but the deliverable was useless.

```markdown
# BETTER acceptance criteria (what should have been)
## Acceptance Criteria
- [ ] `shader-typography.json` exists
- [ ] File contains typography data
- [ ] h1 font-size is NOT 16px (if it is, extraction hit defaults — retry with different selectors)
- [ ] At least 3 distinct font-size values across h1/h2/p/a/button
```

This is evidence for the granularity reference: **atomic tasks need specific acceptance criteria, not just existence checks.** L1 (exists) passed. L2 (runs) passed. L3 (correct results) was never checked — because the acceptance criteria didn't define what "correct" looks like for typography extraction.

## Implication for 047 (Portfolio Site)

The portfolio will be Suero-heavy. Shader contributes only:
- STIX Two Text font family
- Color palette (with the #fff/#000 conflict to resolve)
- Dark mode intent (but not dark mode implementation — that's hand-built)

The "Suero structure + Shader aesthetic" framing needs adjustment. The site will have Suero's structure with a hand-crafted dark terminal aesthetic inspired by Shader, not a mechanical merge of both token sets.
