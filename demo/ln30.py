import os
import sys
import warnings

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath('../'))
import abupy
from abupy import AbuDoubleMaBuy, AbuDoubleMaSell, ABuKLUtil, ABuSymbolPd, AbuUpDownTrend, AbuDownUpTrend, AbuUpDownGolden
from abupy import AbuFactorCloseAtrNStop, AbuFactorAtrNStop, AbuFactorPreAtrNStop, tl
from abupy import abu, ABuProgress, AbuMetricsBase, EMarketTargetType, ABuMarketDrawing

us_choice_symbols = ['usTSLA', 'usNOAH', 'usSFUN', 'usBIDU', 'usAAPL', 'usGOOG', 'usWUBA', 'usVIPS']
cn_choice_symbols = ['002230', '300104', '300059', '601766', '600085', '600036', '600809', '000002', '002594', '002739']
hk_choice_symbols = ['hk03333', 'hk00700', 'hk02333', 'hk01359', 'hk00656', 'hk03888', 'hk02318']

# 初始资金量
cash = 3000000


def run_loo_back(choice_symbols, ps=None, n_folds=3, start=None, end=None, only_info=False):
    """封装一个回测函数，返回回测结果，以及回测度量对象"""
    if choice_symbols[0].startswith('us'):
        abupy.env.g_market_target = EMarketTargetType.E_MARKET_TARGET_US
    else:
        abupy.env.g_market_target = EMarketTargetType.E_MARKET_TARGET_CN
    abu_result_tuple, _ = abu.run_loop_back(cash,
                                            buy_factors,
                                            sell_factors,
                                            ps,
                                            start=start,
                                            end=end,
                                            n_folds=n_folds,
                                            choice_symbols=choice_symbols)
    ABuProgress.clear_output()
    metrics = AbuMetricsBase.show_general(*abu_result_tuple, returns_cmp=only_info,
                                          only_info=only_info,
                                          only_show_returns=True)
    return abu_result_tuple, metrics


# 买入策略使用AbuDownUpTrend
buy_factors = [{'class': AbuDownUpTrend}]
# 卖出策略：利润保护止盈策略+风险下跌止损+较大的止盈位
sell_factors = [{'stop_loss_n': 1.0, 'stop_win_n': 3.0,
                 'class': AbuFactorAtrNStop},
                {'class': AbuFactorPreAtrNStop, 'pre_atr_n': 1.5},
                {'class': AbuFactorCloseAtrNStop, 'close_atr_n': 1.5}]
# 开始回测
abu_result_tuple, metrics = run_loo_back(us_choice_symbols, only_info=True)
ABuMarketDrawing.plot_candle_from_order(abu_result_tuple.orders_pd)
