# Reddit Pain Analyzer Harness — Specification

## System Overview

The harness is a self-executing specification that orchestrates autonomous analysis of Reddit communities through sequential skills. An agent reads this specification and executes it without pausing.

```
OUTER LOOP: /reddit-pain/analyze [subreddit-url]
├─ Orchestrates three inner skills in sequence
├─ Manages state file transitions
└─ Returns JSON + Markdown deliverables

INNER SKILL A: reddit-data-pipeline
├─ Step 1: Validate subreddit
├─ Step 2: Fetch posts using Playwright navigation
├─ Step 3: Extract and clean text
└─ Gate contracts validate inputs/outputs

INNER SKILL B: ai-analysis-engine
├─ Step 1: Identify pain points (LLM)
├─ Step 2: Generate ideas (LLM)
├─ Step 3: Score potential (LLM)
└─ Gate contracts validate inputs/outputs

INNER SKILL C: results-processor
├─ Step 1: Validate results
├─ Step 2: Store in state
├─ Step 3: Export JSON + Markdown
└─ Gate contracts validate inputs/outputs
```

## Execution Flow

### Entry Point: `/reddit-pain/analyze [subreddit-url]`

An agent receives this command and executes the following steps:

```
User invokes: /reddit-pain/analyze r/entrepreneur

Time: T0
├─ Agent checks preconditions:
│  ├─ State file exists ✓
│  ├─ URL valid ✓
│  ├─ Cost estimate < €0.50 ✓
│  └─ Action counter not exceeded ✓
│
T1: OUTER LOOP INITIALIZES
├─ Parse subreddit URL to extract name
├─ Generate job_id (UUID)
├─ Create/load state file (reddit-pain-analyzer_workflow.json)
├─ Set status = "RUNNING"
├─ Estimate cost (€0.18 typical)
│
T2-T5: CALL INNER SKILL A (reddit-data-pipeline)
├─ Step 1: Validate subreddit
│  ├─ Input gate: subreddit_url valid ✓
│  ├─ Action: Navigate to subreddit, confirm it exists
│  └─ Output gate: subreddit_valid ✓
│
├─ Step 2: Fetch posts
│  ├─ Input gate: subreddit exists ✓
│  ├─ Action: Fetch top 50-100 posts from subreddit
│  └─ Output gate: posts_count >= 30 ✓
│
└─ Step 3: Extract text
   ├─ Input gate: posts_count >= 30 ✓
   ├─ Action: Clean, concatenate, tokenize all post text
   └─ Output gate: tokens in [500, 5000] ✓
│
T6-T15: CALL INNER SKILL B (ai-analysis-engine)
├─ Step 1: LLM identify pain points
│  ├─ Input gate: text_tokens >= 500 ✓
│  ├─ Action: Send text to LLM, request pain point identification
│  └─ Output gate: pain_points.count >= 5 ✓
│
├─ Step 2: LLM generate ideas
│  ├─ Input gate: pain_points.count >= 5 ✓
│  ├─ Action: Send pain points to LLM, request startup ideas
│  └─ Output gate: startup_ideas.count >= 5 ✓
│
└─ Step 3: LLM score potential
   ├─ Input gate: startup_ideas.count >= 5 ✓
   ├─ Action: Send ideas to LLM, request market potential scores
   └─ Output gate: scores numeric [1-10] ✓
│
T16-T18: CALL INNER SKILL C (results-processor)
├─ Step 1: Validate results
│  ├─ Input gate: all LLM outputs populated ✓
│  ├─ Action: Check results match schema
│  └─ Output gate: results_valid ✓
│
├─ Step 2: Store in state
│  ├─ Input gate: results_valid ✓
│  ├─ Action: Write results to state file
│  └─ Output gate: persisted ✓
│
└─ Step 3: Export deliverables
   ├─ Input gate: persisted ✓
   ├─ Action: Generate results.json and results.md files
   └─ Output gate: files_created ✓
│
T19: OUTER LOOP COMPLETES
├─ Set status = "COMPLETE"
├─ Update completion timestamp
└─ Return deliverables to user
   ├─ results.json
   └─ results.md

T19+: State logging
├─ Action recorded to actions.jsonl
├─ State file updated
└─ Job marked available for export
```

**Total time:** ~3-5 minutes (limited by LLM API response times)
**Total cost:** €0.18

## State Management

### Level 1: Session State

Agent tracks current session:

```json
{
  "session_started": true,
  "current_task": "reddit-pain-analyzer",
  "context": {
    "current_command": "/reddit-pain/analyze",
    "last_job_id": "uuid-123",
    "pending_actions": []
  }
}
```

### Level 2: Harness Workflow State

Agent maintains job state file:

```json
{
  "harness": "reddit-pain-analyzer",
  "job_id": "uuid-123",
  "subreddit_url": "https://reddit.com/r/entrepreneur",
  "status": "COMPLETE",
  "orchestration": {
    "outer_loop": "analyze_01",
    "inner_skills_completed": ["reddit-data-pipeline", "ai-analysis-engine", "results-processor"],
    "current_step": null
  },
  "timestamps": {
    "started": "2026-06-13T20:00:00Z",
    "completed": "2026-06-13T20:03:30Z"
  },
  "cost": {
    "estimated": 0.18,
    "actual": 0.18
  },
  "results": {
    "job_id": "uuid-123",
    "pain_points": [...],
    "startup_ideas": [...]
  }
}
```

### Level 3: Phase State (Passed Between Skills)

Each inner skill produces state passed to the next:

```
reddit-data-pipeline output:
{
  "text_content": "...",
  "posts_count": 75,
  "tokens": 4200
}
  ↓
ai-analysis-engine validates input via gate contract
  ↓
ai-analysis-engine output:
{
  "pain_points": ["...", "..."],
  "startup_ideas": ["...", "..."],
  "market_scores": [8.5, 7.2, ...]
}
  ↓
results-processor validates input via gate contract
  ↓
results-processor output:
{
  "results.json": {...},
  "results.md": "..."
}
```

## Gate Contracts (Data Validation)

Every transition between steps is protected by a gate contract. See `gate-contracts.md` for full JSON schemas.

**Example: ai-analysis-engine Step 1 → Step 2**

Before Step 2 runs:
1. Validate input has pain_points array with at least 5 items
2. Run Step 2 (LLM generate ideas)
3. After Step 2, validate output has startup_ideas array with at least 5 items
4. If validation fails, retry up to 3 times with exponential backoff
5. If still fails, mark phase failed and stop

## Error Recovery Strategy

| Failure Type | Recovery |
|--------------|----------|
| Transient (network timeout) | Retry 3x with exponential backoff |
| Permanent (invalid subreddit) | Fail immediately, report to user |
| LLM quality issue (bad output) | Retry with refined prompt, max 3x |
| Cost overrun (>€0.50) | Hard block, alert admin |
| State corruption | Roll back to last valid gate, retry |

## Autonomy Guarantees

✅ **No pauses** — Outer loop executes continuously until completion/failure

✅ **No user input** — All decisions made by state + gate contracts

✅ **Deterministic** — Same subreddit → consistent results (barring LLM variance)

✅ **Recoverable** — Failed phase can be retried from that point

✅ **Transparent** — All state logged, agent can inspect anytime

## Comparison: Loop Architecture vs. Traditional REST API

**Loop Architecture (Harness):**
```
User → /reddit-pain/analyze → Agent orchestration → Results
       (one call)
       No waiting, no polling
```

**REST API Architecture (Traditional App):**
```
User → POST /api/analyze → Queue → Worker → DB → User polls /api/status → Results
     (async, requires polling)
     Multiple calls, eventual consistency
```

**Why harness is cleaner:**
- Single call, state-driven execution
- No async/await complexity
- No database synchronization
- No polling loop on client
- Deliverables are immutable (JSON/MD)

## Tech Stack (Agent-Readable Specification)

**Agent must:**
- Read subreddit URLs and validate them
- Navigate to Reddit using Playwright
- Fetch posts by scrolling and extracting text
- Send text to LLM APIs for analysis
- Parse LLM responses (JSON + lists)
- Validate responses against gate contracts
- Write state files (JSON)
- Generate Markdown reports from state

**No code to write — Agent reads markdown and executes.**
