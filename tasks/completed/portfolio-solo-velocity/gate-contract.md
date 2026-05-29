# Gate Contract — Portfolio Solo-Velocity Landing Page

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| RESEARCH-01 | Research report exists | file_exists | `test -f "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/portfolio-message-research/research-report.md"` | Run task 001-002 |
| RESEARCH-02 | Report has validation verdict | grep | `grep -q "validation verdict\|Validated\|validated\|differentiated" "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/portfolio-message-research/research-report.md"` | Add verdict to report |
| BUILD-01 | story.html exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Run task 004 |
| BUILD-02 | story.html has 6 sections | grep | `grep -c "anchor-section__number" "D:/my_ai_projects/isagawa-co.github.io/story.html" \| grep -qE "^[6-9]\|^[1-9][0-9]"` | Add missing sections |
| BUILD-03 | .reveal class present | grep | `grep -q "class=\".*reveal" "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Add reveal classes |
| BUILD-04 | parallax-section present | grep | `grep -q "parallax-section" "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Add parallax classes |
| BUILD-05 | Terminal provenance section | grep | `grep -q "terminal__body" "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Add Section 6 terminal |
| BUILD-06 | Feed entries injected | grep | `grep -q "feed-entry" "D:/my_ai_projects/isagawa-co.github.io/story.html"` | Run task 006 |
| BUILD-07 | CSS user class added | grep | `grep -q "terminal__line--user" "D:/my_ai_projects/isagawa-co.github.io/styles.css"` | Run task 003 |
| BUILD-08 | generate-feed handles story.html | grep | `grep -q "story.html" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` | Run task 005 |
| FUNC-01 | generate-feed.py runs clean | run_code | `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0 | Fix script errors |
| FUNC-02 | Feed visible without JS | run_code | `python -c "html=open('D:/my_ai_projects/isagawa-co.github.io/story.html').read(); assert 'feed-entry' in html, 'No feed entries in raw HTML'"` exits 0 | Run generate-feed |
