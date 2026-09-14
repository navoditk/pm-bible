# TIPS and Breakeven Inflation

## One-line definition
A Treasury Inflation-Protected Security (TIPS) pays a fixed *real*
coupon rate on a principal that's adjusted for realized CPI inflation;
the breakeven inflation rate is the market-implied average inflation
rate that would make a TIPS and a same-maturity nominal Treasury pay the
same total return.

## Formula
`breakeven_inflation = nominal_yield - real_yield`

`index_ratio = CPI_reference_now / CPI_reference_at_issuance`

`inflation_adjusted_principal = original_principal * index_ratio`

`tips_coupon_payment = real_coupon_rate * inflation_adjusted_principal / frequency`

## Why PMs care
Breakeven inflation is the cleanest market-based read on what investors
expect inflation to average over a given horizon — it's quoted and
watched the same way a credit spread is, as a single number summarizing
a view the whole market is pricing. A rates PM with a view that
inflation will come in *above* the current breakeven buys TIPS (or a
breakeven-widener trade); a PM who thinks it'll come in *below* buys
nominal Treasuries instead. Because TIPS coupons are paid on the
*inflation-adjusted* principal, not the original face value, realized
inflation flows through every coupon date, not just at maturity.

## Worked example
A 10-year nominal Treasury yields 4.5%; a 10-year TIPS yields 2.0% (its
real yield). `breakeven = 0.045 - 0.02 = 2.5%`. If realized CPI inflation
averages more than 2.5% over the next 10 years, TIPS outperform; if it
averages less, the nominal bond does. A TIPS issued with
`CPI_reference_at_issuance = 300` when the current reference CPI is
`310` has `index_ratio = 310/300 ≈ 1.0333` — its principal (and every
coupon) is running about 3.33% above face value from realized inflation
alone.

## Common mistakes
- treating the breakeven rate as a precise inflation *forecast* rather
  than a market price that also embeds a liquidity premium (TIPS
  typically trade less liquidly than nominal Treasuries) and an
  inflation risk premium — the breakeven is not a pure expectation
- forgetting TIPS coupons scale with the inflation-adjusted principal,
  not the original face value — a real coupon rate applied to the wrong
  principal understates realized income in an inflationary period
- comparing breakeven rates across different maturities without
  accounting for the term structure of inflation expectations — 5-year
  and 30-year breakevens can (and often do) diverge meaningfully

## Limitations
`tips_index_ratio` and related functions here take CPI reference values
as given inputs — actual TIPS indexation uses a specific lagged CPI-U
reference schedule (roughly a 3-month lag) that this repo doesn't
compute from a raw CPI release calendar.

## Related
- [Bond pricing](bond_pricing.md)
- [Forward rates](forward_rates.md)
- [Carry and rolldown](carry_and_rolldown.md)

## Free resources
- [10-Year Breakeven Inflation Rate (T10YIE) — FRED](https://fred.stlouisfed.org/series/T10YIE) — the actual live data series most PMs watch
- [TIPS for Inflation Protection — Charles Schwab](https://www.schwab.com/learn/story/tips-and-inflation-what-to-know-now) — plain-language TIPS mechanics
- [Inflation expectations and inflation realities — U.S. Bureau of Labor Statistics](https://www.bls.gov/opub/mlr/2019/article/inflation-expectations-and-inflation-realities.htm) — how well breakeven rates have actually tracked realized inflation historically
