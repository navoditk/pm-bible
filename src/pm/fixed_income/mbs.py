import numpy as np


def mortgage_amortization_schedule(balance, annual_rate, months):
    """Level-payment (scheduled, no prepayment) amortization schedule.

    Returns (beginning_balance, scheduled_principal, interest, ending_balance),
    each an array of length `months`.
    """
    r = annual_rate / 12
    payment = balance * r / (1 - (1 + r) ** (-months))
    beginning = np.zeros(months)
    principal = np.zeros(months)
    interest = np.zeros(months)
    bal = balance
    for m in range(months):
        beginning[m] = bal
        interest[m] = bal * r
        principal[m] = payment - interest[m]
        bal -= principal[m]
    ending = beginning - principal
    return beginning, principal, interest, ending

def single_monthly_mortality(cpr):
    """Convert an annualized CPR to a monthly prepayment rate (SMM)."""
    return 1 - (1 - cpr) ** (1 / 12)

def psa_cpr(month, psa_multiplier=1.0):
    """CPR implied by the PSA benchmark: ramps linearly from 0% to
    6%*psa_multiplier over the first 30 months, then flat.
    """
    return 0.06 * psa_multiplier * min(month, 30) / 30

def apply_prepayment(beginning_balance, scheduled_principal, smm):
    """Overlay a prepayment assumption on a scheduled amortization.

    smm may be a scalar (constant) or an array matching beginning_balance.
    Returns (total_principal, ending_balance).
    """
    beginning_balance = np.asarray(beginning_balance, dtype=float)
    scheduled_principal = np.asarray(scheduled_principal, dtype=float)
    smm = np.broadcast_to(np.asarray(smm, dtype=float), beginning_balance.shape)
    prepay = (beginning_balance - scheduled_principal) * smm
    total_principal = scheduled_principal + prepay
    ending_balance = beginning_balance - total_principal
    return total_principal, ending_balance

def refinancing_incentive_cpr(wac, market_rate, base_cpr=0.06, sensitivity=2.0):
    """Simple behavioral prepayment model: CPR rises with refinancing
    incentive (wac - market_rate) when rates fall, and floors at base_cpr
    when rates rise (no incentive to refinance) - this asymmetry is the
    source of MBS negative convexity/extension risk.
    """
    incentive = max(0.0, wac - market_rate)
    return base_cpr + sensitivity * incentive

def weighted_average_life(times, principal_payments):
    times = np.asarray(times, dtype=float)
    principal_payments = np.asarray(principal_payments, dtype=float)
    return float(np.sum(times * principal_payments) / np.sum(principal_payments))

def effective_duration(price_down, price_up, price_base, bump_decimal):
    """Numerical (bump-and-reprice) duration - the right tool when price
    isn't a closed-form function of yield, e.g. because prepayment speed
    changes with rates. Contrast with modified_duration (closed-form).
    """
    return (price_down - price_up) / (2 * price_base * bump_decimal)
