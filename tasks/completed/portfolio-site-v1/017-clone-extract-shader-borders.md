# Extract Shader Development Studio Border & Shadow Styles

## Context
Extract border colors, widths, radii, and shadow/glow effects from Shader. Terminal-aesthetic sites often use subtle borders and glow effects that define the visual identity.

## Type
BUILD

## Execution
inline

## Dependencies
- 016-clone-extract-shader-surfaces.md

## Requirements
- Use `browser_evaluate` to extract border and shadow properties:

```javascript
(() => {
  const borders = { elements: [], summaryRadii: new Set(), summaryColors: new Set() };

  document.querySelectorAll('*').forEach(el => {
    const cs = window.getComputedStyle(el);
    const hasBorder = cs.borderWidth !== '0px' && cs.borderStyle !== 'none';
    const hasShadow = cs.boxShadow !== 'none';
    const hasRadius = cs.borderRadius !== '0px';

    if (hasBorder || hasShadow || hasRadius) {
      borders.elements.push({
        tag: el.tagName.toLowerCase(),
        classes: (el.className || '').toString().substring(0, 100),
        borderWidth: cs.borderWidth,
        borderStyle: cs.borderStyle,
        borderColor: cs.borderColor,
        borderRadius: cs.borderRadius,
        boxShadow: cs.boxShadow,
        outline: cs.outline
      });
      if (hasRadius) borders.summaryRadii.add(cs.borderRadius);
      if (hasBorder) borders.summaryColors.add(cs.borderColor);
    }
  });

  // Convert Sets to arrays for JSON serialization
  borders.summaryRadii = [...borders.summaryRadii];
  borders.summaryColors = [...borders.summaryColors];
  // Limit elements to first 30 to avoid huge output
  borders.elements = borders.elements.slice(0, 30);

  return borders;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-borders.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-borders.json` exists
- [ ] JSON contains border radius values and border color values

## Gates Satisfied
CLONE-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
