# Visual Texture

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-portfolio-site\styles.css`

## Changes

### Body background
Replace flat `rgb(0, 0, 0)` with subtle radial gradient:
```css
body {
  background: radial-gradient(ellipse at 50% 0%, rgb(10, 10, 14) 0%, rgb(0, 0, 0) 70%);
}
```

### Grain overlay
Add a fixed-position pseudo-element on body with inline SVG feTurbulence noise:
```css
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.025;
  pointer-events: none;
  z-index: 9999;
  background-image: url("data:image/svg+xml,...feTurbulence...");
}
```

The grain must not darken text or reduce contrast. `pointer-events: none` ensures it doesn't intercept clicks.
