# Extract Suero Studio Navigation Component

## Context
Extract the navigation component's full style profile — positioning, background, link styles, mobile toggle behavior — to replicate it in the portfolio site header.

## Type
BUILD

## Execution
inline

## Dependencies
- 007-clone-extract-suero-spacing.md

## Requirements
- Use `browser_evaluate` to extract navigation styles:

```javascript
(() => {
  const nav = document.querySelector('nav') || document.querySelector('header');
  if (!nav) return { error: 'No nav/header found' };
  const cs = window.getComputedStyle(nav);
  const links = [];
  nav.querySelectorAll('a').forEach(a => {
    const ls = window.getComputedStyle(a);
    links.push({
      text: a.textContent.trim(),
      href: a.getAttribute('href'),
      styles: {
        color: ls.color,
        fontSize: ls.fontSize,
        fontWeight: ls.fontWeight,
        fontFamily: ls.fontFamily,
        textDecoration: ls.textDecoration,
        textTransform: ls.textTransform,
        letterSpacing: ls.letterSpacing,
        padding: ls.padding
      }
    });
  });
  return {
    element: nav.tagName.toLowerCase(),
    classes: nav.className,
    styles: {
      position: cs.position,
      top: cs.top,
      left: cs.left,
      width: cs.width,
      height: cs.height,
      backgroundColor: cs.backgroundColor,
      backdropFilter: cs.backdropFilter,
      padding: cs.padding,
      display: cs.display,
      justifyContent: cs.justifyContent,
      alignItems: cs.alignItems,
      gap: cs.gap,
      zIndex: cs.zIndex,
      borderBottom: cs.borderBottom,
      boxShadow: cs.boxShadow
    },
    links
  };
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-nav.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-nav.json` exists
- [ ] JSON contains nav position, background, and at least one link entry

## Gates Satisfied
CLONE-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
