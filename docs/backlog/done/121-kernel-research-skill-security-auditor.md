# Research: Skill Security Auditor — Audit Third-Party Skills Before Installation

## Status
Open

## Priority
Medium-High — backlogs 115-118 evaluate 4 external skill sources (claude.ai agents spec, Superpowers, Anthropic frontend-design, systematic debugging). Each installs code that runs with full kernel access. No audit mechanism exists before installation.

## Summary
Third-party skills (`.claude/skills/`, `.claude/agents/`, MCP servers) execute with the same permissions as the kernel itself. Before installing any external skill, there should be a structured audit: what tools does it call, what files does it write, what external network calls does it make, does it conflict with existing kernel mechanisms? This backlog builds a `skill-security-auditor` that performs static analysis on a skill directory before it's added to the workspace.

## Requirements
- Define the audit surface: what does a skill consist of? (SKILL.md, markdown instructions, YAML frontmatter for agents, shell commands embedded in markdown)
- Build static analysis checks:
  - Tool inventory: which tools does the skill invoke? (Bash, Write, Edit, WebFetch, etc.)
  - Destructive pattern detection: `rm -rf`, `git reset --hard`, `force push`, credential access
  - Network call detection: WebFetch, WebSearch, MCP calls to external services
  - Kernel conflict detection: does it write to state files? Does it redefine kernel commands?
  - Model routing: does it specify a model? Does that conflict with run-task.sh routing?
- Output a structured audit report: PASS / WARN / FAIL per check, with remediation notes
- Integrate as a kernel command: `/kernel/audit-skill <path>` — callable before any skill installation
- Consider: should this run automatically as a pre-install hook when adding to `.claude/skills/`?

## References
- Backlogs 115-118: skills under evaluation (agents, Superpowers, frontend-design, debugging)
- Existing skill format: `.claude/skills/*/SKILL.md`
- Existing agent format: `.claude/agents/*.md` (YAML frontmatter)
- Kernel hooks: `.claude/hooks/sr_dev-gate-enforcer.py` (existing enforcement pattern)

## Task Builder Input
- **Deliverable:** A working `skill-security-auditor` — Python script + kernel command wrapper that audits a skill directory and produces a structured report
- **Location:** `workspace:lib/skill-auditor/` and `workspace:.claude/commands/kernel/audit-skill.md`
- **Scope:** RESEARCH
- **Constraints:** Research should cover feasibility, design options, and trade-offs before any build decision. Produce a design spec only if build is recommended.
