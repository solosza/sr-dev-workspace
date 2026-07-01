# Commands Design — Entry Points for the Harness

## Main Command: `/reddit-pain/analyze`

**Purpose:** Submit a subreddit for analysis

**Usage:**
```
/reddit-pain/analyze r/entrepreneur
/reddit-pain/analyze https://reddit.com/r/startups
```

**Instructions:**
1. Parse subreddit URL or name
2. Validate format (r/[name] or reddit.com/r/[name])
3. Check user has credits available (1 credit = 1 analysis)
4. Create job_id (UUID)
5. Initialize harness state file
6. Call outer loop: `/reddit-pain/orchestrate [job_id]`
7. Return job_id + status to user

**State output:**
```json
{
  "job_id": "uuid-123",
  "subreddit": "r/entrepreneur",
  "status": "QUEUED",
  "estimated_cost": "€0.18",
  "message": "Analysis queued. Check status with: /reddit-pain/status uuid-123"
}
```

**Gate contract (input):**
```
Required: subreddit_url
Validations:
  ✓ Valid Reddit URL or r/[name] format
  ✓ Subreddit name matches [a-z0-9_]+
  ✓ User has available credits
```

---

## Status Command: `/reddit-pain/status [job-id]`

**Purpose:** Check analysis progress

**Usage:**
```
/reddit-pain/status uuid-123
```

**Instructions:**
1. Load job state from harness_workflow.json
2. Extract current status and progress
3. If running: Show which step is executing
4. If complete: Show results available
5. If failed: Show error message

**Output:**
```json
{
  "job_id": "uuid-123",
  "status": "COMPLETE",
  "progress": "100%",
  "steps_completed": [
    "Validate subreddit ✓",
    "Fetch posts ✓",
    "Extract text ✓",
    "LLM identify pain points ✓",
    "LLM generate ideas ✓",
    "LLM score potential ✓",
    "Validate results ✓",
    "Export deliverables ✓"
  ],
  "cost": "€0.18",
  "results_available": true,
  "message": "Ready for export. Use: /reddit-pain/export uuid-123"
}
```

---

## Export Command: `/reddit-pain/export [job-id]`

**Purpose:** Download analysis results

**Usage:**
```
/reddit-pain/export uuid-123
/reddit-pain/export uuid-123 --format json
/reddit-pain/export uuid-123 --format markdown
```

**Instructions:**
1. Load results from state
2. Validate results exist
3. Format as JSON, Markdown, or both (default)
4. Return file paths or content

**Output:**
```json
{
  "job_id": "uuid-123",
  "formats_available": ["json", "markdown"],
  "results": {
    "json": {
      "subreddit": "r/entrepreneur",
      "pain_points": [...],
      "startup_ideas": [...]
    },
    "markdown": "# Reddit Pain Analysis — r/entrepreneur\n\n..."
  }
}
```

---

## Admin Command: `/reddit-pain/admin/monitor`

**Purpose:** Monitor running jobs, track costs

**Usage:**
```
/reddit-pain/admin/monitor
/reddit-pain/admin/monitor --cost-summary
/reddit-pain/admin/monitor --failed-jobs
```

**Instructions:**
1. Query all jobs in state directory
2. Filter by status (running, complete, failed)
3. Calculate total cost, average cost
4. Report queue depth, failures

**Output:**
```json
{
  "summary": {
    "total_jobs": 45,
    "running": 2,
    "complete": 40,
    "failed": 3
  },
  "cost_tracking": {
    "total_cost": "€7.50",
    "average_cost": "€0.17",
    "cost_overruns": 0
  },
  "queue": [
    {
      "job_id": "uuid-124",
      "status": "EXECUTING",
      "current_step": "ai-analysis-engine/step-2",
      "elapsed": "2m 30s"
    }
  ],
  "failed_jobs": [
    {
      "job_id": "uuid-100",
      "error": "Subreddit not found"
    }
  ]
}
```

---

## Summary

| Command | Purpose | Entry Point |
|---------|---------|------------|
| `/reddit-pain/analyze [url]` | Submit analysis | User initiates |
| `/reddit-pain/status [id]` | Check progress | User polls |
| `/reddit-pain/export [id]` | Download results | User retrieves |
| `/reddit-pain/admin/monitor` | Admin oversight | Operator monitors |

**Pattern:**
- User calls `/reddit-pain/analyze` once
- Agent orchestrates autonomously
- User checks `/reddit-pain/status` anytime (non-blocking)
- User downloads results via `/reddit-pain/export` when ready

No async callbacks, no webhooks, no email notifications — just state-driven polling.
