# Reddit Data Pipeline — Skill Specification

## Identity

**Skill:** reddit-data-pipeline
**Purpose:** Fetch Reddit posts and prepare text for LLM analysis
**Input:** Subreddit URL (e.g., r/entrepreneur)
**Output:** Cleaned text content (4200 tokens typical) + post metadata
**Platform:** Agent reading markdown + calling Playwright/LLM APIs

---

## File Index

| File | Purpose |
|------|---------|
| `reddit-data-pipeline.md` | This file. Skill overview + step instructions |
| `references/step-01-validate.md` | Validate subreddit exists |
| `references/step-02-fetch.md` | Fetch top posts from subreddit |
| `references/step-03-extract.md` | Extract and clean text content |

---

## Overview

This skill has three sequential steps that an agent executes by reading markdown instructions:

1. **Step 1: Validate Subreddit** — Confirm subreddit exists and is accessible
2. **Step 2: Fetch Posts** — Retrieve 50-100 top posts from the subreddit
3. **Step 3: Extract Text** — Clean, concatenate, and tokenize all text

Each step has an input gate (validates preconditions), an action (what agent does), and an output gate (validates results).

---

## Step 1: Validate Subreddit

**Input Gate:**
- Required: `subreddit_url` (string)
- Validation: URL format is valid (r/[name] or reddit.com/r/[name])

**Agent Instructions:**
1. Parse the subreddit URL to extract name
2. Navigate to the subreddit using Playwright
3. Confirm the page loads successfully
4. Extract subscriber count and description
5. Confirm subreddit is public (not banned or private)

**Output Gate:**
- Required: `subreddit_valid` (boolean), `subreddit_name` (string), `subscriber_count` (number)
- Validation: subreddit_valid is true

**Error Handling:**
- If subreddit not found → Fail immediately with message "Subreddit not found"
- If private/banned → Fail immediately with message "Subreddit is private or banned"
- If navigation timeout → Retry up to 2 times with 2-second backoff

**Example Output:**
```json
{
  "subreddit_valid": true,
  "subreddit_name": "entrepreneur",
  "subscriber_count": 2500000,
  "description": "The web's largest community of entrepreneurs and startup founders"
}
```

---

## Step 2: Fetch Posts

**Input Gate:**
- Required: `subreddit_valid` (boolean), `subreddit_name` (string)
- Validation: subreddit_valid is true

**Agent Instructions:**
1. Navigate to the subreddit's "top" feed filtered by "month"
2. Scroll and extract top 50-100 posts
3. For each post, extract:
   - Title
   - Body text (selftext)
   - Score (upvotes)
   - Comment count
4. Fetch top 5 comments per post
5. Combine post text + top 5 comments
6. Filter out: stickied posts, removed posts, posts with score < 10
7. Store all text content

**Output Gate:**
- Required: `posts_found` (number), `posts` (array), `total_text_chars` (number)
- Validation: posts_found >= 30

**Error Handling:**
- If fewer than 30 posts found → Fail with message "Subreddit too niche or private"
- If API rate limited → Wait 30 seconds, retry up to 3 times
- If navigation timeout → Retry with backoff

**Example Output:**
```json
{
  "posts_found": 75,
  "posts_analyzed": 75,
  "total_comments": 342,
  "total_text_chars": 500000,
  "posts": [
    {
      "title": "How to validate startup ideas",
      "body": "...",
      "top_comments": ["...", "..."],
      "score": 2500,
      "comment_count": 45
    }
  ]
}
```

---

## Step 3: Extract & Clean Text

**Input Gate:**
- Required: `posts_found` (number), `posts` (array)
- Validation: posts_found >= 30

**Agent Instructions:**
1. Concatenate all post titles, bodies, and comments into one text
2. Remove URLs and links (replace with [link])
3. Remove HTML entities (convert to text equivalents)
4. Remove markdown formatting symbols
5. Normalize whitespace (collapse multiple spaces)
6. Remove non-ASCII characters
7. Truncate to 5000 tokens maximum
8. Count final token count

**Output Gate:**
- Required: `text_content` (string), `token_count` (number)
- Validation: token_count > 500 AND token_count < 5000

**Error Handling:**
- If text_content empty → Fail with "No substantive content found"
- If token_count too low (<500) → Fail with "Insufficient content for analysis"
- If token_count too high (>5000) → Truncate and continue

**Example Output:**
```json
{
  "text_content": "How to validate startup ideas Finding qualified contractors is hard...",
  "token_count": 4200,
  "posts_count": 75,
  "comments_count": 342
}
```

---

## Data Quality Metrics

Agent should track and report:

| Metric | Target | Impact |
|--------|--------|--------|
| posts_found | >= 30 | Minimum corpus size |
| token_count | 500-5000 | LLM input constraints |
| text_chars | >5000 | Sufficient content |
| rate_limit_errors | 0-5 | Transient API issues |

---

## Cost Model

**Per execution:**
- Playwright navigation: Free (local execution)
- Page scraping: Free (no API)
- Reddit data: Free (official public data)
- Processing: Free (local text manipulation)
- **Total: €0.00**

---

## State Handoff

This skill produces state passed to `ai-analysis-engine`:

```json
{
  "phase": "reddit-data-pipeline",
  "status": "COMPLETE",
  "output": {
    "text_content": "...",
    "posts_count": 75,
    "tokens": 4200,
    "timestamp": "2026-06-13T20:00:42Z"
  }
}
```

The next skill validates this state against its input gate before proceeding.

---

## Failure Recovery

| Scenario | Recovery |
|----------|----------|
| Subreddit not found | Fail immediately |
| Fewer than 30 posts | Fail immediately (subreddit too niche) |
| Rate limited | Retry 3x with exponential backoff (1s, 2s, 4s) |
| Timeout | Retry 2x with 2s backoff |
| Text too short | Fail (insufficient content) |
| Text too long | Truncate to 5000 tokens, continue |

---

## References

See individual step files for detailed agent instructions:
- `references/step-01-validate.md`
- `references/step-02-fetch.md`
- `references/step-03-extract.md`

---

**Key principle:** This skill is pure specification. Agent reads markdown, follows instructions, produces JSON output.
