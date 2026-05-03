# Gate Contract — Portfolio Visual Refactor

| ID | Check | Method | File | Pass Criteria |
|----|-------|--------|------|---------------|
| CSS-01 | Hero h1 uses clamp typography | grep | styles.css | `clamp(4rem, 9vw, 8rem)` present |
| CSS-02 | Hero h1 has gradient text | grep | styles.css | `background-clip: text` present in #hero h1 block |
| CSS-03 | Section h2 uses clamp | grep | styles.css | `clamp(2.75rem, 5.5vw, 5rem)` present |
| CSS-04 | Body line-height 1.7 | grep | styles.css | `line-height: 1.7` in body rule |
| CSS-05 | Anchor numbers massive + transparent | grep | styles.css | `clamp(5rem, 12vw, 11rem)` and `opacity: 0.08` present |
| CSS-06 | Section padding uses clamp | grep | styles.css | `clamp(8rem, 18vh, 18rem)` present |
| CSS-07 | Radial gradient background | grep | styles.css | `radial-gradient` in body rule |
| CSS-08 | Grain overlay pseudo-element | grep | styles.css | `feTurbulence` present in body::before |
| CSS-09 | Card hover translateY | grep | styles.css | `translateY(-2px)` present |
| CSS-10 | Tag list styles exist | grep | styles.css | `.card-tags` rule present |
| CSS-11 | Chain list line-height 2.4 | grep | styles.css | `line-height: 2.4` in chain-list rule |
| CSS-12 | Badge pulse animation | grep | styles.css | `badge-pulse` keyframes present |
| CSS-13 | Nav underline hover | grep | styles.css | `.nav__links a::after` rule present |
| CSS-14 | Footer grid layout | grep | styles.css | `.footer__grid` rule present |
| CSS-15 | No conflicting 1400px hero override | grep | styles.css | No `2.5rem` in 1400px media query |
| CSS-16 | Bold emphasis styles | grep | styles.css | `.anchor-section__narrative strong` rule present |
| CSS-17 | Chain climax class | grep | styles.css | `.chain-climax` rule present |
| HTML-01 | Em dashes removed from copy | grep | index.html | No `—` in non-script content (excluding JS fallback) |
| HTML-02 | Bold emphasis tags present | grep | index.html | `<strong>natural language</strong>` present |
| HTML-03 | Tag lists on Seed cards | grep | index.html | `GOVERNANCE / PROTOCOL / TOKEN` present |
| HTML-04 | Workspaces stat added | grep | index.html | `GOVERNED` present in evidence-stat |
| HTML-05 | Website Cloner stat added | grep | index.html | `122` in evidence-stat span |
| HTML-06 | Attestation Pipeline stat added | grep | index.html | `5` in evidence-stat span near Attestation Pipeline |
| HTML-07 | This Page nav link exists | grep | index.html | `href="#this-page"` in nav__links |
| HTML-08 | Hero CTA has span-wrapped arrow | grep | index.html | `<span class="hero__arrow">` present |
| HTML-09 | Scroll caption present | grep | index.html | `OR SCROLL` present |
| HTML-10 | Footer has 4 columns | grep | index.html | `footer__grid` present |
| HTML-11 | Third attestation card exists | grep | index.html | `attestation-bundle-3` present |
| HTML-12 | Third bundle JSON embedded | grep | index.html | `id="attestation-bundle-3"` present |
| TEST-01 | Desktop renders correctly at 1440x900 | manual | screenshot | Hero gradient visible, sections spaced, cards have depth |
| TEST-02 | Mobile renders correctly at 375x812 | manual | screenshot | Single column, hamburger visible, readable |
| TEST-03 | Card hover works | run_code | Playwright | translateY visible on hover |
| TEST-04 | Badge pulse animates | run_code | Playwright | Verified badge has animation |
