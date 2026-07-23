# Canonical Kernel — Publish as Single Source of Truth + Deprecate Sprawl

## Status
Open (blocked on 286)

## Priority
High — closes the source-of-truth gap. Once the canonical kernel is prod-tested (286), there must be exactly ONE published kernel everything tracks, and the 28 stale copies must stop being mistaken for current. Third and final of the kernel-consolidation chain.

## Summary
Publish the prod-tested canonical kernel (285 + 286) as the single `isagawa-co/isagawa-kernel`, consolidating the two stale Feb repos (`isagawa-kernel-a` v3, `isagawa-kernel-b`), and deprecate/archive the 28 stale kernel copies on the machine so no one confuses a pre-fix copy for current. Document the sync model so downstreams (domain-spec-factory, platforms) pull from the one canonical kernel instead of drifting.

## Requirements
- **Publish the one canonical:** push the prod-tested canonical to `isagawa-co/isagawa-kernel` as the single source of truth (a new consolidated repo, or re-point one of a/b — owner's call). Tag a clean version (e.g. `v4` — supersedes the Feb `v3`).
- **Consolidate a/b:** archive or redirect `isagawa-kernel-a` and `isagawa-kernel-b` to the one canonical (README pointer + archive) so the two-repo split ends.
- **Deprecate the sprawl:** enumerate the 28 stale kernel copies (the inventory from this session) and mark them deprecated — a DEPRECATED marker / README pointer to the canonical, or archive. Do NOT delete without owner confirmation (some are live projects with an embedded kernel).
- **Document the sync model:** how downstreams stay current — do factory/platforms vendor a pinned kernel version, submodule it, or re-run domain-setup from the canonical? Write the pull/update policy so drift can't silently recur (this is the root cause the whole session exposed).
- **Owner sign-off gate:** this is OUTWARD-FACING — it creates/re-points/archives PUBLISHED repos. The actual publish + any archival of published repos requires the owner's explicit go, AFTER 286 passes. Do not touch published repos autonomously.

## References
- Input: prod-tested canonical from [[285-kernel-build-canonical-kernel-extract-fixdelta]] + [[286-kernel-test-prodtest-canonical-kernel]]
- Published repos to consolidate: `isagawa-co/isagawa-kernel-a` (Feb v3), `isagawa-co/isagawa-kernel-b` (Feb)
- The 28 stale installs (this session's inventory): factory ×3, platform-ssh ×4, deepeval ×3, kernel-minimal, the `-master`/`-test` variants, etc.
- Ties to backlog 277 (spec-kit interop / standardization) + 278 (team scalability) — a single source of truth is a prerequisite for both

## Task Builder Input
- **Deliverable:** One published `isagawa-co/isagawa-kernel` (the prod-tested canonical, tagged), `a`/`b` consolidated into it, the 28 stale copies marked deprecated (not deleted without sign-off), and a written sync/pull policy for downstreams.
- **Location:** new-repo:isagawa-co/isagawa-kernel (+ ops across existing repos)
- **Scope:** BUILD
- **Constraints:** OUTWARD-FACING — publishing/archiving PUBLISHED repos requires owner sign-off, and runs ONLY after 286 passes. Do not delete any copy without explicit confirmation. STRICTLY SEQUENTIAL (last in chain). This is the fix for the drift that let 30 divergent kernels accumulate.
