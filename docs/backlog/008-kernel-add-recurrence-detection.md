# Add Recurrence Detection to Learning System

## Context
Competitive gap identified from ClawHub analysis (2026-03-22). ClawHub's "Self-Improving Agent" tracks pattern-key + recurrence count per learning. Our lessons don't track how often the same issue recurs, so we can't identify systemic problems vs one-off mistakes.

## Problem
Without recurrence tracking, we can't distinguish a lesson triggered once from one triggered 10 times. Recurring issues signal that the lesson or hook isn't preventing the root cause — the fix needs to go deeper.

## Requirements
- Add pattern-key or fingerprint to each lesson
- Track recurrence count per lesson
- Alert/escalate when a lesson recurs above threshold
- Feed recurrence data into tiered memory decay (backlog item 042) and skill extraction (backlog item 043)

## Source
- https://clawhub.ai/pskoett/self-improving-agent

## Task Builder Input
- **Deliverable:** Pattern-key + recurrence count per lesson, alert/escalate on threshold, integration with tiered decay (backlog 006) and skill extraction (backlog 007)
- **Scope:** BUILD
- **Constraints:** Kernel repo. Should be implemented before 007 (skill extraction needs recurrence data to determine maturity).
