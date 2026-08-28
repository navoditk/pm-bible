# Portfolio Return

## One-line definition
The weighted return of the assets held in a portfolio for a given period.

## Formula
`r_p = w^T r = sum_i w_i r_i`

## Units
Return, typically decimal or percent.

## Why PMs care
It is the basic aggregation from security-level performance to portfolio performance.

## Worked example
Weights 60% / 40%; returns +10% / -5%.

`0.6*0.10 + 0.4*(-0.05) = 0.04 = 4%`

## Code recipe
```python
import numpy as np

def portfolio_return(asset_returns, weights):
    r = np.asarray(asset_returns, float)
    w = np.asarray(weights, float)
    return float(w @ r)
```

## Common mistakes
- weights not summing to intended net/gross exposure
- mixing percent and decimal return units
- confusing arithmetic period return with multi-period compounding
