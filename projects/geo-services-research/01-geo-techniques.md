# GEO Techniques — Research

## Research Date
2026-05-28

## Backlog Reference
096 — GEO Services for Professional Firms

---

## How AI Search Engines Select Sources

AI search engines (Perplexity, ChatGPT, Gemini) use Retrieval-Augmented Generation (RAG) pipelines, fundamentally different from Google's traditional PageRank. The process:

1. **Query Analysis:** AI determines the underlying information need (not just keyword match)
2. **Document Retrieval:** Vector embeddings find semantically relevant pages (meaning, not keywords)
3. **Scoring:** Retrieved documents ranked on relevance, authority, recency, and structural quality
4. **Citation Selection:** AI selects specific pages (not domains) to cite in its response
5. **Response Generation:** LLM synthesizes information and attributes sources

### Key Ranking Factors

| Factor | Impact | Notes |
|--------|--------|-------|
| **Multi-platform brand mentions** | r=0.87 correlation | Strongest signal — mentions across sites matter more than backlinks |
| **Content freshness** | AI-surfaced URLs 25.7% fresher | Favors recently updated content |
| **Unique data/insights** | High priority | Original analysis, novel data cited over repetitive content |
| **Structured data** | Enables extraction | Tables, definitions, quotable data points increase citation |
| **Entity authority** | Entity-based selection | AI cites based on entities, not keywords |
| **Source type** | Multiplier effect | Government 11.75x, ecommerce 5.10x, support docs 3.43x, news 2.56x |

**Critical insight:** Only 11% of domains are cited by BOTH ChatGPT and Perplexity. Optimization must target each platform specifically.

## GEO Optimization Techniques

### 1. Content Structure for AI Extraction
- **Clear definitions:** AI loves "X is Y" statements it can quote directly
- **Data tables:** Structured data in tables is cited more than prose
- **FAQ sections:** Question-answer format matches conversational AI queries
- **Quotable statistics:** Specific numbers, percentages, dollar amounts get cited
- **Authoritative framing:** "According to [source]" and citation-rich content

### 2. Schema Markup and Structured Data
- **LocalBusiness schema:** Name, address, phone, hours, practice areas
- **FAQPage schema:** Question-answer pairs about services
- **ProfessionalService schema:** Specializations, credentials, experience
- **Review schema:** Client testimonials with structured ratings
- **Person schema:** Attorney/doctor profiles with credentials

### 3. Authority Building for AI
- **Google Business Profile optimization** — still feeds AI search
- **Wikipedia and Wikidata presence** — heavily cited by AI engines
- **Reddit/Quora mentions** — community platforms are top AI sources
- **Legal/medical directory listings** — Avvo, Martindale, Healthgrades, Zocdoc
- **Press mentions and local news** — news sources cited 2.56x more
- **Published articles and thought leadership** — original content with expertise signals

### 4. Technical Requirements
- **Fast page load** — AI crawlers time out on slow sites
- **Mobile-optimized** — AI engines index mobile-first
- **Clean HTML structure** — semantic headings (H1, H2, H3) for AI parsing
- **XML sitemap** — ensures all pages are discoverable
- **robots.txt allowing AI crawlers** — some sites block Perplexity/ChatGPT bots

### 5. Content Strategy
- **Location-specific pages:** "Best [practice area] lawyer in [city]" pages
- **Service-specific pages:** Detailed pages per practice area (not one generic page)
- **"Questions answered" content:** Address the exact questions people ask AI
- **Case studies/results:** Specific outcomes AI can cite
- **Regular updates:** Freshness signal — update pages quarterly minimum

## Tools and Platforms Needed

| Tool | Purpose | Cost |
|------|---------|------|
| **Otterly.ai** | Track AI citation frequency and share of voice | $49-$199/mo |
| **Semrush AI Toolkit** | AI search visibility monitoring | Part of Semrush subscription |
| **Ahrefs Brand Radar** | Brand mention tracking across AI platforms | Part of Ahrefs subscription |
| **Rankability** | GEO-specific optimization recommendations | $39-$149/mo |
| **LLMrefs** | Track citations across ChatGPT, Perplexity, Claude | Free-$99/mo |
| **Google Business Profile** | Foundation for local AI visibility | Free |
| **Schema markup tools** | Generate structured data | Free (schema.org generators) |

**Minimum viable toolkit:** Google Business Profile (free) + one AI citation tracker ($49-$99/mo) + schema markup generator (free) = **$49-$99/month overhead**.

## Defensibility: Can Clients DIY?

### Short Answer: Eventually, But Not Easily

**Why clients WON'T DIY immediately:**
- GEO is new — most professional firms don't know it exists
- Requires technical knowledge (schema markup, HTML structure, crawl optimization)
- Requires ongoing monitoring with specialized tools
- Requires content strategy expertise
- The "aha moment" (showing them they don't appear in AI search) creates urgency

**Why clients COULD DIY eventually:**
- GEO techniques will become mainstream knowledge within 1-2 years
- WordPress plugins will automate schema markup
- AI citation tracking tools will become standard in SEO suites
- Once optimized, maintenance is less complex than initial setup

**The Window:** 12-24 months of strong defensibility before GEO becomes mainstream. After that, the value shifts from "knowing how to do GEO" to "having a system that does it efficiently at scale."

**Timeline to results:** Most brands see measurable AI citation improvements within 4-8 weeks of proper GEO implementation.

---

## Key Takeaway

GEO is a real, technically sound practice with clear mechanisms. AI engines select sources based on entity authority, content structure, freshness, and unique data — not traditional SEO backlinks. The techniques are learnable, the tools are affordable ($49-$99/mo), and results appear within 4-8 weeks. The defensibility window is 12-24 months before it becomes commoditized.
