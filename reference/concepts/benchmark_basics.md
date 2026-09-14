# Benchmark Basics

## One-line definition
A benchmark is the reference portfolio a manager's holdings and performance are measured against.

## Vocabulary
- **Benchmark weight** `w_b`: the weight of an asset in the benchmark index.
- **Portfolio weight** `w_p`: the weight of an asset actually held.
- **Active weight** `a = w_p - w_b`: over/underweight versus the benchmark. Sums to zero when both are fully invested in the same universe.
- **Active return**: `r_p - r_b`, the portfolio's return in excess of the benchmark's return.
- **Tracking error**: the volatility of active return — see [tracking error](tracking_error.md).

## Why PMs care
Almost no institutional mandate is judged on absolute return alone. Sizing, risk budgets, and compensation are usually defined relative to a benchmark, so "am I long or short this name/sector versus the benchmark" is a more common question than "how much of this do I own."

## Worked example
Portfolio holds 60% US equity / 40% intl equity. Benchmark is 50% / 50%.

Active weights: `+10% US equity, -10% intl equity`.

If US equity returns 10% and intl equity returns 4% this period:
`r_p = 0.6*0.10 + 0.4*0.04 = 0.076`
`r_b = 0.5*0.10 + 0.5*0.04 = 0.070`
`active_return = 0.076 - 0.070 = 0.006` (60 bp)

## Code recipe
```python
def active_weights(portfolio_weights, benchmark_weights):
    return np.asarray(portfolio_weights, float) - np.asarray(benchmark_weights, float)

def active_return(portfolio_return, benchmark_return):
    return float(portfolio_return - benchmark_return)
```

## Common mistakes
- comparing a portfolio to a benchmark it isn't actually mandated against
- forgetting that active weights only sum to zero when portfolio and benchmark share the same universe and are both fully invested
- treating a positive active return in one period as skill rather than noise — see [information ratio](information_ratio.md)

## Limitations / approximations
This page covers vocabulary only. The full quantitative treatment lives
in `src/pm/active.py`: [tracking error](tracking_error.md),
[information ratio](information_ratio.md),
[information coefficient](information_coefficient.md), and the
[Fundamental Law](fundamental_law.md) (which covers breadth and the
transfer coefficient).

## Related
- [Tracking error](tracking_error.md)
- [Information ratio](information_ratio.md)
- [Fundamental Law](fundamental_law.md)

## Free resources
- CFA Institute, Portfolio Risk and Return Part I & II
- [Active management resources](../../resources/active_management.md)
