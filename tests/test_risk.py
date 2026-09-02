import numpy as np

from pm.risk import component_risk_contribution, portfolio_variance, portfolio_volatility


def test_two_asset_variance_matches_expansion():
    v1, v2, rho = 0.20, 0.10, 0.25
    w = np.array([0.5, 0.5])
    cov = np.array([[v1*v1, rho*v1*v2], [rho*v1*v2, v2*v2]])
    expected = w[0]**2*v1**2 + w[1]**2*v2**2 + 2*w[0]*w[1]*rho*v1*v2
    assert np.isclose(portfolio_variance(w, cov), expected)

def test_component_risk_sums_to_volatility():
    cov = np.array([[0.04, 0.005], [0.005, 0.01]])
    w = np.array([0.5, 0.5])
    cr = component_risk_contribution(w, cov)
    assert np.isclose(cr.sum(), portfolio_volatility(w, cov))
