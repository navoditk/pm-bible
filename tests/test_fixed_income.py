import numpy as np
from pm.fixed_income.bond import bond_price
from pm.fixed_income.duration import dv01
from pm.fixed_income.credit import spread_pnl

def test_par_bond_at_coupon_yield():
    assert np.isclose(bond_price(.05, face=100, coupon_rate=.05, years=5, frequency=2), 100.0)

def test_dv01_positive():
    assert dv01(.05, face=100, coupon_rate=.05, years=5, frequency=2) > 0

def test_spread_widening_loses_money():
    assert spread_pnl(1_000_000, 4.0, 50) < 0
