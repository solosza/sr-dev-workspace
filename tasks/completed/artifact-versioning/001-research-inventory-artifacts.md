# Task 001: Research — Inventory Artifacts That Need Versioning

## Objective
Catalog every kernel artifact type that needs versioning, with file counts and locations.

## Instructions

1. Read `docs/backlog/057-kernel-refactor-sync-all-domain-specs/repo-inventory.md` to get the list of 18+ repos
2. Read the master kernel in this workspace to inventory artifact types:
   - `.claude/commands/kernel/*.md` — count files
   - `.claude/skills/*/SKILL.md` — count skill folders
   - `.claude/hooks/*.py` — count files
   - `.claude/protocols/*.md` — count files
   - `lib/*.sh` and `lib/attestation/*.py` — count supporting infra files
   - `CLAUDE.md` — template
   - `run-task.sh`, `run-task-batch.sh` — shell scripts
3. For each artifact type, note:
   - How many files
   - Whether it's kernel-universal or domain-specific
   - How frequently it changes (estimate from git log)
   - Whether it's currently synced manually or not
4. Write findings to a scratch section at the top of `projects/kernel-architecture/artifact-versioning-report.md`
   - Section title: `## 1. What Needs Versioning?`
   - Include a table: `| Artifact Type | Count | Scope | Sync Status |`

## Acceptance Criteria
- Report section exists with artifact inventory table
- All artifact types from backlog 058 are covered (commands, skills, hooks, protocols, domain specs, infrastructure, CLAUDE.md)

## Gate
RESEARCH-01
