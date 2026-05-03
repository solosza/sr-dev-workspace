# Extract Shader Development Studio Color Palette

## Context
Extract the full color palette from Shader — backgrounds, text colors, accent colors, CSS custom properties. This defines the dark/terminal aesthetic for the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 013-clone-screenshot-shader-mobile.md

## Requirements
- Reset viewport: `browser_resize` with `{ "width": 1440, "height": 900 }`
- Use `browser_evaluate` with the global styles extraction JS from extraction.md Step 4a:

```javascript
(() => {
  const body = document.body;
  const bodyStyles = window.getComputedStyle(body);

  // Extract CSS custom properties from :root
  const rootStyles = window.getComputedStyle(document.documentElement);
  const customProps = {};
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule.selectorText === ':root') {
          for (const prop of rule.style) {
            if (prop.startsWith('--')) {
              customProps[prop] = rule.style.getPropertyValue(prop).trim();
            }
          }
        }
      }
    } catch(e) { /* cross-origin stylesheet, skip */ }
  }

  // Extract colors from key semantic elements
  const colorSamples = {};
  const sampleSelectors = ['body', 'main', 'header', 'footer', 'h1', 'h2', 'p', 'a', 'button'];
  sampleSelectors.forEach(sel => {
    const el = document.querySelector(sel);
    if (el) {
      const cs = window.getComputedStyle(el);
      colorSamples[sel] = {
        color: cs.color,
        backgroundColor: cs.backgroundColor
      };
    }
  });

  return {
    body: {
      backgroundColor: bodyStyles.backgroundColor,
      color: bodyStyles.color
    },
    customProperties: customProps,
    colorSamples
  };
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-colors.json`
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 4a

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-colors.json` exists
- [ ] JSON contains background color, text color, and accent color values

## Gates Satisfied
CLONE-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
