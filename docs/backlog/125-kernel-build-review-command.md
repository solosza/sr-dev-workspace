# Build /kernel/review Command and @reviewer Named Agent

## Status
Open

## Priority
Medium — the kernel has no dedicated reviewer with fresh context. Anchor Part B is self-review by the agent that did the work. Gate contracts catch structural issues only. Code quality, design decisions, and missed edge cases fall through both.

## Summary
Research (backlog 116, superpowers-research/code-review-assessment.md) confirmed the gap and recommended adopting the Superpowers code review process implemented via a @reviewer named agent. The review pattern: git-SHA-scoped diff, feedback triage (Critical/Important/Minor), structured response (VERIFY before implementing), no performative language, push back when warranted. Integration point: per-pipeline review at pipeline end + on-demand `/kernel/review` command for interactive sessions.

## Requirements
- Create `.claude/agents/reviewer.md` — named agent with Read/Glob/Grep tools only (Write/Edit/Bash blocked), Sonnet model, protocol + lessons preloaded in system prompt
- Create `.claude/references/code-review-template.md` — SHA-scoped review request format, requirements context, feedback triage structure (Critical/Important/Minor)
- Create `.claude/commands/kernel/review.md` — on-demand review command that captures BASE_SHA + HEAD_SHA, dispatches @reviewer, handles feedback triage
- Add optional review step to execute-pipeline — after all tasks complete, spawn @reviewer with git diff of all pipeline changes; Critical/Important issues block completion; Minor issues are documented
- Wire feedback triage into `/kernel/complete` — if `/kernel/review` was invoked and Critical issues remain open, complete is blocked

## References
- Research assessment: `projects/superpowers-research/code-review-assessment.md`
- Superpowers source: `https://github.com/obra/superpowers`
- Current self-review: `.claude/commands/kernel/anchor.md` Part B
- Named agents spec: backlog 115 (claude-agents-research)
- Execute pipeline skill: `.claude/skills/execute-pipeline/SKILL.md`

## Task Builder Input
- **Deliverable:** Working `/kernel/review` command + @reviewer agent + code-review-template reference + optional execute-pipeline integration
- **Location:** `workspace:.claude/agents/`, `workspace:.claude/commands/kernel/`, `workspace:.claude/references/`
- **Scope:** BUILD
- **Constraints:** @reviewer must be read-only (no Write/Edit/Bash). Review step in execute-pipeline must be OPTIONAL — must not break existing pipelines that don't use it. Feedback triage must use exactly Critical/Important/Minor. SHA-scoped review (not whole codebase). Do not duplicate Anchor Part B — this supplements it with a fresh-context reviewer.
