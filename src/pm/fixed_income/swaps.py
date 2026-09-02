from .duration import dv01


def swap_dv01(notional, swap_rate, years, frequency=2):
    """Proxy: treat the swap's fixed leg as a par bond (coupon = swap_rate,
    priced at par, ytm = swap_rate). Ignores floating-leg resets and
    Libor/OIS discounting basis — real swap DV01 differs, especially for
    off-market swaps.
    """
    return dv01(swap_rate, face=notional, coupon_rate=swap_rate, years=years, frequency=frequency)


def swap_spread(swap_rate, treasury_yield):
    return swap_rate - treasury_yield
