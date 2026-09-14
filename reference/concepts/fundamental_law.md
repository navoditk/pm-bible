# Fundamental Law of Active Management

## One-line definition
Grinold's equation linking expected skill (information ratio) to raw
forecasting ability (IC), how many independent bets that ability gets
applied to (breadth), and how well real-world constraints let those bets
reach the portfolio (transfer coefficient).

## Formula
`IR ~= IC * sqrt(BR) * TC`

- `IC`: [information coefficient](information_coefficient.md) — skill
- `BR`: breadth — number of independent bets per year (use
  `effective_breadth(n_bets, average_correlation)` when bets aren't
  actually independent — correlated bets are worth less than their raw
  count)
- `TC`: transfer coefficient — how much of the unconstrained-optimal
  active weights actually get implemented, `1.0` = no constraint cost
  (the original Grinold form of the law omits TC entirely, i.e. assumes
  TC=1)

## Why PMs care
It explains *why* a modestly-skilled manager (IC around 0.05, not
obviously impressive on its own) can still produce a strong track record
by applying that skill across many independent opportunities — and,
symmetrically, why a manager with genuinely excellent IC can still post a
mediocre IR if constraints (long-only, position limits, turnover caps)
prevent the signal from actually reaching the portfolio. It's the
standard framework for decomposing "why did this fund's IR change" into
skill vs. opportunity-set vs. implementation.

## Worked example
`IC = 0.05`, `BR = 100` independent bets/year, `TC = 1.0` (unconstrained):
`IR ~= 0.05 * sqrt(100) * 1.0 = 0.5`. Halve the transfer coefficient to
`0.5` (heavier constraints) and expected IR halves to `0.25` — the law is
linear in TC, so constraint cost shows up directly and proportionally.

## Effective breadth: correlated bets are worth less
`effective_breadth(n_bets, average_correlation)` implements
`BR_eff = n / (1 + (n-1)*rho)`: at `rho=0` (truly independent bets) it
equals `n` unchanged; at `rho=1` (every "independent" bet is actually the
same bet) it collapses to `1`, no matter how large `n` is. This is why
adding more names to a book doesn't help if they're all really the same
macro or factor bet in disguise.

## Common mistakes
- treating IC and breadth as independent levers — in practice, relaxing a
  signal's threshold to catch more "bets" (raising breadth) usually
  dilutes IC at the same time, since the added bets are lower-conviction
- forgetting the transfer coefficient term entirely and comparing a
  constrained real-world portfolio's IR against the unconstrained
  `IC * sqrt(BR)` prediction — the gap between them *is* the cost of the
  constraints, not a modeling error
- treating the transfer coefficient itself as scale-sensitive: because
  `transfer_coefficient` is a correlation, a portfolio that captures every
  bet's *direction* correctly but only half its *magnitude* (e.g. a
  uniform leverage cap) still scores `TC = 1.0` — correlation doesn't see
  the shrinkage. TC measures whether constraints changed which bets you
  took, not how big they ended up.

## Limitations
The law is an approximation (`~=`, not `=`) that assumes bets are made
independently over time and across assets, forecasts are unbiased, and
risk is proportional across the portfolio. Real portfolios violate all
three to some degree, which is exactly why realized IR (see
[information ratio](information_ratio.md)) and the law's *predicted* IR
often diverge.

## Related
- [Information coefficient](information_coefficient.md)
- [Information ratio](information_ratio.md)
- [Active share](../equity/active_share.md)

## Free resources
- [Fundamental Law of Active Management — Financial Edge Training](https://www.fe.training/free-resources/portfolio-management/fundamental-law-of-active-management/) — covers the law, breadth, and the transfer coefficient together with worked examples
- [Fundamental Law of Active Management Explained (CFA Level 2) — YouTube](https://www.youtube.com/watch?v=vp-NnvYlnPQ)
- CFA Institute, *Analysis of Active Portfolio Management* (already linked in `resources/active_management.md`)
- Clarke, de Silva & Thorley, *Portfolio Constraints and the Fundamental Law of Active Management*, Financial Analysts Journal 58(5), 2002 — the original transfer-coefficient extension (search the title; hosted on SSRN and via most university library databases)
