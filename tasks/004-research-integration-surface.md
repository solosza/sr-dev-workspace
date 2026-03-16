# Research Integration Surface

## Context
The system runs on Claude Code headless + Google Workspace CLI + a thin webhook server. This task maps out the actual capabilities, exact syntax, and constraints of each component. The agent must verify claims against official docs — no assumptions.

## Dependencies
None — independent of domain research. Can run parallel with 001-003.

## Requirements
- Use **WebSearch** to research each component against official documentation
- **Google Workspace CLI** (`gws`):
  - Verify it exists: search `github.com/googleworkspace/cli`
  - Document exact command syntax for: `gws gmail send`, `gws gmail search`, `gws gmail draft`, `gws calendar create`
  - Document auth requirements: GCP project setup, OAuth credentials, scopes needed
  - Document limitations: rate limits, supported Gmail operations, what's NOT supported
  - Document maturity: version, stability, breaking change warnings
  - If gws CLI is not production-ready, document alternatives (Gmail API direct, community MCP servers)
- **Claude Code headless mode**:
  - Search Anthropic docs for Claude Code CLI flags
  - Document exact behavior: `-p` (prompt), `--allowedTools`, `--output-format json`, `--max-turns`
  - Document `--session-id` for lead continuity: how sessions persist, resume behavior
  - Document `--resume` flag: when and how to use it
  - Document authentication: Max subscription vs API key, how Claude Code decides which to use
  - Document cost model: token usage per typical interaction, Max subscription shared pool limits
- **Webhook receiver patterns**:
  - Document minimal Python (FastAPI/Flask) webhook server: receive POST, parse JSON, fire subprocess
  - Document payload formats from: Typeform webhooks, Zapier webhooks, REsimpli webhooks (if documented), generic JSON
  - Document error handling: retries, timeouts, logging
- **Full invocation chain**:
  - Document end-to-end: webhook POST → server parses → `subprocess.run(["claude", "-p", ...])` → Claude calls gws → result returned
  - Document session management: how `--session-id` enables multi-touch lead journeys across separate webhook fires

## Output
- File: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\004-integration-surface.md`

## Validation (check ALL before completing)
- [ ] File exists at the output path
- [ ] gws CLI commands documented with exact syntax (or alternatives documented if gws isn't ready)
- [ ] OAuth/GCP setup steps documented
- [ ] Claude Code headless flags documented with behavior notes for each flag
- [ ] Session management (`--session-id`) pattern documented with example
- [ ] Authentication model documented (Max subscription vs API key)
- [ ] Cost model documented with estimated tokens per lead interaction
- [ ] Webhook receiver pattern documented with code structure (not full code — structure only)
- [ ] At least 2 webhook payload formats documented
- [ ] Full invocation chain documented end-to-end
- [ ] All claims verified against official docs (no assumptions — cite URLs)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
