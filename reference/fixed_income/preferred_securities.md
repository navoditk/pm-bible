# Preferred Securities

## One-line definition
A hybrid security senior to common stock but subordinate to bonds in the
capital structure — usually paying a fixed dividend, with no maturity
date (perpetual), which makes it price like a perpetuity bond far more
than like common equity.

## Formula
`value = dividend / required_return` — a perpetuity with zero growth.

This repo already has the exact function needed:
`pm.equity.valuation.gordon_growth_value(dividend_next, required_return,
growth_rate=0.0)` reduces to precisely this formula when `growth_rate=0`,
since Gordon growth's `D1 / (r - g)` becomes `D1 / r` at `g=0`. No new
function is needed for a non-callable, non-convertible, fixed-rate
preferred — it's the same math already built for equity valuation.

## Why PMs care
Preferred dividends sit ahead of common dividends in payment priority
(and ahead of common shareholders in a liquidation, though behind all
bondholders) but behind bond coupons in seniority — which is why
preferreds trade with a risk/return profile between the two. Because
most preferreds are perpetual with a fixed dividend, their price behaves
like a very long-duration bond: highly sensitive to changes in the
required return (largely driven by rates and the issuer's credit
spread), the same interest-rate sensitivity logic as
[duration](duration.md) applied to an infinite-maturity instrument
instead of a fixed one.

## Worked example
A preferred paying a $2.00 annual dividend, required return 8%:

`value = 2.00 / 0.08 = $25.00`
(`gordon_growth_value(dividend_next=2.0, required_return=0.08,
growth_rate=0.0)` reproduces this exactly.)

If the required return rises to 10% (rates or credit spreads widen), the
same preferred is worth `2.00 / 0.10 = $20.00` — a 20% price decline from
a 2-point move in required return, illustrating just how rate-sensitive
a perpetual, fixed-dividend instrument is.

## Vocabulary
- **Cumulative vs. non-cumulative**: a cumulative preferred's skipped
  dividends accrue and must be paid before any common dividend resumes;
  a non-cumulative preferred's skipped dividends are simply gone.
- **Callable**: most preferreds are callable by the issuer after some
  date, which caps upside the same way a callable bond's price is capped
  near the call price — see [OAS](oas.md) for the general
  embedded-option framing.
- **Convertible preferred**: convertible into common stock, combining
  this page's perpetuity logic with [convertible
  bonds](convertible_bonds.md)'s conversion-value logic.

## Common mistakes
- valuing a callable preferred with the plain perpetuity formula and no
  adjustment — a preferred trading above its call price on this formula
  alone is ignoring the real possibility of being called away at that
  price
- treating preferred dividends as legally guaranteed the way bond coupons
  are — for most preferreds (especially non-cumulative), the issuer can
  skip the dividend without triggering a default, a materially different
  risk than missing a bond coupon
- forgetting the perpetuity formula only fits a plain, fixed-rate,
  non-convertible, non-callable preferred — real preferred structures
  usually have at least one of these complicating features

## Why call/convertible features aren't implemented in `src/pm`
A callable preferred needs the same embedded-option machinery this
repo's [OAS](oas.md) page explains is out of scope; a convertible
preferred needs [convertible bonds](convertible_bonds.md)'s conversion
math layered on top of the perpetuity value. The plain-vanilla case
above is fully codeable today by reusing `gordon_growth_value` — the
complicating features are each a real, separately-scoped project.

## Related
- [Convertible bonds](convertible_bonds.md)
- [OAS](oas.md)
- [Dividend discount model](../equity/dividend_discount_model.md)

## Free resources
- [Cost of Preferred Stock — Wall Street Prep](https://www.wallstreetprep.com/knowledge/cost-of-preferred-stock/) — the perpetuity valuation formula and why preferreds are valued this way
