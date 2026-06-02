# Kernel Integration Design — Release Manager

## Release Workflow

```
feature branch → PR → merge to main → /kernel/release → tag + changelog + smoke test
```

### Flow Detail

1. **Development** — work on feature branch, test locally
2. **PR** — merge to main via PR (existing pattern, keep it)
3. **Release gate** — invoke `/kernel/release` from the sr_dev workspace
   - Runs smoke test against live site
   - Auto-generates changelog entry from commits since last tag
   - Creates version tag (semver)
   - Optionally pushes tag to remote
4. **Verification** — smoke test confirms deployment is healthy

## `/kernel/release` Command Design

### Inputs
- **repo** — path to the GitHub Pages repo (default: `D:/my_ai_projects/isagawa-co.github.io`)
- **version** — optional explicit version; if omitted, auto-increment patch

### Steps

| Step | Action | Gate |
|------|--------|------|
| 1 | Verify on `main` branch, clean working tree | Hard block if dirty |
| 2 | Verify remote is up to date (`git fetch && git diff origin/main`) | Hard block if diverged |
| 3 | Run smoke test (HTTP checks on live pages) | Hard block if any page returns non-200 |
| 4 | Compute version from last tag (or `v0.1.0` if no tags exist) | Auto |
| 5 | Generate changelog from conventional commits since last tag | Auto |
| 6 | Append to CHANGELOG.md | Auto |
| 7 | Create annotated tag (`git tag -a vX.Y.Z -m "..."`) | Auto |
| 8 | Push tag to remote (`git push origin vX.Y.Z`) | Requires confirmation |
| 9 | Clean up merged branches (local only) | Auto |

### Implementation

The command would be a new kernel command at `.claude/commands/kernel/release.md` that:
- Reads the target repo path
- Executes the steps above via Bash
- Updates workflow state with release metadata
- Records the release in the attestation feed (if applicable)

## Changelog Approach

**Recommendation: Auto-generate from conventional commits.**

The repo already uses conventional commit prefixes (`feat:`, `fix:`, `feed:`, `refactor:`). Auto-generation groups commits by type:

```markdown
## v0.2.0 (2026-06-01)

### Features
- add Platform Database to qa-platforms page (65d58c6)
- add terminal demo section to AutoApply page (2d51500)

### Fixes
- terminal grows per line, scrolls only when full (3ae8f1d)
- story.html terminal — static, scrollable, async/await animation (ca62c69)
```

**Why not manual notes?** The site is deployed by pipelines and the kernel agent. Manual notes add friction that will be skipped. Auto-generation from commits is zero-friction and always up to date.

**Edge case: `feed:` prefix.** These are automated attestation count updates. They should be grouped separately or filtered out of the changelog (they're noise). The `/kernel/release` command should exclude `feed:` commits from the changelog by default.

## Rollback Procedure

### For GitHub Pages (static site)

GitHub Pages serves whatever is on `main`. Rollback = revert `main` to the last known-good tag.

```bash
# Option A: Revert specific commits (preserves history)
git revert HEAD~N..HEAD
git push origin main

# Option B: Reset to last tag (clean but destructive)
git reset --hard vX.Y.Z
git push --force origin main
```

**Recommendation: Option A (revert) as default.** Force-push destroys history and requires elevated permissions. Revert is safer and auditable.

### Automated Rollback via `/kernel/release rollback`

| Step | Action |
|------|--------|
| 1 | Find previous tag (`git describe --tags --abbrev=0 HEAD~1`) |
| 2 | Show diff between current and previous tag |
| 3 | Confirm with user (rollback is destructive) |
| 4 | Create revert commits for all commits between tags |
| 5 | Push to main |
| 6 | Run smoke test to verify rollback worked |
| 7 | Tag the rollback as `vX.Y.Z-rollback` |

## Additive vs. Required — Recommendation

### Question: Should `/kernel/release` be part of execute-pipeline or manual?

**Recommendation: Start manual, graduate to pipeline.**

**Phase 1 (now):** `/kernel/release` is a standalone command invoked after pipeline completion. The pipeline builds and pushes code; the human (or agent) decides when to cut a release. This avoids coupling release cadence to pipeline frequency.

**Phase 2 (later):** Add an optional `release_after_pipeline: true` flag to execute-pipeline. When set, the pipeline auto-invokes `/kernel/release` after successful completion. This is appropriate once smoke tests are reliable and the workflow is proven.

**Rationale:**
- Site deployments happen on every push to main (GitHub Pages). The "release" is really about tagging + changelog, not deployment.
- Pipelines that update feed counts (`feed: update attestation count`) shouldn't trigger a release — they're operational, not feature releases.
- Manual invocation lets the user batch multiple pipeline outputs into one release.

### Minimum Addition That Prevents Broken Deployments

The single highest-value addition is the **smoke test**. Everything else (changelog, tags, branch cleanup) is process improvement. The smoke test is the only thing that prevents broken deployments from staying broken.

**Minimum viable release manager:**
1. Smoke test (HTTP 200 on all pages) — run after every push to main
2. Version tags — tag after smoke test passes
3. Everything else is nice-to-have

This could be implemented as a PostToolUse hook on `git push` commands targeting the site repo, or as a standalone command.
