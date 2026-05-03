# Extract Shader Development Studio Terminal/CRT Effects

## Context
Check for and extract terminal-aesthetic effects — scan lines, phosphor glow, CRT styling, monospace code blocks, blinking cursors. These signature effects define Shader's visual identity.

## Type
BUILD

## Execution
inline

## Dependencies
- 018-clone-extract-shader-animations.md

## Requirements
- Use `browser_evaluate` to detect and extract terminal-style patterns:

```javascript
(() => {
  const terminal = {
    scanLines: null,
    glowEffects: [],
    crtEffects: [],
    codeBlocks: [],
    cursorEffects: [],
    pseudoElements: []
  };

  // Check for scan-line overlays (often via ::before/::after with repeating gradients)
  document.querySelectorAll('*').forEach(el => {
    const cs = window.getComputedStyle(el);
    const before = window.getComputedStyle(el, '::before');
    const after = window.getComputedStyle(el, '::after');

    // Detect background gradients that look like scan lines
    [cs, before, after].forEach((styles, idx) => {
      const bgImage = styles.backgroundImage;
      if (bgImage && bgImage !== 'none' && (bgImage.includes('repeating') || bgImage.includes('linear-gradient'))) {
        terminal.scanLines = terminal.scanLines || [];
        terminal.scanLines.push({
          element: el.tagName.toLowerCase() + (el.className ? '.' + (el.className.toString().split(' ')[0] || '') : ''),
          pseudo: idx === 1 ? '::before' : idx === 2 ? '::after' : 'element',
          backgroundImage: bgImage.substring(0, 300)
        });
      }
    });

    // Detect glow effects (text-shadow with bright colors)
    if (cs.textShadow && cs.textShadow !== 'none') {
      terminal.glowEffects.push({
        tag: el.tagName.toLowerCase(),
        classes: (el.className || '').toString().substring(0, 80),
        textShadow: cs.textShadow,
        color: cs.color
      });
    }

    // Detect monospace / code block styling
    if (cs.fontFamily && cs.fontFamily.toLowerCase().includes('mono')) {
      terminal.codeBlocks.push({
        tag: el.tagName.toLowerCase(),
        classes: (el.className || '').toString().substring(0, 80),
        fontFamily: cs.fontFamily,
        backgroundColor: cs.backgroundColor,
        color: cs.color,
        padding: cs.padding,
        borderRadius: cs.borderRadius
      });
    }
  });

  // Detect blinking cursor animations
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule instanceof CSSKeyframesRule && (rule.name.includes('blink') || rule.name.includes('cursor') || rule.name.includes('caret'))) {
          terminal.cursorEffects.push({ name: rule.name, cssText: rule.cssText.substring(0, 300) });
        }
      }
    } catch(e) { /* cross-origin */ }
  }

  // Limit arrays
  if (terminal.scanLines) terminal.scanLines = terminal.scanLines.slice(0, 10);
  terminal.glowEffects = terminal.glowEffects.slice(0, 10);
  terminal.codeBlocks = terminal.codeBlocks.slice(0, 10);

  return terminal;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-terminal.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-terminal.json` exists
- [ ] JSON contains at least one category of terminal effects (glowEffects, codeBlocks, scanLines, or cursorEffects)

## Gates Satisfied
CLONE-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
