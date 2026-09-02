def futures_dv01_per_contract(ctd_dv01_per_contract, conversion_factor):
    """DV01 of one futures contract, approximated from the cheapest-to-deliver
    bond's DV01 and its conversion factor. Ignores the delivery option value
    and changes in which bond is cheapest-to-deliver.
    """
    return ctd_dv01_per_contract / conversion_factor
