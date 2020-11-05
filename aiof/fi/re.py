import math
import datetime
import numpy_financial as npf

import aiof.config as config

from aiof.data.fi import CoastFireSavings

from typing import List

# Configs
_settings = config.get_settings()
_round_dig = _settings.DefaultRoundingDigit


def coast_fire_savings(
    coast_savings: List[CoastFireSavings],
    initial_interest_rate: float = 0.02,
    current_balance: float = 100000) -> List[CoastFireSavings]:
    """
    Show how savings will be affected for Coast FIRE

    Parameters
    ----------
    `coast_savings` : List[CoastFireSavings].
        completely customizable coast fire savings list\n
    `initial_interest_rate` : float.
        initial interest amount used. defaults to `0.02`\n
    `current_balance` : int.
        current starting balance. defaults to `100,000`

    Notes
    ----------
    Based on https://www.reddit.com/r/financialindependence/comments/ja3nks/i_built_a_coastfire_compatible_savings_sheet/
    """
    for i in range(0, len(coast_savings)):
        if i == 0:
            coast_savings[i].total = (current_balance + coast_savings[i].contribution) * (coast_savings[i].yearlyReturn + 1)
        else:
            coast_savings[i].total = (coast_savings[i-1].total + coast_savings[i].contribution) * (coast_savings[i].yearlyReturn + 1)
        coast_savings[i].initialEarning = coast_savings[i].total * coast_savings[i].yearlyReturn
        coast_savings[i].withdrawFour = coast_savings[i].total * 0.04
        coast_savings[i].withdrawThree = coast_savings[i].total * 0.03
        coast_savings[i].withdrawTwo = coast_savings[i].total * 0.02

        coast_savings[i].presentValueFour = -npf.pv(
            rate=initial_interest_rate,
            nper=1,
            pmt=0,
            fv=coast_savings[i].withdrawFour,
            when='end')
        coast_savings[i].presentValueThree = -npf.pv(
            rate=initial_interest_rate,
            nper=1,
            pmt=0,
            fv=coast_savings[i].withdrawThree,
            when='end')
        coast_savings[i].presentValueTwo = -npf.pv(
            rate=initial_interest_rate,
            nper=1,
            pmt=0,
            fv=coast_savings[i].withdrawTwo,
            when='end')

    return coast_savings
