import numpy as np

from pm.fixed_income.bond import bond_price
from pm.fixed_income.duration import modified_duration
from pm.fixed_income.mbs import (
    apply_prepayment,
    effective_duration,
    mortgage_amortization_schedule,
    psa_cpr,
    refinancing_incentive_cpr,
    single_monthly_mortality,
    weighted_average_life,
)


def test_amortization_schedule_fully_pays_off_balance():
    _, principal, _, ending = mortgage_amortization_schedule(1000.0, 0.12, 24)
    assert np.isclose(principal.sum(), 1000.0)
    assert np.isclose(ending[-1], 0.0, atol=1e-6)

def test_single_monthly_mortality_hand_example():
    expected = 1 - (1 - 0.06) ** (1 / 12)
    assert np.isclose(single_monthly_mortality(0.06), expected)

def test_psa_cpr_ramp_and_cap():
    assert np.isclose(psa_cpr(1), 0.002)
    assert np.isclose(psa_cpr(30), 0.06)
    assert np.isclose(psa_cpr(60), 0.06)
    assert np.isclose(psa_cpr(15, psa_multiplier=2.0), 0.06)

def test_apply_prepayment_zero_smm_matches_scheduled():
    beginning = np.array([1000.0, 502.49])
    scheduled = np.array([497.51, 502.49])
    total, ending = apply_prepayment(beginning, scheduled, smm=0.0)
    assert np.allclose(total, scheduled)
    assert np.allclose(ending, beginning - scheduled)

def test_apply_prepayment_positive_smm_speeds_paydown():
    beginning = np.array([1000.0])
    scheduled = np.array([100.0])
    total, ending = apply_prepayment(beginning, scheduled, smm=0.10)
    assert np.isclose(total[0], 100.0 + (1000.0 - 100.0) * 0.10)
    assert np.isclose(ending[0], 1000.0 - total[0])

def test_refinancing_incentive_cpr_floors_at_base_when_no_incentive():
    assert np.isclose(refinancing_incentive_cpr(0.06, 0.08, base_cpr=0.06, sensitivity=2.0), 0.06)

def test_refinancing_incentive_cpr_rises_with_incentive():
    cpr = refinancing_incentive_cpr(0.06, 0.04, base_cpr=0.06, sensitivity=2.0)
    assert np.isclose(cpr, 0.06 + 2.0 * 0.02)

def test_weighted_average_life_hand_example():
    wal = weighted_average_life([1, 2, 3], [500, 300, 200])
    assert np.isclose(wal, 1.7)

def test_effective_duration_hand_example():
    ed = effective_duration(price_down=102.5, price_up=98.0, price_base=100.0, bump_decimal=0.0025)
    assert np.isclose(ed, 9.0)

def test_effective_duration_matches_modified_duration_for_plain_bond():
    ytm, face, coupon_rate, years, frequency = 0.05, 100.0, 0.05, 5.0, 2
    bump = 0.0001
    price_base = bond_price(ytm, face, coupon_rate, years, frequency)
    price_up = bond_price(ytm + bump, face, coupon_rate, years, frequency)
    price_down = bond_price(ytm - bump, face, coupon_rate, years, frequency)
    ed = effective_duration(price_down, price_up, price_base, bump)
    md = modified_duration(ytm, face, coupon_rate, years, frequency)
    assert np.isclose(ed, md, atol=1e-4)

def test_wal_shortens_with_refinancing_incentive():
    wac, balance, months = 0.06, 1_000_000.0, 360
    beginning, scheduled, _, _ = mortgage_amortization_schedule(balance, wac, months)
    times = np.arange(1, months + 1) / 12

    def wal_at(market_rate):
        cpr = refinancing_incentive_cpr(wac, market_rate)
        smm = single_monthly_mortality(cpr)
        total_principal, _ = apply_prepayment(beginning, scheduled, smm)
        return weighted_average_life(times, total_principal)

    assert wal_at(0.04) < wal_at(0.08)
