# Research AI YouTube Content Pipeline Feasibility

## Status
Open

## Priority
High — proven $32k/month model with zero employees, zero camera, zero personal brand. Fits the autonomous pipeline pattern perfectly.

## Summary
Research the feasibility of building an autonomous AI YouTube content pipeline. A faceless YouTube channel where AI writes every script, generates every voiceover, creates every visual — no human on camera, no studio, no editing. The kernel's execute-pipeline loop maps directly: backlog item = video idea, tasks = script → voiceover → visuals → thumbnail → upload. Validate whether this is a viable revenue stream and what the realistic economics look like.

## Requirements

### Pipeline Architecture
- Map the kernel pipeline to YouTube content: idea → script → voiceover → visuals → edit → thumbnail → SEO metadata → upload
- What AI tools handle each step? (Claude for scripts, ElevenLabs/PlayHT for voice, Midjourney/DALL-E/Runway for visuals, FFmpeg for assembly)
- Can each step be fully automated via CLI/API, or do some require manual intervention?
- How does the user's vision of "a workflow like our pipeline command but across different steps" translate? Each video = one execute-pipeline run?

### Revenue Model
- YouTube Partner Program requirements (1,000 subs, 4,000 watch hours)
- CPM rates by niche — which niches pay highest for faceless content?
- Realistic timeline from channel creation to first monetization
- The $32k/month claim — what subscriber/view count does that require? Is it realistic or outlier?
- Additional revenue: sponsorships, affiliate links, merchandise

### Content Strategy
- Which niches work best for faceless AI-generated content? (finance, tech explainers, history, true crime, motivation, compilations)
- What content length performs best? (shorts vs long-form vs both)
- Upload frequency — how many videos/week does the pipeline need to produce?
- SEO and discoverability — can Claude optimize titles, descriptions, tags?

### Technical Feasibility
- End-to-end automation: can every step from script to upload happen without human touch?
- YouTube API for automated uploads — any restrictions on bot uploads?
- Quality bar — will AI-generated content pass YouTube's quality thresholds and viewer expectations?
- Voice quality — are current TTS models good enough to retain viewers for 10+ minutes?

### Platform Risk
- YouTube policies on AI-generated content — any restrictions or labeling requirements?
- Monetization eligibility for AI-generated channels
- Risk of demonetization or channel strikes
- Competition — how saturated is the faceless AI YouTube space already?

### Cost Analysis
- Per-video cost: API calls (Claude, voice, image generation)
- Monthly infrastructure cost at target volume (e.g., 30 videos/month)
- Break-even: at what point do ad revenues exceed production costs?

## References
- Source: @defileo X post (2026-04-28) — $32k/month faceless AI YouTube channel
- Kernel pipeline: `.claude/skills/execute-pipeline/`
- Content production spec: backlog [004](done/004-domain-build-content-production-spec.md) (done)
- Backlog 064: autonomous game content pipeline (similar autonomous content model)

## Task Builder Input
- **Deliverable:** Research report covering pipeline architecture, revenue model, content strategy, technical feasibility, platform risk, cost analysis, and go/no-go recommendation with projected unit economics
- **Location:** `subproject:ai-youtube-pipeline`
- **Scope:** RESEARCH
- **Constraints:** Research only — no building yet. Need real YouTube CPM data, API pricing for voice/image generation, and honest assessment of whether the $32k/month model is reproducible vs outlier. The user visualizes this as "a workflow like our pipeline command but across different steps" — research should validate if that architecture works.
