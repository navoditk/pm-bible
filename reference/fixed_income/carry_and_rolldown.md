# Carry and Rolldown

## One-line definition
The return a bond position earns purely from the passage of time,
assuming the yield curve doesn't move at all — carry is the funding-
adjusted income, rolldown is the price gain (or loss) from the bond
aging into a different point on the curve.

## Formula
`carry = (running_yield - financing_rate) * horizon_years`,
`running_yield = coupon_income / price`

`rolldown = -modified_duration * (rolled_yield - current_yield)`

`total = carry + rolldown`

## Why PMs care
This is the single most common way a rates PM frames a trade idea before
taking any view on where rates are headed: "if nothing happens, what do
I earn just for holding this?" It's the baseline every curve trade gets
measured against — a steepener or flattener view only makes sense
relative to what carry-and-roll alone would deliver.

## Worked example
A 5Y bond yielding 4.00% (priced at par), financed at 3.00% repo, held
one year: `carry = (0.04 - 0.03) * 1 = 1.00%`. On a normal upward-sloping
curve, rolling from the 5Y point to the 4Y point might reduce the yield
by roughly 20bp at a duration of ~4, giving `rolldown ≈ 0.80%` — a
1.80% total expected return with the curve unchanged.

## A cautionary real-world case
`carry_and_rolldown` applied to this repo's own curve data
(`reference/fixed_income/curve_construction.md`'s tenors) tells a
different story: between the 4Y and 5Y points, this curve is **inverted**
(4Y yields *more* than 5Y), and financing at 4.5% exceeds the bond's
~4.0% running yield. Both legs come out negative —
`tests/test_carry_and_linkers.py::test_carry_and_rolldown_real_curve_example`
computes the exact figures. This is the real lesson: in an inverted-
curve, high-financing-cost environment (like 2022–2023), duration-
extension carry trades can lose money even if rates never move at all.

## Common mistakes
- assuming carry-and-roll is always positive — it depends entirely on
  the curve's current shape and level versus financing cost, not a fixed
  property of "owning a bond"
- forgetting rolldown assumes the curve's *shape* stays fixed, not that
  rates stay fixed — a parallel shift still lets rolldown happen exactly
  as calculated; a shape change (steepening/flattening) changes it
- comparing carry-and-roll across bonds of different duration without
  normalizing — a longer-duration bond's rolldown is mechanically larger
  for the same yield-curve slope, which isn't the same as it being a
  "better" trade

## Limitations
This is a linear (duration-only) approximation of rolldown, same caveat
as `modified_duration` itself — see [convexity](convexity.md) for the
second-order correction. `financing_rate` here is a simplification of
whatever a PM's actual repo/funding cost is (see
[repo and financing](repo_and_financing.md)), and `horizon_years` assumes
a clean, single holding period rather than continuous rebalancing.

## Related
- [Duration](duration.md)
- [Curve trades](curve_trades.md)
- [Repo and financing](repo_and_financing.md)
- [Forward rates](forward_rates.md)

## Free resources
- [Carry Roll-Down Explained — Risk Hub](https://riskhub.org/blogs/carry-roll-down-explained) — the exact formula and worked example this page's numbers are checked against
- PIMCO Fixed Income Education Center (already linked in `resources/fixed_income.md`) — practitioner framing of carry and rolldown in real portfolios
