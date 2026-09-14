# Information Ratio

## One-line definition
Active return per unit of active risk — the benchmark-relative analogue
of the Sharpe ratio, and the standard single-number measure of a manager's
skill.

## Formula
Ex-ante (from a covariance matrix, given active weights):

`IR = active_return / tracking_error`

using [`tracking_error`](tracking_error.md) as the denominator.

Ex-post (realized, from a matched portfolio/benchmark return series):

`IR = mean(active_returns) / std(active_returns) * sqrt(periods_per_year)`

`active_returns_t = portfolio_return_t - benchmark_return_t`

## Why PMs care
Absolute return says nothing about how much risk was taken to earn it;
information ratio does the same job Sharpe does for total risk, but
against a benchmark instead of cash — which is the right comparison for
almost any institutional mandate. It's the headline number in manager
selection and in the Fundamental Law of Active Management, where it's
the quantity IC and breadth are trying to explain (see
[Fundamental Law](fundamental_law.md)).

## Worked example
Portfolio returns 3%, 5%, 2%; benchmark returns 1%, 2%, 1% over three
periods. Active returns: 2%, 3%, 1% — mean 2%, sample std 1%.
`IR = 0.02 / 0.01 = 2.0` (unannualized, matching
`src/pm/active.py::information_ratio` at `periods_per_year=1`).

## Common mistakes
- comparing information ratios computed over different sampling
  frequencies without annualizing both consistently
- treating a high IR over a short, lucky window as durable skill — IR
  estimated from a handful of observations is itself very noisy
- confusing the *ex-ante* IR (built from a risk model's covariance
  matrix, forward-looking) with the *ex-post* IR (realized from actual
  returns, backward-looking) — they answer different questions and won't
  generally match

## Limitations
The realized version assumes active returns are independent and
identically distributed across periods; serial correlation or a
fat-tailed active-return distribution both bias the ratio.

## Related
- [Tracking error](tracking_error.md)
- [MCTE and group risk decomposition](mcte_and_group_risk.md)
- [Downside deviation and realized risk](downside_risk.md)
- [Fundamental Law](fundamental_law.md)
- [Sharpe ratio](sharpe_ratio.md)

## Free resources
- [Information ratio — Wikipedia](https://en.wikipedia.org/wiki/Information_ratio) — definition, the Sharpe-ratio comparison, and common criticisms
- CFA Institute, *Analysis of Active Portfolio Management* (already linked in `resources/active_management.md`) — the IR/IC/breadth/transfer-coefficient/Fundamental-Law treatment this repo's Phase 3 follows
