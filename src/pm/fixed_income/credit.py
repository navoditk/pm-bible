def spread_pnl(market_value, spread_duration, spread_change_bp):
    delta_spread = spread_change_bp / 10_000.0
    return -market_value * spread_duration * delta_spread
