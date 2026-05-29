# Page Spec

## Status
NEW — blocked on message-research.md (Phase 1 must complete first; copy TBD by research output)

## Location
`D:\my_ai_projects\isagawa-co.github.io\story.html`

## Page Structure

### Section 1 — Hero (above fold)
- Thesis, plain. No jargon. Legible in 10 seconds to a hiring manager or client.
- Exact copy TBD by message-research — use validated framing, not the draft
- Section number: `01` with `.parallax-number` on `.parallax-section`

### Section 2 — The Loop Mechanic
- One sentence per step: `sentence → /kernel/backlog → /kernel/execute-pipeline → attested output`
- "No human between start and finish" stated explicitly
- Explained without kernel-specific terminology (a first-time visitor should understand it)
- Section number: `02`

### Section 3 — The Numbers (Evidence Cards)
- Hard specifics as `.evidence-grid` + `.evidence-card` cards with `.reveal-stagger`
- Card content driven by message-research findings — use whatever numbers research confirms land hardest
- Draft candidates: `80+` attested runs · `800+` tasks · `9` repos · `1 sentence` per pipeline
- Section number: `03`

### Section 4 — Live Proof (Feed Embed)
- Latest 10 feed entries rendered inline, server-side (same `<!-- FEED_STATIC -->` pattern as pipeline 101)
- NOT a link to feed.html — entries visible without clicking anything
- Callout line near section header: authenticity framing (messy entries are credibility, not a flaw)
- Section number: `04`

### Section 5 — Go Deeper
- Three cards linking into the main site: attestation page, QA platforms, full feed
- Clean, no extra nav — just these three paths

### Section 6 — This Page's Own Provenance (the meta-proof)
This is the most important section. It shows the full chain that produced this specific page — as a terminal animation, real-time, playing out as the visitor scrolls to it.

**The terminal replays the actual conversation and pipeline run that built this page.**

Use the exact same terminal component as the homepage hero (`terminal__header` + `terminal__body` + typing animation IIFE). Same CSS classes, same character-by-character typewriter, same cursor. Copy the IIFE from index.html and swap the `lines` array.

#### Terminal Script (the lines array)
```js
var lines = [
  // — The conversation —
  { text: '# how this page was built', cls: 'terminal__line--comment' },
  { text: '', cls: '' },
  { text: 'user: "what do you think about this new theme?"', cls: 'terminal__line--user' },
  { text: 'user: "maybe we just add this as its own landing page"', cls: 'terminal__line--user' },
  { text: 'user: "be sure it follows the site scroll dynamics"', cls: 'terminal__line--user' },
  { text: 'user: "research the web first on the message"', cls: 'terminal__line--user' },
  { text: 'user: "hash this conversation to the attestation"', cls: 'terminal__line--user' },
  { text: '', cls: '' },
  // — Intent chain hashes —
  { text: 'intent chain → rev 1  e614fc72', cls: 'terminal__line--hash' },
  { text: 'intent chain → rev 2  cc7b7523', cls: 'terminal__line--hash' },
  { text: 'intent chain → rev 3  c00afa94', cls: 'terminal__line--hash' },
  { text: '', cls: '' },
  // — Pipeline execution —
  { text: '> /kernel/execute-pipeline 105', cls: 'terminal__line--prompt' },
  { text: '', cls: '' },
  { text: '  researching market positioning...', cls: '' },
  { text: '  ✓ message validated — differentiated', cls: 'terminal__line--success' },
  { text: '  tasks decomposed: N', cls: '' },
  { text: '  executing via run-task.sh...', cls: '' },
  { text: '  ✓ N/N complete', cls: 'terminal__line--success' },
  { text: '  signing with sigstore...', cls: '' },
  { text: '  ✓ rekor #XXXXXXXXX', cls: 'terminal__line--success' },
  { text: '', cls: '' },
  { text: '  this page is the output.', cls: 'terminal__line--emphasis' },
];
```

**Notes on the script:**
- `N` values (task count, Rekor index) are filled in at build time by the pipeline task that writes this page — the task reads `sr_dev_workflow.json` for task count and the attestation bundle for the Rekor index
- `terminal__line--user`, `terminal__line--hash`, `terminal__line--comment` are new modifier classes — add them to `styles.css` with appropriate colors (user: muted white, hash: accent/green dim, comment: gray)
- The animation loops with `restartDelay` like the homepage terminal
- Section header above the terminal: "How this page was built" — plain, no jargon
- Below the terminal: one Rekor verification link — "Verify on Rekor ↗"

**Why this works:** A visitor scrolls down and watches the conversation that caused the page they're standing on play out in real time. The messages appear. The hashes appear. The pipeline runs. The page exists. That's the loop closing in front of them.

### Footer
- "This page was built by the same pipeline it describes." + Rekor link (added post-pipeline)
- Standard site footer copied verbatim from index.html

## Scroll Animation Requirements

Copy these three IIFE script blocks from `index.html` **verbatim** (do not reimplement):

### 1. Reveal Observer
```js
// Scroll Observer — copy from index.html lines 529-549
// IntersectionObserver at threshold: 0.15
// Adds 'revealed' class when element enters viewport
// Checks prefers-reduced-motion, skips if set
```
Apply `.reveal` class to: all `h2`, `p.anchor-section__subtitle`, `p.anchor-section__narrative`, `.evidence-card` elements.

### 2. Staggered Card Reveals
```js
// reveal-stagger container + --stagger-index CSS variable
// Already handled by styles.css — just use the classes correctly
```
Apply `.reveal-stagger` to `.evidence-grid` containers.
Apply `class="evidence-card reveal" style="--stagger-index:N"` to each card (N = 0, 1, 2...).

### 3. Parallax Section Numbers
```js
// Parallax Scroll — copy from index.html lines 552-578
// requestAnimationFrame scroll handler
// translateY on .parallax-number elements
// Checks prefers-reduced-motion, skips if set
```
Apply `.parallax-number reveal` to `<span>` section numbers inside `.parallax-section` sections.

## CSS
- `<link rel="stylesheet" href="styles.css">` — same stylesheet, no new CSS file, no inline `<style>` blocks
- Structural classes to use: `anchor-section`, `parallax-section`, `parallax-number`, `evidence-grid`, `evidence-card`, `reveal`, `reveal-stagger`
- Only inline style allowed: `--stagger-index` on evidence cards

## Nav & Header
- Copy `<header class="site-header">` + `<nav class="nav">` verbatim from index.html
- Mobile hamburger JS block copied verbatim from index.html
- Dynamic attestation counter (`feed-count.txt` fetch) copied verbatim from index.html

## Feed Embed Implementation
- `generate-feed.py` outputs server-rendered HTML for latest 10 entries
- Inject into `<!-- FEED_STATIC -->` marker (same as pipeline 101 / feed.html)
- `generate-feed.py` must be run as part of the build task so the embed is current at publish time

## Dependencies
- `styles.css` from isagawa-co.github.io (no changes to it)
- `generate-feed.py` for server-rendered feed entries
- `feed-count.txt` for nav counter
- Message research report must exist before writing copy sections
- Nav/footer HTML from index.html (copy verbatim)
