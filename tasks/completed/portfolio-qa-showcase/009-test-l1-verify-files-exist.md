# 009 — L1: Verify All Files Exist

**Type:** TEST
**Depends on:** 003, 004, 005

## Goal
Structural verification — confirm all deliverable files exist on the feature branch.

## Requirements
Run these checks:
```bash
git -C "D:/my_ai_projects/isagawa-co.github.io" checkout feature/showcase-qa-platforms
test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"
test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.css"
test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.js"
grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/index.html"
grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/attestation.html"
grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"
```

## Acceptance Criteria
- [ ] All 3 new files exist (html, css, js)
- [ ] All 3 existing pages have qa-platforms nav link
