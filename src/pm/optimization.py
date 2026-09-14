import cvxpy as cp
import numpy as np

from ._solver import solved_weights


def minimum_variance(covariance, long_only=True, max_weight=None):
    """Global minimum-variance weights: minimize w'Sigma*w s.t. sum(w)=1.

    max_weight is a uniform upper bound per asset. Note a long-only
    portfolio needs max_weight >= 1/n_assets to be feasible at all.
    """
    cov = np.asarray(covariance, float)
    n = cov.shape[0]
    w = cp.Variable(n)
    constraints = [cp.sum(w) == 1]
    if long_only:
        constraints.append(w >= 0)
    if max_weight is not None:
        constraints.append(w <= max_weight)
    problem = cp.Problem(cp.Minimize(cp.quad_form(w, cov)), constraints)
    return solved_weights(problem, w)

def mean_variance(expected_returns, covariance, risk_aversion=5.0, long_only=True, max_weight=None):
    """Mean-variance optimal weights under the standard utility

        maximize  mu'w - (risk_aversion / 2) * w'Sigma*w    s.t. sum(w) = 1

    The factor of 1/2 is the convention this repo uses throughout, and it
    matters: its first-order condition is `mu = risk_aversion * Sigma * w`,
    which is exactly what `pm.robust.market_implied_returns` inverts. Drop
    the 1/2 here and reverse-optimizing market weights into implied returns
    and back no longer round-trips (it closes at risk_aversion/2 instead).
    See `reference/concepts/mean_variance_optimization.md`.
    """
    mu = np.asarray(expected_returns, float)
    cov = np.asarray(covariance, float)
    n = len(mu)
    w = cp.Variable(n)
    constraints = [cp.sum(w) == 1]
    if long_only:
        constraints.append(w >= 0)
    if max_weight is not None:
        constraints.append(w <= max_weight)
    objective = cp.Maximize(mu @ w - 0.5 * risk_aversion * cp.quad_form(w, cov))
    return solved_weights(cp.Problem(objective, constraints), w)
