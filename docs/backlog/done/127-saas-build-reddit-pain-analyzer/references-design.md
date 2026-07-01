# References Design — Soft Constraints & Philosophy

This document defines soft constraints (guidance, best practices, philosophy) that guide agent behavior. Unlike gate contracts (hard enforcement), these are protocol-level recommendations.

---

## Core Philosophy

**Specification-driven execution:** The agent reads markdown specifications and executes them. There is no hidden code, no magic — only written instructions.

**Autonomy through transparency:** Every decision the agent makes is logged in state files. A user can inspect execution history anytime.

**State is truth:** All behavior flows from state files. If state says "step_2_complete", then step 2 is complete. No hidden flags or side effects.

**One subreddit, one analysis, one job:** Each call to `/reddit-pain/analyze` creates a single job_id. That job executes autonomously. State persists for later inspection.

---

## Soft Constraint: Data Quality Over Quantity

**Guidance:** When fetching Reddit posts, prefer quality over quantity.

**What this means:**
- Fetch top 50-100 posts (by score) rather than random posts
- Filter out spam (score < 10)
- Exclude stickied posts (moderator announcements)
- Include top 5 comments per post (signals what community values)

**Why:** Real pain points emerge from popular, highly-discussed posts. Rare or downvoted posts are noise.

**How to measure:**
- Pain point frequency (how many posts mention it?)
- Idea market scores (LLM confidence in market viability?)

---

## Soft Constraint: LLM Prompt Clarity

**Guidance:** When prompting LLMs, be explicit and structured.

**What this means:**
1. Provide full context (text, pain points, ideas)
2. Specify output format (JSON, array, object fields)
3. Give examples (show 2-3 examples of expected output)
4. Set bounds (scores 1-10, 5-10 ideas, etc.)

**Why:** Vague prompts → vague responses → gate contract failures → retries → cost overrun.

**How to measure:**
- First-try success rate (no retries needed?)
- API cost per step (below budget?)

---

## Soft Constraint: Error Transparency

**Guidance:** When something fails, log the full error context.

**What this means:**
- Record why each retry happened (invalid JSON? timeout? low quality?)
- Include full LLM response (for debugging)
- Store retry count per step
- Include timing (how long did this step take?)

**Why:** Failures reveal patterns. After 3 failed analyses of the same subreddit, maybe there's a systemic issue.

**How to measure:**
- Error log completeness (every error documented?)
- Patterns detected (same error repeated?)

---

## Soft Constraint: Cost Awareness

**Guidance:** Always prioritize cheaper models when quality allows.

**What this means:**
- Step 1 (pain points): Use Claude Haiku (€0.002/1K tokens) or GPT-4 mini
- Step 2 (ideas): Use Claude Haiku
- Step 3 (scoring): Use GPT-4 mini (slightly better quality for judgments)

**Why:** LLM costs dominate. Every €0.01 saved on cost = bigger margin. But not at expense of quality.

**How to measure:**
- Actual cost per analysis (target €0.10-0.12)
- Quality score feedback (do users like the ideas?)

---

## Soft Constraint: Retry Strategy

**Guidance:** Retry intelligently based on failure type.

**What this means:**
- Transient errors (timeout, rate limit): Retry 3x with exponential backoff
- Permanent errors (invalid subreddit): Fail immediately
- Quality errors (bad LLM output): Retry with refined prompt, max 3x
- Cost overruns: Hard stop (gate contract blocks)

**Why:** Some failures are fixable, others aren't. Retrying permanent errors wastes time and money.

**How to measure:**
- Retry ratio (retries / total attempts)
- Success rate after retries (do most attempts succeed?)

---

## Soft Constraint: State Hygiene

**Guidance:** Keep state files clean and immutable once written.

**What this means:**
1. Never modify past state (create new state objects)
2. Always append to action logs (never overwrite)
3. Timestamp every state transition
4. Version outputs (results-v1, results-v2 if re-run)

**Why:** Immutability preserves audit trail. User can replay job execution.

**How to measure:**
- State file size (should be < 100KB for single job)
- Action log completeness (every action recorded?)

---

## Soft Constraint: User Communication

**Guidance:** Give users clear status at every step.

**What this means:**
- `/reddit-pain/status [job-id]` returns human-readable progress
- Show which step is executing (e.g., "Fetching posts... 2m 15s elapsed")
- Show estimated time remaining (based on step timings)
- Show costs so far (transparent billing)

**Why:** Users hate uncertainty. Clear status reduces anxiety.

**How to measure:**
- Status accuracy (does "2m remaining" match actual time?)
- User satisfaction (do users wait or abandon?)

---

## Soft Constraint: Caching for Cost Savings

**Guidance:** Cache LLM responses for identical inputs.

**What this means:**
- If same subreddit analyzed twice → reuse pain points + ideas
- Cache key: SHA256(text_content)
- TTL: 7 days (content may change)
- Max size: 1GB

**Why:** Popular subreddits (r/entrepreneur, r/startups) get re-analyzed. Cache saves cost and time.

**How to measure:**
- Cache hit rate (percentage of analyses served from cache)
- Cost savings (lower average cost/analysis with cache)

---

## Soft Constraint: Graceful Degradation

**Guidance:** If analysis can't reach full quality, still return partial results.

**What this means:**
- If fewer than 100 posts available, use what's available (min 30 posts)
- If LLM fails on scoring but succeeds on ideas, return ideas anyway
- Mark partial results clearly ("limited analysis" flag)
- Explain why partial in results

**Why:** Better to give user something than nothing. Transparent about limitations.

**How to measure:**
- Partial analysis rate (how often does this happen?)
- User satisfaction (do partial results still provide value?)

---

## Soft Constraint: Learning from Failures

**Guidance:** Track failure patterns and update prompts/strategies accordingly.

**What this means:**
- After 3x failed analyses of same subreddit, investigate
- If LLM repeatedly fails JSON parsing, refine prompt format
- If cost consistently exceeds budget, switch to cheaper model
- Document lessons in protocol updates

**Why:** Harness improves with time. Each failure teaches something.

**How to measure:**
- Lessons documented (per problem type)
- Protocol updates (were lessons applied?)
- Failure rate trend (decreasing over time?)

---

## Soft Constraint: Monitoring & Alerting

**Guidance:** Actively monitor harness health.

**What this means:**
- Alert if 3+ analyses fail in a row (system issue?)
- Alert if average cost > €0.20/analysis (cost creep?)
- Alert if error rate > 10% (quality degradation?)
- Alert if Reddit API changes (old posts disappearing?)

**Why:** Proactive detection > reactive firefighting.

**How to measure:**
- Alert accuracy (true positives vs. false alarms?)
- Response time (how quickly do we detect issues?)

---

## Soft Constraint: Documentation as Specification

**Guidance:** This harness has NO hidden code. All behavior must be in markdown specifications.

**What this means:**
- Gate contracts: JSON (in gate-contracts.md)
- Skills: Markdown (reddit-data-pipeline.md, etc.)
- Commands: Markdown (commands-design.md)
- State schema: JSON examples (in specs)
- Error codes: Table (in gate-contracts.md)

**Why:** Specification = executable. Agent reads markdown, executes it. No interpretation layer.

**How to measure:**
- Code audit (zero Python/JavaScript in skills?)
- Spec completeness (every action documented?)

---

## Soft Constraint: Iterative Refinement

**Guidance:** The harness spec is version 1.0. Expect updates.

**What this means:**
- Track version in deliverables (v1.0, v1.1, etc.)
- Changes: Minor prompt tweaks, cost model updates, new validation rules
- Breaking changes: New skill structure, state schema changes
- Always backward-compatible when possible

**Why:** Real-world data changes. Strategies must adapt.

**How to measure:**
- Version adoption (are old jobs still supported?)
- Changelog completeness (every change logged?)

---

## Priority Matrix: Soft Constraint Trade-offs

When constraints conflict, prioritize in this order:

| Priority | Constraint | Why |
|----------|-----------|-----|
| 1 | Cost < €0.50 | Hard gate (economic viability) |
| 2 | No false errors | Trust (don't blame user for system issues) |
| 3 | Complete results | Value (user expects full analysis) |
| 4 | Speed (< 5 min) | UX (users wait) |
| 5 | Caching efficiency | Margin (nice-to-have) |

Example: If choosing between quality + slow vs. fast + mediocre → choose quality + slow.

---

## References for Further Context

- `harness-architecture.md` — How outer/inner loops coordinate
- `gate-contracts.md` — Hard constraints (mechanical enforcement)
- `reddit-data-pipeline.md` — Skill: data collection
- `ai-analysis-engine.md` — Skill: LLM analysis
- `results-processor.md` — Skill: output generation

---

**Key principle:** These are guidelines, not rules. Agent reads them, applies them as judgment, logs decisions in state.
