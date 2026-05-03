# Extract Shader Development Studio Animation & Transition Styles

## Context
Extract transition properties, timing functions, and animation patterns from Shader. These motion values define the interactive feel of the portfolio site.

## Type
BUILD

## Execution
inline

## Dependencies
- 017-clone-extract-shader-borders.md

## Requirements
- Use `browser_evaluate` to extract transition and animation properties:

```javascript
(() => {
  const animations = { transitions: [], keyframes: [], animatedElements: [] };

  // Collect all elements with transitions
  document.querySelectorAll('*').forEach(el => {
    const cs = window.getComputedStyle(el);
    if (cs.transition && cs.transition !== 'all 0s ease 0s' && cs.transition !== 'none') {
      animations.transitions.push({
        tag: el.tagName.toLowerCase(),
        classes: (el.className || '').toString().substring(0, 80),
        transition: cs.transition,
        transitionProperty: cs.transitionProperty,
        transitionDuration: cs.transitionDuration,
        transitionTimingFunction: cs.transitionTimingFunction,
        transitionDelay: cs.transitionDelay
      });
    }
    if (cs.animationName && cs.animationName !== 'none') {
      animations.animatedElements.push({
        tag: el.tagName.toLowerCase(),
        classes: (el.className || '').toString().substring(0, 80),
        animationName: cs.animationName,
        animationDuration: cs.animationDuration,
        animationTimingFunction: cs.animationTimingFunction,
        animationIterationCount: cs.animationIterationCount,
        animationDirection: cs.animationDirection
      });
    }
  });

  // Extract @keyframes rules
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule instanceof CSSKeyframesRule) {
          const frames = [];
          for (const kf of rule.cssRules) {
            frames.push({ keyText: kf.keyText, cssText: kf.cssText.substring(0, 200) });
          }
          animations.keyframes.push({ name: rule.name, frames });
        }
      }
    } catch(e) { /* cross-origin */ }
  }

  // Limit transitions to first 20
  animations.transitions = animations.transitions.slice(0, 20);

  return animations;
})()
```

- Write results to `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-animations.json`

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-animations.json` exists
- [ ] JSON contains transition or animation entries

## Gates Satisfied
CLONE-17

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
