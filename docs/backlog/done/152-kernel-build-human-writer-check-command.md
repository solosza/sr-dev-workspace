# Build /kernel/human-check Command — AI Tell Detection

## Status
Open

## Priority
High — User has repeatedly corrected AI tells in human-authored content (resume, LinkedIn, site copy). Every document that represents the user must read as human-written.

## Summary

Build a `/kernel/human-check` command that scans any text file for AI writing patterns and flags them for removal. The command follows the canonical command-skill-pattern from hmsa-healthcare-qa. Everything the user publishes (resume, LinkedIn, site copy, emails, cover letters) must appear human-authored. No em dashes, no AI hedge words, no formulaic structures.

## Design Reference

Architecture follows: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/design.md`

6-layer pattern: Command → Skill → Steps → References → Contracts → Hooks

## Requirements

- **Command:** `.claude/commands/kernel/human-check.md` — user invokes `/kernel/human-check [file-path]` or `/kernel/human-check [inline text]`
- **Skill:** `.claude/skills/human-check/SKILL.md` — orchestrates the check pipeline
- **Detection categories (minimum):**
  - Em dashes (unicode \u2014) — flag every occurrence
  - AI hedge words: "arguably", "notably", "it's worth noting", "it's important to", "in conclusion", "overall", "essentially", "fundamentally", "leveraging", "utilizing", "facilitate", "comprehensive", "robust", "cutting-edge", "innovative", "game-changing", "transformative", "seamless", "streamlined", "holistic"
  - Formulaic sentence starters: "In today's...", "When it comes to...", "It goes without saying...", "At the end of the day..."
  - Passive voice overuse (flag if >20% of sentences)
  - Triple adjective stacking ("comprehensive, robust, and scalable")
  - Colon-list patterns ("There are three key benefits: first... second... third...")
  - Exclamation marks in professional prose
  - "Delve", "dive into", "deep dive", "unpack", "unlock"
  - Emoji in professional documents (unless explicitly requested)
  - Oxford comma inconsistency (flag mixed usage)
  - Overly parallel structure (every paragraph starts the same way)
- **Output:** Report with line numbers, flagged text, category, and suggested fix
- **Exit code:** Non-zero if any AI tells found (enables hook integration)
- **Contract:** Mechanical validations for regex-checkable patterns (em dashes, specific words)
- **Hook integration:** Optional PreToolUse hook that checks .md files before write in designated paths (resume, cover letters)

## References

- Command-skill-pattern: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/design.md`
- User corrections this session: em dashes in LinkedIn, "agents that follow the rules, every time" flagged as debunkable, resume tone mismatches with isagawa.co
- isagawa.co tone: factual, technical, declarative fragments, no inflated claims

## Task Builder Input
- **Deliverable:** `/kernel/human-check` command with skill, steps, references, contracts, and optional hook
- **Location:** workspace:.claude/commands/kernel/, .claude/skills/human-check/
- **Scope:** BUILD
- **Constraints:** Must follow command-skill-pattern from hmsa-healthcare-qa design doc. Detection patterns must be regex-based where possible for mechanical validation. Must work on any .md file.
