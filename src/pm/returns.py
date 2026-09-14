import numpy as np
import pandas as pd

from ._utils import finite_array


def simple_returns(prices: pd.Series | pd.DataFrame):
    """Arithmetic period returns. The first element is NaN by construction
    (there is no prior price to compare against) - the metrics below drop
    it, so `prices -> simple_returns -> metric` composes directly.
    """
    return prices / prices.shift(1) - 1

def log_returns(prices: pd.Series | pd.DataFrame):
    """Log returns. First element is NaN by construction, as above."""
    return np.log(prices / prices.shift(1))

def portfolio_return(asset_returns, weights):
    r = np.asarray(asset_returns, dtype=float)
    w = np.asarray(weights, dtype=float)
    return float(w @ r)

def cumulative_return(returns):
    return float(np.prod(1 + finite_array(returns)) - 1)


def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=12):
    excess = finite_array(returns, min_size=2) - risk_free_rate / periods_per_year
    std = excess.std(ddof=1)
    if not np.isfinite(std) or std <= 0:
        raise ValueError("Excess return volatility must be positive and finite.")
    return float(excess.mean() / std * np.sqrt(periods_per_year))


def max_drawdown(returns):
    wealth = np.cumprod(1 + finite_array(returns))
    running_max = np.maximum.accumulate(wealth)
    drawdown = wealth / running_max - 1
    return float(drawdown.min())
