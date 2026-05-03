# Hero CTA

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html` + `styles.css`

## Changes

### Button sizing
- `padding: 0.875rem 1.75rem`

### Arrow rotation on hover
```css
.hero__cta span {
  display: inline-block;
  transition: transform 200ms ease;
}

.hero__cta:hover span {
  transform: rotate(-45deg);
}
```
Requires wrapping the arrow in a `<span>` in HTML: `See the loop <span>→</span>`

### Scroll caption
Add below the CTA in HTML:
```html
<span class="hero__scroll-hint">OR SCROLL ↓</span>
```

CSS:
```css
.hero__scroll-hint {
  display: block;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
  letter-spacing: 0.1em;
  margin-top: var(--space-md);
}
```
