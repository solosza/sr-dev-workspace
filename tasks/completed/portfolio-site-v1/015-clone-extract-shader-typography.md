# Extract Shader Development Studio Typography

## Context
Extract the font families, weights, sizes, and line heights from Shader — the typographic system that gives the site its terminal/developer aesthetic.

## Type
BUILD

## Execution
inline

## Dependencies
- 014-clone-extract-shader-colors.md

## Requirements
- Use `browser_evaluate` with the font discovery JS from extraction.md Step 4b:

```javascript
(() => {
  const fonts = [];

  // 1. Check loaded fonts via document.fonts API
  for (const font of document.fonts) {
    fonts.push({
      family: font.family,
      weight: font.weight,
      style: font.style,
      status: font.status
    });
  }

  // 2. Find Google Fonts / Adobe Fonts links
  const fontLinks = [];
  document.querySelectorAll('link[href*="fonts.googleapis.com"], link[href*="fonts.gstatic.com"], link[href*="use.typekit.net"]').forEach(link => {
    fontLinks.push(link.href);
  });

  // 3. Extract @font-face declarations
  const fontFaces = [];
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule instanceof CSSFontFaceRule) {
          fontFaces.push({
            family: rule.style.getPropertyValue('font-family'),
            src: rule.style.getPropertyValue('src'),
            weight: rule.style.getPropertyValue('font-weight'),
            style: rule.style.getPropertyValue('font-style')
          });
        }
      }
    } catch(e) { /* cross-origin */ }
  }

  // 4. Extract computed typography from key elements
  const typography = {};
  ['h1','h2','h3','h4','p','a','button','code','pre'].forEach(sel => {
    const el = document.querySelector(sel);
    if (el) {
      const cs = window.getComputedStyle(el);
      typography[sel] = {
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        textTransform: cs.textTransform
      };
    }
  });

  return { loadedFonts: fonts, fontLinks, fontFaces, typography };
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-typography.json`
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 4b

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-typography.json` exists
- [ ] JSON contains font-family values for at least headings and body text

## Gates Satisfied
CLONE-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
