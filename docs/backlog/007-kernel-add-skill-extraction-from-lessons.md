# Add Skill Extraction from Mature Lessons

## Context
Competitive gap identified from ClawHub analysis (2026-03-22). ClawHub's "Self-Improving Agent" auto-generates reusable skills when a learning matures enough. Our `/kernel/learn` updates protocol and hooks, but never auto-generates new commands or skills from repeated patterns.

## Problem
When the same type of fix is applied multiple times, it should graduate from a lesson (passive knowledge) into a skill or command (active capability). Currently this promotion is manual.

## Requirements
- Detect when a lesson has been applied N times or matches a pattern
- Auto-generate a draft command/skill from the mature lesson
- User approval gate before adding to commands/
- Track which lessons have been promoted

## Source
- https://clawhub.ai/pskoett/self-improving-agent

## Task Builder Input
- **Deliverable:** Auto-generation logic in `/kernel/learn` that creates draft commands/skills from mature lessons, user approval gate before adding to commands/
- **Scope:** BUILD
- **Constraints:** Kernel repo. Depends on recurrence detection (backlog 008) to know when a lesson is "mature." User approval required before adding generated commands.
