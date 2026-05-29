# Build: Add Factory Origin CSS to styles.css

**Type:** BUILD
**Phase:** 1

## Goal

Add CSS for the `.factory-origin` strip to `D:\my_ai_projects\isagawa-co.github.io\styles.css`. This is the thin banner that appears on every product page signaling its relationship to the factory.

## CSS to Add

Add near the top of the file, after the `:root` / base variables block:

```css
/* Factory origin strip — product pages only */
.factory-origin {
  display: block;
  width: 100%;
  padding: 0.4rem 2rem;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  opacity: 0.5;
  border-bottom: 1px solid var(--border, rgba(255,255,255,0.08));
  text-align: left;
}
.factory-origin a {
  color: inherit;
  text-decoration: none;
}
.factory-origin a:hover {
  opacity: 1;
  text-decoration: underline;
}
```

## Acceptance Criteria
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/styles.css` exits 0
