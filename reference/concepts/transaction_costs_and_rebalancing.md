# Transaction Costs and Rebalancing

## One-line definition
Moving a portfolio from current weights to target weights generates trades,
and every trade has a cost — attribution and construction decisions that
ignore this overstate what's actually achievable.

## Formula
`trade_i = (target_weight_i - current_weight_i) * PortfolioValue`

`cost_i = |trade_i| * cost_bps / 10,000`

## Why PMs care
An optimizer or a rebalance-to-benchmark rule that looks great on paper
can be a net loser after costs if it trades too often or in illiquid
names — turnover has a price.

## Common mistakes
- optimizing/rebalancing without a transaction-cost penalty, then being
  surprised turnover erodes the theoretical improvement
- using a single flat `cost_bps` across very different liquidity profiles
  (a large-cap Treasury and an off-the-run corporate bond do not cost the
  same to trade)

## Limitations
This repo's `transaction_cost` is a flat-bps model. Real trading costs are
size- and liquidity-dependent (market impact grows with trade size
relative to average volume) — that's `liquidity.md`'s territory, which
this repo treats conceptually only.

## Related
- [Liquidity](liquidity.md)
- [Mean-variance optimization (constraints)](mean_variance_optimization.md)
- [Brinson attribution](brinson_attribution.md)
