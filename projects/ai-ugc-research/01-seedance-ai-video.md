# Seedance & AI Video Generation — Research

## Research Date
2026-05-28

## Backlog Reference
095 — AI UGC Content Pipeline Research

---

## Seedance 2.0 — Capabilities

Seedance 2.0 is ByteDance's AI video generation model, built on a dual-branch diffusion transformer architecture. Key capabilities:

- **Video length:** Up to 15-second cinematic clips per generation
- **Resolution:** Up to 2K
- **Audio:** Synchronized native audio generation (audio-video joint generation)
- **Input modes:** Text-to-video, image-to-video, audio-to-video
- **Control:** Full control over performance, lighting, shadow, and camera movement
- **Multi-shot:** Coherent multi-shot storytelling from a single prompt
- **Platform:** Available via ByteDance Dreamina platform and API

### Evolution
- Seedance 1.0: Initial release on Dreamina
- Seedance 1.5 Pro: Added joint audio-visual generation and cinematic camera control
- Seedance 2.0: Biggest leap — 2K resolution, multi-shot storytelling, dual-branch architecture

## Seedance Pricing

### Consumer Plans
| Plan | Price | Credits/Year | Concurrent Tasks |
|------|-------|-------------|-----------------|
| Free | $0 | 260 credits (~13 videos) | Limited |
| Pro | $16/mo | 960/year | 4 |
| Business | $44/mo | 3,000/year | 8 |

### API Pricing
| Model | Cost per Generation |
|-------|-------------------|
| Seedance 2.0 Standard | ~$1.21 |
| Seedance 2.0 Fast | ~$0.77 (33% cheaper, 2x faster) |
| Seedance 1.5 Fast (Atlas Cloud) | $0.022/sec (lowest cost option) |

**The @twoclipping "$2 per video" claim checks out** — using the Fast model or older versions, a single video generation costs $0.77-$2.00 depending on length and model version.

## Competing AI Video Tools

| Tool | Strengths | Price Range |
|------|-----------|------------|
| **Runway Gen-3** | Industry pioneer, strong motion control | $12-76/mo subscription |
| **Kling AI** | High quality, competitive with Seedance | $5.99-89.99/mo |
| **Pika** | Good for short clips, easy interface | $8-58/mo |
| **Sora (OpenAI)** | High quality but limited availability | Part of ChatGPT Plus/Pro |
| **Veo (Google)** | Integrated with Google ecosystem | API pricing varies |

Seedance 2.0 is competitive on quality and significantly cheaper on API pricing than most alternatives. The $0.77-$1.21 per generation via API is lower than Runway or Sora equivalents.

## Platform Authenticity — Can AI UGC Pass?

### TikTok Policy (2026)
- **Mandatory disclosure:** All AI-generated visuals depicting realistic people or scenes MUST be labeled
- **C2PA Content Credentials:** TikTok auto-detects AI content via embedded metadata (integrated January 2025)
- **Scale:** Over 1.3 billion AI-generated videos have been labeled by the platform
- **Enforcement:** Unlabeled AI content gets auto-labeled, distribution reduced, or removed
- **Deepfakes:** Synthetic media of real private individuals is banned entirely
- **Monetization:** Properly labeled AI content IS eligible for Creator Fund and brand partnerships

### Instagram/Meta Policy (2026)
- Similar disclosure requirements announced Q1 2026
- Meta adds "AI info" labels to detected synthetic content
- Enforcement is softer than TikTok's

### What This Means for AI UGC
- **You CAN use AI UGC on platforms** — but you MUST label it
- **The "looks like real UGC" advantage disappears** once labeled — consumers know it's AI
- **Labeled AI content still monetizable** — the restriction targets deception, not AI use
- **The quality bar is: "good enough to engage despite the AI label"** — not "fool people into thinking it's real"

## Quality Assessment

Seedance 2.0 produces high-quality output that is visually impressive but still has tells:
- **Strengths:** Excellent motion stability, cinematic quality, audio sync, multi-shot coherence
- **Weaknesses:** Subtle uncanny valley in human faces/hands, occasional physics glitches, limited to 15-second clips (need stitching for longer content)
- **For UGC purposes:** Travel scenery, product shots, lifestyle B-roll — strong. Talking-head testimonials — still detectable as AI by most viewers

---

## Key Takeaway

Seedance 2.0 is a capable, cost-effective tool for AI video generation. The $2/video claim is legitimate. However, platform disclosure requirements mean AI UGC cannot masquerade as human-created content — it must be labeled and must engage audiences despite that label.
