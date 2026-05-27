# X Bookmark Scanner

Scan X bookmarks via Playwright MCP. HITL for login. Agent scrapes, analyzes, presents candidates, creates backlogs, and un-bookmarks processed posts.

## Usage

```
/kernel/scan-bookmarks
```

No arguments. The command drives the full pipeline interactively.

## Steps

### Step 1: Open X Login

Navigate to X login page via Playwright MCP.

```
1. Use mcp__playwright__browser_navigate to go to https://x.com/i/flow/login
2. Use mcp__playwright__browser_snapshot to confirm the login page loaded
3. Tell the user: "Browser is open at X login. Please log in manually. Say 'done' when you're logged in."
```

**HITL checkpoint:** Wait for user to confirm login. Do NOT proceed until user says they are logged in.

### Step 2: Navigate to Bookmarks

```
1. Use mcp__playwright__browser_navigate to go to https://x.com/i/bookmarks
2. Wait 3 seconds for content to load (mcp__playwright__browser_wait_for)
3. Use mcp__playwright__browser_snapshot to capture the bookmarks page
```

If the page shows "Log in" or doesn't show bookmarks, tell the user login may have failed and retry Step 1.

### Step 3: Scrape Bookmarks

Scroll and collect bookmark content:

```
1. Take a snapshot of current bookmarks visible
2. For each visible bookmark, extract:
   - Author name and handle
   - Post text (full content)
   - Any links/URLs in the post
   - Post URL (for un-bookmarking later)
3. Scroll down to load more bookmarks:
   - Use mcp__playwright__browser_press_key with "End" key
   - Wait 2 seconds for lazy-load
   - Take another snapshot
   - Repeat until no new bookmarks appear (or 5 scroll cycles max)
4. Deduplicate by post content
```

Build a list of all scraped bookmarks with their content.

### Step 4: Analyze and Rank

For each bookmark, the agent (you) analyzes using full reasoning — not keyword matching:

**Categories to assess:**
- **Business opportunity** — monetizable idea, market gap, revenue model (like govcon, SaaS, contracting)
- **AI/agent technology** — new techniques, frameworks, patterns relevant to Isagawa Kernel
- **Competitive intelligence** — what competitors are building, shipping, or announcing
- **Skill/knowledge** — tutorials, deep dives, reference material worth saving
- **Not actionable** — entertainment, memes, personal posts, stale news

**For each bookmark, produce:**
- Category (from above)
- One-line summary
- Backlog potential: YES (should become a backlog item) or NO (interesting but no action needed)
- If YES: suggested backlog title and scope (RESEARCH or BUILD)

### Step 5: Present Results to User

Show the full ranked list in a table:

```
BOOKMARK SCAN RESULTS — [date]

Bookmarks scanned: [N]

## Backlog Candidates

| # | Author | Summary | Category | Suggested Backlog |
|---|--------|---------|----------|-------------------|
| 1 | @handle | one-line summary | business opportunity | "Research [topic]" |
| 2 | @handle | one-line summary | AI/agent tech | "Build [thing]" |
| ... | | | | |

## Not Actionable (will be un-bookmarked)

| # | Author | Summary | Reason |
|---|--------|---------|--------|
| 1 | @handle | one-line summary | entertainment |
| ... | | | |

Which backlog candidates should I create? (e.g., "1, 3, 5" or "all" or "none")
```

**HITL checkpoint:** Wait for user to select which candidates to create backlogs for.

### Step 6: Create Backlogs

For each selected candidate, invoke `/kernel/backlog` with the bookmark content as context.

Pass the full post text + any links as the argument so the backlog command has full context.

### Step 7: Un-bookmark Processed Posts

After backlogs are created (or user says "none"), un-bookmark ALL scanned posts (both backlog candidates and not-actionable):

```
For each bookmark:
1. Use mcp__playwright__browser_navigate to go to the post URL
2. Use mcp__playwright__browser_snapshot to find the bookmark icon
3. Use mcp__playwright__browser_click on the bookmark icon to un-bookmark
4. Confirm the bookmark was removed (icon state change)
```

This prevents duplicate processing in future scans.

**If un-bookmarking fails for any post, report it but continue with the rest.**

### Step 8: Report

```
BOOKMARK SCAN COMPLETE

Scanned: [N] bookmarks
Backlogs created: [M]
Un-bookmarked: [K]
Failed to un-bookmark: [F] (if any)

Created backlogs:
- [NNN] — [title]
- [NNN] — [title]

Ready for /kernel/execute-pipeline on any of these.
```

## Rules

- **No credentials stored** — user logs in manually via HITL
- **No Python scanner modules** — agent does analysis directly with full reasoning
- **Un-bookmark everything** — processed posts are removed to prevent re-scanning
- **HITL at Step 1 (login) and Step 5 (selection)** — everything else is autonomous
- **Backlog creation uses /kernel/backlog** — follows the standard command, not direct file writes
