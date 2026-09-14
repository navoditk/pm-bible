import numpy as np
import pandas as pd


def simple_returns(prices: pd.Series | pd.DataFrame):
    """Arithmetic period returns. The first element is NaN by construction
    (there is no prior price to compare against) - the metrics below drop
    it, so `prices -> simple_returns -> metric` composes directly.
    """
    return prices / prices.shift(1) - 1

def log_returns(prices: pd.Series | pd.DataFrame):
    """Log returns. First element is NaN by construction, as above."""
    return np.log(prices / prices.shift(1))

def _finite(returns):
    """Drop non-finite entries and return a float array.

    Return series built with `simple_returns`/`log_returns` carry a leading
    NaN by construction, so every metric here has to handle it. Without
    this, one NaN silently turns the whole metric into NaN - and a `<= 0`
    guard won't catch it, because `nan <= 0` is False.
    """
    r = np.asarray(returns, dtype=float)
    finite = r[np.isfinite(r)]
    if finite.size == 0:
        raise ValueError("Return series contains no finite observations.")
    return finite

def portfolio_return(asset_returns, weights):
    r = np.asarray(asset_returns, dtype=float)
    w = np.asarray(weights, dtype=float)
    return float(w @ r)

def cumulative_return(returns):
    return float(np.prod(1 + _finite(returns)) - 1)


def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=12):
    excess = _finite(returns) - risk_free_rate / periods_per_year
    if excess.size < 2:
        raise ValueError("Sharpe ratio needs at least two observations to estimate volatility.")
    std = excess.std(ddof=1)
    if not np.isfinite(std) or std <= 0:
        raise ValueError("Excess return volatility must be positive and finite.")
    return float(excess.mean() / std * np.sqrt(periods_per_year))


def max_drawdown(returns):
    wealth = np.cumprod(1 + _finite(returns))
    running_max = np.maximum.accumulate(wealth)
    drawdown = wealth / running_max - 1
    return float(drawdown.min())
