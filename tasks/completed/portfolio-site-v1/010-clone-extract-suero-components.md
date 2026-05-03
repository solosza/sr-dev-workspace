# Extract Suero Studio Component Styles

## Context
Extract styles for reusable UI components — buttons, cards, accordions — from Suero Studio. These define the interactive component library for the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 009-clone-extract-suero-breakpoints.md

## Requirements
- Use `browser_evaluate` to extract button styles:

```javascript
(() => {
  const components = { buttons: [], cards: [], accordions: [] };

  // Buttons
  document.querySelectorAll('button, a[class*="btn"], a[class*="button"], [class*="cta"]').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    components.buttons.push({
      text: el.textContent.trim().substring(0, 50),
      tag: el.tagName.toLowerCase(),
      classes: el.className,
      styles: {
        display: cs.display, padding: cs.padding,
        backgroundColor: cs.backgroundColor, color: cs.color,
        border: cs.border, borderRadius: cs.borderRadius,
        fontSize: cs.fontSize, fontWeight: cs.fontWeight,
        fontFamily: cs.fontFamily, textTransform: cs.textTransform,
        letterSpacing: cs.letterSpacing, cursor: cs.cursor,
        transition: cs.transition, boxShadow: cs.boxShadow
      }
    });
  });

  // Cards
  document.querySelectorAll('[class*="card"], [class*="item"], [class*="project"]').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    components.cards.push({
      classes: el.className,
      styles: {
        display: cs.display, padding: cs.padding,
        backgroundColor: cs.backgroundColor,
        border: cs.border, borderRadius: cs.borderRadius,
        boxShadow: cs.boxShadow, overflow: cs.overflow
      }
    });
  });

  // Accordions / expandable elements
  document.querySelectorAll('[class*="accordion"], [class*="faq"], details, [class*="expand"]').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    components.accordions.push({
      classes: el.className,
      tag: el.tagName.toLowerCase(),
      styles: {
        display: cs.display, padding: cs.padding,
        border: cs.border, borderRadius: cs.borderRadius,
        backgroundColor: cs.backgroundColor,
        transition: cs.transition
      }
    });
  });

  return components;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-components.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-components.json` exists
- [ ] JSON contains at least a `buttons` array with style data

## Gates Satisfied
CLONE-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
