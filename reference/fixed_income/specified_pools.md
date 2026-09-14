# Specified Pools

## One-line definition
A specified ("spec") pool is an actual, identified agency MBS pool traded
for its specific collateral characteristics — as opposed to a TBA trade,
where the buyer accepts whatever "substantially similar" pools the seller
delivers.

## Vocabulary
- **Pay-up**: the price premium a specified pool trades at over the
  generic TBA price for the same coupon/program, paid for more
  predictable (usually slower) prepayment behavior.
- **Low-balance pools**: pools of mortgages with small original loan
  balances (e.g., under $85k, $110k, $125k cutoffs). A borrower with a
  small loan has little dollar incentive to pay the fixed costs of
  refinancing even when rates drop, so these pools prepay slower and more
  predictably than a generic TBA pool of the same coupon.
- **Geographic/LTV/loan-age concentration**: pools identified by state,
  loan-to-value ratio, or loan age can also command a pay-up — each is a
  different lens on the same underlying question, "how predictable is
  this pool's prepayment speed?"
- **Discount vs. premium pay-up direction**: predictable *slow*
  prepayment is valuable for a premium-priced pool (an investor who paid
  above par wants prepayments to happen slowly, since prepayment returns
  principal at par, below the price paid); predictable *fast* prepayment
  can instead be valuable for a discount-priced pool (prepayment at par
  is a gain relative to a price paid below par). Which characteristic
  commands a pay-up depends on which side of par the coupon sits.

## Why PMs care
TBA is a convenience and a liquidity pool, not a claim on any specific
loans — a PM who wants a particular prepayment profile (e.g., protection
from fast refinancing in a rallying-rate environment) has to buy specified
pools, not TBA, and pay for that certainty. Reading the [dollar
roll](tba_and_dollar_roll.md)'s implied financing rate on TBA doesn't
tell you anything about a specific spec pool's financing — spec pools
generally roll worse (less special, sometimes even negative specialness)
than TBA, since a dealer can't deliver *any* pool to cover a spec-pool
short, only the identified one. A mortgage REIT or bank managing
extension/contraction risk (see [MBS convexity](mbs_convexity.md)) will
often pay up for low-balance or seasoned pools specifically to reduce
that risk, accepting a lower running yield for more predictable duration.

## Why this isn't implemented in `src/pm`
The pay-up itself isn't a formula — it's a market-observed price
premium that reflects the market's collective prepayment-speed forecast
for a specific pool's characteristics relative to the generic TBA
population, which requires either a full prepayment model calibrated to
loan-level data or live market pricing, neither of which this repo's
"small transparent function" style can responsibly approximate. The
prepayment mechanics that *are* implemented —
[`psa_cpr`, `refinancing_incentive_cpr`, `single_monthly_mortality`](prepayment_models.md)
— are the same functions that would, in principle, drive a spec pool's
projected cash flows differently from a generic pool's; this repo doesn't
have the loan-level or pool-level data to calibrate that difference
pool-by-pool.

## Common mistakes
- assuming a pay-up is a fixed, quotable spread — it moves with the
  market's prepayment outlook the same way option-adjusted spreads do,
  richening when prepayment risk is most feared and cheapening when it
  isn't
- confusing "specified pool" with "specified in the trade confirmation"
  — TBA trades also specify issuer/coupon/program in the confirm; what
  makes a pool "specified" is that the *exact* pool numbers are agreed at
  trade time, not just announced before settlement
- assuming spec pools are always the safer choice — paying up for
  predictability is a real cost, and for an investor without a specific
  convexity concern, generic TBA (with its superior liquidity and roll
  economics) can be the better default

## Related
- [TBA and the dollar roll](tba_and_dollar_roll.md)
- [Prepayment models](prepayment_models.md)
- [MBS negative convexity](mbs_convexity.md)
- [Pass-throughs](pass_throughs.md)

## Free resources
- [Specified Pool and TBA Trading in the Mortgage Backed Securities Market — SMU Cox Finance Seminar Series](https://www.smu.edu/-/media/site/cox/departments/finance/finaseminarseries/tba_specified_pool_liquidity_smu.pdf?la=en) — an academic treatment of why specified pools trade at a pay-up and what loan characteristics drive it
- [Cash Payups for Mortgages with Specified Characteristics — Freddie Mac FAQ](https://sf.freddiemac.com/faqs/cash-payups-for-mortgages-with-specified-characteristics-faq) — the mechanics of how an issuer actually prices and allocates specified pay-ups, from the source that pays them
