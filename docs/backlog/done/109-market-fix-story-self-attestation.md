# Fix: Wire story.html's Own Rekor Index Into Its Verify Links

## Status
Open

## Priority
High — story.html's entire thesis is "produced, not written, proven cryptographically" but its own verify links are dead (#) and the footer links point to April 26 runs that predate the page

## Summary
`story.html` was built by pipeline 105 (attestation bundle `105-20260529T182722Z.json`). However the bundle is unsigned (Sigstore signing was skipped — browser not present). The "How This Page Was Built" section has `href="#"` for its Rekor verify link, and the footer's three verify links are borrowed from index.html (April 26 runs). A skeptic clicking verify on the page making the strongest provenance claim finds a dead link. Fix requires: (1) sign the pipeline 105 bundle to get a real Rekor log index, then (2) update story.html with that index.

## Two-Step Fix

### Step 1: Sign the existing bundle
Run attestation signing manually (requires browser for OIDC):
```bash
python lib/attestation/attest.py "docs/backlog/done/105-market-build-portfolio-site-reframe.md" "tasks/completed/portfolio-solo-velocity/"
```
Sign in when browser opens. Note the Rekor log index from output.

### Step 2: Update story.html
- Find `href="#"` in the "How This Page Was Built" section → replace with real Rekor URL
- Update footer verify links to include the pipeline 105 Rekor entry
- Regenerate feed (so feed-data.json picks up the new signed attestation)
- `git add story.html feed-data.json feed-count.txt feed.html && git commit && git push`

## Acceptance Criteria
- [ ] `story.html` "Verify on Rekor ↗" link resolves to a real Rekor entry for pipeline 105
- [ ] Footer verify links include one entry for the pipeline that built this page (not just April 26 entries)
- [ ] No `href="#"` in story.html
- [ ] `grep -c 'href="#"' story.html` returns 0

## References
- Bundle: `.claude/state/attestations/105-20260529T182722Z.json` (unsigned, needs signing)
- `D:\my_ai_projects\isagawa-co.github.io\story.html`
- Pipeline 105 intent chain: 3 revisions, hashes e614fc72 → cc7b7523 → c00afa94

## Task Builder Input
- **Deliverable:** story.html with real Rekor verify link; feed regenerated; changes pushed
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Requires browser present for Sigstore OIDC signing (Step 1 is interactive); Step 2 is fully automatable once log index is known
