import numpy as np


def key_rate_return_approximation(key_rate_durations, curve_shocks_decimal):
    krd = np.asarray(key_rate_durations, float)
    shocks = np.asarray(curve_shocks_decimal, float)
    return float(-(krd @ shocks))


def bootstrap_zero_rates(par_yields, frequency=1):
    """Bootstrap annual zero (spot) rates from annual-pay par yields.

    par_yields[i] is the par yield for the (i+1)-year maturity — tenors must
    be consecutive integer years starting at 1. This does not handle
    semiannual coupons or off-cycle/sparse tenors (e.g. 2Y/5Y/10Y/30Y);
    a real curve build needs interpolation for the missing coupon dates.
    """
    par_yields = np.asarray(par_yields, dtype=float)
    zero_rates = np.zeros_like(par_yields)
    for i in range(len(par_yields)):
        n = i + 1
        coupon = 100 * par_yields[i] / frequency
        pv_coupons = sum(coupon / (1 + zero_rates[j]) ** (j + 1) for j in range(i))
        zero_rates[i] = ((coupon + 100) / (100 - pv_coupons)) ** (1 / n) - 1
    return zero_rates


def interpolate_zero_rate(tenor, curve_tenors, curve_rates):
    return float(np.interp(tenor, curve_tenors, curve_rates))


def forward_rate(t1, z1, t2, z2):
    """Annually-compounded forward rate between t1 and t2 (t2 > t1) implied
    by zero rates z1 and z2."""
    return float((((1 + z2) ** t2) / ((1 + z1) ** t1)) ** (1 / (t2 - t1)) - 1)
