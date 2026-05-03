# Extract Suero Studio Breakpoints

## Context
Extract all CSS media query breakpoints from Suero Studio's stylesheets. These pixel values define the responsive grid for the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 008-clone-extract-suero-nav.md

## Requirements
- Use `browser_evaluate` with the media query extraction JS from extraction.md Step 4d:

```javascript
(() => {
  const breakpoints = new Set();
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule instanceof CSSMediaRule) {
          const match = rule.conditionText.match(/(\d+)px/g);
          if (match) match.forEach(bp => breakpoints.add(bp));
        }
      }
    } catch(e) { /* cross-origin stylesheet, skip */ }
  }
  return { breakpoints: [...breakpoints].sort((a,b) => parseInt(a) - parseInt(b)) };
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-breakpoints.json`
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 4d

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-breakpoints.json` exists
- [ ] JSON contains a `breakpoints` array with pixel values

## Gates Satisfied
CLONE-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
