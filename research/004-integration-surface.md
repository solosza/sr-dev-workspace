# Integration Surface — Lease Option Wholesaling Pipeline

## Google Workspace CLI (`gws`)

### Overview

The Google Workspace CLI is an official Google-published tool (`github.com/googleworkspace/cli`) that provides a single command-line interface for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. It dynamically builds its command surface from Google's Discovery Service — when Google adds an API endpoint, `gws` picks it up automatically.

**Status:** Pre-v1.0. Under active development. **Expect breaking changes.**

> "This is not an officially supported Google product."

Source: [googleworkspace/cli README](https://github.com/googleworkspace/cli/blob/main/README.md)

### Installation

```bash
npm install -g @googleworkspace/cli
```

**Prerequisites:**
- Node.js 18+
- Google Cloud project (create via Cloud Console or `gws auth setup`)
- Google account with Workspace access
- gcloud CLI (optional but recommended for automated setup)

Alternative install methods: GitHub releases (pre-built binaries), Cargo (`cargo install --git https://github.com/googleworkspace/cli --locked`), Nix flake.

### Gmail Command Syntax

The general pattern:

```bash
gws gmail <resource> <method> [flags]
```

**Shortcut commands (recommended for pipeline use):**

| Shortcut | Full Command | Purpose |
|----------|-------------|---------|
| `gws +send` | `gws gmail users.messages send` | Send an email |
| `gws +triage` | `gws gmail users.messages list` (filtered) | Show unread inbox summary |
| `gws +watch` | `gws gmail users watch` | Watch for new emails (NDJSON stream) |

**Discovering exact parameters:**

```bash
gws schema gmail.users.messages.send    # Shows required/optional params for send
gws schema gmail.users.messages.list    # Shows params for search/list
gws schema gmail.users.drafts.create    # Shows params for draft creation
```

**General pattern for all commands:**

```bash
# Send email (using generic API pattern)
gws gmail users.messages send --json '{"raw": "<base64-encoded-RFC2822>"}'

# Search/list emails
gws gmail users.messages list --params '{"q": "from:seller@example.com subject:lease option"}'

# Create draft
gws gmail users.drafts create --json '{"message": {"raw": "<base64-encoded-RFC2822>"}}'

# Dry run (preview without sending)
gws gmail users.messages send --json '...' --dry-run
```

**Note:** The `gws` CLI uses Google API primitives directly. Email bodies must be RFC 2822-formatted and base64-encoded, which is the same format as the Gmail API. The `+send` shortcut may simplify this — check `gws +send --help` for current syntax.

Source: [gws-gmail SKILL.md](https://github.com/googleworkspace/cli/blob/main/skills/gws-gmail/SKILL.md)

### Calendar Command Syntax

```bash
# Create calendar event
gws calendar events insert --params '{"calendarId": "primary"}' --json '{
  "summary": "Lease Option Consultation — [Buyer Name]",
  "start": {"dateTime": "2026-03-10T14:00:00-07:00"},
  "end": {"dateTime": "2026-03-10T14:30:00-07:00"},
  "attendees": [{"email": "buyer@example.com"}]
}'

# List upcoming events
gws calendar events list --params '{"calendarId": "primary", "timeMin": "2026-03-05T00:00:00Z"}'
```

### OAuth / GCP Setup

**Step 1: Create GCP project**

```bash
gws auth setup     # Interactive — creates project + OAuth consent screen
```

Or manually:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project (e.g., "lease-option-pipeline")
3. Enable Gmail API + Calendar API
4. Create OAuth 2.0 credentials (Desktop app type)
5. Download `client_secret.json`

**Step 2: Configure credentials**

```bash
# Option A: Interactive login
gws auth login

# Option B: Manual credential file
# Place at: ~/.config/gws/client_secret.json

# Option C: Service account (for automation)
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/service-account.json

# Option D: Pre-obtained token
export GOOGLE_WORKSPACE_CLI_TOKEN="ya29...."
```

**Required OAuth scopes (minimum for pipeline):**

| Scope | Purpose |
|-------|---------|
| `gmail.send` | Send emails |
| `gmail.compose` | Create drafts |
| `gmail.readonly` | Search/read incoming replies |
| `calendar.events` | Create consultation appointments |

**Critical:** Add yourself as a test user in the OAuth consent screen, or access will be blocked. Unverified (testing mode) apps are limited to ~25 scopes.

### Limitations and Risks

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| **Pre-v1.0** — breaking changes expected | Commands may change without notice | Pin to specific version, test after updates |
| **Unverified app scope limit (~25)** | Can't use "recommended" preset (85+ scopes) | Use minimal scopes — only gmail.send, gmail.readonly, calendar.events |
| **RFC 2822 email encoding** | Email body construction is complex | Build a helper function to encode emails |
| **No official support** | No SLA, no guaranteed bug fixes | Have Gmail API direct fallback ready |
| **Rate limits** | Gmail API: 250 messages/day for consumer accounts, higher for Workspace | Batch outreach, respect daily limits |

### Alternatives (If gws Isn't Ready)

| Alternative | Pros | Cons |
|-------------|------|------|
| **Gmail API direct** (Python `google-api-python-client`) | Stable, well-documented, production-proven | More code, manual OAuth flow |
| **Community MCP servers** (e.g., `@anthropic/gmail-mcp`) | Native Claude Code integration | Depends on community maintenance |
| **Nodemailer + SMTP** | Simple, no API needed | No read/search capability, less control |
| **SendGrid / Mailgun** | Production-grade email delivery | Separate service, not Google-native |

**Recommendation:** Use `gws` for MVP (fastest path to working). Have Gmail API direct as fallback if `gws` breaks before v1.0.

Source: [googleworkspace/cli](https://github.com/googleworkspace/cli), [gws-gmail SKILL.md](https://github.com/googleworkspace/cli/blob/main/skills/gws-gmail/SKILL.md)

---

## Claude Code Headless Mode (Agent SDK CLI)

### Overview

Claude Code's `-p` flag (formerly "headless mode") runs Claude non-interactively from the command line. This is how the pipeline invokes Claude to process leads — each webhook fire triggers a `claude -p` call with the lead data.

Source: [Claude Code Docs — Run programmatically](https://code.claude.com/docs/en/headless)

### CLI Flags

| Flag | Syntax | Behavior |
|------|--------|----------|
| **`-p` / `--print`** | `claude -p "prompt"` | Non-interactive mode. Prints result and exits. |
| **`--allowedTools`** | `--allowedTools "Bash,Read,Edit"` | Auto-approve specified tools without prompting. Uses prefix matching with trailing space + `*`. |
| **`--output-format`** | `--output-format json` | Output format: `text` (default), `json` (structured with session ID), `stream-json` (real-time NDJSON). |
| **`--json-schema`** | `--json-schema '{"type":"object",...}'` | Force output to conform to a JSON Schema. Result in `structured_output` field. |
| **`--continue`** | `--continue` | Continue the most recent conversation. |
| **`--resume`** | `--resume "session-id"` | Resume a specific conversation by session ID. |
| **`--append-system-prompt`** | `--append-system-prompt "..."` | Add instructions while keeping Claude Code's default behavior. |
| **`--system-prompt`** | `--system-prompt "..."` | Fully replace the default system prompt. |
| **`--max-turns`** | `--max-turns 10` | Limit the number of agentic turns (tool use cycles). |
| **`--model`** | `--model claude-sonnet-4-5-20250929` | Specify which model to use. |
| **`--verbose`** | `--verbose` | Show detailed output including tool calls. |
| **`--include-partial-messages`** | `--include-partial-messages` | With `stream-json`, receive tokens as generated. |

### Session Management Pattern

Sessions enable multi-touch lead journeys across separate webhook fires. Each lead gets a persistent session ID that carries context across interactions.

**First touch (new lead):**

```bash
# Process new lead — capture session ID from output
result=$(claude -p "New seller lead: [lead data]. Qualify and draft first-touch email." \
  --allowedTools "Bash(gws *),Read,Grep" \
  --output-format json)

# Extract session ID for future interactions
session_id=$(echo "$result" | jq -r '.session_id')
# Store session_id in lead record: lead.claude_session_id = session_id
```

**Follow-up touch (existing lead):**

```bash
# Resume the lead's conversation — Claude has full prior context
claude -p "Seller replied: '[reply text]'. Draft follow-up response." \
  --resume "$session_id" \
  --allowedTools "Bash(gws *),Read,Grep" \
  --output-format json
```

**How sessions persist:**
- Sessions are stored locally on disk by Claude Code
- `--resume` loads the full conversation history from a previous session
- Claude sees all prior context (lead data, previous drafts, decisions made)
- This means Day 3 follow-up knows what Day 1 first touch said

### Authentication Model

| Method | How It Works | Use Case |
|--------|-------------|----------|
| **API Key** | Set `ANTHROPIC_API_KEY` env var. Pay-per-token. | **Required for headless/programmatic mode.** Agent SDK only supports API keys. |
| **Max Subscription** ($100-$200/mo) | OAuth tokens via Claude Code CLI. Shared pool. | Interactive CLI use only. NOT supported for Agent SDK / headless. |
| **Pro Subscription** ($20/mo) | Same OAuth, lower limits. | Interactive use, low volume. |

**Critical constraint:** The Agent SDK (which powers `-p` mode) **only supports API Keys** — Max subscription billing is NOT supported for programmatic use. The pipeline must use an API key.

Source: [Claude Code — Manage costs](https://code.claude.com/docs/en/costs), [ShareUHack — Claude Code Cost Comparison](https://www.shareuhack.com/en/posts/openclaw-claude-code-oauth-cost)

### Cost Model

**Average usage data (from Anthropic):**
- Average: **$6 per developer per day**
- 90th percentile: **< $12/day**
- Monthly estimate: **~$100-200/month** with Sonnet

**Per-lead cost estimate for pipeline:**

| Operation | Estimated Tokens | Estimated Cost |
|-----------|-----------------|----------------|
| Lead qualification (read lead + apply criteria) | ~2,000-4,000 input + ~1,000 output | ~$0.02-$0.04 |
| Email draft (qualify + write email) | ~3,000-5,000 input + ~2,000 output | ~$0.04-$0.08 |
| Follow-up (resume session + new context) | ~5,000-8,000 input + ~1,000 output | ~$0.05-$0.10 |
| Buyer matching (load deal + score buyers) | ~4,000-6,000 input + ~2,000 output | ~$0.05-$0.10 |
| **Full lead journey (5-7 touches)** | ~30,000-50,000 total | **~$0.30-$0.60** |

**Cost optimization levers:**
- **Prompt caching:** Cache reads cost 0.1x base input price (90% savings on repeated context)
- **Batch API:** 50% discount on input and output tokens
- **Model selection:** Use Sonnet for routine operations, reserve Opus for complex decisions
- **`--max-turns`:** Limit agentic loops to prevent runaway costs

**Rate limit recommendations (per user):**

| Team Size | TPM per User | RPM per User |
|-----------|-------------|-------------|
| 1-5 users | 200K-300K | 5-7 |
| 5-20 users | 100K-150K | 2.5-3.5 |
| Solo pipeline | 200K-300K | 5-7 |

Source: [Claude Code — Manage costs](https://code.claude.com/docs/en/costs), [Anthropic API Pricing](https://platform.claude.com/docs/en/about-claude/pricing)

---

## Webhook Receiver Patterns

### Architecture

A thin Python server (FastAPI or Flask) that:
1. Receives POST webhooks from lead sources
2. Parses the JSON payload
3. Fires `subprocess.run(["claude", "-p", ...])` with the lead data
4. Returns 200 immediately (processing happens async)

### Server Structure (FastAPI)

```
webhook_receiver/
├── server.py              # FastAPI app with webhook endpoint
├── parsers/
│   ├── typeform.py        # Parse Typeform payload → standard lead format
│   ├── zapier.py          # Parse Zapier payload → standard lead format
│   └── generic.py         # Parse generic JSON → standard lead format
├── processor.py           # Fire claude -p subprocess
├── config.py              # Environment vars, lead source config
└── requirements.txt       # fastapi, uvicorn, pydantic
```

**Core endpoint pattern:**

```python
# server.py (structure only — not production code)
@app.post("/webhook/{source}")
async def receive_webhook(source: str, payload: dict, background_tasks: BackgroundTasks):
    # 1. Parse payload based on source
    lead = parse_lead(source, payload)  # → standardized LeadData

    # 2. Validate minimum fields
    if not lead.is_valid():
        return {"status": "rejected", "reason": lead.validation_errors}

    # 3. Queue processing (don't block the webhook response)
    background_tasks.add_task(process_lead, lead)

    # 4. Return 200 immediately
    return {"status": "accepted", "lead_id": lead.id}
```

**Processing pattern:**

```python
# processor.py (structure only)
def process_lead(lead: LeadData):
    prompt = build_prompt(lead)  # Format lead data into Claude prompt

    result = subprocess.run(
        ["claude", "-p", prompt,
         "--allowedTools", "Bash(gws *),Read,Grep",
         "--output-format", "json"],
        capture_output=True, text=True, timeout=120
    )

    response = json.loads(result.stdout)
    session_id = response.get("session_id")

    # Store session_id for follow-up touches
    save_session(lead.id, session_id)
```

### Error Handling

| Scenario | Handling |
|----------|----------|
| **Webhook timeout** (source expects response < 15s) | Return 200 immediately, process in background |
| **Claude subprocess fails** (non-zero exit) | Log error, retry once after 60s, alert investor after 2nd failure |
| **Invalid payload** (missing required fields) | Return 400 with validation errors, log for debugging |
| **Rate limit hit** (too many claude calls) | Queue leads, process sequentially with 5s delay between calls |
| **Duplicate webhook** (same lead, same source) | Deduplicate by `event_id` or `lead.email + lead.phone` hash |

### Webhook Payload Formats

#### Typeform Webhook

Typeform sends form responses as webhooks via HTTP POST with JSON body.

**Key fields:**

```json
{
  "event_id": "unique-event-id",
  "event_type": "form_response",
  "form_response": {
    "form_id": "abc123",
    "token": "unique-response-token",
    "submitted_at": "2026-03-05T14:00:00Z",
    "definition": {
      "fields": [
        {"id": "field-1", "title": "What's your name?", "type": "short_text"},
        {"id": "field-2", "title": "Property address?", "type": "long_text"},
        {"id": "field-3", "title": "Why are you selling?", "type": "multiple_choice"}
      ]
    },
    "answers": [
      {"field": {"id": "field-1"}, "type": "text", "text": "Jane Smith"},
      {"field": {"id": "field-2"}, "type": "text", "text": "123 Main St, Phoenix AZ"},
      {"field": {"id": "field-3"}, "type": "choice", "choice": {"label": "Relocating"}}
    ]
  }
}
```

**Parser approach:** Map `answers` array by `field.id` → extract values → build standardized `LeadData` object.

Source: [Typeform Webhook Example Payload](https://www.typeform.com/developers/webhooks/example-payload/)

#### Zapier Webhook (Catch Hook)

Zapier sends a flat JSON object with user-defined field names. The payload shape depends on how the user configured their Zap.

**Typical structure (configured for seller leads):**

```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "602-555-0123",
  "property_address": "123 Main St, Phoenix AZ 85001",
  "motivation": "Relocating for work",
  "asking_price": "350000",
  "source": "facebook_ad",
  "timestamp": "2026-03-05T14:00:00Z"
}
```

**Parser approach:** Direct field mapping. Validate required fields exist. Handle missing fields gracefully (Zapier fields are user-configured and may vary).

#### Generic JSON (Direct Integration / Custom Forms)

For lead sources that POST directly to the webhook (custom website forms, CRM integrations).

**Standardized format (what the pipeline expects internally):**

```json
{
  "lead_type": "seller",
  "source": "website_form",
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "602-555-0123",
  "property_address": "123 Main St, Phoenix AZ 85001",
  "city": "Phoenix",
  "state": "AZ",
  "zip": "85001",
  "motivation": "Relocating for work",
  "asking_price": 350000,
  "bedrooms": 3,
  "bathrooms": 2,
  "notes": "Needs to move by June",
  "submitted_at": "2026-03-05T14:00:00Z"
}
```

**Parser approach:** Validate against schema, normalize field names (e.g., `propertyAddress` → `property_address`), coerce types.

---

## Full Invocation Chain

### End-to-End Flow

```
Lead Source (Typeform/Zapier/Website)
    │
    ▼
[HTTP POST] → Webhook Receiver (FastAPI)
    │
    ├── Parse payload (source-specific parser)
    ├── Validate minimum fields
    ├── Return 200 immediately
    │
    ▼ (background task)
Build Claude prompt with lead data
    │
    ▼
subprocess.run(["claude", "-p", prompt,
    "--allowedTools", "Bash(gws *),Read,Grep",
    "--output-format", "json"])
    │
    ▼
Claude Code Agent (headless)
    │
    ├── Reads pipeline spec (qualification criteria, scoring rubric)
    ├── Qualifies lead against criteria
    ├── Scores lead (0-100)
    ├── If score >= threshold:
    │       ├── Drafts personalized first-touch email
    │       ├── Executes: gws gmail users.drafts create --json '...'
    │       │   (or gws +send if auto-send enabled)
    │       └── Returns: { qualified: true, score: 85, action: "draft_created" }
    │   If score < threshold:
    │       └── Returns: { qualified: false, score: 30, reason: "underwater" }
    │
    ▼
Store result + session_id in lead record
    │
    ▼
[Future webhook / scheduled task]
    │
    ├── Follow-up timer fires (Day 3, Day 7, etc.)
    ├── Load lead record + session_id
    │
    ▼
subprocess.run(["claude", "-p", follow_up_prompt,
    "--resume", session_id,
    "--allowedTools", "Bash(gws *),Read,Grep",
    "--output-format", "json"])
    │
    ▼
Claude resumes with full context from first touch
    ├── Knows what was said, what score was given
    ├── Drafts follow-up with different angle
    └── Executes gws command to send/draft
```

### Session Management for Multi-Touch Journeys

Each lead gets a Claude session ID stored in their record. This enables:

| Touch | Trigger | Claude Command |
|-------|---------|---------------|
| **First touch** | Webhook received | `claude -p "[lead data]" --output-format json` → capture `session_id` |
| **Follow-up #1** (Day 3) | Scheduled task | `claude -p "Send follow-up #1" --resume "$session_id"` |
| **Reply handling** | Gmail `+watch` detects reply | `claude -p "Seller replied: [text]" --resume "$session_id"` |
| **Follow-up #2** (Day 7) | Scheduled task | `claude -p "Send follow-up #2" --resume "$session_id"` |
| **Deal locked** | Investor confirms | `claude -p "Deal locked. Match to buyers." --resume "$session_id"` |
| **Buyer outreach** | Match found | New session per buyer: `claude -p "[deal + buyer data]" --output-format json` |

### HITL (Human-in-the-Loop) Gates

| Action | Default Behavior | Configurable Override |
|--------|-----------------|----------------------|
| **First-touch email** | `gws gmail users.drafts create` (investor reviews draft) | Auto-send if lead score > `config.auto_send_threshold` |
| **Follow-up emails** | Auto-send (investor approved cadence) | Draft if `config.hitl_all_emails: true` |
| **Buyer match outreach** | Draft for review | Auto-send for Excellent matches (85-100) |
| **Pricing decisions** | Always HITL | Never automated |
| **Legal questions** | Always HITL | Never automated |
| **Scheduling** | `gws calendar events insert` (auto) | Draft if `config.hitl_scheduling: true` |

---

## Cost Model Summary

### Per-Lead Economics

| Scenario | Leads/Month | Claude Cost | gws Cost | Total |
|----------|-------------|------------|----------|-------|
| **Low volume** | 20 leads | ~$6-$12 | $0 (free tier) | ~$6-$12/mo |
| **Medium volume** | 100 leads | ~$30-$60 | $0 | ~$30-$60/mo |
| **High volume** | 500 leads | ~$150-$300 | $0 | ~$150-$300/mo |

**Notes:**
- Claude costs assume Sonnet model, ~$0.30-$0.60 per full lead journey (5-7 touches)
- Gmail API is free for consumer accounts (250 messages/day limit)
- Google Workspace accounts have higher limits
- No gws CLI licensing cost (open source)
- No hosting cost if webhook runs on existing server

### Break-Even Analysis

At $5,000 average assignment fee per closed deal:

| Close Rate | Leads to Close | Monthly Leads | Pipeline Cost | Revenue |
|------------|---------------|---------------|---------------|---------|
| 2% | 50 leads → 1 deal | 50 | ~$15-$30 | $5,000 |
| 5% | 20 leads → 1 deal | 100 | ~$30-$60 | $25,000 |
| 10% | 10 leads → 1 deal | 100 | ~$30-$60 | $50,000 |

**Pipeline cost is negligible relative to deal revenue.** Even at 1% close rate, the math works.

Sources: [Claude Code — Manage costs](https://code.claude.com/docs/en/costs), [Anthropic API Pricing](https://platform.claude.com/docs/en/about-claude/pricing), [googleworkspace/cli](https://github.com/googleworkspace/cli), [Typeform Webhooks](https://www.typeform.com/developers/webhooks/example-payload/), [FastAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/)
