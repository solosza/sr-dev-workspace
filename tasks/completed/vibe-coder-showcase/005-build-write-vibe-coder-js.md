# 005 — Write vibe-coder.js

## Type
BUILD

## Description
Write JavaScript for the Vibe Coder Pack showcase page. Terminal animation showing a `/vibe` discovery session.

## Terminal Animation Content
Simulate a `/vibe` session with the 4 discovery questions:

```
$ /vibe
> What does your app do?
  "I want a booking system for my barber shop"

> Who uses it?
  "My customers book appointments, I manage the schedule"

> Web, mobile, or both?
  "Web for now, maybe mobile later"

> Any services you already use?
  "I use Square for payments"

> Generating app profile...
> Analyzing requirements...

DECISION: Frontend Stack

  Your app needs a way for customers to see available
  times and book appointments.

  OPTION A: Next.js
    Best for: Fast web apps with good SEO
    Tradeoff: Slightly more complex setup

  OPTION B: React + Vite
    Best for: Simple SPAs, fast development
    Tradeoff: No server-side rendering

  MY RECOMMENDATION: Next.js — your booking page
  needs to show up in Google searches.

> Which do you prefer? (A)

✓ Architecture generated. Scaffolding project...
✓ 12 files created. Dev server running.
```

## Features
- Typewriter effect on command lines
- Delayed line-by-line output
- Loop after completion (4s pause, then restart)
- Feed counter fetch from feed-count.txt

## Acceptance Criteria
- [ ] File exists at `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.js`
- [ ] Terminal animation with /vibe command and discovery questions
- [ ] Typewriter effect on command input
- [ ] Auto-loop after completion
- [ ] Feed counter fetch
