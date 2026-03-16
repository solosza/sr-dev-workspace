# Build gws CLI Integration Reference

## Context
Reference code and documentation for Google Workspace CLI integration — Gmail send/search/draft, Calendar create, OAuth setup. This is the communication layer the pipeline uses. All output goes into the creative-finance-spec repo.

## Dependencies
- **004** — integration research (gws CLI syntax, OAuth requirements, alternatives)
- **006** — schemas (gmail_patterns.md as reference)

## Requirements

Read these files before building:
- `creative-finance-spec/research/004-integration-surface.md`
- `creative-finance-spec/pipeline/interfaces/gmail_patterns.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\integration\`

### gws_patterns.py
Reference Python module showing how the pipeline interacts with Gmail and Calendar:
- `search_prior_contact(email: str) -> list[dict]` — search Gmail for prior threads with this person
- `send_email(to: str, subject: str, body: str, thread_id: str = None) -> dict` — send email (new or reply)
- `create_draft(to: str, subject: str, body: str) -> dict` — create draft for HITL review
- `create_calendar_event(title: str, datetime: str, attendees: list[str], notes: str) -> dict` — schedule call
- Each function: uses `subprocess.run` to call `gws` CLI (or alternative from 004 research)
- Include error handling: auth failures, rate limits, network errors
- Include logging: what was sent, to whom, result

### oauth_setup.md
Step-by-step guide for setting up Google OAuth for the pipeline:
- Create Google Cloud project
- Enable Gmail API and Calendar API
- Create OAuth credentials (desktop app type)
- Required scopes: `gmail.send`, `gmail.readonly`, `gmail.compose`, `calendar.events`
- First-time auth flow: how the investor authorizes the app
- Token storage and refresh
- Troubleshooting: common errors and fixes

### gws_integration_README.md
- What these files are (reference implementation)
- Prerequisites: Google Cloud project, OAuth credentials, gws CLI installed (or alternative)
- If gws CLI is pre-v1.0 or not production-ready (from 004 research): document the recommended alternative (direct Gmail API, community MCP server, etc.)
- How to test: example commands to verify Gmail and Calendar access work
- Session management: how session-id maps to email threads (search by session-id in subject or custom header)

## Output
- `creative-finance-spec/pipeline/integration/gws_patterns.py`
- `creative-finance-spec/pipeline/integration/oauth_setup.md`
- `creative-finance-spec/pipeline/integration/gws_integration_README.md`

## Validation (check ALL before completing)
- [ ] All 3 files exist at their output paths
- [ ] gws_patterns.py is valid Python (syntax check)
- [ ] gws_patterns.py has all 4 functions: search, send, draft, calendar
- [ ] Each function has error handling and logging
- [ ] oauth_setup.md has numbered steps from GCP project creation through first auth
- [ ] oauth_setup.md lists required scopes
- [ ] oauth_setup.md has troubleshooting section
- [ ] gws_integration_README.md addresses gws CLI maturity status honestly (from 004 research)
- [ ] If gws CLI isn't ready: alternative approach documented

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
