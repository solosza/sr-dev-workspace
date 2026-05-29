# Fix Portfolio Feed — Duplicate Entry Grouping

## Status
Open

## Priority
Medium — duplicates are not bugs (they're real reruns and forensic history), but ungrouped they read as noise to a first-time viewer

## Summary
The portfolio feed contains repeated intent entries for the same job run at short intervals — e.g., "Build 53Man Rosters" logged three times within 15 minutes, and multiple identical "Research Ssh Compliance Spec Decomposition" runs. These are authentic reruns and should NOT be deleted; the messiness is part of what makes the feed credible as evidence of real autonomous output. The fix is presentation: collapse repeated intents into a grouped entry ("3 runs") that is expandable, so the forensic trail stays intact but the feed reads cleanly at a glance.

## Requirements
- Use Playwright MCP to identify all duplicate intent groups in the live feed (same intent text, multiple entries)
- Update the feed renderer to group consecutive or same-intent entries, showing a "N runs" count with expand/collapse
- All Rekor verification links from every individual entry must survive and remain accessible in the expanded view
- No entries are deleted — deletion would undermine the authenticity of the feed as a forensic trail
- Verify: Playwright MCP scrapes the updated feed, confirms duplicates are visually grouped, all Rekor links resolve

## References
- Live feed: https://www.isagawa.co (pipeline feed page)
- Prior feed work: `docs/backlog/done/075-market-build-portfolio-live-feed-update.md`
- Related: `099-market-fix-portfolio-feed-null-tasks.md`

## Task Builder Input
- **Deliverable:** Updated feed renderer with duplicate grouping UI; all Rekor links preserved
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio`
- **Scope:** FIX
- **Constraints:** Deletion is explicitly prohibited — any approach that removes entries is a violation of the acceptance criteria. Playwright MCP available for detection and verification.
