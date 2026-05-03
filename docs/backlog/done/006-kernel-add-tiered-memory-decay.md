# Add Tiered Memory Decay to Learning System

## Context
Competitive gap identified from ClawHub analysis (2026-03-22). ClawHub's "Self-Improving + Proactive" skill uses hot/warm/cold memory tiers with auto-promotion (3x in 7 days → HOT) and demotion. Our lessons are flat — everything stays forever with equal weight.

## Problem
As lessons accumulate, the protocol grows without bound. Stale lessons that no longer apply sit alongside critical recent ones. No way to distinguish a lesson learned yesterday from one learned 3 months ago that may no longer be relevant.

## Requirements
- Define memory tiers (e.g., hot / warm / cold) with promotion/demotion rules
- Track recency and relevance per lesson
- Auto-demote lessons that haven't been triggered in N cycles
- Auto-promote lessons that recur frequently
- Pruning or archival for cold lessons

## Source
- https://clawhub.ai/ivangdavila/self-improving

## Task Builder Input
- **Deliverable:** Updated lessons system with hot/warm/cold tiers, auto-promotion/demotion logic, updated lessons.md format
- **Scope:** BUILD
- **Constraints:** Must be backwards-compatible with existing flat lessons. Kernel repo (`isagawa-kernel`). Feeds into backlog 007 (skill extraction) and 008 (recurrence detection).
