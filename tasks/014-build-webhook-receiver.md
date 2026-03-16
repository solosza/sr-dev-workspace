# Build Webhook Receiver Reference

## Context
The thin server (~50 lines) that receives lead webhooks and invokes Claude Code headless as a subprocess. This is reference implementation code — the investor deploys their own. All output goes into the creative-finance-spec repo.

## Dependencies
- **004** — integration research (webhook patterns, Claude Code headless flags)
- **006** — schemas (webhook payload mapping to seller lead schema)

## Requirements

Read these files before building:
- `creative-finance-spec/research/004-integration-surface.md`
- `creative-finance-spec/pipeline/interfaces/schemas.json`
- `creative-finance-spec/pipeline/interfaces/webhook_schemas.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\integration\`

### webhook_receiver.py
Reference Python implementation (FastAPI or Flask):
- Receive POST at `/webhook/lead`
- Parse JSON payload
- Validate required fields against seller lead schema
- Generate session-id: `seller-{name_slug}-{address_slug}`
- Invoke Claude Code headless:
  ```
  subprocess.run([
    "claude", "-p", prompt,
    "--allowedTools", "Bash",
    "--output-format", "json",
    "--session-id", session_id
  ])
  ```
- Construct the prompt: include lead data, reference the domain spec, instruct to run pipeline-workflow
- Return: 200 OK with processing status
- Error handling: invalid payload → 400, Claude invocation fails → 500 with retry logic
- Logging: log every incoming lead and every Claude invocation result

### webhook_receiver_README.md
- What this file is (reference implementation, not production-ready)
- How to run locally: `pip install fastapi uvicorn` → `uvicorn webhook_receiver:app`
- Environment requirements: Claude Code installed, `claude` on PATH, authenticated (Max subscription or API key)
- How to test: `curl -X POST localhost:8000/webhook/lead -H "Content-Type: application/json" -d '{"name": "...", ...}'`
- How to deploy: Railway, Render, AWS Lambda (brief notes, not full guides)
- Security considerations: validate webhook source, rate limiting, don't log sensitive data

## Output
- `creative-finance-spec/pipeline/integration/webhook_receiver.py`
- `creative-finance-spec/pipeline/integration/webhook_receiver_README.md`

## Validation (check ALL before completing)
- [ ] Both files exist at their output paths
- [ ] webhook_receiver.py is valid Python (no syntax errors — run `python -c "import ast; ast.parse(open('file').read())"`)
- [ ] webhook_receiver.py has POST endpoint for `/webhook/lead`
- [ ] webhook_receiver.py validates incoming payload against required fields
- [ ] webhook_receiver.py generates session-id from lead data
- [ ] webhook_receiver.py invokes `claude -p` via subprocess with correct flags
- [ ] webhook_receiver.py has error handling (400 for bad payload, 500 for invocation failure)
- [ ] webhook_receiver_README.md has local run instructions
- [ ] webhook_receiver_README.md has test curl command
- [ ] Code is under 100 lines (this is a reference, not a framework)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
