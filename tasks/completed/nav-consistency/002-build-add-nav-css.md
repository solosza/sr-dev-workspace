# Build: Add Nav Dropdown CSS + JS to styles.css

**Type:** BUILD
**Phase:** 1
**Depends on:** 001

## Goal

Add dropdown CSS and JS to `D:\my_ai_projects\isagawa-co.github.io\styles.css` and create an inline JS snippet for keyboard/aria support.

## CSS to Add

Add after the existing `.nav__links` block (before `.nav__hamburger`):

```css
/* Nav dropdown */
.nav__dropdown {
  position: relative;
}
.nav__dropdown-trigger {
  background: none;
  border: none;
  color: inherit;
  font: inherit;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
.nav__dropdown-menu {
  display: none;
  position: absolute;
  top: calc(100% + 0.5rem);
  left: 0;
  background: var(--bg, #0a0a0a);
  border: 1px solid var(--border, rgba(255,255,255,0.12));
  padding: 0.5rem 0;
  min-width: 180px;
  z-index: 100;
  list-style: none;
  margin: 0;
}
.nav__dropdown:hover .nav__dropdown-menu,
.nav__dropdown:focus-within .nav__dropdown-menu {
  display: block;
}
.nav__dropdown-menu li {
  padding: 0;
}
.nav__dropdown-menu a {
  display: block;
  padding: 0.4rem 1rem;
  white-space: nowrap;
}
@media (max-width: 768px) {
  .nav__dropdown-menu {
    display: block;
    position: static;
    border: none;
    padding: 0;
    min-width: unset;
  }
  .nav__dropdown-trigger::after {
    display: none;
  }
}
```

## Acceptance Criteria
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/styles.css` exits 0
- [ ] `grep -q "nav__dropdown-menu" D:/my_ai_projects/isagawa-co.github.io/styles.css` exits 0
- [ ] `grep -q "nav__dropdown-trigger" D:/my_ai_projects/isagawa-co.github.io/styles.css` exits 0
