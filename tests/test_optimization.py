import numpy as np

from pm.optimization import mean_variance, minimum_variance


def test_minimum_variance_two_asset_closed_form():
    cov = [[0.04, 0.0], [0.0, 0.01]]
    w = minimum_variance(cov)
    assert np.isclose(w[0], 0.2, atol=1e-3)
    assert np.isclose(w[1], 0.8, atol=1e-3)

def test_minimum_variance_weights_sum_to_one_and_long_only():
    cov = [[0.04, 0.01, 0.0], [0.01, 0.09, 0.02], [0.0, 0.02, 0.02]]
    w = minimum_variance(cov)
    assert np.isclose(w.sum(), 1.0, atol=1e-3)
    assert (w >= -1e-6).all()

def test_mean_variance_prefers_higher_return_asset():
    cov = [[0.04, 0.0], [0.0, 0.04]]
    w = mean_variance([0.10, 0.05], cov, risk_aversion=5.0)
    assert w[0] > w[1]
