# Extract Shader Development Studio Surface Layers

## Context
Extract the background surface hierarchy — base, card, elevated, overlay — to replicate Shader's depth layering system in the portfolio site's dark theme.

## Type
BUILD

## Execution
inline

## Dependencies
- 015-clone-extract-shader-typography.md

## Requirements
- Use `browser_evaluate` to extract background colors at different depth levels:

```javascript
(() => {
  const surfaces = { base: null, cards: [], elevated: [], overlays: [] };

  // Base surface
  const bodyCs = window.getComputedStyle(document.body);
  surfaces.base = {
    backgroundColor: bodyCs.backgroundColor,
    color: bodyCs.color
  };

  // Cards / content containers
  document.querySelectorAll('[class*="card"], [class*="panel"], [class*="box"], [class*="item"], article').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== bodyCs.backgroundColor) {
      surfaces.cards.push({
        classes: el.className,
        backgroundColor: cs.backgroundColor,
        boxShadow: cs.boxShadow,
        border: cs.border,
        borderRadius: cs.borderRadius
      });
    }
  });

  // Elevated elements (modals, dropdowns, tooltips)
  document.querySelectorAll('[class*="modal"], [class*="dropdown"], [class*="tooltip"], [class*="popup"]').forEach(el => {
    const cs = window.getComputedStyle(el);
    surfaces.elevated.push({
      classes: el.className,
      backgroundColor: cs.backgroundColor,
      boxShadow: cs.boxShadow,
      zIndex: cs.zIndex
    });
  });

  // Sections with distinct backgrounds
  document.querySelectorAll('section').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    surfaces.overlays.push({
      index: i,
      classes: el.className,
      backgroundColor: cs.backgroundColor,
      backgroundImage: cs.backgroundImage !== 'none' ? cs.backgroundImage.substring(0, 200) : 'none'
    });
  });

  return surfaces;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-surfaces.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-surfaces.json` exists
- [ ] JSON contains a `base` background color and at least one additional surface layer

## Gates Satisfied
CLONE-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
