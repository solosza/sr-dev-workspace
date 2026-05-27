# Multi-Model Routing — Task Index

**Backlog:** docs/backlog/087-kernel-research-multi-model-routing.md
**Type:** BUILD
**Location:** workspace:lib/

## Tasks

| # | Task | Type | Description |
|---|------|------|-------------|
| 001 | Create model-routing-config.json | BUILD | Routing config with tier definitions, keywords, task-type mappings |
| 002 | Create model-router.sh | BUILD | Shell function that reads task file and returns model ID |
| 003 | Edit run-task.sh — integrate router | BUILD | Call router before spawning claude -p, pass --model flag |
| 004 | Edit run-task.sh — add retry-on-upgrade | BUILD | If gate fails on cheaper model, retry with next tier |
| 005 | Validate routing logic | TEST | Test router returns correct model for different task types |
| 006 | Commit | BUILD | Commit all changes |
