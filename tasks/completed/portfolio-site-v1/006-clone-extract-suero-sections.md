# Extract Suero Studio Section Computed Styles

## Context
Extract the computed CSS styles for each major page section — layout, dimensions, colors, font sizes. This data drives the structural CSS of the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-clone-extract-suero-structure.md

## Requirements
- Use `browser_evaluate` to run the section-by-section computed styles JS from extraction.md Step 4c
- Run for each major section identified in suero-structure.md (hero, process, testimonials, CTA, footer)
- For each section, extract via this pattern (adapt selector per section):

```javascript
((selector) => {
  const el = document.querySelector(selector);
  if (!el) return null;
  const styles = window.getComputedStyle(el);
  const children = [];
  el.querySelectorAll(':scope > *').forEach((child, i) => {
    const cs = window.getComputedStyle(child);
    children.push({
      tag: child.tagName.toLowerCase(),
      classes: child.className,
      text: child.textContent?.substring(0, 100),
      styles: {
        display: cs.display, position: cs.position,
        width: cs.width, height: cs.height,
        padding: cs.padding, margin: cs.margin,
        color: cs.color, backgroundColor: cs.backgroundColor,
        fontSize: cs.fontSize, fontWeight: cs.fontWeight,
        fontFamily: cs.fontFamily, lineHeight: cs.lineHeight,
        textAlign: cs.textAlign, flexDirection: cs.flexDirection,
        justifyContent: cs.justifyContent, alignItems: cs.alignItems,
        gap: cs.gap, gridTemplateColumns: cs.gridTemplateColumns,
        borderRadius: cs.borderRadius, boxShadow: cs.boxShadow,
        opacity: cs.opacity, transform: cs.transform,
        transition: cs.transition
      }
    });
  });
  return {
    tag: el.tagName.toLowerCase(),
    styles: {
      display: styles.display, position: styles.position,
      width: styles.width, maxWidth: styles.maxWidth,
      padding: styles.padding, margin: styles.margin,
      backgroundColor: styles.backgroundColor,
      flexDirection: styles.flexDirection,
      justifyContent: styles.justifyContent,
      alignItems: styles.alignItems,
      gap: styles.gap, gridTemplateColumns: styles.gridTemplateColumns
    },
    childCount: children.length, children
  };
})('SECTION_SELECTOR')
```

- Aggregate all section results into a single JSON object keyed by section name
- Write to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-sections.json`
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 4c

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-sections.json` exists
- [ ] JSON contains at least 3 section entries with computed style data

## Gates Satisfied
CLONE-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
