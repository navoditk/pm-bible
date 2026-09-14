# Alternative Investments Overview

## One-line definition
Investments outside the traditional public-equity, fixed-income, and
cash universe this repo otherwise covers — private capital (private
equity, private debt), real assets (real estate, infrastructure, natural
resources), and hedge funds — grouped together not because they share
common characteristics, but because they share the *absence* of the
characteristics traditional assets have (public pricing, daily
liquidity, standardized reporting).

## Vocabulary
- **Private equity**: leveraged buyouts (acquiring a mature company with
  significant debt, targeting an eventual sale), venture capital (early-
  stage equity in high-growth companies), and distressed/special-
  situations investing. Structured as closed-end funds with general
  partners (GPs) managing capital committed by limited partners (LPs).
- **Private debt**: direct lending and other non-bank credit extended to
  companies — the private-market analogue of the [leveraged
  loans](../fixed_income/leveraged_loans.md) and [fundamental credit
  analysis](../fixed_income/fundamental_credit_analysis.md) machinery
  this repo already has for public credit, applied where there's no
  public market price.
- **Real assets**: real estate, infrastructure (toll roads, utilities,
  power generation), and natural resources (timberland, farmland,
  commodities-adjacent assets) — often held for inflation-hedging and
  diversification properties as much as for outright return.
- **Hedge funds**: pooled vehicles pursuing absolute-return strategies
  (long/short equity, macro, relative value, event-driven) using leverage
  and derivatives more freely than a typical long-only mandate,
  targeting returns less correlated with traditional market beta.
- **J-curve**: the typical private-equity fund cash-flow pattern —
  reported returns dip negative early (fees and early losses precede
  realized gains) before rising sharply as portfolio companies are exited
  years later. A defining feature of illiquid, closed-end structures that
  has no analogue in this repo's daily-liquid, mark-to-market portfolio
  model.

## Why PMs care
An allocator moving from a purely public-markets seat needs at least
survey-level fluency here even without managing alternatives directly —
institutional asset-allocation decisions (endowments, pensions, sovereign
wealth funds) routinely carve out 20-50%+ to alternatives specifically
for diversification and illiquidity-premium reasons that don't show up
in a standard [efficient frontier](../concepts/efficient_frontier.md)
built on daily-liquid asset classes alone. Interviewing for a
multi-asset or allocator-facing role without being able to speak to why
an institution holds private equity or real assets at all is a real gap.

## Why this isn't implemented in `src/pm`
Nearly everything that makes alternatives analytically distinct —
J-curve cash-flow modeling, public-market-equivalent (PME) benchmarking,
NAV-based (rather than market-price-based) valuation and its associated
smoothing/stale-pricing effects, fund-level fee waterfalls (carried
interest, hurdle rates) — is genuinely different machinery from this
repo's daily-return, market-priced portfolio model, not a variation on
it. This page is deliberately survey-level: interview-ready vocabulary
and framing, not a working implementation.

## Common mistakes
- treating an alternative asset's reported volatility as comparable to a
  public asset's — infrequent NAV marking artificially smooths reported
  returns, understating true volatility and overstating diversification
  benefits if taken at face value
- assuming "alternatives" is one asset class with one risk/return
  profile — venture capital, core real estate, and macro hedge funds
  have almost nothing in common except illiquidity and being outside the
  traditional public-markets universe
- ignoring the illiquidity premium's other side: an investor who *needs*
  liquidity (to meet redemptions, rebalance, or respond to opportunity)
  pays for that need by being structurally excluded from this premium

## Related
- [ESG and sustainable investing](esg_and_sustainable_investing.md)
- [Leveraged loans](../fixed_income/leveraged_loans.md)
- [Liability-driven investing](../concepts/liability_driven_investing.md)
- [Strategic and tactical asset allocation](../concepts/strategic_and_tactical_asset_allocation.md)

## Free resources
- [Overview of Alternative Investments — AnalystPrep (CFA Level 1)](https://analystprep.com/cfa-level-1-exam/alternative-investments/description-alternative-investments/) — the standard category breakdown (hedge funds, private equity, real assets) at exam depth
