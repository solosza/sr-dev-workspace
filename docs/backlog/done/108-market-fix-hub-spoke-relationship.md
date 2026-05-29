# Fix: Make Hub-Spoke Relationship Visible on Product Pages

## Status
Open

## Priority
High — a cold visitor on any product page has no felt sense they're looking at one output of a factory that built five of these; the relationship is the whole flex

## Summary
Every product page (vibe-coder, attestation, qa-platforms, ssh-compliance, story) has a one-line "produced by the same system" whisper at the top. A visitor landing cold (shared link, search, etc.) reads a standalone page with no sense of the factory behind it. The fix is a persistent, visible element on every product page that signals "1 of N things this factory built" — a breadcrumb strip, a factory badge, or a "← Back to the factory" banner — making the hub-spoke architecture felt, not just asserted.

## Requirements
- Every product page shows: a visible back-link or badge that reads something like "← Built by the factory" or "1 of 6 · isagawa.co" linking back to index.html
- The element must be above the fold, prominent enough to read without scrolling
- Consistent across all product pages (same component, same position)
- Does not compete with each page's own hero/CTA — it anchors the page in the factory without overriding its product message
- story.html should also show this (it's a product of the system too)
- The "N" in "1 of N" should be a static number for now (not dynamically counted)

## Design Options to Evaluate
- Thin top banner strip: "← isagawa.co — built by the same system" (low height, full width)
- Breadcrumb: `isagawa.co / vibe-coder` in small type above the hero
- Factory badge: a small pill/badge near the logo: "FACTORY OUTPUT"
- Hero subtitle prefix: "One of 6 things this factory built." before the page's own subtitle

## References
- Backlog 107 (nav unification) — coordinate so the hub indicator doesn't conflict with nav
- `D:\my_ai_projects\isagawa-co.github.io\styles.css`
- AJ feedback: "I can't tell what this page is for" — this element answers that
- Analysis: "the single most powerful thing about your site is invisible unless you start on the home page"

## Task Builder Input
- **Deliverable:** Thin factory-origin strip/breadcrumb added to all 5 product pages; CSS added to styles.css; all product pages updated
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Additive only — no changes to existing hero/section content; vanilla CSS; consistent with monochrome aesthetic; can run parallel to 107
