import numpy as np


def key_rate_return_approximation(key_rate_durations, curve_shocks_decimal):
    krd = np.asarray(key_rate_durations, float)
    shocks = np.asarray(curve_shocks_decimal, float)
    return float(-(krd @ shocks))
