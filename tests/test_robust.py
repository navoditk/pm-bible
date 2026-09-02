import numpy as np

from pm.risk import component_risk_contribution
from pm.robust import (
    black_litterman_posterior,
    risk_parity_weights,
    scenario_robust_weights,
    shrink_covariance,
)


def test_shrink_covariance_full_shrinkage_is_diagonal():
    cov = [[0.04, 0.01], [0.01, 0.09]]
    shrunk = shrink_covariance(cov, shrinkage=1.0)
    assert np.isclose(shrunk[0][1], 0.0)
    assert np.isclose(shrunk[0][0], 0.04)
    assert np.isclose(shrunk[1][1], 0.09)

def test_shrink_covariance_zero_shrinkage_unchanged():
    cov = np.array([[0.04, 0.01], [0.01, 0.09]])
    shrunk = shrink_covariance(cov, shrinkage=0.0)
    assert np.allclose(shrunk, cov)

def test_black_litterman_no_confidence_view_leaves_prior_unchanged():
    prior = np.array([0.05, 0.07])
    sigma = np.array([[0.04, 0.01], [0.01, 0.09]])
    P = np.array([[1.0, 0.0]])
    Q = np.array([0.20])  # wildly different from prior
    omega_huge = np.array([[1e6]])
    posterior_mean, _ = black_litterman_posterior(prior, sigma, P, Q, omega_huge)
    assert np.allclose(posterior_mean, prior, atol=1e-4)

def test_black_litterman_confident_view_shifts_posterior_toward_it():
    prior = np.array([0.05, 0.07])
    sigma = np.array([[0.04, 0.01], [0.01, 0.09]])
    P = np.array([[1.0, 0.0]])
    Q = np.array([0.10])
    omega_confident = np.array([[0.0001]])
    posterior_mean, _ = black_litterman_posterior(prior, sigma, P, Q, omega_confident)
    assert posterior_mean[0] > prior[0]
    assert abs(posterior_mean[0] - 0.10) < abs(prior[0] - 0.10)

def test_risk_parity_equal_vol_uncorrelated_gives_equal_weights():
    cov = [[0.04, 0.0], [0.0, 0.04]]
    w = risk_parity_weights(cov)
    assert np.allclose(w, [0.5, 0.5], atol=1e-3)

def test_risk_parity_equalizes_risk_contribution_not_weights():
    cov = np.array([[0.04, 0.0], [0.0, 0.16]])
    w = risk_parity_weights(cov)
    contributions = component_risk_contribution(w, cov)
    assert np.isclose(contributions[0], contributions[1], atol=1e-3)
    assert not np.isclose(w[0], w[1], atol=1e-2)

def test_scenario_robust_weights_symmetric_scenarios_give_equal_weights():
    scenario_returns = [
        [0.10, -0.05],
        [-0.05, 0.10],
    ]
    w = scenario_robust_weights(scenario_returns)
    assert np.allclose(w, [0.5, 0.5], atol=1e-3)
