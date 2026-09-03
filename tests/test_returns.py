import numpy as np
import pandas as pd

from pm.returns import (
    cumulative_return,
    log_returns,
    max_drawdown,
    portfolio_return,
    sharpe_ratio,
    simple_returns,
)


def test_portfolio_return_hand_example():
    assert np.isclose(portfolio_return([0.10, -0.05], [0.60, 0.40]), 0.04)

def test_simple_returns_hand_example():
    prices = pd.Series([100.0, 110.0, 121.0])
    result = simple_returns(prices)
    assert np.isnan(result.iloc[0])
    assert np.allclose(result.iloc[1:], [0.10, 0.10])

def test_log_returns_hand_example():
    prices = pd.Series([100.0, 110.0])
    result = log_returns(prices)
    assert np.isnan(result.iloc[0])
    assert np.isclose(result.iloc[1], np.log(1.10))

def test_plus_50_minus_50_is_minus_25():
    assert np.isclose(cumulative_return([0.50, -0.50]), -0.25)

def test_sharpe_ratio_hand_example():
    returns = [0.02, 0.04, 0.03]
    assert np.isclose(sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=1), 3.0)

def test_zero_excess_return_gives_zero_sharpe():
    assert np.isclose(sharpe_ratio([0.01, -0.01], periods_per_year=1), 0.0)

def test_max_drawdown_hand_example():
    assert np.isclose(max_drawdown([0.10, -0.20, 0.05]), -0.20)
