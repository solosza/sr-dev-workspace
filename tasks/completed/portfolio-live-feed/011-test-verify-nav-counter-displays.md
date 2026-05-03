# 011 — Verify Nav Counter Displays (L2)

**Type:** TEST
**Depends on:** 009

## Requirements
Open `D:\my_ai_projects\isagawa-co.github.io\index.html` in the Playwright browser and verify:

1. Nav bar shows the attestation counter (number + ✓)
2. Counter number matches `feed-count.txt`
3. Counter links to `feed.html`
4. "Feed" nav link is visible
5. Self-Extension section shows updated stats (30+, 74+)
6. Capability list contains clickable links

Use Playwright MCP `browser_navigate` to `file:///D:/my_ai_projects/isagawa-co.github.io/index.html` and take a screenshot of the nav area.

## Acceptance Criteria
- [ ] Nav counter element visible with a number
- [ ] Updated stats visible in Self-Extension section
- [ ] Screenshot captured showing updated nav + Self-Extension
