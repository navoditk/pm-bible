# Liability-Driven Investing (LDI)

## One-line definition
Structuring a portfolio around the size, timing, and interest-rate
sensitivity of a known set of future obligations (a pension plan's
promised benefits, an insurer's policy payouts) rather than around
maximizing return in isolation — the goal is a stable funded ratio, not
the highest possible Sharpe ratio.

## Formula
`funded_ratio = assets / liabilities` — 1.0 is exactly funded; below 1.0
is underfunded.
`surplus = assets - liabilities` — the same idea in currency terms
rather than a ratio.

`pm.allocation.funded_ratio` and `pm.allocation.surplus` implement both
directly.

## Why PMs care
A pension or insurance PM isn't managing assets against a market
benchmark — they're managing assets against a stream of liabilities that
itself moves with interest rates (a liability's present value is just a
bond-like discounted cash flow, so it has a duration too, in exactly the
sense [duration and DV01](../fixed_income/duration.md) describe for a
bond). If asset duration is shorter than liability duration, falling
rates raise the liability's present value faster than the asset
portfolio's, shrinking the funded ratio even if every asset in the
portfolio gained value — the exact opposite of what a naive "the
portfolio is up, therefore we're doing well" read would suggest. LDI's
core discipline is closing that duration gap so the funded ratio (or
surplus) stays stable across rate moves, not just the asset side's
return.

## Duration/PV01 matching reuses existing tools, not new ones
The hedging math itself is nothing new —
[`dv01`](../fixed_income/dv01.md) already prices a $1bp move in a bond's
value, and [`hedge_ratio`](../fixed_income/duration.md) already sizes a
hedge instrument to offset a target DV01. LDI applies exactly this
machinery with the liability (treated as a bond-like discounted cash
flow stream) as the thing being hedged, and the asset portfolio's
fixed-income sleeve as the hedge instrument — no new formula is needed,
only the reframing of "what is the DV01 I'm trying to offset."

## Why full LDI hedging isn't implemented end-to-end in `src/pm`
A real LDI program prices the liability itself (which requires
actuarial cash-flow projections — mortality/longevity assumptions,
benefit formulas, discount-curve selection specific to pension
accounting standards) before `dv01`/`hedge_ratio` can even be applied to
it. That liability-pricing step is actuarial machinery this repo doesn't
build; `funded_ratio`, `surplus`, and the existing duration-hedging
functions are the genuinely reusable pieces once a liability's present
value and duration are already known from elsewhere.

## Common mistakes
- judging an LDI program's success by asset returns alone — a rate-
  driven jump in liability value can erase an otherwise-good asset
  return's contribution to the funded ratio entirely
- assuming full liability hedging is free — matching liability duration
  usually means holding more long-duration, lower-yielding fixed income
  than an unconstrained return-maximizing portfolio would, a real
  opportunity cost traded for funding-ratio stability
- confusing "immunized" (duration-matched, insulated from small parallel
  rate moves) with "risk-free" — convexity mismatches, non-parallel
  curve moves, and the liability's own assumption risk (mortality,
  inflation) all remain

## Related
- [Duration, DV01](../fixed_income/duration.md)
- [Performance measurement](performance_measurement.md)
- [Strategic and tactical asset allocation](strategic_and_tactical_asset_allocation.md)

## Free resources
- [Liability-driven investment strategy — Wikipedia](https://en.wikipedia.org/wiki/Liability-driven_investment_strategy) — funded ratio, duration matching, and cash-flow matching explained plainly
