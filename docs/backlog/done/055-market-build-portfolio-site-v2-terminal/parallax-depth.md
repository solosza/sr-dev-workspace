# Parallax Depth

## Status
NEW

## Location
`isagawa-portfolio-site-v2/` — section numbers, terminal

## What It Does
Subtle parallax scrolling on select elements to create depth and the "floating" quality seen on Shader.se. Not aggressive — just enough to break the flat plane.

## Elements with Parallax
- **Section numbers (01-04):** Scroll at 0.3-0.5x speed relative to content. They appear to hang in space behind the text.
- **Terminal in hero:** Very subtle vertical parallax as user begins scrolling away from hero (terminal drifts up slower than the page).
- **Grain overlay:** Already fixed position, inherently parallax.

## Implementation
- CSS-only approach preferred: `transform: translateZ()` with `perspective` on parent
- Fallback: lightweight scroll listener with `requestAnimationFrame` and `transform: translate3d()` for GPU acceleration
- No scroll-jacking — native scroll remains untouched
- `prefers-reduced-motion` disables parallax entirely

## Performance
- Only apply to 4-5 elements total
- Use `will-change: transform` sparingly
- GPU-composited layers only (transform, opacity)
- No layout-triggering properties in scroll handlers
