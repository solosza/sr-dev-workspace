# Code Review Skill Assessment

**Skills:** requesting-code-review + receiving-code-review (Superpowers)
**Assessed against:** Kernel anchor Part B + @reviewer named agent concept (backlog 115)

---

## What the Superpowers Code Review Skills Do

### Requesting Code Review
1. **Obtain git SHAs** — `BASE_SHA` (start) and `HEAD_SHA` (end) to scope the review
2. **Dispatch reviewer subagent** — uses a `code-reviewer.md` template with placeholders: description of work, plan/requirements, base SHA, head SHA
3. **Act on feedback** — Critical (fix now), Important (fix before proceeding), Minor (document for later)

### Receiving Code Review
1. **READ → UNDERSTAND → VERIFY → EVALUATE → RESPOND → IMPLEMENT** — structured response pattern
2. **No performative language** — no "great point!", no gratitude, just technical evaluation
3. **Verify before implementing** — check feedback against actual codebase before acting
4. **Push back when warranted** — if suggestion breaks functionality, lacks context, or violates YAGNI
5. **Source-specific handling** — human partner vs external reviewer have different response patterns
6. **One fix at a time** — implement individually, test each

---

## Kernel's Current Review Mechanisms

### Anchor Part B (Inter-Anchor Work Review)
- Reviews all actions since last anchor against protocol
- Checks: naming conventions, architecture patterns, anti-patterns, quality gates
- Self-review by the same agent that did the work
- **Limitation:** agent reviews its own work — no fresh perspective

### Gate Contracts
- Mechanical verification at task completion
- file_exists, grep, run_code, run_test
- **Limitation:** structural checks only — doesn't evaluate code quality, design decisions, or missed edge cases

### What's Missing
- No dedicated reviewer with fresh context
- No git-SHA-scoped review (review specific changes, not entire codebase)
- No feedback triage system (Critical/Important/Minor)
- No structured pushback mechanism
- No two-stage review (spec compliance + code quality)

---

## Comparison: Superpowers vs @reviewer Named Agent

| Aspect | Superpowers Code Review | @reviewer Named Agent (backlog 115) |
|--------|------------------------|-------------------------------------|
| **Architecture** | Subagent dispatched per review | Named agent invoked via @-mention |
| **Context** | Git SHAs + plan/requirements template | Protocol + lessons preloaded, read-only tools |
| **Model** | Configurable (most capable for review) | Sonnet (pattern-matching sufficient) |
| **Scope** | Per-task in subagent-driven-development | On-demand or per-pipeline |
| **Tools** | Not specified (subagent inherits) | Read, Glob, Grep only (Write/Edit/Bash blocked) |
| **State mutation** | Not addressed | Explicitly none — read-only |
| **Feedback format** | Critical/Important/Minor triage | Unstructured (depends on prompt) |
| **Integration** | Tightly coupled with subagent-driven-development | Standalone, composable |

### Are They the Same Thing or Complementary?

**Complementary.** They solve different problems:

- **Superpowers code review** = a workflow pattern (when to review, how to dispatch, how to handle feedback). It's a *process*.
- **@reviewer named agent** = an implementation mechanism (a configured agent with specific model, tools, and permissions). It's a *thing*.

The Superpowers process could USE the @reviewer named agent as its implementation. The @reviewer needs the Superpowers process to know WHEN to activate and HOW to handle results.

---

## Pipeline vs On-Demand Usage

### As a Pipeline Task
- Run after each BUILD task in execute-pipeline
- Dispatch @reviewer with git diff of that task's changes
- Block next task until Critical/Important issues resolved
- **Pros:** catches issues early, prevents compounding
- **Cons:** adds latency per task, may be excessive for simple tasks

### As an On-Demand Command
- `/kernel/review` — invoke manually or at pipeline end
- Review all changes since last anchor or since pipeline start
- **Pros:** lower overhead, reviews in context
- **Cons:** issues compound before detection

### Recommendation
- **Per-pipeline review** (at pipeline end, not per-task) — review all changes from the pipeline as a batch
- **On-demand** for interactive work — user invokes when they want a check
- NOT per-task — too much overhead for the kernel's task granularity (one action per task)

---

## Recommendation: ADOPT (the process, implement via @reviewer)

### What to Adopt
1. **Git-SHA-scoped review** — review specific changes, not entire codebase. Superpowers' approach of using BASE_SHA/HEAD_SHA is correct.
2. **Feedback triage** — Critical/Important/Minor classification. Adopt this from Superpowers' requesting-code-review.
3. **Structured response** — VERIFY before implementing feedback. Adopt from receiving-code-review.
4. **No performative language** — already aligned with kernel style, but worth formalizing.

### What to Skip
1. **Two-stage review (spec + quality)** — overkill for kernel's current scope. One review pass is sufficient.
2. **Per-task review dispatch** — too granular for one-action-per-task atomicity.
3. **Subagent-driven-development workflow** — the full workflow is redundant with execute-pipeline. Just take the review piece.

### Integration Path
1. **Create @reviewer named agent** (backlog 115 already specifies this) — `.claude/agents/reviewer.md` with Read/Glob/Grep only, Sonnet model, protocol+lessons preloaded
2. **Add review template** — `.claude/references/code-review-template.md` with SHA scope, requirements, feedback triage format
3. **Wire into execute-pipeline** — optional review step at pipeline end (spawn @reviewer with git diff of all pipeline changes)
4. **Add `/kernel/review` command** — on-demand review invocation for interactive sessions
5. **Adopt feedback triage** — Critical (block), Important (fix before merge), Minor (document)
