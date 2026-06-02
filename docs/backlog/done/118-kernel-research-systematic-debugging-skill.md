# Research: Systematic Debugging Skill — Kernel Integration

## Status
Open

## Priority
Low-Medium — the kernel has `/kernel/fix` for kernel-level failures but no structured debugging methodology for general code bugs (Python, TypeScript, SQL, etc.) encountered during platform builds or client work

## Summary
The Superpowers package includes a 4-phase systematic debugging skill using Root Cause Analysis with component boundary logging. The claim is bug resolution in 15-30 minutes vs 2-3 hours of "chaotic guessing." The kernel's `/kernel/fix` command is scoped to kernel operation failures (hook violations, anchor issues); it doesn't prescribe a methodology for debugging application code. Research determines whether a general debugging skill would add value and where it would live.

## Requirements
- Read the systematic debugging skill from Superpowers — what are the 4 phases, what is "component boundary logging," and how is RCA applied?
- Compare to the kernel's existing `/kernel/fix` command — is there overlap or are these genuinely different scopes?
- Assess fit for the existing platform builds: when debugging Python pytest failures (hmsa-healthcare-qa), TypeScript Playwright failures (platform-playwright), or SSH compliance issues, would this skill change how the agent approaches the problem?
- Determine integration point: extend `/kernel/fix` to cover application code, create a new `/kernel/debug` command, or create a named agent `@debugger`?
- Identify whether this is better as a kernel skill (applies within pipelines) or a standalone agent (invoked ad-hoc when a bug is encountered)

## References
- Systematic debugging skill: `https://github.com/obra/superpowers` (part of Superpowers package)
- Current `/kernel/fix` command: `.claude/commands/kernel/fix.md`
- Existing QA platforms that encounter bugs: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa`, `D:/my_ai_projects/project_test_repos/isagawa-qa-platform`
- Backlog 115: named agents research (integration point question)
- Backlog 116: Superpowers integration (parent research)

## Task Builder Input
- **Deliverable:** Research report — assessment of the debugging skill, comparison to `/kernel/fix`, recommendation for integration point, and (if recommended) a design for the new skill or command
- **Location:** `subproject:systematic-debugging-research`
- **Scope:** RESEARCH
- **Constraints:** Must not duplicate or conflict with `/kernel/fix`. If a new command or agent is recommended, design must fit the kernel's existing command/skill format. Should be evaluated against real debugging scenarios from existing platform work.
