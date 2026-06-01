# Kernel Integration — Named Agents for On-Demand Interactive Use

## Status
NEW — no named agents currently exist in .claude/agents/

## Context
The kernel has pipelines for autonomous batch execution (run-task.sh). What it lacks is on-demand, single-invocation agents for interactive work that doesn't warrant a full pipeline — "check this commit before I push," "write the PR description," "scan for secrets before deploy."

## Candidate Agents to Create

### @reviewer
- Trigger: after any edit to isagawa-co.github.io, platform repos, or workspace files before committing
- Tools: Read, Grep, Glob, Bash (git diff only)
- Model: claude-sonnet-4-6 (cheaper, focused task)
- Output: CRITICAL / WARNING / INFO issues, ready for immediate action
- Kernel concern: does it need to follow anchor/learn? Probably not for a stateless reviewer

### @pr-writer
- Trigger: before any `git push` or PR creation
- Tools: Read, Grep, Glob, Bash (git log, git diff only)
- Model: claude-sonnet-4-6
- Output: PR description in the standard commit format used in this workspace
- Value: currently written manually every commit

### @security
- Trigger: before any deploy or push to public repos (isagawa-co.github.io)
- Tools: Read, Grep, Glob, Bash (grep -rn for secrets)
- Model: claude-sonnet-4-6
- Output: security report with file + line for each issue

### @doc-writer (lower priority)
- Trigger: after adding new skills, commands, or protocols
- Tools: Read, Grep, Glob, Write
- Output: updated documentation

## Design Questions
- Should these agents be in `.claude/agents/` (this workspace only) or `~/.claude/agents/` (global, available in all repos)?
- Should the `@reviewer` agent be aware of the kernel protocol (read CLAUDE.md)? Or should it be intentionally stateless (no kernel overhead)?
- Does auto-delegation create any risk? If the user says "review this" during a pipeline run, could Claude auto-route to @reviewer mid-pipeline, conflicting with state?

## What to Produce
- Draft agent files for @reviewer, @pr-writer, @security
- Decision on `.claude/agents/` vs `~/.claude/agents/` placement
- Notes on whether kernel hooks apply

## Dependencies
- agents-spec-research.md (need to understand isolation model before writing agents)
