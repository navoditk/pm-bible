# Active Share

## One-line definition
Half the sum of absolute active weights across all holdings — the
fraction of the portfolio, by market value, positioned differently from
the benchmark.

## Formula
`active_share = 0.5 * sum(|w_portfolio_i - w_benchmark_i|)`

## Why PMs care
It's the standard answer to "how much of a stock-picker is this manager,
versus a closet indexer" — a fund with 98% overlap to its benchmark
can't generate much alpha no matter how skilled the manager is, since so
little of the portfolio differs from the free benchmark return.

## Worked example
Portfolio 60% US equity / 40% international equity against a 50/50
benchmark — the same example as
[benchmark basics](../concepts/benchmark_basics.md). Active weights are +10%/-10%,
so `active_share = 0.5*(0.10 + 0.10) = 0.10`: 10% of the portfolio is
actively positioned.

## Common mistakes
- confusing active share (a positioning measure) with tracking error (a
  realized/predicted risk measure, [tracking error](../concepts/tracking_error.md))
  — two large but offsetting bets can produce high active share with low
  tracking error if they cancel risk, and vice versa
- computing it at the sector level instead of individual holdings, which
  understates it

## Limitations
A pure positioning metric — it says nothing about whether the active
bets are good ones, only how large they are.

## Related
- [Tracking error](../concepts/tracking_error.md)
- [Equity factor investing (style tilt)](equity_factor_investing.md)
