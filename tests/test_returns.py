import numpy as np
from pm.returns import portfolio_return, cumulative_return

def test_portfolio_return_hand_example():
    assert np.isclose(portfolio_return([0.10, -0.05], [0.60, 0.40]), 0.04)

def test_plus_50_minus_50_is_minus_25():
    assert np.isclose(cumulative_return([0.50, -0.50]), -0.25)
