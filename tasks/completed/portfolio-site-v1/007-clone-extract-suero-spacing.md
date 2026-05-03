# Extract Suero Studio Spacing System

## Context
Extract the spacing system — paddings, margins, gaps, max-widths, grid values — to replicate Suero's layout rhythm in the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-clone-extract-suero-sections.md

## Requirements
- Use `browser_evaluate` to extract spacing properties from all major containers and sections:

```javascript
(() => {
  const spacingData = {};
  const selectors = ['body', 'main', 'header', 'footer', 'section', '[class*="container"]', '[class*="wrapper"]', '[class*="grid"]'];
  selectors.forEach(sel => {
    document.querySelectorAll(sel).forEach((el, i) => {
      const cs = window.getComputedStyle(el);
      const key = sel + (i > 0 ? `[${i}]` : '');
      spacingData[key] = {
        padding: cs.padding,
        paddingTop: cs.paddingTop,
        paddingBottom: cs.paddingBottom,
        paddingLeft: cs.paddingLeft,
        paddingRight: cs.paddingRight,
        margin: cs.margin,
        marginTop: cs.marginTop,
        marginBottom: cs.marginBottom,
        gap: cs.gap,
        rowGap: cs.rowGap,
        columnGap: cs.columnGap,
        maxWidth: cs.maxWidth,
        width: cs.width,
        gridTemplateColumns: cs.gridTemplateColumns,
        gridTemplateRows: cs.gridTemplateRows
      };
    });
  });
  return spacingData;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-spacing.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-spacing.json` exists
- [ ] JSON contains padding, margin, and gap values for multiple elements

## Gates Satisfied
CLONE-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
