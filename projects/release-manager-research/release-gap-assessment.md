# Release Gap Assessment — isagawa-co.github.io

## Current Deployment Method

The site deploys via **direct git push to `main`** on a GitHub Pages repo (`isagawa-co.github.io`). There is:

- **No CI/CD pipeline** — no `.github/workflows/` directory exists
- **No build step** — the repo is static HTML/CSS/JS served directly by GitHub Pages
- **No staging environment** — changes go straight to production on merge/push
- **No automated testing** — no smoke tests, no link checkers, no visual regression

Deployment happens two ways:
1. **Feature branches -> PR -> merge** — used for larger features (13+ PRs visible in history)
2. **Direct push to main** — used for feed updates, small fixes, and pipeline-driven deployments (e.g., `feed: update attestation count` commits)

## Repository Stats

- **111 total commits** across all branches
- **19 local feature branches** (most merged, not cleaned up)
- **27 files** at top level (flat structure, no subdirectories)
- **Custom domain**: www.isagawa.co via CNAME

## Specific Gaps

### 1. Changelog — MISSING
No CHANGELOG.md exists. No structured release notes. Commit messages are the only record of what changed, and they vary in quality:
- Good: `feat: add Platform Database to qa-platforms page`
- Minimal: `feed: update attestation count` (repeated 5+ times)
- No grouping of related changes into releases

### 2. Version Tags — MISSING
`git tag -l` returns empty. No semantic versioning, no release markers. Impossible to answer "what version is deployed?" or "what changed since the last release?"

### 3. Smoke Test — MISSING
No post-deployment verification. After a push to main, there is no automated check that:
- Pages load (HTTP 200)
- CSS loads correctly
- Navigation links work
- JavaScript doesn't throw errors
- Custom domain resolves

### 4. Rollback Capability — AD HOC ONLY
Rollback is possible via `git revert` or `git reset`, but:
- No documented rollback procedure
- No tagged "known good" states to roll back to
- No one-command rollback mechanism
- With 111 commits and no tags, finding the right commit to revert to requires manual log reading

### 5. Branch Cleanup — MISSING
19 local feature branches remain after merging. Several remote branches are also stale (already merged). No branch hygiene policy.

### 6. Pre-deployment Review — PARTIAL
PRs exist for some changes (13 visible merge commits), but many changes are pushed directly to main. No required review policy. No PR template. No checklist.

## What a Bad Deployment Looks Like

Based on the commit history, the site has experienced:
- **CSS not loading properly** — multiple `fix:` commits for layout shifts, spacing, nav issues
- **Broken navigation** — several rounds of nav refactoring (hamburger -> pill nav -> fixes)
- **Layout breaks** — `fix: fixed-height terminal to prevent layout shift during animation`
- **Dead links** — `fix: replace dead rekor href in story.html with honest pending state`

These were caught manually and fixed with follow-up commits. An automated smoke test would catch most of these.

## Gap Summary

| Capability | Status | Risk Level |
|-----------|--------|------------|
| Changelog | Missing | Medium — no release history |
| Version tags | Missing | High — no rollback targets |
| Smoke test | Missing | High — broken deploys reach production |
| Rollback | Ad hoc only | High — slow, error-prone |
| Branch cleanup | Missing | Low — cosmetic |
| Pre-deploy review | Partial (PRs exist but not enforced) | Medium |
| Build/CI pipeline | Missing | Low — static site, no build needed |
| Staging environment | Missing | Medium — no preview before production |
