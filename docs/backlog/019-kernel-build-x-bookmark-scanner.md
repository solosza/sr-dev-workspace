# Build X Bookmark Scanner — Competitive Intelligence Pipeline

## Status
Open

## Priority
High — recurring competitive intelligence that feeds positioning, backlog, and product decisions

## Summary
Automated pipeline that logs into the Isagawa X account, scans recent bookmarks, filters for AI/agent/LLM content, compares each post against Isagawa products (kernel, QA platform, spec factory, eval specs), identifies what's better/worse/borrowable, auto-generates backlog items for anything actionable, and sends a summary report via text message. Runs regularly since bookmarks are added daily.

## Requirements

### Browser Automation
- Use Playwright MCP to log into X (Isagawa account)
- Navigate to bookmarks
- Scan posts from the last N days (configurable, default 3)
- Filter for AI/agent/LLM/evaluation content relevant to Isagawa
- Skip posts already processed (track processed post IDs in a state file)

### Competitive Analysis Per Post
- Capture post content (text, images if relevant, links)
- Identify what product/tool/framework is being discussed
- Compare against applicable Isagawa products:
  - Kernel (self-improving agent infrastructure)
  - QA Platform / DeepEval spec (LLM evaluation)
  - Spec factory / meta-spec (domain spec generation)
  - Run-task scripts (headless execution)
- Assessment: what's better about theirs, what's better about ours, what can we borrow
- If borrowable: auto-generate a backlog item via `/kernel/backlog` format

### Notification
- Send summary report via text message (SMS) to user's mobile number
- Research MCP options: Twilio MCP, Google Voice, or SMS API
- Fallback: Gmail MCP for email notification if SMS not available
- Report format: concise, scannable — post title, link, assessment, action items

### State Tracking
- Track processed bookmark IDs in `.claude/state/x_bookmarks_processed.json`
- Skip already-processed posts on subsequent runs
- Track scan date for "last N days" filtering

### Recurrence
- Designed to run regularly (daily or on-demand)
- Can be triggered via `/kernel/task-builder` or headless `run-task-batch.sh`
- State file persists between runs

## Key Questions
- What Playwright MCP commands are needed for X login + bookmark navigation?
- Is there a Twilio MCP or SMS MCP available for Claude Code?
- If not, is there a Gmail MCP that can send emails?
- X rate limits / anti-bot detection — how to handle gracefully?
- Credentials storage — where to put X login securely? Environment variables?

## References
- Playwright MCP already configured in this workspace
- Isagawa X account (bookmarks are AI/agent content only)
- Backlog 003: agent-first positioning (feeds from this analysis)
- Existing competitive analysis: ClawHub scan from 2026-03-22

## Task Builder Input
- **Deliverable:** Working bookmark scanner skill/command, state tracking, SMS/email notification, first scan report
- **Scope:** BUILD
- **Constraints:** Needs Playwright MCP for browser automation. Needs SMS or email MCP for notifications (research required). X credentials via environment variables. Recurring — must be idempotent with state tracking. HUMAN REQUIRED for X credentials setup and SMS service selection.
