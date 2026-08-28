import numpy as np
import pandas as pd

def simple_returns(prices: pd.Series | pd.DataFrame):
    return prices / prices.shift(1) - 1

def log_returns(prices: pd.Series | pd.DataFrame):
    return np.log(prices / prices.shift(1))

def portfolio_return(asset_returns, weights):
    r = np.asarray(asset_returns, dtype=float)
    w = np.asarray(weights, dtype=float)
    return float(w @ r)

def cumulative_return(returns):
    r = np.asarray(returns, dtype=float)
    return float(np.prod(1 + r) - 1)
