# Fix Portfolio Feed — Server-Side Rendering

## Status
Open

## Priority
High — the feed is the strongest proof asset on the portfolio; a non-JS fetcher (crawler, preview bot, AI model) currently sees "Loading..." instead of 73 attested pipeline runs

## Summary
The isagawa.co pipeline feed currently renders client-side via JavaScript. Any crawler, link preview bot, or AI model that fetches the page without executing JS sees a blank "Loading..." state instead of the feed entries. This makes the portfolio's most convincing proof asset invisible to every automated reader. The fix is to pre-render the feed entries into static HTML so that a plain HTTP fetch (no JS) returns the full list of runs in the raw response body.

## Requirements
- Move feed data from client-side JS rendering to server-side or static pre-rendered HTML
- Acceptance criterion is mechanically verifiable: `curl https://www.isagawa.co/[feed-page]` (no JS) returns all feed entries in the raw HTML response — not "Loading..."
- Rekor links and all entry metadata must be present in the static HTML
- NOTE: Playwright MCP (human-like browser with JS on) is NOT the right verification tool for this fix — it renders past "Loading..." instantly. Verification must use a no-JS fetch (curl or equivalent raw HTTP response check)
- After fix, the agent should verify by fetching raw HTML and asserting feed entries are present without JS execution

## References
- Live feed: https://www.isagawa.co (pipeline feed page)
- Prior feed work: `docs/backlog/done/075-market-build-portfolio-live-feed-update.md`
- Related: `099-market-fix-portfolio-feed-null-tasks.md`, `100-market-fix-portfolio-feed-duplicates.md`

## Task Builder Input
- **Deliverable:** Static/SSR feed page — all entries present in raw HTML without JS execution
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio`
- **Scope:** FIX
- **Constraints:** Verification MUST use a no-JS HTTP fetch (curl or raw response), not Playwright MCP browser navigation. Playwright MCP is appropriate for 099 and 100 but not this item — the bug is invisible to a human-like browser.
