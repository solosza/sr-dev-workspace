# Research: Market Analysis — Replica Streetwear

## Context
Produce a competitor and market landscape document for US replica streetwear sales. This is the foundation for the GTM recommendation — it identifies where buyers are, which brands move, and what the competitive landscape looks like. Output: `projects/hoi-an-knockoff-shirts/market-analysis.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists

## Requirements
- Use WebSearch and WebFetch to research where replica streetwear is sold in the US (Depop, eBay, DHgate, Discord, Telegram, TikTok Shop)
- Identify the 3-5 most cloned brands by apparent demand (Stussy, Supreme, Polo, Off-White, Bape, Essentials, Corteiz)
- Find 5+ active sellers — note their handle/store, platform, price per item, how they describe product, review count
- Identify the top 3 market gaps or opportunities
- Recommend go-to-market positioning (replica underground vs inspired-by brand)
- Include a keyword/search term list (what buyers search for)

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/market-analysis.md` exists
- [ ] File contains a platform map section (where replicas are sold + risk level per platform)
- [ ] File contains a brand demand ranking (top brands by volume)
- [ ] File contains a competitor table (seller, platform, price, positioning)
- [ ] File contains at least 3 market gap/opportunity findings
- [ ] `grep -qi "platform" projects/hoi-an-knockoff-shirts/market-analysis.md` passes
- [ ] `grep -qi "competitor\|seller" projects/hoi-an-knockoff-shirts/market-analysis.md` passes

## Gates Satisfied
- DOC-01, DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
