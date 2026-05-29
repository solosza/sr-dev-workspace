# Build: Write story.html

**Type:** BUILD
**Phase:** 2
**Depends on:** 002 (research report — copy comes from there), 003 (CSS classes must exist first)

## Goal

Write the complete `story.html` landing page at `D:\my_ai_projects\isagawa-co.github.io\story.html`.

## Reference Files
- `D:\my_ai_projects\isagawa-co.github.io\index.html` — copy nav, footer, and all 3 IIFE script blocks verbatim
- `D:\my_ai_projects\project_test_repos\sr_dev_workspace\projects\portfolio-message-research\research-report.md` — use validated copy from "## Refined Message" and "## Copy Elements to Use" sections
- `D:\my_ai_projects\project_test_repos\sr_dev_workspace\docs\backlog\105-market-build-portfolio-site-reframe\page-spec.md` — full page structure spec
- `D:\my_ai_projects\project_test_repos\sr_dev_workspace\docs\backlog\105-market-build-portfolio-site-reframe\conversation-origin.md` — intent chain data for Section 6 terminal script

## Page Structure

### Head
- Same `<head>` as index.html with updated title: `Isagawa | Solo Founder. Team Velocity. Proven.`
- `<link rel="stylesheet" href="styles.css">` — same stylesheet, no new CSS

### Nav
- Copy `<header class="site-header">` + `<nav class="nav">` verbatim from index.html

### Section 1 — Hero (id="hero-story", parallax-section)
- Use hero copy from research-report.md `## Copy Elements to Use → Hero headline`
- Section number `01` with `.parallax-number reveal`
- No terminal widget in hero — just the headline and one-line thesis

### Section 2 — The Loop (id="loop", anchor-section parallax-section)
- Section number `02`
- Title: "One Sentence In."
- Subtitle: use research-report.md copy
- Show the loop as a chain list (same `.chain-list` pattern as index.html Section 4):
  ```
  Natural language intent → /kernel/backlog → /kernel/execute-pipeline → Tasks executed → Signed to Rekor → Output
  ```
- Each step: one line, no jargon explanation

### Section 3 — The Numbers (id="numbers", anchor-section parallax-section)
- Section number `03`
- Title: "The Numbers"
- evidence-grid with reveal-stagger cards, use numbers from research-report.md
- 4 cards: attested runs, tasks executed, repos produced, intent per pipeline

### Section 4 — Live Proof (id="proof", anchor-section parallax-section)
- Section number `04`
- Title: "Live Proof"
- Subtitle: "Every entry below is real. Including the failed ones."
- Feed embed div: `<div class="feed-entries" id="story-feed-entries"><!-- FEED_STATIC --></div>`

### Section 5 — Go Deeper (id="depth", anchor-section parallax-section)
- Section number `05`
- Title: "Go Deeper"
- 3 evidence cards linking to: attestation.html, qa-platforms.html, feed.html

### Section 6 — How This Page Was Built (id="provenance-story", anchor-section parallax-section)
- Section number `06`
- Title: "How This Page Was Built"
- Subtitle: "Not written. Produced."
- Terminal widget (same `.terminal` + `.terminal__header` + `.terminal__body` as index.html)
- Terminal script lines (see below)
- Below terminal: `<a href="#" class="rekor-link" id="story-rekor-link" target="_blank">Verify on Rekor ↗</a>` — href filled after attestation

### Footer
- Copy verbatim from index.html

## Terminal Script (Section 6)

The lines array for the Section 6 terminal animation:

```js
var lines = [
  { text: '# how this page was built', cls: 'terminal__line--comment' },
  { text: '', cls: '' },
  { text: 'user: "what do you think about this new theme?"', cls: 'terminal__line--user' },
  { text: 'user: "maybe we just add this as its own landing page"', cls: 'terminal__line--user' },
  { text: 'user: "be sure it follows the site scroll dynamics"', cls: 'terminal__line--user' },
  { text: 'user: "research the web first on the message"', cls: 'terminal__line--user' },
  { text: 'user: "hash this conversation to the attestation"', cls: 'terminal__line--user' },
  { text: '', cls: '' },
  { text: 'intent chain \u2192 rev 1  e614fc72', cls: 'terminal__line--hash' },
  { text: 'intent chain \u2192 rev 2  cc7b7523', cls: 'terminal__line--hash' },
  { text: 'intent chain \u2192 rev 3  c00afa94', cls: 'terminal__line--hash' },
  { text: '', cls: '' },
  { text: '> /kernel/execute-pipeline 105', cls: 'terminal__line--prompt' },
  { text: '', cls: '' },
  { text: '  researching market positioning...', cls: '' },
  { text: '  \u2713 message validated \u2014 differentiated', cls: 'terminal__line--success' },
  { text: '  tasks decomposed: 8', cls: '' },
  { text: '  executing via run-task.sh...', cls: '' },
  { text: '  \u2713 8/8 complete', cls: 'terminal__line--success' },
  { text: '  signing with sigstore...', cls: '' },
  { text: '  \u2713 rekor #PENDING', cls: 'terminal__line--success' },
  { text: '', cls: '' },
  { text: '  this page is the output.', cls: 'terminal__line--emphasis' },
];
```

Note: `rekor #PENDING` gets updated to the real index after attestation runs.

## JavaScript Blocks to Copy Verbatim from index.html

1. **Mobile nav toggle** — lines 343-356
2. **Dynamic attestation counter** (feed-count.txt fetch) — lines 358-368
3. **Scroll Observer** (IntersectionObserver .reveal) — lines 529-549
4. **Parallax Scroll** (.parallax-number requestAnimationFrame) — lines 552-578
5. **Terminal Typing Animation** — lines 454-525, adapted with the Section 6 lines array above

Each must be a separate `<script>` block at bottom of body. Copy verbatim — do not simplify or rewrite.

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\story.html` exists
- [ ] File contains 6 `anchor-section__number` elements
- [ ] File contains `.reveal` class on at least 3 elements
- [ ] File contains `parallax-section` class on at least 3 sections
- [ ] File contains `terminal__body` element (Section 6 terminal)
- [ ] File contains `<!-- FEED_STATIC -->` marker in Section 4
- [ ] File contains all 5 JS blocks (mobile nav, counter, scroll observer, parallax, terminal)
- [ ] `<link rel="stylesheet" href="styles.css">` present (no inline style blocks)
