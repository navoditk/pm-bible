# Mean–Variance Optimization

## Core problem
A common utility formulation:

`maximize mu^T w - lambda * w^T Sigma w`

subject to portfolio constraints.

## Objects
- `mu`: expected return vector
- `Sigma`: covariance matrix
- `w`: weights
- `lambda`: risk-aversion coefficient

## Why PMs care
It formalizes the tradeoff between expected return, risk, and implementation constraints.

## Important limitation
Optimal weights can be extremely sensitive to estimation error, especially in expected returns.
