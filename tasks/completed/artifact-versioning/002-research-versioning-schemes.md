# Task 002: Research — Evaluate Versioning Schemes

## Objective
Evaluate candidate versioning schemes and recommend the best fit for kernel artifacts.

## Instructions

1. Read the artifact inventory from task 001 in `projects/kernel-architecture/artifact-versioning-report.md`
2. Evaluate each scheme against the kernel's constraints (no external tooling, works with session-start/anchor/learn):
   - **Semver (v1.2.3)** — familiar, human-readable, but requires manual bumping. Evaluate: per-file vs per-kernel-release
   - **Hash-based (content hash)** — automatic, no manual step, but not human-readable. Evaluate: SHA256 of each file
   - **Manifest file** — single `kernel-manifest.json` listing all artifacts + their versions/hashes. Evaluate: manifest-as-source-of-truth pattern
   - **Git tags on master kernel repo** — version the kernel as a unit. Evaluate: tag-per-release
   - **Hybrid** — kernel semver + per-file content hashes in manifest. Evaluate: best of both worlds
3. For each scheme, assess:
   - Automation potential (can it be zero-human-effort?)
   - Integration with existing workflow (session-start, anchor, domain-setup)
   - Readability (can a human glance at a repo and know if it's up to date?)
   - Complexity (how many moving parts?)
4. Write findings as `## 2. Versioning Scheme Evaluation` in the report
   - Include a comparison table: `| Scheme | Automation | Integration | Readability | Complexity | Verdict |`
   - State the recommended approach with rationale

## Acceptance Criteria
- At least 3 schemes evaluated with pros/cons
- Comparison table present
- Clear recommendation stated

## Gate
RESEARCH-02
