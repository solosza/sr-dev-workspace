# Design Constraints & Content Template

## Status
NEW — cross-cutting design doc

## Visual Language
Must match existing isagawa.co portfolio site:
- Dark theme (near-black background, light text)
- Terminal/monospace aesthetic
- Accent colors from existing palette
- Same responsive breakpoints
- No JavaScript frameworks — vanilla HTML/CSS

## Reference Sites to Clone
Focus on developer portfolio project pages and case studies:
- Linear.app case studies (minimalist, strong brand)
- Vercel customer showcases (platform + showcase pattern)
- Stripe developer docs (technical depth presentation)
- Resend.com (modern developer tool site)

## Content Template Per Page

Each showcase page follows this structure:

```
1. Hero
   - One-sentence value prop
   - Key visual (screenshot, diagram, or live counter)

2. Problem Statement
   - What testing challenge this solves
   - Why existing tools fall short

3. Architecture
   - Diagram showing how it works
   - Key components and data flow

4. Tech Stack
   - Technology logos/badges
   - Framework choices with rationale

5. Demo
   - Screenshot, GIF, or embedded terminal
   - Showing it actually running

6. Results
   - Metrics (tests run, coverage, attestations signed)
   - Concrete numbers, not vague claims

7. Navigation
   - Back to portfolio
   - Links to other showcase pages
   - GitHub repo link (if public)
```

## Layout Patterns
- Full-width hero with gradient overlay
- Two-column layout for architecture diagrams
- Card grid for tech stack
- Terminal-style code blocks for examples
- Sticky navigation back to portfolio

## Process
1. Clone 2-3 reference case study pages using /clone
2. Extract layout patterns and components
3. Build pages using extracted patterns + existing isagawa.co design system
4. Visual QA against references
5. Deploy to GitHub Pages
