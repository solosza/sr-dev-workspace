# Build: Commit + Push Hub-Spoke Origin Strips

**Type:** BUILD
**Phase:** 1
**Depends on:** 003

## Commands

```bash
git -C "D:/my_ai_projects/isagawa-co.github.io" add styles.css vibe-coder.html attestation.html qa-platforms.html ssh-compliance.html story.html
git -C "D:/my_ai_projects/isagawa-co.github.io" commit -m "feat: add factory origin strip to all product pages

- Thin above-the-fold strip on 5 product pages: '← Built by the factory'
- Links back to index.html (the hub)
- Makes hub-spoke relationship visible to cold visitors
- Additive only — no changes to index.html
- CSS: .factory-origin added to styles.css

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git -C "D:/my_ai_projects/isagawa-co.github.io" push
```

## Acceptance Criteria
- [ ] `git add` exits 0
- [ ] `git commit` exits 0
- [ ] `git push` exits 0
