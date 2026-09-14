# Multi-Period Optimization

## One-line definition
Choosing a portfolio (or trading path) to optimize wealth over multiple
future periods, accounting for how today's trade affects tomorrow's
opportunity set — as opposed to single-period optimization, which
re-solves from scratch each period with no memory of the path.

## Why PMs care
Single-period optimization implicitly assumes rebalancing is free and
that today's decision doesn't affect what's achievable tomorrow — false
whenever transaction costs, tax lots, or liquidity constraints carry
across periods. A single-period-optimal trade today can be a bad trade
once its effect on next period's costs and constraints is priced in.

## Why this isn't implemented in `src/pm`
Genuine multi-period optimization is a stochastic control / dynamic
programming problem — it needs a model of how the opportunity set
evolves and a way to solve (or approximate) the resulting Bellman
equation. That's a different category of tool from the closed-form and
single-period-convex functions this repo builds elsewhere.

## Related
- [Transaction costs and rebalancing](transaction_costs_and_rebalancing.md)
- [Scenario-robust optimization](scenario_robust_optimization.md)
