from __future__ import division

import warnings

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath('../'))
import abupy

abupy.env.enable_example_env_ipython()

from abupy import abu, AbuFactorBuyTD, BuyCallMixin, ABuSymbolPd, ABuKLUtil
from abupy import AbuFactorSellNDay, AbuMetricsBase, ABuProgress

if __name__ == '__main__':
    us_choice_symbols = ['usTSLA', 'usNOAH', 'usSFUN', 'usBIDU', 'usAAPL', 'usGOOG', 'usWUBA', 'usVIPS']
    kl_dict = {us_symbol[2:]: ABuSymbolPd.make_kl_df(us_symbol, start='2014-07-26', end='2015-07-26') for us_symbol in
               us_choice_symbols}
    # ABuKLUtil.wave_change_rate(kl_dict)
    pd.options.display.precision = 2
    pd.options.display.max_columns = 30
    dww = ABuKLUtil.date_week_win(kl_dict)
    print(dww)
