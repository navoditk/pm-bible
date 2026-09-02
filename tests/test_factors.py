import numpy as np

from pm.factors import factor_model_covariance


def test_factor_model_covariance_one_factor_hand_example():
    exposures = [[1.0], [0.5]]
    factor_covariance = [[0.04]]
    specific_variance = [0.01, 0.02]
    expected = [[0.05, 0.02], [0.02, 0.03]]
    result = factor_model_covariance(exposures, factor_covariance, specific_variance)
    assert np.allclose(result, expected)
