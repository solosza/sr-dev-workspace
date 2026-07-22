# Build /kernel/summarize Command — Dynamic Summarization Loop

## Status
Open

## Priority
High — every completed agent produces output that sits unread until user manually asks; closes the visibility gap between completion and review

## Summary
Build a `/kernel/summarize` command that reads completed agent output (backlog + tasks + deliverables + agent state), diffs deliverables against backlog requirements, and produces a dynamic summary with decision flags. Works as both a standalone command and integrated into the agent completion flow (auto-fires from `/kernel/complete`, feeds summaries into review-queue). Summaries are dynamically sized — they capture everything relevant, not a fixed line count. May surface discussion points and produce follow-up backlogs.

## Requirements
- **Dynamic sizing** — summary scales with output complexity. 10 findings = 10 findings shown. 15 files created = 15 files listed. No artificial compression.
- **Requirement diffing** — reads backlog requirements, checks each against deliverable. Per-requirement status: met (with file path), partial (with notes), not addressed.
- **Decision flags** — two categories: "decisions needed" (recommendations requiring human choice) vs "informational" (facts, completions, findings).
- **Deliverable inventory** — lists all files created/changed with paths and brief descriptions.
- **Problem surfacing** — failures, skips, blockers, anything that needs attention.
- **Discussion mode** — summary may invite follow-up discussion. If user responds with direction, can produce follow-up backlogs via `/kernel/backlog`.
- **Standalone loop** — works as independent command:
  - `/kernel/summarize 188` — summarize backlog 188's output
  - `/kernel/summarize projects/ssh-*` — summarize a project folder
  - `/kernel/summarize` — summarize all unreviewed completions
- **Integrated mode** — `/kernel/complete` calls it automatically for one-shot agents. Summary written to review-status.json entry.
- **Review-queue integration** — when reviewing an item, review-queue shows the summary instead of requiring user to read raw output.
- **Input sources** — reads: backlog file (what was asked), task folder (what was planned), deliverable (what was produced), agent state (what happened).

## Design Requirement
**Use `/design` command before building.** This command has multiple integration points (complete, review-queue, standalone) and needs careful interface design before task decomposition.

## References
- Review-queue skill: `.claude/skills/review-queue/`
- Complete command: `.claude/commands/kernel/complete.md`
- Agent state files: `.claude/state/agent-*-state.json`
- Review status: `.claude/state/review-status.json`
- Discussion that produced this: user requested auto-summary on agent completion, standalone loop, dynamic sizing, requirement diffing, decision flags

## Task Builder Input
- **Deliverable:** `/kernel/summarize` command + summarize skill + integration into complete + integration into review-queue
- **Location:** workspace:.claude/commands/kernel/summarize.md and .claude/skills/summarize/
- **Scope:** BUILD
- **Constraints:** Must use /design command first. Must not break existing complete or review-queue flows. Dynamic sizing means no hardcoded line limits. Must handle both research (reports) and build (code) deliverables.
