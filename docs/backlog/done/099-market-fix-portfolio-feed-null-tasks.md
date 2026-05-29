# Fix Portfolio Feed — Null Tasks Field

## Status
Open

## Priority
High — the live feed is the strongest sales asset on the portfolio; null values undercut credibility with sharp buyers

## Summary
May 27 entries in the isagawa.co pipeline feed display "null tasks" instead of an integer task count. The root cause is ambiguous — either the newer runs aren't writing the task count into the attestation bundle, or the renderer is reading the wrong field for the newer bundle schema. Diagnosing which layer is broken must happen before any patch is applied; fixing the renderer without checking the bundle would paper over a data-integrity problem and produce a false green run.

## Requirements
- Use Playwright MCP to scrape the live feed and identify every entry rendering "null tasks" (by intent name and timestamp)
- Read the source attestation bundle JSON for one or more of the null entries to determine root cause: is the task count missing from the bundle, or is the renderer reading the wrong field?
- Apply the fix at the correct layer (bundle writer or renderer, not a display fallback that hides the gap)
- Verify: after fix, every entry shows an integer task count or an explicit "—" with a documented reason — no entry renders the string "null"

## References
- Live feed: https://www.isagawa.co (pipeline feed page)
- Prior feed work: `docs/backlog/done/075-market-build-portfolio-live-feed-update.md`

## Task Builder Input
- **Deliverable:** Patched feed — no null task counts visible, root cause identified and fixed at source
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio`
- **Scope:** FIX
- **Constraints:** Diagnose-before-patch ordering is mandatory — task-builder must gate the patch task on the diagnosis task. Playwright MCP is available for browser-based detection and verification.
