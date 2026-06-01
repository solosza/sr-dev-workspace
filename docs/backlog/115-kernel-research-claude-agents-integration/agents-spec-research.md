# Agents Spec Research — `.claude/agents/` YAML Frontmatter

## Status
NEW — no prior research on this spec

## Research Questions
- What fields does the YAML frontmatter support? (`name`, `description`, `model`, `tools` — are there others: `temperature`, `max_tokens`, `context`, `system`?)
- Does the `description` field affect auto-delegation — does Claude read it to decide when to route to the agent?
- What happens to kernel hooks (PreToolUse, PostToolUse) when a named agent runs? Does it inherit the parent session's hooks, or does it get a fresh environment?
- Does a named agent read the project's CLAUDE.md? Or is it governed entirely by its own system prompt?
- What is the isolation model — does the named agent share context with the parent session, or is it a clean fork?
- What tools can be restricted? Can you restrict to Read-only, or specific tool subsets? Does Bash restriction work?
- What models are supported in the `model` field? Does it accept model aliases or only full model IDs?
- Is `~/.claude/agents/` truly global (all projects) vs `.claude/agents/` (project-only)?
- What is the `/agents` command — is it a UI for managing agents, or also an invocation mechanism?
- How does auto-delegation interact with the kernel's existing hook enforcement? If a user says "review this code," could Claude auto-delegate to `@reviewer` even if an anchor is pending?

## What to Produce
- Complete field reference for the YAML frontmatter spec
- Isolation model diagram: what the named agent inherits vs what it doesn't
- Governance assessment: does named agent run fall under kernel hooks or bypass them?
- Comparison table: named agent vs Agent tool vs run-task.sh (`claude -p`)

## Dependencies
- Claude Code documentation / source inspection
- Empirical testing if documentation is incomplete
