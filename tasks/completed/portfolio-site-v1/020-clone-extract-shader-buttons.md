# Extract Shader Development Studio Button Styles with Hover States

## Context
Extract button styles including hover-state differences from Shader. Uses browser_hover to trigger hover states and re-extracts styles to capture the transition delta.

## Type
BUILD

## Execution
inline

## Dependencies
- 019-clone-extract-shader-terminal.md

## Requirements
- Use `browser_evaluate` to extract default button styles first:

```javascript
(() => {
  const buttons = [];
  document.querySelectorAll('button, a[class*="btn"], a[class*="button"], [class*="cta"], [role="button"]').forEach((el, i) => {
    const cs = window.getComputedStyle(el);
    buttons.push({
      index: i,
      text: el.textContent.trim().substring(0, 50),
      tag: el.tagName.toLowerCase(),
      classes: el.className,
      selector: el.tagName.toLowerCase() + (el.className ? '.' + el.className.toString().split(' ').join('.') : ''),
      defaultStyles: {
        display: cs.display,
        padding: cs.padding,
        backgroundColor: cs.backgroundColor,
        color: cs.color,
        border: cs.border,
        borderRadius: cs.borderRadius,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        fontFamily: cs.fontFamily,
        textTransform: cs.textTransform,
        letterSpacing: cs.letterSpacing,
        cursor: cs.cursor,
        transition: cs.transition,
        boxShadow: cs.boxShadow,
        textShadow: cs.textShadow,
        textDecoration: cs.textDecoration
      }
    });
  });
  return buttons;
})()
```

- For each button found (up to 3), use `browser_hover` on the button's selector
- After hovering, use `browser_evaluate` to re-extract that button's computed styles
- Compare default vs hovered styles to identify the hover delta
- Combine default styles and hover deltas into final output
- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-buttons.json`
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 5

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-buttons.json` exists
- [ ] JSON contains at least one button with default styles
- [ ] At least one button entry includes hover state differences (if hover effects exist)

## Gates Satisfied
CLONE-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
