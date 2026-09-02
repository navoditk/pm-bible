import numpy as np

from pm.fixed_income.bond import bond_price
from pm.fixed_income.credit import spread_pnl
from pm.fixed_income.curve import bootstrap_zero_rates, forward_rate, interpolate_zero_rate
from pm.fixed_income.duration import dv01, hedge_ratio
from pm.fixed_income.futures import futures_dv01_per_contract
from pm.fixed_income.swaps import swap_dv01, swap_spread


def test_par_bond_at_coupon_yield():
    assert np.isclose(bond_price(.05, face=100, coupon_rate=.05, years=5, frequency=2), 100.0)

def test_dv01_positive():
    assert dv01(.05, face=100, coupon_rate=.05, years=5, frequency=2) > 0

def test_spread_widening_loses_money():
    assert spread_pnl(1_000_000, 4.0, 50) < 0

def test_interpolate_zero_rate_linear():
    assert np.isclose(interpolate_zero_rate(6, [2, 10], [0.03, 0.04]), 0.035)

def test_forward_rate_hand_example():
    expected = (1.03**2 / 1.02**1) ** (1 / (2 - 1)) - 1
    assert np.isclose(forward_rate(1, 0.02, 2, 0.03), expected)

def test_bootstrap_zero_rates_single_period_equals_par_yield():
    zero_rates = bootstrap_zero_rates([0.05])
    assert np.isclose(zero_rates[0], 0.05)

def test_bootstrap_zero_rates_two_period():
    zero_rates = bootstrap_zero_rates([0.05, 0.06])
    pv_first_coupon = 6 / 1.05
    expected_z2 = ((106) / (100 - pv_first_coupon)) ** (1 / 2) - 1
    assert np.isclose(zero_rates[1], expected_z2)

def test_hedge_ratio_short_to_offset_long_dv01():
    assert np.isclose(hedge_ratio(100_000, 50), -2000)

def test_swap_dv01_matches_par_bond_proxy():
    expected = dv01(0.04, face=10_000_000, coupon_rate=0.04, years=5, frequency=2)
    assert np.isclose(swap_dv01(10_000_000, 0.04, 5, 2), expected)

def test_swap_spread_and_futures_dv01():
    assert np.isclose(swap_spread(0.045, 0.040), 0.005)
    assert np.isclose(futures_dv01_per_contract(120, 0.9), 120 / 0.9)
