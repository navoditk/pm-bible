def tax_equivalent_yield(muni_yield, tax_rate):
    """The pre-tax yield a fully taxable bond would need to match a
    tax-exempt municipal bond's after-tax return.

    tax_equivalent_yield = muni_yield / (1 - tax_rate)

    tax_rate is the investor's relevant marginal rate (federal, or
    federal+state combined for an in-state muni) - see
    reference/fixed_income/municipal_bonds.md for what this does and
    doesn't account for (AMT, de minimis rules, state-specific treatment).
    """
    return muni_yield / (1 - tax_rate)
