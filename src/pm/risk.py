import numpy as np

def portfolio_variance(weights, covariance):
    w = np.asarray(weights, dtype=float)
    cov = np.asarray(covariance, dtype=float)
    return float(w @ cov @ w)

def portfolio_volatility(weights, covariance):
    return portfolio_variance(weights, covariance) ** 0.5

def marginal_risk_contribution(weights, covariance):
    w = np.asarray(weights, dtype=float)
    cov = np.asarray(covariance, dtype=float)
    sigma = portfolio_volatility(w, cov)
    if sigma <= 0:
        raise ValueError("Portfolio volatility must be positive.")
    return (cov @ w) / sigma

def component_risk_contribution(weights, covariance):
    w = np.asarray(weights, dtype=float)
    return w * marginal_risk_contribution(w, covariance)
