import numpy as np
import cvxpy as cp

def minimum_variance(covariance, long_only=True, max_weight=None):
    cov = np.asarray(covariance, float)
    n = cov.shape[0]
    w = cp.Variable(n)
    constraints = [cp.sum(w) == 1]
    if long_only:
        constraints.append(w >= 0)
    if max_weight is not None:
        constraints.append(w <= max_weight)
    problem = cp.Problem(cp.Minimize(cp.quad_form(w, cov)), constraints)
    problem.solve()
    return np.asarray(w.value).ravel()

def mean_variance(expected_returns, covariance, risk_aversion=5.0, long_only=True):
    mu = np.asarray(expected_returns, float)
    cov = np.asarray(covariance, float)
    n = len(mu)
    w = cp.Variable(n)
    constraints = [cp.sum(w) == 1]
    if long_only:
        constraints.append(w >= 0)
    objective = cp.Maximize(mu @ w - risk_aversion * cp.quad_form(w, cov))
    cp.Problem(objective, constraints).solve()
    return np.asarray(w.value).ravel()
