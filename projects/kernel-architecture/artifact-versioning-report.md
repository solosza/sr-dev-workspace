# Artifact Versioning Strategy — Research Report

## Executive Summary

The Isagawa kernel has grown to 15 commands, 7 skills, 6 hooks, and supporting infrastructure — deployed across 18+ repos with zero versioning. Repos range from Tier 1 (near-current) to Tier 4 (legacy/pre-standard), with drift invisible until manual inspection. This report recommends a **hybrid versioning approach**: semver for the kernel as a unit, content hashes per artifact in a manifest file, with drift detection at session-start. The migration path is 5 steps, starting with a manifest in the master workspace and ending with automated sync.

---

## 1. What Needs Versioning?

### Master Kernel Artifact Inventory

| Artifact Type | Count | Scope | Sync Status | Change Frequency |
|---------------|-------|-------|-------------|-----------------|
| Commands (`.claude/commands/kernel/*.md`) | 15 | Kernel-universal | Manual copy | Medium — new commands added every 2-3 weeks |
| Skills (`.claude/skills/*/`) | 7 folders (30+ files) | Kernel-universal | Manual copy | Low — skills stabilize after creation |
| Hooks (`.claude/hooks/*.py`) | 6 | Kernel-universal | Manual copy | Medium — hooks evolve with lessons |
| Protocol (`.claude/protocols/*.md`) | 1 per repo | Domain-specific | Never synced | High — changes with every domain-setup |
| CLAUDE.md | 1 | Kernel-universal (template) | Manual copy | Medium — updated when commands/skills change |
| Shell scripts (`run-task.sh`, `run-task-batch.sh`) | 2 | Kernel-universal | Manual copy | Low — stable after initial build |
| Lib (`lib/common.sh`) | 1 | Kernel-universal | Manual copy | Low |
| Attestation (`lib/attestation/*.py`) | 6 | Kernel-universal | Manual copy | Low — stable after 049 fix |
| Lessons (`.claude/lessons/*.md`) | 14+ files | Kernel-universal | Never synced | High — grows with every failure |
| State templates (`.claude/state/*.json`) | 2 | Kernel-universal (schema) | Implicit | Low — schema rarely changes |
| Domain commands | Varies | Domain-specific | N/A | Varies per domain |
| Domain skills | Varies | Domain-specific | N/A | Varies per domain |
| Domain specs | Varies | Domain-specific | N/A | Varies per domain |

**Total kernel-universal artifacts:** ~65 files across 7 categories
**Total domain-specific artifacts:** Varies per repo (3-15 files typically)

### Repo Tier Distribution

| Tier | Repos | Kernel Completeness | Drift Level |
|------|-------|-------------------|-------------|
| Tier 1: Recent | domain-spec-factory, hmsa-healthcare-qa | 60-70% of master | Moderate |
| Tier 2: Medium | game-dev, healthcare-qa-spec-master, platform-deepeval | 30-40% of master | High |
| Tier 3: Old | cognitive-agent, isagawa-qa-zentyant, platform-playwright, platform-selenium, test-content-production, test-kernel-bootstrap, test-platform-deepeval | 10-20% of master | Critical |
| Tier 4: Legacy | isagawa-kernel, isagawa-kernel-a/b, py_sel_framework_mcp, qa_kernel_test | <10% of master | Total (pre-standard) |

**Key finding:** No repo has 100% of master. Even Tier 1 repos are missing 5+ commands and 1-2 hooks. The drift is cumulative — every kernel improvement since a repo's last sync increases the gap.

---

## 2. Versioning Scheme Evaluation

### Candidate Schemes

### A. Semver (v1.2.3)

Version the entire kernel as a release unit. Each breaking change bumps major, new features bump minor, fixes bump patch.

- **Pros:** Human-readable, familiar, works with git tags, communicates scope of change
- **Cons:** Requires manual version bumps, doesn't tell you WHICH files changed, per-file granularity lost
- **Automation:** Low — someone must decide major/minor/patch
- **Integration:** Medium — can store in CLAUDE.md or state, check at session-start
- **Readability:** High — "kernel v2.3.1" is instantly meaningful

### B. Hash-Based (Content Hash)

SHA256 each artifact file. Store hashes in a manifest. Drift = any hash mismatch.

- **Pros:** Fully automatic, no manual bumping, per-file granularity, detects any change
- **Cons:** Not human-readable ("is abc123 newer than def456?"), no semantic meaning
- **Automation:** High — compute hashes on any change
- **Integration:** High — hash comparison is trivial
- **Readability:** Low — requires tooling to interpret

### C. Manifest File (`kernel-manifest.json`)

Single JSON file listing all artifacts with metadata (path, hash, version, category).

- **Pros:** Single source of truth, combines per-file tracking with manifest-level versioning, machine-readable
- **Cons:** One more file to sync, manifest itself can drift
- **Automation:** High — manifest is generated, not hand-edited
- **Integration:** High — any command can read and compare manifests
- **Readability:** Medium — structured but requires reading JSON

### D. Git Tags on Master Repo

Tag each kernel release in sr_dev_workspace. Repos store which tag they synced from.

- **Pros:** Built into git, no additional files, links to commit history
- **Cons:** Requires git operations, repos don't always have remote access, doesn't track per-file changes
- **Automation:** Medium — tagging can be scripted but requires git
- **Integration:** Low — requires git access at session-start
- **Readability:** High — "synced from v2.3.1" is clear

### E. Hybrid (Recommended)

Kernel semver (v1.2.3) as the release identifier + per-file content hashes in a manifest. The manifest IS the version — if your manifest matches master's, you're current.

- **Pros:** Human-readable version + per-file precision, automatic hash computation + semantic version bumps, single manifest file contains everything
- **Cons:** Slightly more complex than pure semver or pure hash
- **Automation:** High — hashes are automatic, semver bump is the only manual step (and can be scripted with change-type detection)
- **Integration:** High — manifest comparison at session-start
- **Readability:** High — "kernel v2.3.1, 3 files outdated" tells you everything

### Comparison

| Scheme | Automation | Integration | Readability | Complexity | Verdict |
|--------|-----------|-------------|-------------|------------|---------|
| Semver | Low | Medium | High | Low | Too coarse — doesn't show which files drifted |
| Hash-based | High | High | Low | Low | Too opaque — can't tell if drift matters |
| Manifest | High | High | Medium | Medium | Good foundation but needs version identity |
| Git tags | Medium | Low | High | Low | Too dependent on git, doesn't work offline |
| **Hybrid** | **High** | **High** | **High** | **Medium** | **Recommended — best of semver + hash** |

### Recommendation

**Hybrid approach: kernel semver + per-artifact content hashes in `kernel-manifest.json`.**

The manifest serves dual purposes:
1. **Identity:** "This repo runs kernel v2.3.1"
2. **Precision:** "These 3 specific files are outdated"

---

## 3. Drift Detection

### Detection Approaches

**Approach A: Manifest Comparison**

Each repo has its own `kernel-manifest.json`. Compare it to master's:
```
Master manifest: { "version": "2.3.1", "commands/anchor.md": "sha256:abc..." }
Repo manifest:   { "version": "2.2.0", "commands/anchor.md": "sha256:def..." }
→ Drift: kernel version outdated (2.2.0 < 2.3.1), anchor.md content differs
```

- **Trigger:** session-start (check once per session)
- **Output:** Warning with file-level diff summary
- **Domain handling:** Domain artifacts have `category: "domain"` — excluded from kernel drift check

**Approach B: Content Hash Spot-Check**

Hash local files on-the-fly, compare to expected hashes stored in local manifest:
```
local_hash = sha256(read(".claude/commands/kernel/anchor.md"))
expected = manifest["commands/anchor.md"]["hash"]
if local_hash != expected: drift detected (local file modified outside sync)
```

- **Trigger:** anchor (periodic integrity check)
- **Output:** Integrity warning — local files may have been hand-edited
- **Purpose:** Catches unauthorized local modifications, not version drift

### Recommended Detection Mechanism

**Two-layer detection:**

1. **Version drift** (session-start): Compare `manifest.version` to known master version. If outdated, warn:
   ```
   KERNEL DRIFT DETECTED
   Local: kernel v2.2.0 (synced 2026-03-15)
   Master: kernel v2.3.1 (released 2026-04-20)

   Outdated artifacts: 5
   - commands/anchor.md (hash mismatch)
   - commands/execute-pipeline.md (hash mismatch)
   - hooks/universal-gate-enforcer.py (hash mismatch)
   - skills/task-builder/references/step-07-plan-review.md (hash mismatch)
   - CLAUDE.md (hash mismatch)

   Run /kernel/sync to update.
   ```

2. **Integrity check** (anchor, optional): Hash local files vs local manifest. Catches local edits that bypass sync:
   ```
   INTEGRITY CHECK
   Modified locally (not from sync):
   - commands/learn.md (local hash differs from manifest)

   This may be intentional (domain customization) or accidental.
   ```

**Domain exclusion:** Manifest entries with `"category": "domain"` are never flagged as kernel drift. Domain artifacts version independently.

---

## 4. Sync Workflow Integration

### Integration Points

**1. session-start (version check)**
- Read local `kernel-manifest.json`
- Compare `manifest.version` to a known master version (stored in manifest itself as `master_version_url` or cached)
- If outdated: emit warning (non-blocking)
- Changes required: Add 3-5 lines to session-start command
- Network: Not required if master version is cached locally from last sync

**2. `/kernel/sync` (new command)**
- Reads master manifest (from master repo path or cached location)
- Compares per-file hashes
- Copies updated files from master to local repo
- Updates local manifest
- Reports what changed
- Changes required: New command (~50 lines) + new skill with sync logic
- Network: Requires access to master repo (local filesystem path, not network)

**3. domain-setup (stamp version)**
- After creating protocol and hooks, domain-setup stamps the kernel version:
  ```json
  { "kernel_version": "2.3.1", "domain_version": "1.0.0", "synced_from": "sr_dev_workspace" }
  ```
- Changes required: Add manifest generation step to domain-setup skill (step 10 or 11)

**4. anchor (integrity spot-check, optional)**
- Every N anchors, hash a random sample of kernel files
- Compare to manifest hashes
- Catches unauthorized local modifications
- Changes required: Add optional check to anchor command Part A

### Workflow Diagram

```
Session Start
    │
    ├─ Read kernel-manifest.json
    │   ├─ Version matches master? → proceed normally
    │   └─ Version outdated? → WARN: "kernel v2.2.0, master is v2.3.1"
    │                              └─ User can run /kernel/sync
    │
    ▼
Work Loop (anchor every 20 actions)
    │
    ├─ [Optional] Integrity spot-check during anchor
    │   └─ Hash sample files vs manifest → warn if local edits found
    │
    ▼
/kernel/sync (user-invoked)
    │
    ├─ Read master kernel-manifest.json
    ├─ Compare per-file hashes
    ├─ Copy changed files from master
    ├─ Update local manifest (version + hashes)
    └─ Report: "Updated 5 files, kernel now at v2.3.1"
```

### Implementation Priority

| Priority | Integration Point | Effort | Dependencies |
|----------|------------------|--------|--------------|
| 1 | Create `kernel-manifest.json` in master | Small | None |
| 2 | Stamp version in domain-setup | Small | Manifest exists |
| 3 | Version check in session-start | Small | Manifest exists in repos |
| 4 | `/kernel/sync` command | Medium | Manifest exists everywhere |
| 5 | Integrity spot-check in anchor | Small | Manifest exists |

---

## 5. Domain-Specific Artifact Versioning

### Kernel vs Domain Distinction

| Category | Examples | Versioned By | Sync Source |
|----------|----------|-------------|-------------|
| **Kernel** | commands/kernel/*.md, skills/*, hooks/*.py, CLAUDE.md, lib/*, run-task.sh | Master manifest | sr_dev_workspace |
| **Domain** | protocols/*.md, domain commands, domain skills, domain specs | Domain manifest | Per-repo (no sync) |
| **Hybrid** | CLAUDE.md (has kernel template + domain sections) | Both | Kernel template synced, domain sections preserved |

### Dual-Version Notation

Each repo carries two version identifiers:

```
kernel@2.3.1 + domain@1.0.0
```

In the manifest:
```json
{
  "kernel_version": "2.3.1",
  "domain_version": "1.0.0",
  "domain_name": "hmsa_healthcare_qa"
}
```

- **Kernel version** — tracks which master release this repo synced from
- **Domain version** — tracks domain-specific changes (protocol updates, domain commands added)
- **Domain version bumping** — automatic: increment patch on every domain-setup or learn that modifies domain files

### Edge Cases

**Domain skill wrapping a kernel command:**
- The skill file is domain-scoped (versioned under domain)
- The kernel command it wraps is kernel-scoped
- If the kernel command changes, the domain skill may need updating — drift detection should flag this as "kernel dependency changed"

**Protocol referencing both kernel and domain patterns:**
- Protocol is always domain-scoped
- But it references kernel patterns (naming conventions, quality gates)
- Solution: Protocol includes a `kernel_patterns_version` field indicating which kernel version's patterns it was built against

**Vanilla kernel repos (no domain):**
- `domain_version` is `null` or `"0.0.0"`
- Only `kernel_version` matters
- These are the simplest case — pure kernel sync

### Domain Specs from Spec-Factory

Domain specs produced by spec-factory carry their own version:
```json
{
  "spec_name": "ssh-image-testing",
  "spec_version": "1.0.0",
  "built_with_factory_version": "1.2.0",
  "kernel_version_at_build": "2.3.1"
}
```

This creates a three-tier version chain: `kernel@2.3.1 + factory@1.2.0 + spec@1.0.0`. The factory version matters because factory improvements may produce better specs.

---

## 6. Migration Path

### Current State
- 18+ repos, zero versioning
- No manifests
- Sync is manual file-by-file copy
- Drift is invisible until someone manually inspects

### Migration Steps

**Step 1: Create Master Manifest** (Small effort, no dependencies)
- Write `kernel-manifest.json` in sr_dev_workspace
- Include: kernel version (start at v1.0.0), all kernel artifact paths with SHA256 hashes
- Compute hashes automatically via a Python script
- This is the bootstrap step — everything else depends on it

**Step 2: Stamp Repos During Backlog 057 Sync** (Medium effort, depends on Step 1)
- When syncing each repo (backlog 057), also copy the manifest
- Update the manifest's `synced_timestamp` and `synced_from` fields
- Each repo now knows what version it has
- This is a natural fit — 057 already touches every repo

**Step 3: Add Drift Detection to Session-Start** (Small effort, depends on Step 1)
- Add manifest version check to session-start command
- Non-blocking warning only (repos still work if outdated)
- Can be added to master kernel before 057 executes — repos get it during sync

**Step 4: Build `/kernel/sync` Command** (Medium effort, depends on Steps 1-3)
- New command + skill that automates what 057 does manually
- Reads master manifest, compares, copies changed files, updates local manifest
- Makes future syncs a single command instead of a manual process
- This is a separate backlog item (post-058)

**Step 5: Add Integrity Spot-Check to Anchor** (Small effort, depends on Step 1)
- Optional periodic hash verification during anchor
- Catches unauthorized local edits
- Low priority — implement after the core versioning is working

### Dependencies

```
Step 1 (master manifest)
  ├── Step 2 (stamp repos via 057)
  ├── Step 3 (drift detection in session-start)
  │     └── Step 4 (/kernel/sync command)
  └── Step 5 (integrity spot-check)
```

Steps 2, 3, and 5 can run in parallel after Step 1. Step 4 depends on Step 3 (sync should include drift detection output).

### Bootstrap Problem

**Problem:** Repos synced before Step 1 have no manifest. How do they get one?

**Solution:** The `/kernel/sync` command (Step 4) handles this:
1. If local manifest exists → compare and update
2. If no local manifest → generate one from current local files, then compare to master
3. The "generate from local" path creates a manifest with `kernel_version: "0.0.0"` (pre-versioning), then immediately shows drift against master

For repos synced during 057 (Step 2), the manifest comes along with the sync. For repos synced before 057, the `/kernel/sync` command bootstraps them.

---

## Recommendation

**Adopt the hybrid approach:**
1. Kernel semver (`v1.0.0`) for human-readable release identity
2. Per-artifact content hashes in `kernel-manifest.json` for precise drift detection
3. Domain versioning as a separate track (`domain@1.0.0`)
4. Manifest comparison at session-start for drift awareness
5. `/kernel/sync` command for automated updates

**Start with Step 1** — create the master manifest in this workspace. It's small effort, no dependencies, and unlocks everything else. Step 2 integrates naturally with backlog 057 (sync all specs). Steps 3-5 are kernel enhancements that can be individual backlog items.

## Open Questions

1. **Version bump policy:** Should kernel version bumps be manual (developer decides major/minor/patch) or automated (script detects change type)? Recommendation: automated with override.
2. **Lessons sync:** Should lessons.md be synced across repos? Currently it's never synced. Lessons are workspace-specific (different repos encounter different problems), but kernel-level lessons (RULE ZERO) apply everywhere.
3. **Breaking changes:** How to handle a kernel change that breaks existing domain commands? Need a compatibility check or migration script in `/kernel/sync`.
4. **Offline master access:** Should each repo cache the master manifest, or always read from the filesystem path? Recommendation: cache locally, refresh on sync.

## Next Steps

1. **Backlog item:** Create manifest generation script + initial `kernel-manifest.json` (Step 1)
2. **Integrate with 057:** Add manifest stamping to the sync process (Step 2)
3. **Backlog item:** Build `/kernel/sync` command (Step 4) — separate from 057
4. **Backlog item:** Add drift detection to session-start (Step 3) — can ship with or after sync
