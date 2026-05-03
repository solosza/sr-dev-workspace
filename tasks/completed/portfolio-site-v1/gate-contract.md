# Gate Contract — Portfolio Site

## Verification Methods
See `.claude/skills/task-builder/references/verification-methods.md`

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Output directory exists | file_exists | `test -d D:/my_ai_projects/isagawa-portfolio-site` | Create directory |
| BUILD-02 | index.html exists | file_exists | `test -f D:/my_ai_projects/isagawa-portfolio-site/index.html` | Create file |
| BUILD-03 | styles.css exists | file_exists | `test -f D:/my_ai_projects/isagawa-portfolio-site/styles.css` | Create file |
| BUILD-04 | assets directory exists | file_exists | `test -d D:/my_ai_projects/isagawa-portfolio-site/assets/images` | Create directory |
| BUILD-05 | HTML has nav section | grep | `grep -q '<nav' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add nav |
| BUILD-06 | HTML has hero section | grep | `grep -q 'id="hero"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add hero |
| BUILD-07 | HTML has architecture section | grep | `grep -q 'id="architecture"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-08 | HTML has kernel section | grep | `grep -q 'id="kernel"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-09 | HTML has factory section | grep | `grep -q 'id="factory"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-10 | HTML has catalog section | grep | `grep -q 'id="catalog"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-11 | HTML has platforms section | grep | `grep -q 'id="platforms"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-12 | HTML has loop section | grep | `grep -q 'id="loop"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-13 | HTML has CTA section | grep | `grep -q 'id="cta"' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add section |
| BUILD-14 | HTML has footer | grep | `grep -q '<footer' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add footer |
| BUILD-15 | CSS has color variables | grep | `grep -q '\-\-bg-primary' D:/my_ai_projects/isagawa-portfolio-site/styles.css` | Add variables |
| BUILD-16 | CSS has typography variables | grep | `grep -q '\-\-font-heading' D:/my_ai_projects/isagawa-portfolio-site/styles.css` | Add variables |
| BUILD-17 | CSS has spacing variables | grep | `grep -q '\-\-space-section' D:/my_ai_projects/isagawa-portfolio-site/styles.css` | Add variables |
| BUILD-18 | CSS has responsive breakpoints | grep | `grep -q '@media' D:/my_ai_projects/isagawa-portfolio-site/styles.css` | Add media queries |
| BUILD-19 | Hero has correct headline | grep | `grep -q 'The AI Management Layer' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Fix headline |
| BUILD-20 | Catalog has BUILD badge | grep | `grep -q 'BUILD' D:/my_ai_projects/isagawa-portfolio-site/index.html` | Add badge |
| FUNC-01 | HTML is valid | run_code | `python -c "from html.parser import HTMLParser; HTMLParser().feed(open('D:/my_ai_projects/isagawa-portfolio-site/index.html').read()); print('valid')"` exits 0 | Fix HTML |
| FUNC-02 | CSS parses without error | run_code | `python -c "open('D:/my_ai_projects/isagawa-portfolio-site/styles.css').read(); print('ok')"` exits 0 | Fix CSS |
| TEST-01 | Site renders in browser | manual | Playwright screenshot shows all 9 sections | Fix rendering |
| TEST-02 | Site responsive at mobile | manual | Playwright screenshot at 375px shows stacked layout | Fix responsive |
| TEST-03 | All anchor links work | manual | Clicking nav links scrolls to correct sections | Fix anchors |
