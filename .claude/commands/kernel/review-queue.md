# /kernel/review-queue

Track human review and acceptance of completed pipeline work.

## Usage

```
/kernel/review-queue
/kernel/review-queue [backlog-number]
/kernel/review-queue --stats
```

| Argument | Purpose | Example |
|----------|---------|---------|
| (none) | Present next unreviewed item | `/kernel/review-queue` |
| `[number]` | Review specific backlog | `/kernel/review-queue 185` |
| `--stats` | Show review statistics only | `/kernel/review-queue --stats` |

## What It Does

Discovers unreviewed completed pipeline work by diffing `docs/backlog/done/` against `.claude/state/review-status.json`. Presents items in priority order with quick actions: accept, iterate, reject, skip, defer. Iteration creates follow-up backlogs via `/kernel/backlog` with parent linking.

## Instructions

1. Read and follow: `.claude/skills/review-queue/SKILL.md`
2. Execute steps 1-5 sequentially, reading each step file before executing

## Skill Reference

> `.claude/skills/review-queue/`
