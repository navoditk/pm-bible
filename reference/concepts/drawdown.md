# Drawdown

## One-line definition
The peak-to-trough decline in cumulative portfolio value.

## Formula
Given a wealth path `W_t = prod(1+r_s)` for `s<=t`:

`DD_t = W_t / max(W_0..W_t) - 1`

`Max drawdown = min(DD_t)` over the path.

## Units
Decimal or percent, always <= 0.

## Why PMs care
It measures realized pain along the path, not just end-of-period volatility. Two strategies with identical Sharpe ratios can have very different worst-case drawdowns, which matters for client tolerance, leverage limits, and redemption risk.

## Worked example
Period returns +10%, -20%, +5%:

`W = [1.10, 0.88, 0.924]`, running max `= [1.10, 1.10, 1.10]`

`DD = [0, -0.20, -0.16]` -> max drawdown = **-20%**

## Code recipe
```python
import numpy as np

def max_drawdown(returns):
    r = np.asarray(returns, float)
    wealth = np.cumprod(1 + r)
    running_max = np.maximum.accumulate(wealth)
    drawdown = wealth / running_max - 1
    return float(drawdown.min())
```

## Common mistakes
- computing drawdown on returns instead of the cumulative wealth path
- resetting the running peak too early (must be the max seen so far, not a rolling window)
- reporting drawdown as a positive number and forgetting the sign convention elsewhere

## Limitations / approximations
- Path-dependent: same returns in a different order produce a different max drawdown.
- A single historical path is one draw from many possible outcomes — pair with scenario/stress analysis for forward-looking risk.

## Related
- [Sharpe ratio](sharpe_ratio.md)
- [Portfolio volatility](portfolio_volatility.md)

## Free resources
- [Portfolio foundations resources](../../resources/portfolio_foundations.md)
