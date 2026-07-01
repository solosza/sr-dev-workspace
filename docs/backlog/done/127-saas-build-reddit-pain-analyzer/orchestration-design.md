# Reddit Pain Analyzer — Agent Orchestration Design

## Overview

The entire Reddit Pain Analyzer is built on the **agent orchestration framework**. Every analysis job runs as an autonomous, multi-step orchestrated process with no human intervention.

The framework provides:
- **Commands:** Entry points for users and admins
- **Skills:** Multi-step analysis orchestrators
- **State management:** Job status, credit ledger, results cache
- **Gate contracts:** Validation at each phase boundary
- **Error recovery:** Automatic retries, fallbacks

## High-Level Orchestration Loop

```
User Input (subreddit URL)
         ↓
Command: /reddit-pain/submit-analysis
         ↓
Skill: reddit-data-pipeline
  ├─ Step 1: Validate subreddit
  ├─ Step 2: Fetch posts (PRAW)
  ├─ Step 3: Extract text
  └─ [Gate contract: posts_extracted ✓]
         ↓
Skill: ai-analysis-engine
  ├─ Step 1: LLM - identify pain points
  ├─ Step 2: LLM - generate ideas
  ├─ Step 3: LLM - score market potential
  └─ [Gate contract: analysis_complete ✓]
         ↓
Skill: results-processor
  ├─ Step 1: Validate results
  ├─ Step 2: Store in DB
  ├─ Step 3: Cache in Redis
  └─ [Gate contract: results_stored ✓]
         ↓
User Views Results
```

## Commands (User Entry Points)

### Command 1: `/reddit-pain/submit-analysis`
**What:** User submits a subreddit URL for analysis

**Instructions:**
1. Validate subreddit URL format
2. Check user has available credits
3. Deduct 1 credit from account
4. Create analysis_job record (status: queued)
5. Queue job to background worker (via Celery message)
6. Return job_id to user

**State Output:**
```json
{
  "analysis_job": {
    "id": "uuid",
    "user_id": "uuid",
    "subreddit_url": "https://reddit.com/r/entrepreneur",
    "status": "queued",
    "created_at": "2026-06-13T20:00:00Z"
  }
}
```

## Skills (Multi-Step Orchestrators)

### Skill 1: reddit-data-pipeline
**Purpose:** Fetch Reddit posts and extract analysis-ready text

**Steps:**
- Step 1: Validate subreddit (check exists, is public)
- Step 2: Fetch posts via PRAW (top 50-100 posts)
- Step 3: Extract text, clean, truncate to 5000 tokens

### Skill 2: ai-analysis-engine
**Purpose:** Run LLM analysis to identify pain points and generate ideas

**Steps:**
- Step 1: LLM - Identify pain points (GPT-4 mini)
- Step 2: LLM - Generate startup ideas
- Step 3: LLM - Score market potential (1-10 scale)

### Skill 3: results-processor
**Purpose:** Validate, store, cache, and prepare results for export

**Steps:**
- Step 1: Validate results structure
- Step 2: Store in PostgreSQL
- Step 3: Cache in Redis + prepare JSON export

## Autonomous Loop Contract

When a job is submitted, the entire orchestration runs **autonomously**:

✅ **No pauses** — Analysis runs to completion or failure
✅ **No user input** — Errors handled internally (retry or fail)
✅ **State-driven** — All behavior determined by state files
✅ **Error recovery** — Transient failures retry automatically
✅ **Reporting** — Results logged, user notified when complete

## Cost Tracking in State

Each job tracks costs in real-time:

```json
{
  "job_id": "uuid",
  "cost_breakdown": {
    "praw_api": 0.0,
    "llm_calls": 0.20,
    "db_operations": 0.01,
    "storage": 0.02
  },
  "total_cost": 0.23,
  "revenue_per_analysis": 0.50,
  "gross_margin": "54%"
}
```

This enables real-time profitability monitoring and cost-based decisions (e.g., if cost exceeds €0.40, alert admin).
