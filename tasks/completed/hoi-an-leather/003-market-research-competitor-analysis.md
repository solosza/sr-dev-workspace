# Research: Competitor Analysis — Etsy & Shopify Hội An Leather Sellers

## Context
Search Etsy and the web for sellers of Vietnamese/Hội An handmade leather goods targeting US buyers. Map the competitive landscape: pricing, positioning, gaps. Output is `market-analysis.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-leather/` directory exists

## Requirements
- Search Etsy for: "hoi an leather bag", "vietnamese leather bag", "handmade leather bag vietnam"
- Identify top 5 sellers by review count — capture: shop name, platform, price range (duffel + shoulder bag), review count, shipping time, positioning notes
- Identify top 3 gaps / opportunities (e.g., slow shipping from VN, no US-based stock, no customization)
- Write a recommended positioning statement for this business
- List top keywords buyers use in this category (for Etsy SEO)
- Write all findings to `projects/hoi-an-leather/market-analysis.md`

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/market-analysis.md` exists
- [ ] Contains a competitor table with at least 3 sellers
- [ ] Contains a "Gaps" or "Opportunities" section
- [ ] Contains a "Positioning" section with a recommended statement
- [ ] Contains a keyword list for Etsy SEO

## Gates Satisfied
- BUILD-03, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
