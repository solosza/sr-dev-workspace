# Task 005: Extend anchor.md Step 10 with Rolling Ledger Schema

**Type:** BUILD
**Gates Satisfied:** AC-05

## Action

Edit `.claude/commands/kernel/anchor.md` (ONE file): extend Step 10's context schema with the `ledger` array, add the rolling-window rule, and add the `compaction_anchor_reason` clear to Step 14.

## Spec

READ anchor.md fully first (RULE ZERO) — it has the 244 routing section; place edits without disturbing it.

1. **Step 10 schema** — extend the `context` JSON example with:

```json
"ledger": [
  { "ts": "ISO timestamp", "kind": "decision | failure | constraint", "summary": "one sentence", "refs": ["file or task"] }
]
```

Schema per backlog 245 (flat entries, NOT the per-cycle variant from the research doc — the backlog wins). Add rules text:
- Append entries during Step 10 for the just-completed anchor cycle: decisions made (with the alternative rejected), FAILED attempts (what was tried, what happened, what was done instead), constraints discovered
- Rolling window: keep the most recent 5 entries per kind at most 15 total — truncate oldest first
- Perfunctory entries ("task completed per spec") are a violation — if nothing notable happened, append nothing
- Design source: Candidate A in `projects/kernel-rolling-summarization-research/02-gap-analysis-and-design.md` (Candidate B rejected)

2. **Step 14** — add: also set `compaction_anchor_reason: null` and leave `compaction_timestamp` as-is (diagnostics distinguish compaction-triggered from timer-triggered anchors; the PreCompact hook sets the reason).

## Acceptance Criteria (mechanical)

- grep anchor.md: `"ledger"` in Step 10 schema block
- grep: `decision | failure | constraint` (the kind enum)
- grep: rolling window text (`most recent 5` or `rolling window`)
- grep: `compaction_anchor_reason` in Step 14
- 244 routing section (`State File Routing (KERNEL_AGENT_ID)`) still present and unchanged
