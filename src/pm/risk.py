import numpy as np
from scipy.stats import norm


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

def parametric_var(portfolio_value, volatility, confidence=0.95):
    """Gaussian (delta-normal) VaR, same units/horizon as volatility."""
    z = norm.ppf(confidence)
    return portfolio_value * volatility * z

def expected_shortfall(portfolio_value, volatility, confidence=0.95):
    """Gaussian expected shortfall (average loss beyond the VaR threshold)."""
    z = norm.ppf(confidence)
    return portfolio_value * volatility * norm.pdf(z) / (1 - confidence)
