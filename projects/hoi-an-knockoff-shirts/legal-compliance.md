# Legal & Compliance: Trademark Risk and Private Label Path

## Overview

This document is the **gating decision** for the Hoi An knockoff streetwear project. Every downstream choice — sourcing approach, platform selection, sales strategy — depends on which risk tier the operator selects. The analysis covers US federal trademark law, Customs enforcement, platform-specific policies, the "inspired by" defense, and the private label alternative.

---

## 1. US Trademark Law Exposure

### The Lanham Act (15 U.S.C. ss 1051-1141n)

The Lanham Act is the primary federal statute governing trademarks. It provides civil remedies for trademark infringement, including counterfeiting. A "counterfeit" is defined as a spurious mark that is **identical with or substantially indistinguishable from** a registered mark.

### Criminal Penalties (18 U.S.C. ss 2320 — Trademark Counterfeiting Act)

| Offense | Individual | Organization |
|---------|-----------|--------------|
| First offense | Up to $2M fine + 10 years prison | Up to $5M fine |
| Subsequent offense | Up to $5M fine + 20 years prison | Up to $15M fine |

### Civil Remedies

- **Statutory damages:** $1,000 to $200,000 per counterfeit mark per type of goods
- **Willful infringement:** up to $2,000,000 per mark per type of goods
- **Treble damages:** court may award 3x profits or damages (whichever is greater) + attorney's fees
- **Injunctive relief:** immediate cease-and-desist, asset freeze

### Key Takeaway

Criminal prosecution targets **commercial-scale trafficking.** Civil suits can be filed by any trademark holder at any scale. A single Instagram seller with 50 fake Nike tees is unlikely to get an FBI raid but could absolutely receive a cease-and-desist or civil lawsuit from Nike's legal team.

---

## 2. US Customs & Border Protection (CBP) Enforcement

### Seizure Statistics (FY 2024)

- **32+ million** counterfeit goods seized
- **$5.4 billion** estimated MSRP value
- Top categories: handbags/wallets (15.8% of seizures), jewelry (30% of total value), apparel, footwear
- **90%+ of seizures** occur in international mail and express shipping channels (the exact channels small e-commerce packages use)

### Personal Use Exemption (19 U.S.C. ss 1526(d))

- Travelers entering the US may bring **one article of each type** bearing a counterfeit mark
- Must physically accompany the traveler (no shipping — no FedEx, UPS, DHL)
- Limited to once every 30 days
- Strictly personal use — no gifts, no resale

### Commercial Import Risk Escalation

| Volume | Risk Level | What Happens |
|--------|-----------|--------------|
| 1-2 items via mail | Low | Seizure + destruction, no penalty |
| 3-10 items via mail | Medium | Seizure + CBP letter of demand, possible fine |
| 10+ items / $1K+ value | High | Seizure + investigation referral to ICE/HSI |
| Bulk commercial shipment | Critical | Criminal referral, asset forfeiture, prosecution |

**Heuristic:** Once the aggregate import value exceeds ~$1,000, CBP treats it as commercial trafficking, not personal use. Multiple small shipments to the same address are aggregated.

---

## 3. Platform Policy Matrix

| Platform | Replica/Counterfeit Policy | Enforcement Method | Consequence | Severity |
|----------|---------------------------|-------------------|-------------|----------|
| **Etsy** | Prohibited — violates IP policy | Automated scanning + brand reports + buyer reports | Listing removal, shop suspension, permanent ban | HIGH |
| **eBay** | VeRO program — zero tolerance | Brand owners file takedowns directly; automated keyword scanning | Listing removed, account restricted, permanent suspension after repeat | HIGH |
| **Depop** | Prohibited — 30% increase in enforcement actions (2025) | AI-assisted detection + manual review + buyer reports | Listing removal, account ban | HIGH |
| **Poshmark** | Prohibited — automated moderation | New auto-removal system for reported replicas; Posh Authenticate for luxury | Listing removal, account suspension | HIGH |
| **TikTok Shop** | Strictly forbidden | Pre-listing review + brand reports | Listing rejection, shop ban, legal referral | VERY HIGH |
| **Instagram/Facebook** | Prohibited under Commerce Policies | Brand reports via IP reporting form | Post removal, shop disabled, account restricted | HIGH |
| **Shopify** | Permitted (seller's own store) | Only enforced via DMCA/trademark complaints from brand owners | Store takedown only after valid legal complaint | LOW (self-hosted) |
| **Personal website** | No platform policy | Only enforced via direct legal action from brand owners | Civil lawsuit or cease-and-desist | LOW (but legal risk remains) |

### Key Insight

Every major marketplace **actively bans** replicas. The only channels with low platform risk are self-hosted (Shopify, personal site) — but these still carry full legal risk from trademark holders. Self-hosting just removes the platform intermediary; it doesn't remove the law.

---

## 4. The "Inspired By" / Dupe Defense

### Legal Distinction

| Category | Definition | Legal Status |
|----------|-----------|--------------|
| **Counterfeit** | Reproduces the trademarked name, logo, or mark — attempts to pass as genuine | Illegal (criminal + civil liability) |
| **Dupe / Knockoff** | Copies the design/aesthetic but uses different branding, no trademarked marks | Gray area — depends on trade dress analysis |
| **Inspired-by** | Captures a similar style/aesthetic with original branding, distinct design elements | Generally legal if sufficiently differentiated |

### What's Legally Defensible

- **Removing all trademarked marks** (logos, brand names, proprietary patterns) is necessary but may not be sufficient
- **Trade dress** (the overall commercial image — distinctive color combinations, signature silhouettes, unique design elements) can also be protected
- The test is **likelihood of confusion** — would a reasonable consumer believe the product is made by or affiliated with the original brand?
- Recent case (2025): Lululemon sued Costco over "dupes" that copied trade dress without using the Lululemon name — the design similarity alone was enough to trigger a lawsuit

### What's NOT Defensible

- Putting "inspired by Nike" on a product that copies Nike's design elements
- Using similar-but-not-identical logos (e.g., a swoosh variant)
- Copying proprietary patterns (e.g., Louis Vuitton monogram, Burberry check)
- Any representation that creates consumer confusion about the source

### Practical Reality

The "inspired by" defense works best when the product is **genuinely original** but appeals to the same customer. A plain premium black tee with original graphics targeting the same demographic as Supreme is legal. A tee with a box logo in a similar font that says "Suprime" is not.

---

## 5. Risk Spectrum Table

| Tier | Description | Legal Risk | CBP Risk | Platform Availability | Estimated Margin | Overall Risk Rating |
|------|------------|-----------|----------|----------------------|-----------------|-------------------|
| **Tier 1: Branded Replica** | Exact copies with brand logos/marks (fake Supreme, Nike, etc.) | CRITICAL — criminal + civil liability, up to $2M fine + 10 years | CRITICAL — 90%+ seizure rate in mail channels | NONE — banned on all marketplaces | 60-80% (if not seized) | **DO NOT PURSUE** |
| **Tier 2: Unbranded Knockoff** | Same design/silhouette, logos removed, no brand marks | HIGH — trade dress infringement risk, civil lawsuits | MODERATE — lower seizure risk but still flagged if design is recognizable | LIMITED — some marketplaces may flag, self-hosted OK | 50-70% | **HIGH RISK** |
| **Tier 3: "Inspired By" / Dupe** | Similar aesthetic, distinct design, original branding, no copied elements | MODERATE — defensible if sufficiently differentiated, but trade dress claims possible | LOW — no trademark triggers at customs | MODERATE — marketplace policies may still flag if too similar | 40-60% | **PROCEED WITH CAUTION** |
| **Tier 4: Private Label** | Original designs, original brand, premium blanks, captures same demand | LOW — standard business risk, no IP issues | NONE — legitimate branded goods | FULL — all platforms available | 30-50% (higher at scale) | **RECOMMENDED** |

---

## 6. Private Label Path: Full Scoping

### What It Takes

Build an original streetwear brand that captures the same aesthetic demand without any IP risk. Target the customer who wants the Supreme/Bape/Off-White look, not the logo.

### Blank Garment Options

| Supplier | Product | Wholesale Cost | Quality |
|----------|---------|---------------|---------|
| Bella+Canvas 3001 | Unisex Jersey Tee | $3.50-5.00 | Premium (side-seamed, retail fit) |
| Bella+Canvas 3719 | Unisex Fleece Hoodie | $14-18 | Premium |
| AS Colour 5001 | Staple Tee | $5-7 | Heavy premium (5.5oz) |
| AS Colour 5101 | Supply Hoodie | $18-22 | Heavyweight premium |
| Next Level 3600 | Unisex Cotton Tee | $3.00-4.50 | Mid-premium |
| Independent Trading Co. IND4000 | Heavyweight Hoodie | $16-20 | Streetwear weight |

### Custom Branding Add-Ons

| Service | Cost Per Unit | MOQ |
|---------|--------------|-----|
| Screen printing (1-2 colors) | $3-6 | 24-48 pcs |
| DTG printing (full color) | $8-15 | 1 pc (print-on-demand) |
| Embroidery | $4-8 | 12-24 pcs |
| Custom woven labels | $0.15-0.50 | 100-500 pcs |
| Custom hang tags | $0.10-0.30 | 100 pcs |
| Custom packaging (poly mailer) | $0.15-0.40 | 100 pcs |

### Startup Budget Estimate

| Category | Low End | Mid Range | Notes |
|----------|---------|-----------|-------|
| Initial inventory (50 pcs) | $350 | $600 | Blanks + printing |
| Brand design (logo, tags, labels) | $100 | $500 | Fiverr vs professional |
| Shopify store | $39/mo | $39/mo | Basic plan |
| Domain name | $12/yr | $12/yr | |
| Product photography | $0 | $200 | DIY vs professional |
| Initial marketing | $100 | $500 | Social media ads |
| **Total launch cost** | **$600** | **$1,850** | First production run |

### Print-on-Demand Alternative (Zero Inventory)

| Provider | Base Cost (Tee) | Base Cost (Hoodie) | Shipping | Margin @ $35 Retail |
|----------|----------------|-------------------|----------|---------------------|
| Gooten | $8.40 | $18.90 | $4.95 | ~62% on tee |
| Printify | $14.95 | $29.25 | $3.99 | ~46% on tee |
| Printful | $12.95 | $27.95 | $4.99 | ~49% on tee |

Print-on-demand eliminates inventory risk entirely. Lower margins but zero upfront cost beyond the store.

### Revenue Model (Private Label)

| Scenario | Units/Month | Avg Price | Revenue | COGS (40%) | Gross Profit |
|----------|------------|-----------|---------|-----------|-------------|
| Side hustle | 30 | $35 | $1,050 | $420 | $630 |
| Growing | 100 | $35 | $3,500 | $1,400 | $2,100 |
| Scaled | 500 | $30 | $15,000 | $6,000 | $9,000 |

---

## 7. Go/No-Go Risk Recommendation

### DO NOT PURSUE: Tier 1 (Branded Replicas)

- Criminal liability with prison time
- CBP will seize shipments
- Every marketplace bans them
- No legitimate path exists

### DO NOT PURSUE: Tier 2 (Unbranded Knockoffs)

- Trade dress lawsuits are expensive to defend even if you win
- CBP still flags recognizable designs
- Marketplace risk is high
- Margins don't justify the legal exposure

### PROCEED WITH EXTREME CAUTION: Tier 3 (Inspired-By / Dupes)

- Only viable if designs are **genuinely differentiated** (not just logos removed)
- Must pass the "likelihood of confusion" test
- Self-hosted only (Shopify/personal site) — marketplaces will likely flag
- Consult an IP attorney before launching
- Budget $2-5K for legal review of designs

### RECOMMENDED: Tier 4 (Private Label)

- **Zero legal risk** from IP
- Full platform access (all marketplaces + self-hosted)
- Lower margins compensated by: no seizure risk, no legal fees, no account bans, scalability
- Startup cost as low as $600 (inventory model) or $50 (print-on-demand)
- The same customer who buys knockoff Supreme wants **the aesthetic, not the logo** — a well-designed private label brand captures this demand legally

### Final Verdict

**Go with Tier 4 (Private Label).** The risk/reward on Tiers 1-2 is catastrophically bad. Tier 3 is theoretically possible but requires constant legal vigilance and limits your platform options. Tier 4 gives you the same target market, comparable margins at scale, full platform access, and zero legal risk. The Hoi An angle (Vietnam-made premium streetwear) becomes a brand *asset* instead of a liability — "designed in [city], made in Vietnam" is a legitimate brand story.

---

## Sources

- [Trademark Counterfeiting Laws — UpCounsel](https://www.upcounsel.com/trademark-counterfeiting)
- [What is Counterfeiting — Nolo](https://www.nolo.com/legal-encyclopedia/what-counterfeiting.html)
- [18 U.S.C. ss 2320 — Trafficking in Counterfeit Goods](https://www.law.cornell.edu/uscode/text/18/2320)
- [CBP IPR Seizure Statistics](https://www.cbp.gov/trade/priority-issues/ipr/statistics)
- [CBP Personal Use Exemption](https://www.help.cbp.gov/s/article/Article1858?language=en_US)
- [CBP Seizure FAQ — Great Lakes Customs Law](https://greatlakescustomslaw.com/cbp-seizure-for-online-counterfeit-purchases-faq/)
- [Depop Policy Changes 2026 — CLOSO](https://closo.co/blogs/platform-specific-guides/depop-policy)
- [Trademark Tactics: Dupes — Nixon Peabody](https://www.nixonpeabody.com/insights/articles/2025/07/28/trademark-tactics-protecting-your-brand-amid-rising-legal-battles-over-dupes)
- [Fast Fashion and IP — Vogue College](https://www.voguecollege.com/articles/madrid/fast-fashion-and-intellectual-property-when-is-it-considered-copying-or-inspiration/)
- [Start a Clothing Brand — Bella+Canvas](https://blog.bellacanvas.com/start-clothing-brand-tools/)
- [2025 USTR Notorious Markets Review](https://downloads.regulations.gov/USTR-2025-0018-0009/attachment_1.pdf)
