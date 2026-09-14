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


def realized_volatility(returns, periods_per_year=12):
    """Ex-post portfolio volatility: annualized sample standard deviation
    of a realized return series - the natural counterpart to
    `pm.risk.portfolio_volatility`'s ex-ante (covariance-based) version.
    Comparing the two is how you check whether realized risk matched what
    a risk model predicted.
    """
    r = finite_array(returns, min_size=2)
    return float(r.std(ddof=1) * np.sqrt(periods_per_year))

def downside_deviation(returns, target=0.0, periods_per_year=12):
    """Semi-deviation below `target` (Sortino's risk measure): like
    volatility, but only shortfalls below the target count, not upside
    moves. Averaged over *all* periods, per Sortino's original
    definition - not just the shortfall periods - so a mostly-upside
    return series has a small downside deviation even if its total
    volatility (which treats upside and downside symmetrically) is large.
    """
    r = finite_array(returns, min_size=2)
    shortfall = np.minimum(r - target, 0.0)
    return float(np.sqrt(np.mean(shortfall**2)) * np.sqrt(periods_per_year))
