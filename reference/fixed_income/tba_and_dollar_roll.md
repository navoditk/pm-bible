# TBA and the Dollar Roll

## One-line definition
"TBA" (to-be-announced) is how the agency MBS market trades pass-throughs
without specifying which exact pools will be delivered — a dollar roll is
a short-term financing trade built on top of that convention: sell TBA
for near-month settlement, buy back a "substantially similar" TBA for
far-month settlement, usually at a lower ("dropped") price.

## Vocabulary
- **TBA (to-be-announced)**: a forward contract on generic agency MBS —
  issuer (Fannie Mae/Freddie Mac/Ginnie Mae), coupon, and settlement
  month are specified; the exact pools are announced only shortly before
  settlement (per SIFMA's "48-hour rule"). This is what makes agency MBS
  as liquid as it is — a buyer doesn't need to pick specific pools to
  trade the market.
- **The roll**: selling a TBA position for near-month settlement and
  simultaneously buying the same coupon/program back for far-month
  settlement — the seller doesn't actually need to own or deliver a
  specific pool at any point if they roll before settlement.
- **The drop**: `near_price - far_price` — the amount the far-month price
  is below the near-month price. A positive drop is normal (the buyer of
  the far leg is compensated for the coupon income they won't collect in
  the interim); an unusually large drop signals collateral scarcity or
  strong dealer demand to be short the near-month settlement.
- **Roll specialness**: how much cheaper (or more expensive) financing via
  the roll is compared to the prevailing GC repo rate for the same
  collateral — see [repo and financing](repo_and_financing.md) for the
  Treasury-market version of the same idea.

## Formula
`implied_financing_rate = (coupon_income - drop_income) / near_amount / horizon_years`

- `coupon_income`: the coupon interest given up over the roll period
  (not annualized) — approximately `face * coupon_rate / 12` for a
  standard monthly roll
- `drop_income`: the drop converted to dollars — `(near_price -
  far_price) / 100 * face`
- `near_amount`: near-leg proceeds, `near_price / 100 * face`
- `horizon_years`: the roll period in years (a standard monthly TBA roll
  is `1/12`)

`pm.fixed_income.mbs.dollar_roll_implied_financing_rate` implements this.
It is a **simplified** version of the real calculation, which also nets
reinvestment income earned on the sale proceeds and any scheduled
principal paydown given up during the roll period — see Limitations.

## Why PMs care
The dollar roll is one of the cheapest, most liquid ways to finance an
MBS position — for a levered MBS investor (a bank, a mortgage REIT, a
relative-value fund), rolling instead of financing in cash-and-repo can
be materially cheaper when the roll is "special." Reading a roll's
implied financing rate against GC repo tells you whether the roll is
cheap (special — attractive financing, but a signal of collateral
scarcity) or expensive (better to hold and finance in repo instead).
Because implied financing rate embeds a prepayment-speed assumption (via
the coupon income and principal given up), it is also a read on the
market's collateral-scarcity and prepayment expectations, not purely a
funding-cost number.

## Worked example
A $1,000,000 face, 5% coupon TBA pool: near price 101.00, far price
100.625 (a 0.375-point drop), rolled for one month (`horizon_years =
1/12`).

- `coupon_income = 1,000,000 * 0.05 / 12 = $4,166.67`
- `drop_income = 0.375 / 100 * 1,000,000 = $3,750.00`
- `near_amount = 101.00 / 100 * 1,000,000 = $1,010,000`
- `implied_financing_rate = (4,166.67 - 3,750.00) / 1,010,000 / (1/12) ≈ 0.495%`

If GC repo for agency MBS is trading around 5.30%, this roll is deeply
"special" — financing at ~50bp is far cheaper than repo, telling a PM
that this coupon/program is in unusually high demand to be short for
delivery (`tests/test_mbs.py::test_dollar_roll_implied_financing_rate_hand_example`
computes this exact figure).

## Common mistakes
- assuming a positive drop always means cheap financing — a large drop
  can still be *expensive* financing if the coupon given up is even
  larger (see the "zero-drop" and "drop exceeds coupon" test cases in
  `tests/test_mbs.py`); it's the ratio to coupon income that matters, not
  the drop in isolation
- treating "the pool" as if it's the same pool across the roll — TBA
  delivery only guarantees *substantially similar* collateral (same
  issuer/coupon/program), not the identical pool, which is precisely what
  distinguishes a dollar roll from a repurchase agreement
- ignoring that implied financing rate is a blended read on financing
  *and* prepayment expectations — a change in the roll's implied rate
  isn't purely a funding-market signal

## Limitations
This repo's formula omits two components the real calculation includes:
reinvestment income on the near-leg sale proceeds over the roll period,
and the value of scheduled principal paydown given up (not just coupon
interest) — both are typically small relative to coupon income and drop
for a par-priced pool but can matter for premium/discount pools or longer
rolls. See [specified pools](specified_pools.md) for how pool-level
prepayment characteristics feed into this same calculation in practice.

## Related
- [Repo and financing](repo_and_financing.md)
- [Specified pools](specified_pools.md)
- [Pass-throughs](pass_throughs.md)
- [Prepayment models](prepayment_models.md)

## Free resources
- [Dollar roll — Wikipedia](https://en.wikipedia.org/wiki/Dollar_roll) — plain-language definition of the roll, the drop, and roll specialness
- [Using Dollar Rolls as a Balance Sheet and Earnings Strategy for Banks and Credit Unions — Doeren Mayhew](https://www.doeren.com/viewpoint/using-dollar-rolls-as-a-balance-sheet-and-earnings-strategy-for-banks-and-credit-unions) — a worked implied-financing-rate example with real dollar figures, the source this page's formula structure was checked against
