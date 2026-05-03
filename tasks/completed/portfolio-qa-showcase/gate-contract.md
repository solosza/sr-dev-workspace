## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Feature branch exists | run_code | `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --list feature/showcase-qa-platforms \| grep -q showcase` | Create branch |
| BUILD-02 | qa-platforms.html exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Create file |
| BUILD-03 | qa-platforms.css exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.css"` | Create file |
| BUILD-04 | qa-platforms.js exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.js"` | Create file |
| BUILD-05 | Hero section in HTML | grep | `grep -q 'class="hero"' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Add hero section |
| BUILD-06 | Architecture section in HTML | grep | `grep -q 'architecture' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Add architecture section |
| BUILD-07 | Platform grid in HTML | grep | `grep -q 'platform-grid' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Add platform grid |
| BUILD-08 | Loop badge in HTML | grep | `grep -q 'loop-badge' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Add loop badge |
| BUILD-09 | Nav link in index.html | grep | `grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/index.html"` | Add nav link |
| BUILD-10 | Nav link in attestation.html | grep | `grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/attestation.html"` | Add nav link |
| BUILD-11 | Nav link in ssh-compliance.html | grep | `grep -q 'qa-platforms' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Add nav link |
| FUNC-01 | CSS has root variables | grep | `grep -q ':root' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.css"` | Add CSS variables |
| FUNC-02 | JS has terminal animation | grep | `grep -q 'terminal' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.js"` | Add terminal code |
| TEST-01 | Page renders in browser | run_code | Open qa-platforms.html in Playwright, verify no console errors | Fix rendering |
| TEST-02 | Visual QA screenshot | run_code | Take desktop + mobile screenshots, verify layout matches design | Fix layout |
