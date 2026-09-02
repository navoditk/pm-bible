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


def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=12):
    r = np.asarray(returns, dtype=float)
    excess = r - risk_free_rate / periods_per_year
    std = excess.std(ddof=1)
    if std <= 0:
        raise ValueError("Excess return volatility must be positive.")
    return float(excess.mean() / std * np.sqrt(periods_per_year))


def max_drawdown(returns):
    r = np.asarray(returns, dtype=float)
    wealth = np.cumprod(1 + r)
    running_max = np.maximum.accumulate(wealth)
    drawdown = wealth / running_max - 1
    return float(drawdown.min())
