# Floating Terminal Component

## Status
NEW

## Location
`isagawa-portfolio-site-v2/` — hero section

## What It Does
A terminal window floating in the hero with 3D perspective, showing a conversation loop typing itself in real time. This is the visual centerpiece — the equivalent of Shader.se's retro CRT but for a conversational agent factory.

## Visual Spec
- Dark terminal surface (--bg-surface or slightly lighter)
- Rounded corners, subtle border (--border-subtle)
- Faint glow/shadow underneath for depth
- CSS 3D transform: slight perspective tilt (rotateX/rotateY) with a gentle floating animation (translateY oscillation, 4-6s ease-in-out infinite)
- Terminal header bar with three dots (red/yellow/green) and a title like "isagawa session"
- Monospace text content

## Typing Animation
The terminal shows a looping conversation sequence:

```
> describe: build a portfolio site from conversational intent

  backlog created: 047-market-build-portfolio-site-loop-theme.md
  tasks decomposed: 25
  executing...

  ✓ 25/25 tasks complete
  ✓ signed: rekor #1387966928

  the loop closes.
```

- Each line types character-by-character (40-60ms per char)
- Pause between lines (400-800ms)
- Blinking cursor (--accent color)
- After full sequence completes, pause 3s, clear, restart
- Pure JS, no libraries

## Mobile Behavior
- Remove 3D perspective tilt on screens < 768px
- Keep the float animation but reduce amplitude
- Terminal scales down but remains readable
- Consider reducing the typing sequence length on mobile

## Dependencies
- CSS custom properties from v1 (colors, fonts, spacing)
- No external dependencies
