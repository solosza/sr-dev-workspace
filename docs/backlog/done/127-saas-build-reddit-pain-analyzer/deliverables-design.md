# Deliverables Design — JSON + Markdown Output Format

**Core principle:** Single source of truth (state file) → two renderings (JSON machine-readable, Markdown human-readable)

## JSON Schema (Machine-Readable)

**File:** `results-[job-id].json`

```json
{
  "metadata": {
    "job_id": "8f2c4a1b-3d9e-4a7c-8b2f-1a5c3d8e9f2a",
    "harness": "reddit-pain-analyzer",
    "version": "1.0",
    "timestamp": "2026-06-13T20:10:00Z"
  },
  "input": {
    "subreddit": "r/entrepreneur",
    "subreddit_url": "https://reddit.com/r/entrepreneur",
    "posts_requested": 100
  },
  "data_collection": {
    "posts_found": 75,
    "posts_analyzed": 75,
    "total_comments": 342,
    "text_tokens": 4200,
    "collection_time_seconds": 42
  },
  "analysis_results": {
    "pain_points": [
      {
        "rank": 1,
        "description": "Hard to find qualified contractors",
        "frequency_percent": 45,
        "sentiment": "frustrated",
        "supporting_quote": "I've spent weeks vetting freelancers..."
      },
      {
        "rank": 2,
        "description": "Expensive freelance platforms",
        "frequency_percent": 38,
        "sentiment": "frustrated",
        "supporting_quote": "Upwork takes 20% and..."
      }
    ],
    "startup_ideas": [
      {
        "rank": 1,
        "title": "Vetted Freelancer Marketplace",
        "description": "Automate contractor vetting using background checks and skill verification. Focus on quality over quantity.",
        "solves_pain_points": [1, 2],
        "market_potential_score": 8.5,
        "market_reasoning": "Large market ($50B+ freelance economy), clear user demand, moderate competition",
        "implementation_difficulty": "Medium",
        "estimated_timeline_weeks": 12
      },
      {
        "rank": 2,
        "title": "Fractional Executive Network",
        "description": "Connect startups with part-time C-level executives for mentoring and advisory roles.",
        "solves_pain_points": [1, 3],
        "market_potential_score": 7.2,
        "market_reasoning": "Growing demand for experienced guidance, underserved market",
        "implementation_difficulty": "Low",
        "estimated_timeline_weeks": 8
      }
    ]
  },
  "cost_tracking": {
    "estimated_cost_euros": 0.18,
    "actual_cost_euros": 0.18,
    "breakdown": {
      "reddit_api": 0.00,
      "llm_calls": {
        "pain_point_analysis": 0.05,
        "idea_generation": 0.08,
        "scoring": 0.05
      },
      "processing": 0.02
    }
  },
  "execution": {
    "start_time": "2026-06-13T20:00:00Z",
    "end_time": "2026-06-13T20:03:30Z",
    "total_time_seconds": 210,
    "status": "COMPLETE",
    "errors": []
  }
}
```

## Markdown Schema (Human-Readable)

**File:** `results-[job-id].md`

**Template:**

```markdown
# Reddit Pain Analysis Report

**Subreddit:** [r/entrepreneur](https://reddit.com/r/entrepreneur)
**Analyzed:** 2026-06-13 20:10:00Z
**Analysis ID:** 8f2c4a1b-3d9e-4a7c-8b2f-1a5c3d8e9f2a

---

## Summary

Analyzed **75 posts** from r/entrepreneur with **342 comments** to identify recurring pain points and generate startup ideas.

| Metric | Value |
|--------|-------|
| Posts analyzed | 75 |
| Total comments | 342 |
| Pain points identified | 10 |
| Startup ideas generated | 8 |
| Analysis time | 3m 30s |
| Cost | €0.18 |

---

## Top 5 Pain Points

### 1. Hard to find qualified contractors (45%)

**Sentiment:** Frustrated
**Frequency:** 45% of posts mention this

> "I've spent weeks vetting freelancers only to find they don't meet our quality standards. The time investment is brutal."

**Context:** Users struggle with contractor quality and vetting processes. Upwork and Fiverr don't provide enough filtering.

---

### 2. Expensive freelance platforms (38%)

**Sentiment:** Frustrated
**Frequency:** 38% of posts mention this

> "Upwork takes 20% and the quality isn't there. I'm looking for alternatives that cost less."

**Context:** Platform fees (Upwork 20%, Toptal 30%) eat into margins, especially for early-stage startups.

---

### 3. Time-consuming vetting process (32%)

**Sentiment:** Frustrated
**Frequency:** 32% of posts mention this

> "Vetting freelancers takes as much time as the actual work. There has to be a better way."

**Context:** Manual review of portfolios, references, and test projects is time-intensive.

---

### 4. [Etc.]

---

## Startup Ideas

### Rank 1: Vetted Freelancer Marketplace

**Market Potential:** 8.5/10

**Description:**
A marketplace that automates contractor vetting using background checks, skill verification, and community reviews. Focus on quality over quantity — every contractor pre-screened.

**Solves pain points:** #1, #2 (hard to find qualified contractors, expensive platforms)

**Market Size:** $50B+ freelance economy globally

**Competitive Advantage:**
- Pre-vetted talent reduces hiring time by 50%+
- Lower platform fees (15% vs. Upwork 20%)
- Better quality filtering than existing platforms

**Implementation:**
- Timeline: 12 weeks to MVP
- Difficulty: Medium (vetting + marketplace)
- Technology: Next.js + PostgreSQL + Stripe

---

### Rank 2: Fractional Executive Network

**Market Potential:** 7.2/10

[...]

---

## Data Collection Details

**Source:** Reddit public data
**Subreddit:** r/entrepreneur
**Posts collected:** 75 (top posts by score, filtered by month)
**Comments collected:** Top 5 per post
**Total text analyzed:** 4,200 tokens

---

## Analysis Process

1. **Fetch posts** from subreddit (top 100)
2. **Extract text** from posts + top comments
3. **Identify pain points** via LLM analysis
4. **Generate ideas** based on pain points
5. **Score potential** for each idea (market size, feasibility, competition)

---

## Cost Breakdown

| Component | Cost | Notes |
|-----------|------|-------|
| Reddit data fetch | €0.00 | Public data, no API cost |
| Pain point analysis | €0.05 | LLM API call |
| Idea generation | €0.08 | LLM API call |
| Scoring | €0.05 | LLM API call |
| Processing | €0.02 | State management, export |
| **Total** | **€0.18** | Profitable at €0.50/credit |

---

## How to Use These Results

### For Market Research
- Validate product-market fit
- Understand customer pain points
- Identify unmet needs

### For Pitch Decks
- Include pain points + market size
- Show idea validation from real users
- Quote community feedback

### For Building
- Start with highest-score idea (8.5/10)
- Validate with interviews (find r/entrepreneur users)
- Iterate based on feedback

---

*Generated by Reddit Pain Analyzer Harness*
*[JSON version](results-[job-id].json) | [Raw data](results-[job-id]-data.json)*
```

## Consistency Rules

Agent must ensure both JSON and Markdown are consistent:

**Rule 1:** Both files contain identical pain point lists
**Rule 2:** Both files contain identical startup ideas and scores
**Rule 3:** Both files have same job_id and timestamp
**Rule 4:** Markdown renders all data from JSON without divergence
**Rule 5:** If state updates, both files regenerate together

## File Organization

```
results-[job-id]/
├── results.json              (structured data, machine-readable)
├── results.md                (human-readable report)
└── results-raw.jsonl         (optional: debugging, intermediate states)
```

## Validation Checklist

Both JSON and Markdown must pass:

- ✓ All pain points present in both
- ✓ All startup ideas present in both
- ✓ Scores match exactly
- ✓ Timestamps identical
- ✓ Job ID consistent
- ✓ No formatting errors in Markdown
- ✓ Valid JSON syntax
- ✓ No missing fields

## File Size Guidelines

| File | Expected Size | Status |
|------|---------------|--------|
| results.json | 10-15 KB | JSON compact |
| results.md | 8-12 KB | Markdown with sections |
| Total | 18-27 KB | Reasonable download |

## Example Usage

**Download JSON:**
```
/reddit-pain/export uuid-123 --format json
# Returns: results.json (for data pipelines, further analysis)
```

**Download Markdown:**
```
/reddit-pain/export uuid-123 --format markdown
# Returns: results.md (for reading, sharing, pitch decks)
```

**Download both (default):**
```
/reddit-pain/export uuid-123
# Returns: results.json + results.md
```

---

**Key principle:** One analysis, two representations, zero duplication.
