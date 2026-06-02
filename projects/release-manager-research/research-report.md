# Release Manager Research — Final Report

## Executive Summary

The isagawa-co.github.io site deploys via raw git push with no release management. This report assesses the gap, designs a kernel integration, and evaluates standalone product viability.

**Recommendation:** Build `/kernel/release` as a kernel command. Skip standalone product.

---

## 1. Current Release Gap

The isagawa site (111 commits, 27 static files, GitHub Pages) has no formal release process:

| Capability | Status |
|-----------|--------|
| Changelog | Missing — commit messages are the only record |
| Version tags | Missing — `git tag -l` returns empty |
| Smoke test | Missing — broken CSS/nav/links reached production multiple times |
| Rollback | Ad hoc — no tagged states, no documented procedure |
| Branch cleanup | Missing — 19 stale local branches |
| Pre-deploy review | Partial — PRs exist but not enforced |

**Impact:** Bad deployments (broken CSS, dead links, layout shifts) were caught manually via follow-up fix commits. No automated detection. No prevention gate.

**Highest-risk gap:** Smoke test. Everything else is process improvement; the smoke test is the only thing that prevents broken deployments from persisting.

---

## 2. Kernel Integration Design

### `/kernel/release` Command

A new kernel command that wraps the release workflow:

```
verify clean state -> smoke test -> compute version -> generate changelog -> tag -> push
```

**9-step flow:**

| Step | Action | Gate |
|------|--------|------|
| 1 | Verify on `main`, clean working tree | Hard block |
| 2 | Verify remote is up to date | Hard block |
| 3 | Run smoke test (HTTP 200 on all pages) | Hard block |
| 4 | Compute next version from last tag | Auto |
| 5 | Generate changelog from conventional commits | Auto |
| 6 | Append to CHANGELOG.md | Auto |
| 7 | Create annotated tag | Auto |
| 8 | Push tag to remote | Confirmation |
| 9 | Clean up merged branches | Auto |

**Changelog approach:** Auto-generate from conventional commits (`feat:`, `fix:`, etc.). The repo already uses this prefix convention. `feed:` commits (automated attestation updates) are excluded by default.

**Rollback:** Revert-based (not force-push). Find previous tag, create revert commits, push to main, smoke test the rollback.

**Integration with execute-pipeline:** Start manual, graduate to automatic. Phase 1: invoke `/kernel/release` after pipeline completion. Phase 2: add `release_after_pipeline: true` flag.

### What This Catches That Current Pipelines Miss

Current pipelines push code and stop. No verification that the deployed site works. The `/kernel/release` smoke test would catch:

- Pages returning non-200 (broken HTML, missing files)
- CSS not loading (broken stylesheets)
- Navigation failures (dead links)
- JavaScript errors (broken interactivity)

These are the exact failures visible in the commit history — every `fix:` commit after a `feat:` commit is a deployment that went live with a bug.

---

## 3. Standalone Product Assessment

### Market Analysis

- **Target:** GitHub Pages users who want release management without switching to Netlify/Vercel
- **Size:** ~50-100K "serious" GitHub Pages sites; ~2,500-5,000 would potentially pay
- **Revenue ceiling:** $12,500-50,000/month (best case); $500-1,500/month (likely case)

### Competition

Netlify, Vercel, and Cloudflare Pages all provide release management (preview deploys, rollback, deploy logs) as part of their hosting. They're free-tier and better than anything we'd build for GitHub Pages.

The only reason users stay on GitHub Pages is: it's free, it's simple, or it's organizationally required. Users who value "free" won't pay for tooling. Users who value "required" might — but that's a tiny segment.

### Existing Tools

`release-drafter`, `semantic-release`, `lighthouse-ci` — pieces exist but nobody has assembled them for GitHub Pages. However, assembling them is a GitHub Action away, not a product.

### Distribution

Best channel: GitHub Action (Marketplace visibility, zero install). But even as a GitHub Action, the addressable market is too small for a revenue-generating product.

---

## 4. Two-Track Recommendation

### Track A: Kernel Integration — BUILD

**Verdict: BUILD `/kernel/release` as a kernel command.**

Rationale:
- Solves Isagawa's own deployment problem (eat your own dog food)
- Smoke test is the single highest-value addition to the deployment workflow
- Fits naturally into the kernel command model (command → hook enforcement → state tracking)
- Low effort: one command file, one smoke test script, changelog generation from existing commit conventions
- Immediate ROI: prevents the broken deployments visible in the commit history

**Priority:** Medium. Not blocking any revenue or customer work, but prevents quality regressions on the public-facing site. Build after current research batch completes.

**Next steps:**
1. Create backlog item for `/kernel/release` command
2. Implement smoke test (HTTP 200 check on all pages via curl or Playwright)
3. Implement changelog generation from conventional commits
4. Implement version tagging
5. Test on isagawa-co.github.io

### Track B: Standalone Product — SKIP

**Verdict: SKIP building a standalone release manager product.**

Rationale:
- Market too small (2,500-5,000 potential customers)
- Free alternatives exist (switch to Netlify/Vercel)
- GitHub could ship this themselves
- Revenue ceiling too low to justify the maintenance burden
- Time better spent on kernel and RT automation

**Exception:** If `/kernel/release` works well internally, extract the smoke test + changelog logic as a free, open-source GitHub Action for visibility/credibility. Not a product — a marketing asset.

---

## 5. Priority and Concrete Next Steps

1. **Now:** Complete this research (this report)
2. **Next sprint:** Create backlog item `XXX-kernel-release-command` with tasks:
   - Build `/kernel/release` command (`.claude/commands/kernel/release.md`)
   - Build smoke test script (curl-based HTTP 200 checks on all site pages)
   - Build changelog generator (parse conventional commits since last tag)
   - Build version tagging logic (semver auto-increment)
   - Test on isagawa-co.github.io
   - Integrate with execute-pipeline (optional `release_after_pipeline` flag)
3. **Later:** Extract smoke test + changelog as open-source GitHub Action (free)

**Estimated effort:** 1 pipeline run (task-builder decomposition + run-task.sh execution). The command is straightforward — mostly Bash/Git operations wrapped in a kernel command structure.
