# Research: Artifact Versioning Strategy

## Status
Open

## Priority
High — without versioning, kernel drift across 18+ repos is invisible. Backlog 057 (sync all specs) is a one-time fix; versioning makes it sustainable.

## Summary
Design a versioning system for all Isagawa kernel artifacts: commands, skills, hooks, protocols, domain specs, and supporting infrastructure. The system must answer: what version is each artifact? Is this repo's kernel up to date? What changed between versions? The research should survey the current landscape (18 repos, no versioning), evaluate approaches (semver, hash-based, manifest files, git tags), and recommend a plan that works with the existing kernel workflow.

## Research Questions

1. **What needs versioning?**
   - Kernel commands (15 files)
   - Kernel skills (7 folders with sub-files)
   - Kernel hooks (6 files)
   - Domain specs (per-repo)
   - Protocols (per-repo)
   - Supporting infrastructure (run-task.sh, lib/common.sh, lib/attestation/)
   - CLAUDE.md template

2. **What versioning scheme fits?**
   - Semver (v1.2.3) — familiar, but heavy for individual files
   - Hash-based (content hash) — automatic, no manual bumping, but not human-readable
   - Manifest file (`kernel-manifest.json`) — single source of truth with versions per artifact
   - Git tags on the master kernel repo — version the kernel as a unit
   - Hybrid: kernel version (semver) + per-file content hashes

3. **How do repos detect drift?**
   - Manifest comparison: repo's manifest vs master's manifest
   - Content hash comparison: hash each file, compare to master hashes
   - Version field in each file's frontmatter
   - A `kernel-version` field in CLAUDE.md or session_state.json

4. **How does sync work with versioning?**
   - `domain-setup` could check kernel version and warn if outdated
   - A new command (`/kernel/sync` or `/kernel/upgrade`) could pull latest from master
   - Backlog 057's manual sync becomes automated

5. **What about domain-specific artifacts?**
   - Domain commands/skills are versioned separately from kernel
   - Protocol versions track independently
   - How to distinguish "kernel v2.1 + domain-healthcare v1.3"?

6. **What's the migration path?**
   - Current state: zero versioning
   - Step 1: add version to master kernel
   - Step 2: stamp each synced repo (backlog 057)
   - Step 3: add drift detection
   - Step 4: add automated sync

## References
- Backlog 057: `docs/backlog/057-kernel-refactor-sync-all-domain-specs.md` (the sync that motivates versioning)
- 18 repos inventoried in `docs/backlog/057-kernel-refactor-sync-all-domain-specs/repo-inventory.md`
- Existing attestation pipeline (intent.py, Sigstore) — could versioning piggyback on this?

## Task Builder Input
- **Deliverable:** Research report with versioning recommendation, migration plan, and proposed manifest schema
- **Location:** `subproject:kernel-architecture`
- **Scope:** RESEARCH
- **Constraints:** Must work with existing kernel workflow (session-start, anchor, learn). Must not require external tooling (no package managers). Should be simple enough to implement in one pipeline after the research is done.
