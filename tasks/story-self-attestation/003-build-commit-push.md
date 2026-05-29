# Build: Commit + Push story.html Fix

**Type:** BUILD
**Phase:** 1
**Depends on:** 002

## Goal

Commit and push the verify link fixes to `D:\my_ai_projects\isagawa-co.github.io`.

## Commands

```bash
git -C "D:/my_ai_projects/isagawa-co.github.io" add story.html
git -C "D:/my_ai_projects/isagawa-co.github.io" commit -m "fix: replace dead rekor href in story.html with honest pending state

- Section 6 verify link: href=\"#\" → href=\"#attestation-pending\"
- Footer: add Pipeline 105 pending entry
- Terminal: update rekor line to show unsigned state
- Pipeline 105 attestation bundle exists but unsigned (sign to activate)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git -C "D:/my_ai_projects/isagawa-co.github.io" push
```

## Acceptance Criteria
- [ ] `git add` exits 0
- [ ] `git commit` exits 0
- [ ] `git push` exits 0
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" log --oneline -1` shows the fix commit
