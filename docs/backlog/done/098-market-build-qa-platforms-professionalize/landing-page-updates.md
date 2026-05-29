# QA Platforms Landing Page Updates

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-co.github.io\qa-platforms.html`

## What It Needs
1. **Add API platform** entry to "The Platforms" section (below Playwright)
   - Stack: Python, REST/GraphQL, pytest
   - Tests: API endpoints, contract testing, response validation
   - Link to repo (TBD which repo, or placeholder if repo doesn't exist yet)

2. **Update "Built for" messaging**
   - Current: "Works with Claude Code, Cursor, and Windsurf via MCP"
   - Change to: "Built for Claude Code" (accurate, no false promises)
   - Remove MCP badge from tech stack if inaccurate

3. **Verify all repo links resolve**
   - platform-selenium GitHub link
   - platform-playwright GitHub link
   - platform-docker GitHub link
   - platform-deepeval GitHub link (only if public)
   - platform-ssh GitHub link (already verified)

4. **Update platform count** if API is added (5 becomes 6)

5. **Commit and push** to deploy

## Dependencies
- All repo professionalization complete (so links resolve to good READMEs)
- Decision on platform-deepeval public/private
- Decision on whether API platform repo exists or is planned
