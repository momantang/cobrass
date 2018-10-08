import os
import sys

sys.path.insert(0, os.path.abspath('../'))
import abupy

abupy.env.enable_example_env_ipython()

from abupy import AbuFactorSellNDay, AbuFactorBuyWD, AbuPickStockNTop
from abupy import AbuFactorBuyBreak, AbuFactorAtrNStop, AbuFactorPreAtrNStop, AbuWeekMonthBuy
from abupy import abu, AbuFactorCloseAtrNStop, ABuProgress, AbuMetricsBase, EMarketTargetType

cash = 3000000
# 延用周期突破策略做为买入因子
buy_factors = [{'xd': 21, 'class': AbuFactorBuyBreak},
               {'xd': 42, 'class': AbuFactorBuyBreak}]
# 卖出策略也还是继续延用
sell_factors = [
    {'stop_loss_n': 1.0, 'stop_win_n': 3.0,
     'class': AbuFactorAtrNStop},
    {'class': AbuFactorPreAtrNStop, 'pre_atr_n': 1.5},
    {'class': AbuFactorCloseAtrNStop, 'close_atr_n': 1.5}
]
def run_loo_back(choice_symbols, ps=None, n_folds=2, start=None, end=None, only_info=False):
    """封装一个回测函数"""
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
    AbuMetricsBase.show_general(*abu_result_tuple, returns_cmp=only_info,
                                only_info=only_info,
                                only_show_returns=True)
    return abu_result_tuple

# 使用沙盒内的美股做为回测目标
us_choice_symbols = ['usTSLA', 'usNOAH', 'usSFUN', 'usBIDU', 'usAAPL',
                     'usGOOG', 'usWUBA', 'usVIPS']
_ = run_loo_back(us_choice_symbols)