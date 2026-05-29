# Build: Commit + Push Nav Unification

**Type:** BUILD
**Phase:** 1
**Depends on:** 005

## Commands

```bash
git -C "D:/my_ai_projects/isagawa-co.github.io" add styles.css index.html feed.html attestation.html qa-platforms.html ssh-compliance.html vibe-coder.html story.html
git -C "D:/my_ai_projects/isagawa-co.github.io" commit -m "feat: unified nav across all pages — Products dropdown, remove on-page anchors

- All 7 pages: consistent nav (Home, Feed, Attestation, Products dropdown, counter)
- Products dropdown: QA Platforms, SSH Compliance, Vibe Coder
- Removed on-page anchors (Seed, Growth, etc.) from global nav
- Per-page active indicators in dropdown
- Dropdown CSS + keyboard/aria JS added to styles.css and all pages
- Research: Pipeline 106 — every multi-product reference site uses this pattern

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git -C "D:/my_ai_projects/isagawa-co.github.io" push
```

## Acceptance Criteria
- [ ] `git add` exits 0
- [ ] `git commit` exits 0
- [ ] `git push` exits 0
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" log --oneline -1` shows the nav commit
