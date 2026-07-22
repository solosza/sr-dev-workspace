# Gate Contract - 250 Portfolio Scaffold + Pages Deploy

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PF-01 | Repo at D:/my_ai_projects/portfolio-site, git initialized, main branch | run_code | 001 | git status clean after commit |
| PF-02 | index.html: semantic sections with ids about/isagawa/evidence/case-study/selected-work/resume/contact + nav anchor links to each (guide section 2); theme per section 14 (one accent, body max-width 760-980px, readable without JS); OG metadata + browser title per section 14 | grep + html parse | 002 | all ids + nav hrefs present; no JS required for content |
| PF-03 | Public GitHub repo created via gh CLI under the logged-in account; remote wired; pushed | run_code (gh) | 003 | gh repo view returns; git push clean |
| PF-04 | GitHub Pages enabled (main branch root or /docs) via gh api | run_code (gh api) | 004 | pages status shows built/building |
| PF-05 | L1: no kernel-internal vocabulary in the repo (hook names, state file names, command protocols); no absolute claims ('100%%', 'guaranteed', 'unbypassable', 'zero drift'); real name present (not YOUR NAME placeholder) | run_test | 005 | greps clean |
| PF-06 | L3 GATE: live *.github.io URL returns HTTP 200 and contains the hero title + all 7 nav anchors (Pages builds can take minutes - poll up to 10 min) | run_test | 006 | live 200 + content asserts |

## Rules
- READ the guide sections 1, 2, 14 fully before writing HTML (RULE ZERO)
- Name/contact from profile.json - never placeholders in shipped copy
- gh CLI for repo + Pages (check gh auth status first; if not authenticated, report BLOCKED with the exact state - do not attempt interactive login)
- Static only: no package.json, no CDN-pulled assets (machine registry block), system font stack
- Any red: fix then /kernel/learn
