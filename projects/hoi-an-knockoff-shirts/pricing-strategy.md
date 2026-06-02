# Pricing Strategy: Landed Cost and Margin Model

**Pipeline:** 114 — Hoi An Knockoff Shirts
**Date:** 2026-06-01

---

## 1. Landed Cost Model — Replica T-Shirt (Vietnam Origin, Cotton)

### Per-Unit Cost Breakdown by Batch Size

| Cost Component | 12 Units | 36 Units | 72 Units |
|---------------|----------|----------|----------|
| FOB cost (Vietnam factory) | $4.00 | $4.00 | $3.50 |
| Import duty (16.5% MFN) | $0.66 | $0.66 | $0.58 |
| Air freight | $3.88 | $2.59 | $2.00 |
| Customs broker / entry fee | $2.50 | $0.83 | $0.42 |
| Packaging (poly bag + label) | $0.50 | $0.50 | $0.50 |
| **Landed cost per unit** | **$11.54** | **$8.58** | **$7.00** |

**Notes:**
- Air freight rates: $6-9.50/kg, volumetric weight ~0.33 kg/unit for T-shirts
- Customs broker flat fee ~$30 per entry (amortized across batch)
- 72-unit FOB reflects modest volume discount ($3.50 vs $4.00)
- Excludes domestic shipping to customer (added in margin analysis below)

### Per-Unit Cost Breakdown — China Origin Comparison

| Cost Component | 12 Units | 36 Units | 72 Units |
|---------------|----------|----------|----------|
| FOB cost (Guangzhou factory) | $3.50 | $3.50 | $3.00 |
| Import duty (24.0% — MFN + Section 301) | $0.84 | $0.84 | $0.72 |
| Air freight | $3.88 | $2.59 | $2.00 |
| Customs broker / entry fee | $2.50 | $0.83 | $0.42 |
| Packaging | $0.50 | $0.50 | $0.50 |
| **Landed cost per unit** | **$11.22** | **$8.26** | **$6.64** |

**China vs Vietnam delta:** China FOB is $0.50 cheaper but duty is 7.5% higher (Section 301). Net difference is only $0.32-0.36/unit. Vietnam is the better source when factoring in lower seizure risk (see logistics-fulfillment.md Section 4).

---

## 2. Landed Cost Model — Replica Hoodie (Vietnam Origin, Cotton)

### Per-Unit Cost Breakdown by Batch Size

| Cost Component | 12 Units | 36 Units | 72 Units |
|---------------|----------|----------|----------|
| FOB cost (Vietnam factory) | $8.00 | $8.00 | $7.00 |
| Import duty (16.5% MFN) | $1.32 | $1.32 | $1.16 |
| Air freight | $6.46 | $6.03 | $5.00 |
| Customs broker / entry fee | $2.50 | $0.83 | $0.42 |
| Packaging (poly bag + label) | $0.75 | $0.75 | $0.75 |
| **Landed cost per unit** | **$19.03** | **$16.93** | **$14.33** |

**Notes:**
- Hoodies are heavier (~0.5 kg/unit) and bulkier — volumetric weight drives freight up
- At 12 units, freight alone is $6.46/unit — nearly as much as the product itself
- 72-unit batch drops landed cost by 25% vs 12-unit batch

---

## 3. Platform Fee Structures (2026)

| Platform | Commission / Fee | Payment Processing | Per-Order Fee | Effective Take Rate |
|----------|-----------------|-------------------|---------------|-------------------|
| **Depop** | 0% (US sellers) | 3.3% | $0.45 | ~4.8% on $25 sale |
| **eBay** | 15.3% (clothing) | Included | $0.30-0.40 | ~16.5% on $25 sale |
| **Poshmark** | 20% (sales >= $15) | Included | — | 20.0% |
| **TikTok Shop** | 6% referral | ~2% processing | — | ~8.0% |
| **Etsy** | 6.5% transaction | 3% + $0.25 processing | $0.20 listing | ~11.3% on $25 sale |
| **Shopify** (own store) | 0% | 2.9% + $0.30 | — | ~4.1% on $25 sale |

### Platform Fee Per Unit at $25 Sell Price

| Platform | Fee Amount | Net to Seller |
|----------|-----------|---------------|
| Depop | $1.28 | $23.72 |
| Shopify | $1.03 | $23.98 |
| TikTok Shop | $2.00 | $23.00 |
| Etsy | $2.83 | $22.18 |
| eBay | $4.13 | $20.88 |
| Poshmark | $5.00 | $20.00 |

### Platform Fee Per Unit at $45 Sell Price (Hoodie)

| Platform | Fee Amount | Net to Seller |
|----------|-----------|---------------|
| Depop | $1.94 | $43.07 |
| Shopify | $1.61 | $43.40 |
| TikTok Shop | $3.60 | $41.40 |
| Etsy | $4.78 | $40.23 |
| eBay | $7.19 | $37.82 |
| Poshmark | $9.00 | $36.00 |

**Recommendation:** Start on Depop (lowest fees, streetwear audience) and TikTok Shop (viral discovery). Avoid eBay and Poshmark — their fee structures eat 16-20% of revenue.

---

## 4. Retail Pricing at Margin Targets

### T-Shirt — 36-Unit Batch (Landed: $8.58)

| Margin Target | Sell Price | Domestic Ship | Platform Fee (Depop) | Gross Profit | Margin % |
|--------------|-----------|---------------|---------------------|-------------|----------|
| 50% | $22.00 | $4.50 | $1.18 | $7.74 | 35.2% net |
| 60% | $27.00 | $4.50 | $1.34 | $12.58 | 46.6% net |
| 70% | $32.00 | $4.50 | $1.50 | $17.42 | 54.4% net |

### T-Shirt — 72-Unit Batch (Landed: $7.00)

| Margin Target | Sell Price | Domestic Ship | Platform Fee (Depop) | Gross Profit | Margin % |
|--------------|-----------|---------------|---------------------|-------------|----------|
| 50% | $20.00 | $4.50 | $1.11 | $7.39 | 36.9% net |
| 60% | $25.00 | $4.50 | $1.28 | $12.23 | 48.9% net |
| 70% | $30.00 | $4.50 | $1.44 | $17.06 | 56.9% net |

### Hoodie — 36-Unit Batch (Landed: $16.93)

| Margin Target | Sell Price | Domestic Ship | Platform Fee (Depop) | Gross Profit | Margin % |
|--------------|-----------|---------------|---------------------|-------------|----------|
| 50% | $40.00 | $5.50 | $1.77 | $15.80 | 39.5% net |
| 60% | $48.00 | $5.50 | $2.03 | $23.54 | 49.0% net |
| 70% | $58.00 | $5.50 | $2.36 | $33.21 | 57.3% net |

### Hoodie — 72-Unit Batch (Landed: $14.33)

| Margin Target | Sell Price | Domestic Ship | Platform Fee (Depop) | Gross Profit | Margin % |
|--------------|-----------|---------------|---------------------|-------------|----------|
| 50% | $35.00 | $5.50 | $1.61 | $13.57 | 38.8% net |
| 60% | $42.00 | $5.50 | $1.84 | $20.33 | 48.4% net |
| 70% | $52.00 | $5.50 | $2.17 | $30.01 | 57.7% net |

**Note:** "Margin %" is gross sell price minus all costs (landed + shipping + platform fee) divided by sell price. "Margin Target" is the aspirational target; net margin is lower because domestic shipping and platform fees aren't included in the landed cost.

**Recommended price points:**
- **T-shirt: $25-30** (targets 47-57% net margin at 72 units; positions in the streetwear mid-range)
- **Hoodie: $45-55** (targets 47-57% net margin at 72 units; competitive with branded streetwear)

---

## 5. Replica vs Private Label Cost Comparison

### Private Label Model (Domestic — No Import)

Private label = buy US-stocked blank (Bella+Canvas, AS Colour, Gildan Heavy) + add custom print (DTG or screen print).

| Component | T-Shirt | Hoodie |
|-----------|---------|--------|
| Blank garment (wholesale) | $5.00-6.50 (Bella+Canvas 3001) | $14.00-18.00 (AS Colour 5101 / Independent Trading SS4500) |
| DTG print (small batch, 12-36 pcs) | $8.00-15.00 | $10.00-18.00 |
| Screen print (36+ pcs, 1-2 colors) | $5.00-8.00 | $6.00-10.00 |
| **Total (DTG, small batch)** | **$13.00-21.50** | **$24.00-36.00** |
| **Total (screen print, 36+ pcs)** | **$10.00-14.50** | **$20.00-28.00** |

### Replica Import Model (Vietnam, 36 Units)

| Component | T-Shirt | Hoodie |
|-----------|---------|--------|
| Landed cost (all-in) | $8.58 | $16.93 |

### Side-by-Side Comparison

| Factor | Replica Import (36 units) | Private Label DTG (36 units) | Private Label Screen Print (36 units) |
|--------|--------------------------|-----------------------------|------------------------------------|
| **Per-unit cost** | T: $8.58 / H: $16.93 | T: $15.00 / H: $28.00 | T: $12.00 / H: $24.00 |
| **Cost delta vs replica** | Baseline | T: +$6.42 (+75%) / H: +$11.07 (+65%) | T: +$3.42 (+40%) / H: +$7.07 (+42%) |
| **Lead time** | 3-5 weeks (production + shipping) | 1-2 weeks (US fulfillment) | 2-3 weeks (setup + print) |
| **MOQ** | 12-36 (via agent) | 1 (DTG) / 24-36 (screen print) | 24-36 minimum |
| **IP risk** | HIGH (branded replicas) / LOW (unbranded) | ZERO | ZERO |
| **Brand story** | None (commodity) | "Original streetwear brand" | "Original streetwear brand" |
| **Quality control** | Remote QC photos, variable | In-hand before shipping | In-hand before shipping |
| **Customs/duty** | $1.49/unit (T-shirt) | $0 (domestic) | $0 (domestic) |
| **Margin at $25 tee** | 46.6% net (Depop) | 21.9% net (DTG) / 32.9% net (screen) | 32.9% net (screen) |
| **Margin at $45 hoodie** | 49.0% net (Depop) | 27.3% net (DTG) / 36.7% net (screen) | 36.7% net (screen) |

### Key Insight

Replica imports have a **40-75% cost advantage** over private label, but that advantage comes with:
1. **IP seizure risk** for branded items (mitigated by going unbranded/inspired-by)
2. **Longer lead times** (3-5 weeks vs 1-2 weeks)
3. **No brand equity** — you're reselling someone else's design
4. **Quality variance** — remote QC is never as reliable as in-hand inspection

**The hybrid play:** Import unbranded blanks from Vietnam ($3.50-4.00/tee, $7-8/hoodie) and add DTG or screen printing domestically. Cost: $11.50-12.00/tee, $17-18/hoodie — only $3-4 more than full import, with zero IP risk and full brand control.

---

## 6. Break-Even Analysis

### Assumptions
- Initial investment: $750 (midpoint of $500-1000 range)
  - Sample orders from 3 sellers: $200
  - First production batch (36 T-shirts): $309 (36 x $8.58 landed)
  - Packaging supplies + labels: $100
  - Platform setup + listing photos: $50
  - Buffer / returns / quality issues: $91

### T-Shirt Break-Even (36-Unit Batch, $27 Sell Price)

| Metric | Value |
|--------|-------|
| Sell price | $27.00 |
| Landed cost | $8.58 |
| Domestic shipping | $4.50 |
| Platform fee (Depop) | $1.34 |
| **Net profit per unit** | **$12.58** |
| **Break-even units** | **60 units** (750 / 12.58) |
| **Break-even at 10 units/week** | **6 weeks** |

### Hoodie Break-Even (36-Unit Batch, $48 Sell Price)

| Metric | Value |
|--------|-------|
| Sell price | $48.00 |
| Landed cost | $16.93 |
| Domestic shipping | $5.50 |
| Platform fee (Depop) | $2.03 |
| **Net profit per unit** | **$23.54** |
| **Break-even units** | **32 units** (750 / 23.54) |
| **Break-even at 5 units/week** | **6.4 weeks** |

### Mixed SKU Scenario (Realistic)

Selling a mix of tees and hoodies at the recommended price points:

| Period | Units Sold | Revenue | Total Costs | Cumulative Profit |
|--------|-----------|---------|-------------|------------------|
| Week 1-2 | 8 tees, 3 hoodies | $360 | $195 | +$165 |
| Week 3-4 | 10 tees, 4 hoodies | $462 | $243 | +$384 |
| Week 5-6 | 12 tees, 5 hoodies | $564 | $293 | +$655 |
| **Week 6** | **Cumulative: 30 tees, 12 hoodies** | **$1,386** | **$731** | **+$655 (break-even passed at ~week 4)** |

**Break-even is achievable within 4-6 weeks** at modest sales velocity (5-10 tees + 2-5 hoodies per week).

### Sensitivity: What If Sales Are Slower?

| Sales Rate | Break-Even Timeline |
|-----------|-------------------|
| 15 units/week (mix) | ~4 weeks |
| 10 units/week (mix) | ~5-6 weeks |
| 5 units/week (mix) | ~10-12 weeks |
| 3 units/week (mix) | ~16-20 weeks |

At fewer than 5 units/week, the project is still profitable but takes 3-5 months to recover the initial investment. Below 3 units/week, consider whether the time investment justifies the return.

---

## 7. Key Pricing Decisions

1. **Price tees at $25-30, hoodies at $45-55** — targets 47-57% net margin on Depop at 72-unit batches
2. **Start on Depop + TikTok Shop** — lowest combined fees (3-8%), best streetwear audience
3. **Avoid eBay and Poshmark** for primary sales — 15-20% fees destroy margin on sub-$50 items
4. **Order 36-unit minimum batches** — the per-unit cost cliff from 12→36 units ($11.54→$8.58 for tees) justifies the larger commitment
5. **Scale to 72 units once validated** — another $1.58/unit savings on tees, $2.60 on hoodies
6. **Consider the hybrid play** — Vietnam blanks + domestic printing at $11.50-12/tee gives 90% of the margin with 0% of the IP risk
7. **Break-even is fast** — 60 tees or 32 hoodies to recover $750 initial investment (4-6 weeks at moderate velocity)

---

*Data sources: Task 003 (sourcing-suppliers.md) FOB costs and supplier data; Task 005 (logistics-fulfillment.md) freight, duty, and fulfillment costs; Depop, eBay, Poshmark, TikTok Shop official fee schedules (2026); Bella+Canvas and AS Colour wholesale pricing via BlankStyle, S&S Activewear; screen print and DTG pricing from French Press Custom, Branded Reno, Aesthetic BK (2026 guides).*
