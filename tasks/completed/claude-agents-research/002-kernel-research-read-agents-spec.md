# Research: Read and Summarize Claude Agents Spec

## Context
The Claude agents spec (agents.md in the Anthropic Claude Code docs) defines how named agents work — YAML frontmatter, tool restrictions, model routing, auto-delegation, and isolation model. This is the primary source of truth for the integration research. Must be read before any integration assessment can be made.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/claude-agents-research/` exists

## Requirements
- Search for the official Claude agents spec documentation (search for "Claude Code agents.md named agents YAML frontmatter" or check anthropic.com/docs/claude-code)
- Document: YAML frontmatter fields (model, tools, description, system)
- Document: tool restriction mechanism — how does specifying `tools:` limit what the agent can do?
- Document: model routing — how does an agent specify which model it uses?
- Document: auto-delegation — what triggers it, how does it work, can it be disabled?
- Document: isolation model — does a named agent get a fresh context window? Does it inherit the parent session's state?
- Document: global vs project placement (`.claude/agents/` vs `~/.claude/agents/`) — what's the difference?
- Document: invocation methods — @-mention, auto-delegation, explicit `claude --agent`
- Note any gaps, ambiguities, or undocumented behaviors found during research

## Acceptance Criteria
- [ ] `projects/claude-agents-research/agents-spec-summary.md` exists
- [ ] File covers YAML frontmatter fields (grep: "model:\|tools:\|frontmatter")
- [ ] File covers auto-delegation (grep: "auto.del\|delegation\|@-mention")
- [ ] File covers isolation model (grep: "isolat\|context window\|inherit")
- [ ] File covers placement options (grep: "global\|project\|~/.claude\|.claude/agents")

## Gates Satisfied
- DOC-02, DOC-03, DOC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
