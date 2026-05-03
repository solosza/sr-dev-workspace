# Design Tokens

## Status
NEW — generated during Phase 2 (merge) from extracted donor site data

## Overview
Merged design system combining Shader's visual identity with Suero's structural spacing. All values stored as CSS custom properties in `:root`.

## Color Palette (from Shader)
Extract exact values via `getComputedStyle()` during clone phase. Expected token structure:

```css
:root {
  /* Backgrounds */
  --bg-primary: /* Shader's main background */;
  --bg-surface: /* Shader's card/elevated surface */;
  --bg-elevated: /* Shader's highest elevation */;

  /* Text */
  --text-primary: /* Shader's primary text */;
  --text-secondary: /* Shader's muted/secondary text */;
  --text-accent: /* Shader's accent/highlight color */;

  /* Accent */
  --accent: /* Shader's primary accent */;
  --accent-hover: /* Shader's accent hover state */;
  --accent-glow: /* If Shader uses glow effects */;

  /* Borders */
  --border-subtle: /* Shader's subtle border */;
  --border-strong: /* Shader's visible border */;
}
```

## Typography (from Shader)
Extract font families, weights, and sizes. Expected structure:

```css
:root {
  --font-heading: /* Shader's heading font */;
  --font-body: /* Shader's body font */;
  --font-mono: /* Shader's monospace/code font, or fallback */;

  /* Scale */
  --text-xs: /* ~12px */;
  --text-sm: /* ~14px */;
  --text-base: /* ~16px */;
  --text-lg: /* ~18-20px */;
  --text-xl: /* ~24px */;
  --text-2xl: /* ~32px */;
  --text-3xl: /* ~48px */;
  --text-hero: /* ~64-80px */;
}
```

## Spacing (from Suero)
Extract spacing scale from Suero's section padding and element gaps:

```css
:root {
  --space-xs: /* ~4-8px */;
  --space-sm: /* ~12-16px */;
  --space-md: /* ~24-32px */;
  --space-lg: /* ~48-64px */;
  --space-xl: /* ~80-96px */;
  --space-section: /* vertical padding between sections */;

  --max-width: /* Suero's content max-width */;
  --grid-gap: /* Suero's grid gap */;
}
```

## Component Tokens
Derived from both donors:

```css
:root {
  /* Buttons */
  --btn-bg: var(--accent);
  --btn-text: var(--bg-primary);
  --btn-radius: /* from Suero */;
  --btn-padding: /* from Suero */;

  /* Cards */
  --card-bg: var(--bg-surface);
  --card-border: var(--border-subtle);
  --card-radius: /* from Suero */;
  --card-padding: /* from Suero */;

  /* Badges (spec type) */
  --badge-build-bg: /* accent variant for BUILD */;
  --badge-workspace-bg: /* accent variant for WORKSPACE */;
  --badge-operate-bg: /* accent variant for OPERATE */;
}
```

## Dependencies
- Requires completed extraction from both donor sites (Phase 1)
- Values are populated by reading extraction output, not hardcoded
