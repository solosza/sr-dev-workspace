# 005 — Update Nav with Attestation Counter

**Type:** BUILD
**Depends on:** 003

## Requirements
Edit `D:\my_ai_projects\isagawa-co.github.io\index.html` to add an attestation counter in the nav bar.

- Add a `<li>` element with class `attested-counter` to the `nav__links` list
- Content: `<a href="feed.html"><span class="counter-number">N</span> ✓</a>` where N is read from `feed-count.txt`
- Since this is static HTML (no build step), read the count from `feed-count.txt` and hard-code the number in the HTML
- Position: after the last nav link (Provenance) but before the hamburger button
- Add corresponding CSS in `styles.css`: `.attested-counter` styled subtly — smaller font, muted color, doesn't compete with section links

## Acceptance Criteria
- [ ] `index.html` contains element with class `attested-counter`
- [ ] Counter displays a number followed by ✓
- [ ] Counter links to `feed.html`
