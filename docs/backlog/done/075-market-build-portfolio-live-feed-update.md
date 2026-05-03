# Update Portfolio Site — Live Attestation Feed + Stats Refresh

## Status
Open

## Priority
High — this is the foundation update. Showcase pages 071-074 link from here. Must ship first.

## Summary
Update the live isagawa.co portfolio site with three additions: (1) a nav bar attestation counter that links to a live feed page, (2) a feed/provenance page showing every attested pipeline run as a timeline, and (3) refreshed stats in the Self-Extension section with clickable capability links. This makes the site current and creates the structure that showcase pages 071-074 will link into.

## Requirements

### 1. Nav Bar Attestation Counter
- Add a counter to the nav: e.g. "73 ✓" or "73 attested" — the current count of signed pipeline runs
- Links to the feed page (`/feed` or expanded provenance section)
- Built from the attestation directory at build time — count the attestation bundle JSON files
- Number goes up every time a pipeline runs and produces a new bundle
- Styling: subtle, fits the existing nav aesthetic, doesn't compete with section links

### 2. Live Attestation Feed Page
- New page or expanded section showing every attested pipeline run as a timeline
- Each entry shows:
  - Backlog title (human-readable, extracted from `metadata.pipeline_backlog`)
  - Timestamp (from `predicate.timestamp.start`)
  - Task count + completed count (from `metadata`)
  - Intent revision count (length of `invocation.intent_chain`)
  - Category tag derived from backlog name (kernel / market / domain / test)
  - "Verify on Rekor ↗" link (from `predicate.rekor.entryUrl`)
- Newest at top, scrolls vertically
- Color-coded by category — kernel in one color, market in another, domain in a third
- Header text: "Every entry below was produced from a sentence of natural language, executed under kernel governance, and signed with Sigstore."
- Footer text: "This feed updates automatically. Come back tomorrow and there will be more."
- Static HTML generated at build time from attestation bundle JSON files — no database, no API

### 3. Self-Extension Section Stats Refresh
- Update "27+ Domain Specs" → current count (30+)
- Update "55+" backlog count → current (74+)
- Update "849 tasks" → current count
- Update "70+ pipelines" → current count
- Make the capability list clickable — each product name links to its showcase page (placeholder `#` links for pages not yet built)
- Add any new capabilities not currently listed

### Design Constraints
- Match existing isagawa.co visual language (dark theme, terminal aesthetic)
- Mobile responsive
- Static (GitHub Pages compatible)
- Feed page must work without JavaScript (entries rendered in HTML at build time), with optional JS enhancement for filtering/search
- **Feature branch:** all work on `feature/live-feed-update` branch in `isagawa-co.github.io` repo. Do not merge to main until user approves.

### Data Source
- Attestation bundles live in `D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\state\attestations\` and also within individual task repos
- The build step should scan all available attestation bundles, parse the JSON, and generate the feed HTML
- A simple Python or Node script that reads bundles → produces feed HTML is sufficient
- The script output (generated HTML) gets committed to the repo, not the script's runtime

## References
- Portfolio site (live): `D:\my_ai_projects\isagawa-co.github.io` (deploys to www.isagawa.co)
- Current index.html: already has Provenance section with 3 attestation cards — extend, don't replace
- Attestation bundles: `.claude/state/attestations/` in this workspace + individual repos
- Agent attestation spec: `D:\my_ai_projects\agent-attestation-spec`
- Backlog 071-074: showcase pages that will link from the updated Self-Extension section
- Previous conversation on feed concept: nav counter + live feed + "the number goes up every visit"

## Task Builder Input
- **Deliverable:** Updated isagawa.co with nav attestation counter linking to live feed page, feed page with timeline of all attested pipeline runs, refreshed Self-Extension stats with clickable capability links. On feature branch `feature/live-feed-update`.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Feature branch only — do not merge to main. Must match existing dark theme terminal aesthetic. Static HTML/CSS (GitHub Pages). Feed page generated at build time from attestation bundle JSON files. Existing Provenance section preserved — feed page extends it. Showcase page links can be placeholders (#) until 071-074 ship.
