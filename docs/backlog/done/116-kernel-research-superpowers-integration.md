# Research: Superpowers Framework — Kernel Integration

## Status
Open

## Priority
Medium — fills real gaps (TDD, git worktrees, code review) the kernel doesn't currently cover; worth evaluating before building equivalents from scratch

## Summary
Jesse Vincent's Superpowers package (`github.com/obra/superpowers`) is a 20+ skill framework for agentic coding including TDD, brainstorming, planning, code review, git worktree workflows, and subagent-driven development. The kernel has autonomous pipelines but no explicit TDD discipline, no structured code review skill, and the `EnterWorktree` tool is available but unused. Research determines whether to adopt, adapt, or ignore.

## Requirements
- Read the Superpowers README and skill list — what are the 20+ skills and what does each do?
- Assess the TDD skill specifically: does it add value over the kernel's existing test-task pattern?
- Assess the git worktree skill: how does it use worktrees, and how would this interact with the kernel's existing git workflow (`D:/my_ai_projects/isagawa-co.github.io`, feature branches per pipeline)?
- Assess the code review skill: how does it differ from what backlog 115 (@reviewer named agent) would provide?
- Identify any skills that would conflict with or duplicate kernel mechanisms (anchor, learn, lessons, gate contracts)
- Determine adoption recommendation: adopt as-is, adapt into kernel skill format, or skip

## References
- Superpowers repo: `https://github.com/obra/superpowers`
- Backlog 115: named agents research (includes @reviewer candidate)
- Current kernel test pattern: `tasks/*/NNN-test-*.md` task files via run-task.sh
- `EnterWorktree` tool available but unused in current workflow

## Task Builder Input
- **Deliverable:** Research report — skill-by-skill assessment of Superpowers, adoption recommendation, and (if recommended) a plan for integrating the top 1-3 skills into the kernel
- **Location:** `subproject:superpowers-research`
- **Scope:** RESEARCH
- **Constraints:** Must not duplicate kernel mechanisms. TDD and worktree skills are the priority; other skills are lower priority. If adoption is recommended, integration plan should use existing kernel skill format (`.claude/skills/` or `.claude/agents/`).
