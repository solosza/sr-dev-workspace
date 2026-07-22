# Design Doc Completeness Checklist

<!-- Payload of: command-skill-pattern/index.md -->

Every design doc MUST include these sections before moving to implementation. Capture them while the design is fresh. They map directly to the 6 layers and are required for the skill build phase.

## Required Sections (7)

| # | Section | What It Contains | Maps To |
|---|---------|------------------|---------|
| 1 | Skill Identity | Who the agent is when running this command. One sentence role. | Layer 2 |
| 2 | Philosophy | 3-5 guiding principles that govern decisions during execution | Layer 2 |
| 3 | Vocabulary | Domain terms used in this command (avoids ambiguity during execution) | Layer 2 |
| 4 | Critical Rules | Hard constraints the agent must never violate | Layer 2 |
| 5 | Workflow Summary | Step table with Responsibility + Output + HITL columns | Layer 2 |
| 6 | Step Specs | Per-step: Purpose, Procedure (minimum). Full: + Input, Output, Acceptance Criteria, Verification, Failure Recovery | Layer 3 |
| 7 | File Structure | Full `.claude/` tree showing every file the skill will create | All layers |

## Optional Sections (5)

| # | Section | What It Contains | Maps To |
|---|---------|------------------|---------|
| 8 | Reference Frontmatter | Per-reference: artifact_type, related_step, purpose, source, canonical_hash | Layer 4 |
| 9 | INDEX.md Structure | Wikilink format, organized by step and by artifact type | Layer 4 |
| 10 | Contract Definitions | Per-step: validation rules, mechanical checks, canonical reference pointers | Layer 5 |
| 11 | State Persistence | What gets saved for resume, where it lives, what triggers save | State |
| 12 | Hook Specs | Mechanical validations that need hard gate enforcement | Layer 6 |

## Why Now, Not Later

These details are hardest to reconstruct after the design conversation ends. The design doc is the spec that the build phase reads. If it's missing sections, the build phase will guess, and guesses cause drift.

## Minimum Depth

- Identity: at least one sentence describing the agent's role
- Philosophy: at least 3 principles
- Vocabulary: at least 3 terms defined
- Critical rules: at least 2 rules
- Workflow: at least 2 steps with all columns filled
- Step specs: each step has at minimum Purpose + Procedure
- File structure: shows at least skills/ directory tree
