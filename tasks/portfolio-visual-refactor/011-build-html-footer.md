# HTML Footer Rewrite

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
index.html

## Acceptance Criteria
Replace existing footer with 4-column layout:

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
      <p class="footer__body">© 2026 Isagawa</p>
      <p class="footer__sub">Open source</p>
    </div>
  </div>
</footer>
```

## Gates
HTML-10

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/footer-redesign.md
