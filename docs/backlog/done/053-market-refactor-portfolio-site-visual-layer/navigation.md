# Navigation

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html` + `styles.css`

## Changes

### Add missing nav link
- Add `<li><a href="#this-page">This Page</a></li>` between "Self-Extension" and "Provenance"

### Logo
- `letter-spacing: 0.15em` to `0.2em`

### Nav link hover underline
```css
.nav__links a {
  position: relative;
}

.nav__links a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 50%;
  width: 0;
  height: 1px;
  background: var(--accent);
  transition: width 250ms ease, left 250ms ease;
}

.nav__links a:hover::after {
  width: 100%;
  left: 0;
}
```
Underline grows from center on hover.
