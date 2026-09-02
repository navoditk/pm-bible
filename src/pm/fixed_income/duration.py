import numpy as np

from .bond import bond_cashflows, bond_price


def macaulay_duration(ytm, face=100.0, coupon_rate=0.05, years=5.0, frequency=2):
    times, flows = bond_cashflows(face, coupon_rate, years, frequency)
    periods = np.arange(1, len(flows) + 1)
    pv = flows / (1 + ytm / frequency) ** periods
    price = pv.sum()
    return float(np.sum(times * pv) / price)

def modified_duration(ytm, face=100.0, coupon_rate=0.05, years=5.0, frequency=2):
    mac = macaulay_duration(ytm, face, coupon_rate, years, frequency)
    return mac / (1 + ytm / frequency)

def dv01(ytm, face=100.0, coupon_rate=0.05, years=5.0, frequency=2):
    p = bond_price(ytm, face, coupon_rate, years, frequency)
    d = modified_duration(ytm, face, coupon_rate, years, frequency)
    return d * p * 1e-4
