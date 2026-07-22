# Task 003: Responsive + Print + OG
**Type:** TEST | **Gates:** RS-03
## Action
ONE script: verify OG metadata (og:title/description/type) + browser title present in the live HTML; check the page has responsive signals (viewport meta, max-width body, media queries) and a print consideration; if Playwright MCP is available, load at mobile (375px) and desktop (1280px) widths and confirm no horizontal overflow of the body. Otherwise assert the CSS responsive markers structurally.
## Acceptance
OG valid + responsive markers present (+ Playwright viewport check if available). Exit 0. Red: fix then /kernel/learn.
