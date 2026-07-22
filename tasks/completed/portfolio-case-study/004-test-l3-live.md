# Task 004: L3 - Live (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives.
**Gates:** CS-05

## Action
ONE script: poll https://solosza.github.io/?cb=256 up to 10 min (cache-bust query param - GitHub Pages CDN caches aggressively, lesson from backlog 253); assert case study section present with problem/role/result/trade-off; coverage language matches the verified state from task 001; kernel-internal grep 0; absolute-claims grep 0 (watch for CSS max-width:100% false positives - check match context before failing, lesson from 255).

## Acceptance
Live asserts PASS, exit 0. Red: fix then /kernel/learn.
