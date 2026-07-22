# Test: L3 Live Flow via Interface Primitives

## Type
TEST
## Execution
inline
## Dependencies
- 004

## Requirements
- Fresh seed + boot on 8018; ONE realistic flow using ONLY ApiInterface primitives (no api-objects — they're backlog 211):
  POST customer → POST order (PENDING) → POST process → POST process (COMPLETE) → GET verify → invalid transition returns ApiResponse with status 400 (interface must RETURN the 4xx response, not raise — 4xx is a valid HTTP answer; verify the design doc's rule on this and follow it) → DELETE → GET 404
- Assert response_time populated on every call; cleanup in finally; env problem → L3-BLOCKED honestly

## Acceptance Criteria
- [ ] Flow green end-to-end through the interface

## Gates Satisfied
- AIF-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
