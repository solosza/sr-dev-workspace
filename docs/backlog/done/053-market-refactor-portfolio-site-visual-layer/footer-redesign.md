# Footer Redesign (Shader-derived)

## Status
EXISTS (needs major rewrite)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html` + `styles.css`

## Current
Single-line footer: tagline + email link + copyright.

## Target
4-column layout matching Shader's dense footer pattern.

### HTML structure
```html
<footer>
  <div class="footer__grid">
    <div class="footer__col">
      <span class="footer__label">About</span>
      <p class="footer__body">Built by the system it describes.</p>
      <p class="footer__sub">An attested artifact.</p>
    </div>
    <div class="footer__col">
      <span class="footer__label">Contact</span>
      <a href="mailto:hello@isagawa.dev">hello@isagawa.dev</a>
    </div>
    <div class="footer__col">
      <span class="footer__label">Verify</span>
      <a href="https://search.sigstore.dev/?logIndex=1384683702">Rekor #1384683702</a>
      <a href="https://search.sigstore.dev/?logIndex=1387514162">Rekor #1387514162</a>
      <a href="https://search.sigstore.dev/?logIndex=1387966928">Rekor #1387966928</a>
    </div>
    <div class="footer__col">
      <span class="footer__label">Legal</span>
      <p>© 2026 Isagawa</p>
      <p class="footer__sub">Open source</p>
    </div>
  </div>
</footer>
```

### CSS
- `.footer__grid`: 4-column grid on desktop, single column on mobile
- `.footer__label`: small caps, `--font-mono`, `letter-spacing: 0.1em`, `--text-secondary`
- Footer links: `--font-mono`, `--text-xs`, `--accent`
- Padding: `clamp(4rem, 8vh, 6rem)` top/bottom
- Border-top: `1px solid var(--border-subtle)`
