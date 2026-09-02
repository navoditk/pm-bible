import numpy as np

from pm.fixed_income.bond import bond_price
from pm.fixed_income.credit import (
    cds_bond_basis,
    credit_spread_from_hazard,
    expected_loss,
    spread_pnl,
    survival_probability,
    z_spread,
)
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

def test_z_spread_matches_flat_curve_closed_form():
    par_price = bond_price(0.06, face=100, coupon_rate=0.06, years=5, frequency=2)
    spread = z_spread(par_price, face=100, coupon_rate=0.06, years=5, frequency=2,
                       curve_tenors=[1, 30], curve_rates=[0.04, 0.04])
    assert np.isclose(spread, 0.02, atol=1e-6)

def test_survival_probability_decreases_with_time():
    assert survival_probability(0.02, 0) == 1.0
    assert survival_probability(0.02, 5) < survival_probability(0.02, 1)

def test_expected_loss_hand_example():
    assert np.isclose(expected_loss(1_000_000, 0.02, 0.40), 12_000)

def test_credit_spread_from_hazard_hand_example():
    assert np.isclose(credit_spread_from_hazard(0.03, 0.40), 0.018)

def test_cds_bond_basis_hand_example():
    assert np.isclose(cds_bond_basis(0.018, 0.022), -0.004)
