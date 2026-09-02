import numpy as np
from scipy.optimize import brentq

from .bond import bond_cashflows
from .curve import interpolate_zero_rate


def spread_pnl(market_value, spread_duration, spread_change_bp):
    delta_spread = spread_change_bp / 10_000.0
    return -market_value * spread_duration * delta_spread

def z_spread(price, face, coupon_rate, years, frequency, curve_tenors, curve_rates):
    """Constant spread over the interpolated zero curve that reprices the
    bond to `price`. Solved by root-finding, not closed-form.
    """
    times, flows = bond_cashflows(face, coupon_rate, years, frequency)

    def _price_at_spread(spread):
        discounted = 0.0
        for t, cf in zip(times, flows):
            z = interpolate_zero_rate(t, curve_tenors, curve_rates)
            discounted += cf / (1 + (z + spread) / frequency) ** (t * frequency)
        return discounted - price

    return brentq(_price_at_spread, -0.05, 0.50)

def survival_probability(hazard_rate, t):
    """Probability of no default by time t, under a constant hazard rate."""
    return float(np.exp(-hazard_rate * t))

def expected_loss(notional, default_probability, recovery_rate):
    return notional * default_probability * (1 - recovery_rate)

def credit_spread_from_hazard(hazard_rate, recovery_rate):
    """Approximate par CDS/credit spread implied by a constant hazard rate
    and recovery assumption: spread ~= hazard_rate * (1 - recovery_rate).
    """
    return hazard_rate * (1 - recovery_rate)

def cds_bond_basis(cds_spread, bond_spread):
    return cds_spread - bond_spread
