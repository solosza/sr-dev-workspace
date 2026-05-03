# 011 — L3: Visual QA Screenshots

**Type:** TEST
**Depends on:** 010

## Goal
Production verification — take desktop and mobile screenshots of the showcase page and verify visual quality.

## Requirements
1. Desktop screenshot (1440x900):
   - `mcp__playwright__browser_resize` to 1440x900
   - `mcp__playwright__browser_take_screenshot` — save as `qa-platforms-desktop.png`
2. Mobile screenshot (375x812):
   - `mcp__playwright__browser_resize` to 375x812
   - `mcp__playwright__browser_take_screenshot` — save as `qa-platforms-mobile.png`
3. Visual checks:
   - Dark theme applied (black/near-black background)
   - Hero text readable and properly sized
   - Architecture diagram visible and aligned
   - Platform grid cards visible
   - Terminal animation area present
   - Footer visible
   - Mobile layout stacks correctly (no horizontal overflow)

## Acceptance Criteria
- [ ] Desktop screenshot taken and reviewed
- [ ] Mobile screenshot taken and reviewed
- [ ] No visual layout issues identified
