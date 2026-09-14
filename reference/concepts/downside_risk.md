# Downside Deviation and Realized (Ex-Post) Risk

## One-line definition
Downside deviation is volatility computed only from returns that fall
short of a target — the risk measure behind the Sortino ratio.
`realized_volatility` and `realized_tracking_error` are the plain
ex-post (measured-after-the-fact) counterparts to this repo's ex-ante,
covariance-based risk functions.

## Formula
Downside deviation, per Sortino's original definition (averaged over
*all* periods, not just the shortfall periods):

`DD = sqrt( mean( min(r_t - target, 0)^2 ) ) * sqrt(periods_per_year)`

Realized volatility: `sqrt(periods_per_year) * std(returns, ddof=1)`

Realized tracking error: same formula, applied to the active-return
series `portfolio_returns - benchmark_returns` (see
[information ratio](information_ratio.md), which uses this as its
denominator).

## Why PMs care
Volatility penalizes an unusually good month exactly as much as an
unusually bad one — for most investors that's not actually the risk they
care about. Downside deviation only counts shortfalls, so two return
series with identical volatility can have very different downside
deviation if one is more asymmetric (frequent small gains, rare large
losses looks worse than the reverse, even at equal total volatility).
`realized_volatility`/`realized_tracking_error` matter for a different
reason: they let you check an ex-ante risk model against what actually
happened — a persistent gap between predicted and realized risk is a
sign the covariance matrix (or the active weights driving tracking
error) don't reflect current market conditions.

## Worked example
Returns `[2%, -3%, 1%, -1%]`, target 0%. Shortfalls: `[0, -3%, 0, -1%]`.
`DD = sqrt(mean([0, 0.0009, 0, 0.0001])) = sqrt(0.00025) ≈ 1.58%`
(unannualized) — matching `src/pm/returns.py::downside_deviation`.

## Common mistakes
- comparing downside deviation across managers who use different `target`
  values (0%, the risk-free rate, and a fund's own mean return all give
  different, non-comparable numbers) — the Sortino ratio has the exact
  same issue: it's not one fixed number, it depends entirely on which MAR
  (minimum acceptable return) you pick
- treating a low realized tracking error as proof a risk model is
  accurate — a quiet historical window can mask real ex-ante risk that
  simply hasn't shown up yet
- annualizing realized volatility/tracking error with the wrong
  `periods_per_year` for the data's actual frequency (daily data needs
  ~252, not 12)

## Limitations
`downside_deviation` here only supports a single scalar `target`, not a
time-varying minimum acceptable return. Neither ex-post function adjusts
for serial correlation in the return series, which can bias the
annualized figure.

## Related
- [Information ratio](information_ratio.md)
- [Sharpe ratio](sharpe_ratio.md)
- [Drawdown](drawdown.md)
- [Value at risk](value_at_risk.md)

## Free resources
- [Sortino Ratio — Wall Street Prep](https://www.wallstreetprep.com/knowledge/sortino-ratio/) — formula, a worked 12-month example, and when it's preferred over Sharpe
- [Semi-Deviation — Financial Edge Training](https://www.fe.training/free-resources/asset-management/semi-deviation/) — semi-deviation vs. downside deviation vs. standard deviation, with a worked comparison
