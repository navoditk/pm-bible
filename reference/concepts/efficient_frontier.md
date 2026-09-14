# Efficient Frontier and Tangency Portfolio

## One-line definition
The efficient frontier is the curve of portfolios offering the lowest
possible risk for each level of expected return; the tangency portfolio
is the single point on it with the highest Sharpe ratio.

## Formula
For each target return `mu_target`, the frontier point is:

`minimize w'Sigma*w  s.t. sum(w) = 1, mu'w = mu_target [, w >= 0]`

traced over a range of targets by `src/pm/optimization.py::efficient_frontier`.

The tangency (max-Sharpe) portfolio maximizes
`(mu'w - r_f) / sqrt(w'Sigma*w)` — see
`src/pm/optimization.py::max_sharpe`. Long-only, this needs a
change-of-variables reformulation (a fractional objective isn't directly
convex); unconstrained, it has the closed form
`w ~ Sigma^-1 (mu - r_f)`, renormalized to sum to 1.

## Why PMs care
The frontier makes "dominated" concrete: any portfolio below it is
strictly worse than some frontier portfolio at the same risk (or the same
return at lower risk) — there's no argument for holding it. The tangency
portfolio is the theoretical anchor for the whole mean-variance
framework: Tobin's separation theorem says every rational investor should
hold *some mix* of the risk-free asset and the tangency portfolio,
differing only in how much leverage/cash they add, never in which risky
portfolio they hold.

## Worked example
Three assets returning 4%/8%/12% with a diagonal covariance —
`efficient_frontier`'s lowest-return frontier point (target=4%) is
100% in the low-return asset (there's no other way to hit exactly 4%);
its highest-return point (target=12%) is 100% in the high-return asset.
Every point in between blends the three to minimize variance at that
target. See `tests/test_optimization.py` for the exact numbers.

## Common mistakes
- treating the entire traced curve as "the efficient frontier" — the
  lower half, below the global-minimum-variance point, is real and
  computable (`efficient_frontier` returns it) but is *dominated* by the
  upper half at the same risk, so "efficient" only describes the upper arm
- assuming the tangency portfolio is unique when short-selling is allowed
  but changes character (or may not exist) when `long_only=True` and no
  asset offers a positive Sharpe ratio — see `max_sharpe`'s
  `risk_free_rate` guard
- forgetting the whole frontier shifts whenever `expected_returns`
  changes — see [mean-variance optimization](mean_variance_optimization.md)'s
  note on estimation-error sensitivity

## Limitations
Like `minimum_variance` and `mean_variance`, this takes `expected_returns`
and `covariance` as given — it says nothing about how to estimate them
well (see [covariance shrinkage](covariance_shrinkage.md) and
[Black-Litterman](black_litterman.md) for that problem).

## Related
- [Mean-variance optimization](mean_variance_optimization.md)
- [Black-Litterman](black_litterman.md)
- [Sharpe ratio](sharpe_ratio.md)

## Free resources
- [Modern portfolio theory — Wikipedia](https://en.wikipedia.org/wiki/Modern_portfolio_theory) — the efficient frontier, capital allocation line, and the one-fund (separation) theorem
- [Efficient Portfolio That Maximizes Sharpe Ratio — MathWorks](https://www.mathworks.com/help/finance/efficient-portfolio-that-maximizes-sharpe-ratio.html) — a worked numerical example of finding the tangency portfolio on a traced frontier
