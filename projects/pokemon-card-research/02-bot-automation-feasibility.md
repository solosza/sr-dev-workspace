# Bot/Automation Tools & Agentic Buying Feasibility

## Current Bot & Monitoring Ecosystem

### Monitoring-Only Services (Legal, Low Risk)

| Tool/Service | Type | Cost | What It Does |
|-------------|------|------|-------------|
| **Discord communities** (Pokemon Restocks & Alerts, PokePings) | Free Discord servers | Free | Real-time human + automated alerts across 100+ retailers. Community-driven. |
| **RestockR** | App/notification service | Free/paid tiers | Instant alerts for Target, Walmart, Amazon, Pokemon Center restocks |
| **Restockd** | Web app + alerts | Free/paid tiers | Tracks 129+ Pokemon products across major retailers in real-time |
| **Visualping** | Website change monitor | Freemium ($0-$15/mo) | Monitors any webpage for changes — general purpose, not Pokemon-specific |
| **TrackaLacker** | Price/stock tracker | Free | Dedicated Pokemon restock tracker for Target, Walmart, Pokemon Center |
| **BrickSeek** | Inventory checker | Free/paid | Checks local Walmart/Target inventory by zip code |

### Auto-Checkout Bots (TOS-Violating, Higher Risk)

| Bot | Retailers | Cost | Notes |
|-----|----------|------|-------|
| **Stellar AIO** | Pokemon Center, Target, Amazon, Walmart, Best Buy, Costco | $150 initial + $150/quarter | Most popular for Pokemon. Full auto-checkout. Active Discord + guides. |
| **Refract** | Major retailers | ~$200+ (varies, often sold via resale market) | Competitor to Stellar, retail-focused |
| **Cheddah** | Target, Walmart | Varies | Specialized Target checkout bot for Pokemon/sports cards |
| **Custom bots (Fiverr)** | Any retailer | $10-$440+ | Custom-built restock monitors and auto-checkout bots |
| **GitHub DIY** | Various | Free (code) + proxy costs | Open-source checkout bot templates (e.g., ThomasCantuti/Checkout-bot-Card-Collection) |

## Anti-Bot Countermeasures by Retailer

| Retailer | Measures | Difficulty to Bot |
|----------|----------|-------------------|
| **Pokemon Center** | Queue system, CAPTCHA challenges during high-traffic drops, Cloudflare protection | HIGH — irregular restocks + active anti-bot |
| **Target** | PerimeterX bot detection, purchase limits, queue system on drops | HIGH — sophisticated fingerprinting |
| **Walmart** | Bot detection, 5-item purchase limit, Akamai protection | MEDIUM-HIGH |
| **Best Buy** | Datacenter IP blocking (added late 2025), queue system | HIGH |
| **Amazon** | CAPTCHA, account-level purchase limits, IP monitoring | MEDIUM |
| **GameStop** | Basic protections, purchase limits | MEDIUM-LOW |

### What Modern Anti-Bot Systems Detect
- Browser fingerprints (user agent, screen resolution, fonts, WebGL renderer)
- Mouse movement patterns (headless browsers lack natural movement)
- Datacenter IP addresses (vs residential IPs)
- Request timing patterns (bots are too fast and too regular)
- Cookie/session anomalies

### What Bots Use to Evade
- **Residential proxies** — each task runs through a different residential IP ($5-$15/GB)
- **Patchright** — stealth-patched Playwright fork that evades detection better than vanilla Playwright
- **Fingerprint spoofing** — randomized browser attributes per session (puppeteer-extra-plugin-stealth)
- **CAPTCHA harvesters** — multiple pre-solved CAPTCHA tokens ready to inject (recommended: 5+ harvesters)
- **Human-like delays** — randomized timing between actions

## Playwright-Based Agentic Buyer: Feasibility Assessment

### Could We Build It?

**Monitoring component: YES — straightforward.**
- Playwright can poll retailer product pages on a schedule
- Detect "Add to Cart" button state changes
- Send Discord/SMS/push notification on restock
- This is legal and low-risk (passive monitoring)

**Auto-checkout component: TECHNICALLY FEASIBLE but problematic.**
- Playwright can fill forms, click buttons, complete checkout
- Would need: residential proxy rotation, fingerprint spoofing, CAPTCHA solving integration
- Libraries exist: patchright (stealth Playwright), puppeteer-extra-plugin-stealth

### Technical Barriers

| Barrier | Severity | Workaround |
|---------|----------|------------|
| CAPTCHA challenges | HIGH | CAPTCHA harvester services ($2-$5/1000 solves) — adds cost and latency |
| Browser fingerprinting | HIGH | Patchright + randomized profiles — arms race with retailers |
| IP blocking | HIGH | Residential proxies ($5-15/GB) — ongoing cost |
| Account bans | MEDIUM | Multiple accounts — but violates TOS further |
| Purchase limits | MEDIUM | Multiple addresses/payment methods — logistically complex |
| Dynamic site changes | MEDIUM | Selectors break when retailers update UI — maintenance burden |

### Cost-Benefit: Build vs Buy

| Factor | Build Custom Agent | Buy Stellar AIO ($150 + $150/qtr) | Use Free Alerts Only |
|--------|-------------------|-----------------------------------|---------------------|
| Development time | 40-80 hours | 0 | 0 |
| Ongoing maintenance | 5-10 hrs/month (selector updates) | Updates included | 0 |
| Proxy costs | $20-50/month | $20-50/month | $0 |
| CAPTCHA costs | $5-15/month | Included | $0 |
| Success rate | Unknown (untested) | Proven (200+ drops tested) | Manual speed |
| Legal risk | Same as commercial bots | Same | None |
| Retailer ban risk | HIGH | HIGH | None |
| Savings per box | $20-60 markup avoided | $20-60 markup avoided | $20-60 if you're fast enough manually |

**Verdict: Building a custom agent is NOT worth it.** The ROI doesn't justify the development time when proven solutions (Stellar AIO) exist for $600/year, and free monitoring services (Discord alerts + RestockR) get you 80% of the benefit at zero cost and zero legal risk.

## Legal & Ethical Landscape

### Legal Status
- **Monitoring/alerts**: Legal. Passive stock checking and price monitoring are generally acceptable.
- **Auto-checkout bots**: NOT explicitly illegal under US federal law, but:
  - Violates Terms of Service of every major retailer
  - May violate CFAA (Computer Fraud and Abuse Act) if bypassing CAPTCHA/queue systems
  - Some states have anti-bot legislation (primarily for event tickets, but expanding)
  - Retailers can ban accounts, cancel orders, and pursue civil action

### Real Consequences
- Account permanent bans (all orders cancelled, no refund)
- IP/address blacklisting
- Payment method blocking
- Civil lawsuits (rare but possible for commercial-scale operations)
- The Pokemon Company actively working on anti-scalper measures

## Recommendation

**For personal use (buying 1-3 boxes per set):**
1. Join free Discord alert communities (Pokemon Restocks & Alerts, PokePings)
2. Set up RestockR or Restockd notifications
3. Know the retailer schedules (Walmart Wednesdays at 9 PM ET, Target Thursday nights)
4. Be ready to manually checkout when alerted — for most sets, this is sufficient

**Don't build a custom bot.** The development time, maintenance burden, proxy costs, and legal risk aren't justified when:
- Free alerts get you most of the way
- Stellar AIO exists if you want automation ($600/yr)
- The markup savings per box ($20-60) require high volume to recoup costs
- Most modern sets aren't that hard to get at retail with alerts

## Sources
- [Decodo: Pokemon Card Bot Setup Guide 2026](https://decodo.com/blog/pokemon-card-bot)
- [Stellar AIO Pokemon Center Guide](https://guides.stellaraio.com/stellar/retailers/pokemon-center)
- [Stellar AIO Pricing](https://guides.stellaraio.com/stellar/general-stellaraio-faq/how-much-does-stellaraio-cost)
- [Cop Supply: Pokemon Bots](https://cop.supply/pokemon-bots/)
- [Cyberyozh: Best Pokemon Bot Proxy 2026](https://app.cyberyozh.com/blog/pokemon-bot-proxy/)
- [Cheddah: Automated Target Checkout Bot](https://cheddah.store/blog)
- [AIO Bot: 7 Best Retail Bots](https://www.aiobot.com/retail-bots/)
- [PokeBeach: Pokemon Center Queue System](https://www.pokebeach.com/forums/threads/pokemon-center-implementing-a-new-queue-system-presumably-to-combat-bots.155667/page-2)
- [ComicBook: Pokemon Cracking Down on Bots](https://comicbook.com/gaming/news/pokemon-trading-card-game-cracking-down-bots-tcg-scalpers/)
- [Queue-it: Scalping Bots](https://queue-it.com/blog/scalping-bots/)
- [GitHub: Checkout-bot-Card-Collection](https://github.com/ThomasCantuti/Checkout-bot-Card-Collection)
