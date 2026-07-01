# Results Processor — Skill Specification

## Identity

**Skill:** results-processor
**Purpose:** Validate AI analysis results and export as JSON + Markdown
**Input:** Scored startup ideas + pain points from ai-analysis-engine
**Output:** results.json + results.md files ready for user consumption
**Platform:** Agent reading state, validating schemas, writing files

---

## File Index

| File | Purpose |
|------|---------|
| `results-processor.md` | This file. Skill overview + step instructions |
| `references/step-01-validate.md` | Schema validation instructions |
| `references/step-02-store.md` | State persistence instructions |
| `references/step-03-export.md` | JSON and Markdown generation instructions |

---

## Overview

This skill has three sequential steps that an agent executes by reading markdown instructions:

1. **Step 1: Validate Results** — Check all data matches required schema
2. **Step 2: Store in State** — Persist results to state file
3. **Step 3: Export Deliverables** — Generate results.json and results.md

Each step has gate contracts.

---

## Step 1: Validate Results

**Input Gate:**
- Required: `pain_points` (array), `startup_ideas` (array), `scored_ideas` (array)
- Validation: All three arrays present and non-empty

**Agent Instructions:**

1. Validate `pain_points` array:
   - Must be array of strings
   - Length >= 5
   - All items non-empty

2. Validate `startup_ideas` array:
   - Must be array of objects
   - Length >= 5
   - Each object must have: title, description
   - All titles and descriptions non-empty

3. Validate `scored_ideas` array:
   - Must be array of objects
   - Length >= 5
   - Each object must have: title, score, reasoning
   - All scores numeric and in range [1, 10]
   - All reasoning non-empty

4. Cross-validate:
   - scored_ideas.length == startup_ideas.length
   - All scored_ideas.title values match startup_ideas.title values

5. Record validation timestamp

**Output Gate:**
- Required: `results_valid` (boolean), `validation_timestamp` (ISO 8601 string)
- Validation: results_valid is true

**Error Handling:**
- If any array missing → Fail with "Missing required data: [array names]"
- If array too small → Fail with "Insufficient ideas: need 5+, found X"
- If score out of range → Fail with "Invalid score X: must be 1-10"
- If fields missing → Fail with "Missing field: [field names]"

**Example Output:**
```json
{
  "results_valid": true,
  "validation_timestamp": "2026-06-13T20:02:45Z",
  "validated_pain_points": 10,
  "validated_ideas": 8,
  "validation_errors": []
}
```

---

## Step 2: Store in State

**Input Gate:**
- Required: `results_valid` (boolean), all validated data
- Validation: results_valid is true

**Agent Instructions:**

1. Load current harness state file
2. Create results object with structure:
```json
{
  "job_id": "[from current state]",
  "subreddit": "[from current state]",
  "timestamp": "[current ISO 8601]",
  "data": {
    "pain_points": [...],
    "startup_ideas": [...],
    "scored_ideas": [...]
  }
}
```

3. Write results to state file:
   - Path: `.claude/state/reddit-pain-analyzer_workflow.json`
   - Format: Valid JSON, indented with 2 spaces

4. Verify file written successfully

**Output Gate:**
- Required: `persisted` (boolean), `state_file_path` (string)
- Validation: persisted is true AND state file exists

**Error Handling:**
- If state file not found → Fail with "State file missing"
- If file write fails → Retry up to 2 times
- If JSON invalid → Fail with "Invalid JSON written"

**Example Output:**
```json
{
  "persisted": true,
  "state_file_path": ".claude/state/reddit-pain-analyzer_workflow.json",
  "bytes_written": 12500,
  "verification": "file readable and valid JSON"
}
```

---

## Step 3: Export Deliverables

**Input Gate:**
- Required: `persisted` (boolean), results object
- Validation: persisted is true

**Agent Instructions:**

### 3a. Generate results.json

1. Create JSON file with structure:
```json
{
  "metadata": {
    "job_id": "[UUID]",
    "harness": "reddit-pain-analyzer",
    "version": "1.0",
    "timestamp": "[ISO 8601]"
  },
  "input": {
    "subreddit": "[name]",
    "subreddit_url": "[full URL]"
  },
  "analysis_results": {
    "pain_points": [
      {
        "rank": 1,
        "description": "...",
        "frequency_percent": 45
      }
    ],
    "startup_ideas": [
      {
        "rank": 1,
        "title": "...",
        "description": "...",
        "market_potential_score": 8.5,
        "reasoning": "..."
      }
    ]
  },
  "cost_tracking": {
    "estimated_cost_euros": 0.18,
    "actual_cost_euros": 0.18
  },
  "execution": {
    "start_time": "[ISO 8601]",
    "end_time": "[ISO 8601]",
    "status": "COMPLETE",
    "errors": []
  }
}
```

2. Write to file: `results-[job_id].json`
3. Validate: File exists, is valid JSON, is readable

### 3b. Generate results.md

1. Create Markdown report with structure:
```markdown
# Reddit Pain Analysis Report

**Subreddit:** [Link to subreddit]
**Analyzed:** [Timestamp]
**Analysis ID:** [job_id]

---

## Summary

Analyzed **X posts** from [subreddit] to identify pain points and generate startup ideas.

| Metric | Value |
|--------|-------|
| Posts analyzed | X |
| Pain points identified | Y |
| Startup ideas generated | Z |
| Cost | €0.18 |

---

## Top 5 Pain Points

### 1. [Pain point title] (X%)

**Sentiment:** [positive/neutral/frustrated]
**Frequency:** X% of posts mention this

> "[Supporting quote from Reddit]"

**Context:** [Brief explanation]

---

## Startup Ideas

### Rank 1: [Idea title]

**Market Potential:** X/10

**Description:** [Full description]

**Solves pain points:** [List]

**Implementation:**
- Timeline: X weeks
- Difficulty: [Low/Medium/High]

---

[Additional ideas...]

---

## Cost Breakdown

[Cost table]

---

## How to Use These Results

[Usage guidance]

---

*Generated by Reddit Pain Analyzer Harness*
```

2. Write to file: `results-[job_id].md`
3. Validate: File exists, renders as valid Markdown, is readable

### 3c. Validate Consistency

1. Load both results.json and results.md
2. Verify:
   - Job ID matches in both files
   - Timestamps match
   - Pain point list matches
   - Idea list and scores match
   - No data divergence

**Output Gate:**
- Required: `files_created` (boolean), `json_path` (string), `markdown_path` (string)
- Validation: Both files exist, are readable, pass consistency check

**Error Handling:**
- If JSON file creation fails → Retry 2x
- If Markdown file creation fails → Retry 2x
- If files not consistent → Fail with "JSON/Markdown divergence detected"
- If either file not readable → Fail with "File accessibility error"

**Example Output:**
```json
{
  "files_created": true,
  "json_path": "results-uuid-123.json",
  "markdown_path": "results-uuid-123.md",
  "json_size_bytes": 12500,
  "markdown_size_bytes": 8900,
  "consistency_check": "PASSED",
  "timestamp_created": "2026-06-13T20:02:50Z"
}
```

---

## Output File Specifications

### results.json

- **Format:** Valid JSON (UTF-8, 2-space indent)
- **Size:** Typical 10-15KB
- **Schema:** See deliverables-design.md
- **Availability:** Machine-readable, can be piped to other tools

### results.md

- **Format:** Valid Markdown (GitHub-flavored)
- **Size:** Typical 8-12KB
- **Content:** Human-readable report with sections for pain points, ideas, costs, usage
- **Availability:** Shareable, printable, readable in browser

---

## State Handoff

This skill is the final phase. Output delivered to user:

```json
{
  "phase": "results-processor",
  "status": "COMPLETE",
  "deliverables": {
    "json": "results-[job_id].json",
    "markdown": "results-[job_id].md",
    "job_id": "[UUID]",
    "timestamp": "2026-06-13T20:02:50Z"
  }
}
```

---

## Quality Metrics

Agent should track:

| Metric | Target | Impact |
|--------|--------|--------|
| validation_success | 100% | Data quality gate |
| file_creation_success | 100% | Deliverable availability |
| consistency_check | PASSED | No divergence |
| json_size | 10-20KB | Reasonable payload |
| markdown_size | 8-15KB | Reasonable payload |

---

## Failure Recovery

| Scenario | Recovery |
|----------|----------|
| Validation fails | Fail immediately (fix input) |
| State file missing | Fail immediately (upstream issue) |
| File write fails | Retry 2x, then fail |
| JSON invalid | Fail with error message |
| Markdown invalid | Fail with error message |
| Files diverge | Fail and regenerate both |

---

## References

See individual step files for detailed instructions:
- `references/step-01-validate.md`
- `references/step-02-store.md`
- `references/step-03-export.md`

---

**Key principle:** This skill is pure specification. Agent reads markdown, validates data structures, writes JSON/Markdown files, ensures consistency.
