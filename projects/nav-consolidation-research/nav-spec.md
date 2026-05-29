# Nav Spec (from Pipeline 106)

## Primary items (always visible)
- Logo: ISAGAWA → index.html
- Home: index.html (omitted on index.html itself)
- Feed: feed.html
- Attestation: attestation.html
- Products: dropdown trigger (not a link)
- [count] ✓: feed.html (attested counter badge)

## Dropdown label
Products ▾

## Dropdown items
- QA Platforms: qa-platforms.html
- SSH Compliance: ssh-compliance.html
- Vibe Coder: vibe-coder.html

When on a product page, that page's link gets `nav__active` class and the "Products" label also gets active indicator.

## Counter
Keep in nav as badge link to feed.html

## CSS pattern
Hover/focus-within dropdown using `.nav__dropdown` container with `.nav__dropdown-trigger` button and `.nav__dropdown-menu` list. Hidden by default (`display: none`), shown on `:hover` and `:focus-within`. Positioned absolute below trigger. Dark background matching site theme (`#0a0a0a`), border `#222`. Mobile: flat list under hamburger, no dropdown behavior.

## Removed from global nav
- Seed, Growth, Self-Extension, This Page, Provenance (on-page story anchors — not global nav items)

## HTML structure reference

```html
<nav class="nav">
  <a href="index.html" class="nav__logo">isagawa</a>
  <ul class="nav__links">
    <li><a href="index.html">Home</a></li>
    <li><a href="feed.html">Feed</a></li>
    <li><a href="attestation.html">Attestation</a></li>
    <li class="nav__dropdown">
      <button class="nav__dropdown-trigger" aria-expanded="false" aria-haspopup="true">
        Products <span class="arrow">▾</span>
      </button>
      <ul class="nav__dropdown-menu">
        <li><a href="qa-platforms.html">QA Platforms</a></li>
        <li><a href="ssh-compliance.html">SSH Compliance</a></li>
        <li><a href="vibe-coder.html">Vibe Coder</a></li>
      </ul>
    </li>
    <li class="attested-counter"><a href="feed.html"><span class="counter-number" id="nav-count">--</span> ✓</a></li>
  </ul>
  <button class="nav__hamburger" aria-label="Toggle menu">...</button>
</nav>
```
