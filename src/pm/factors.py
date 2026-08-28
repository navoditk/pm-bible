import numpy as np

def factor_model_covariance(exposures, factor_covariance, specific_variance):
    B = np.asarray(exposures, float)
    F = np.asarray(factor_covariance, float)
    d = np.asarray(specific_variance, float)
    return B @ F @ B.T + np.diag(d)
