# Gate Contract — Job Application Product Page

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Feature branch exists | run_code | `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --list feature/job-application-page \| grep feature/job-application-page` exits 0 | Create branch |
| BUILD-02 | job-application.html exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Write file |
| BUILD-03 | job-application.css exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/job-application.css"` | Write file |
| BUILD-04 | job-application.js exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/job-application.js"` | Write file |
| FUNC-01 | HTML loads pill-nav.css | grep | `grep -q "pill-nav.css" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Fix link tag |
| FUNC-02 | HTML loads pill-nav.js | grep | `grep -q "pill-nav.js" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Fix script tag |
| FUNC-03 | HTML has loop-badge | grep | `grep -q "loop-badge" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Add loop-badge div |
| FUNC-04 | HTML has hero section | grep | `grep -q 'class="hero"' "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Add hero section |
| FUNC-05 | HTML has page-section elements | grep | `grep -q "page-section" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Add sections |
| FUNC-06 | HTML has factory-origin | grep | `grep -q "factory-origin" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Add div |
| FUNC-07 | HTML has CTA to GitHub | grep | `grep -q "github.com/isagawa-co/job-application-spec" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Fix CTA link |
| FUNC-08 | HTML has footer grid | grep | `grep -q "footer__grid" "D:/my_ai_projects/isagawa-co.github.io/job-application.html"` | Add footer |
| FUNC-09 | CSS has reveal animation | grep | `grep -q "\.reveal" "D:/my_ai_projects/isagawa-co.github.io/job-application.css"` | Add reveal CSS |
| FUNC-10 | CSS has hero entered | grep | `grep -q "\.hero.entered" "D:/my_ai_projects/isagawa-co.github.io/job-application.css"` | Add CSS rule |
| FUNC-11 | JS has IntersectionObserver | grep | `grep -q "IntersectionObserver" "D:/my_ai_projects/isagawa-co.github.io/job-application.js"` | Add scroll reveal |
| FUNC-12 | JS adds hero entered class | grep | `grep -q "entered" "D:/my_ai_projects/isagawa-co.github.io/job-application.js"` | Add hero entrance |
| FUNC-13 | vibe-coder.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"` | Update nav |
| FUNC-14 | qa-platforms.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"` | Update nav |
| FUNC-15 | index.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/index.html"` | Update nav |
| FUNC-16 | ssh-compliance.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Update nav |
| FUNC-17 | story.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Update nav |
| FUNC-18 | feed.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` | Update nav |
| FUNC-19 | attestation.html has Job Application nav | grep | `grep -q "job-application.html" "D:/my_ai_projects/isagawa-co.github.io/attestation.html"` | Update nav |
