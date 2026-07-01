# AI Analysis Engine — Skill Specification

## Identity

**Skill:** ai-analysis-engine
**Purpose:** Analyze Reddit text to identify pain points and generate startup ideas
**Input:** Cleaned text content (4200 tokens) from reddit-data-pipeline
**Output:** Pain points list + Startup ideas list + Market potential scores
**Platform:** Agent calling LLM APIs and parsing responses

---

## File Index

| File | Purpose |
|------|---------|
| `ai-analysis-engine.md` | This file. Skill overview + step instructions |
| `references/step-01-pain-points.md` | LLM prompt for identifying pain points |
| `references/step-02-ideas.md` | LLM prompt for generating startup ideas |
| `references/step-03-scoring.md` | LLM prompt for scoring market potential |

---

## Overview

This skill has three sequential steps that an agent executes by reading markdown instructions and calling LLMs:

1. **Step 1: Identify Pain Points** — Send text to LLM, extract top 10 pain points
2. **Step 2: Generate Startup Ideas** — Send pain points to LLM, generate 5-10 startup ideas
3. **Step 3: Score Market Potential** — Send ideas to LLM, score each 1-10

Each step has gate contracts and retry logic.

---

## Step 1: Identify Pain Points

**Input Gate:**
- Required: `text_content` (string), `token_count` (number)
- Validation: token_count >= 500

**Agent Instructions:**

1. Prepare LLM prompt:
```
Analyze this Reddit discussion and identify the top 10 pain points or frustrations
mentioned by users. Be specific and concrete. Only extract actual pain points,
not solutions.

Format your response as a JSON array of strings:
["pain point 1", "pain point 2", ...]

Text:
[INSERT text_content HERE]
```

2. Call LLM API (GPT-4 mini or Claude Haiku)
3. Parse response as JSON array
4. Extract pain point list
5. Count items in array

**Output Gate:**
- Required: `pain_points` (array of strings), `pain_points_count` (number)
- Validation: pain_points.length >= 5 AND all items are non-empty strings

**Error Handling:**
- If response not valid JSON → Retry with stricter prompt
- If fewer than 5 pain points → Retry with refined prompt
- If API timeout → Retry 3x with exponential backoff (1s, 2s, 4s)
- If API error → Retry up to 3 times, then fail

**Retry Backoff:** 1 second, 2 seconds, 4 seconds (max 3 retries)

**Cost:**
- Typical: €0.02-0.05 depending on model choice
- Budget: €0.05 max per step

**Example Output:**
```json
{
  "pain_points": [
    "Hard to find qualified contractors",
    "Expensive freelance platforms",
    "Time-consuming vetting process",
    "Quality inconsistency across providers",
    "Hidden fees and surprise charges"
  ],
  "pain_points_count": 5
}
```

---

## Step 2: Generate Startup Ideas

**Input Gate:**
- Required: `pain_points` (array), `pain_points_count` (number)
- Validation: pain_points_count >= 5

**Agent Instructions:**

1. Prepare LLM prompt:
```
Based on these user pain points, generate 5-10 creative and feasible startup ideas
that solve one or more of these problems. For each idea, include a clear title and
brief description (1-2 sentences).

Format your response as JSON array:
[
  {"title": "Idea Name", "description": "What it does..."},
  ...
]

Pain Points:
[INSERT pain_points array HERE]
```

2. Call LLM API
3. Parse response as JSON array of objects
4. Validate each object has "title" and "description"
5. Count ideas

**Output Gate:**
- Required: `startup_ideas` (array of objects), `startup_ideas_count` (number)
- Validation: startup_ideas.length >= 5 AND each object has non-empty title + description

**Error Handling:**
- If response not valid JSON → Retry with stricter prompt
- If fewer than 5 ideas → Retry
- If missing fields → Retry with template reminder
- If API timeout → Retry 3x with backoff
- If API error → Retry up to 3 times, then fail

**Retry Backoff:** 1 second, 2 seconds, 4 seconds (max 3 retries)

**Cost:**
- Typical: €0.03-0.08 depending on model and token count
- Budget: €0.10 max per step

**Example Output:**
```json
{
  "startup_ideas": [
    {
      "title": "Vetted Freelancer Marketplace",
      "description": "Automate contractor vetting using background checks and skill verification. Focus on quality over quantity."
    },
    {
      "title": "Fractional Executive Network",
      "description": "Connect startups with part-time C-level executives for mentoring and advisory roles."
    }
  ],
  "startup_ideas_count": 2
}
```

---

## Step 3: Score Market Potential

**Input Gate:**
- Required: `startup_ideas` (array), `startup_ideas_count` (number)
- Validation: startup_ideas_count >= 5

**Agent Instructions:**

1. Prepare LLM prompt:
```
Rate each startup idea for market potential on a scale of 1-10. Consider:
- Market size and growth potential
- User demand clarity
- Competitive intensity
- Technical feasibility
- Timeline to MVP

Format your response as JSON array:
[
  {"title": "Idea Name", "score": 8, "reasoning": "Why this score..."},
  ...
]

Ideas:
[INSERT startup_ideas array HERE]
```

2. Call LLM API
3. Parse response as JSON array of objects
4. Validate each object has "title", "score" (1-10), "reasoning"
5. Extract scores

**Output Gate:**
- Required: `scored_ideas` (array of objects), `scores` (array of numbers)
- Validation: All scores are numbers 1-10 AND all objects have title + score + reasoning

**Error Handling:**
- If score outside 1-10 range → Retry with strict bounds reminder
- If missing fields → Retry
- If response not JSON → Retry
- If API timeout → Retry 3x with backoff
- If API error → Retry up to 3 times, then fail

**Retry Backoff:** 1 second, 2 seconds, 4 seconds (max 3 retries)

**Cost:**
- Typical: €0.02-0.05 depending on model
- Budget: €0.05 max per step

**Example Output:**
```json
{
  "scored_ideas": [
    {
      "title": "Vetted Freelancer Marketplace",
      "score": 8.5,
      "reasoning": "Large market ($50B+ freelance economy), clear user demand, moderate competition"
    },
    {
      "title": "Fractional Executive Network",
      "score": 7.2,
      "reasoning": "Growing demand, underserved market, moderate implementation complexity"
    }
  ],
  "scores": [8.5, 7.2]
}
```

---

## Model Choice Guidance

Agent should choose LLM based on cost targets:

| Model | Cost per 1K tokens | Recommended Use |
|-------|-------------------|-----------------|
| Claude Haiku | €0.002 | Steps 1-2 (cheap, fast) |
| GPT-4 mini | €0.00002 | Step 3 (scoring, quality) |

**Target total cost:** €0.08-0.12 per execution

---

## State Handoff

This skill produces state passed to `results-processor`:

```json
{
  "phase": "ai-analysis-engine",
  "status": "COMPLETE",
  "output": {
    "pain_points": [...],
    "startup_ideas": [...],
    "scored_ideas": [...],
    "timestamp": "2026-06-13T20:02:15Z"
  }
}
```

---

## Quality Metrics

Agent should track:

| Metric | Target | Impact |
|--------|--------|--------|
| pain_points_count | >= 5 | Minimum unique problems |
| startup_ideas_count | >= 5 | Sufficient options |
| scores range | 1-10 | Quality validation |
| API errors | 0 | Success rate |
| avg_retry_count | < 1 | Efficiency |

---

## Failure Recovery

| Scenario | Recovery |
|----------|----------|
| Invalid JSON response | Retry 3x with stricter prompt |
| Too few ideas | Retry 3x with refined prompt |
| Score out of range | Retry 3x with bounds reminder |
| API timeout | Retry 3x with exponential backoff |
| API error (rate limit) | Retry 3x with 2s+ backoff |
| API error (auth) | Fail immediately |

---

## References

See individual step files for detailed prompts and examples:
- `references/step-01-pain-points.md`
- `references/step-02-ideas.md`
- `references/step-03-scoring.md`

---

**Key principle:** This skill is pure specification. Agent reads markdown, calls LLM APIs per instructions, parses JSON responses, validates against gates.
