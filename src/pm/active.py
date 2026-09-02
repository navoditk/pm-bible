import numpy as np


def active_weights(portfolio_weights, benchmark_weights):
    return np.asarray(portfolio_weights, float) - np.asarray(benchmark_weights, float)

def tracking_error(portfolio_weights, benchmark_weights, covariance):
    a = active_weights(portfolio_weights, benchmark_weights)
    cov = np.asarray(covariance, float)
    return float(np.sqrt(a @ cov @ a))


def active_return(portfolio_return, benchmark_return):
    return float(portfolio_return - benchmark_return)
