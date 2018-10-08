import sys
import os

sys.path.insert(0, os.path.abspath('../'))
import warnings

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import abupy
from abupy import ABuSymbolPd, AbuFactorBuyXD, BuyCallMixin, AbuBenchmark, AbuCapital
from abupy import ABuPickTimeExecute
from abupy import AbuFactorSellXD, ESupportDirection
from abupy import AbuFactorAtrNStop, AbuFactorPreAtrNStop, AbuFactorCloseAtrNStop
from abupy import AbuSlippageBuyBase, slippage

abupy.env.enable_example_env_ipython()

g_open_down_rate = 0.02


class AbuFactorBuyBreak(AbuFactorBuyXD, BuyCallMixin):
    def fit_day(self, today):
        if today.close == self.xd_kl.close.max():
            return self.buy_tomorrow()
        return None


class AbuFactorSellBreak(AbuFactorSellXD):
    def support_direction(self):
        return [ESupportDirection.DIRECTION_CAll.value]

    def fit_day(self, today, orders):
        """
        寻找向下突破作为策略卖出驱动event
        :param today: 当前驱动的交易日金融时间序列数据
        :param orders: 买入择时策略中生成的订单序列
        """
        # 今天的收盘价格达到xd天内最低价格则符合条件
        if today.close == self.xd_kl.close.min():
            for order in orders:
                self.sell_tomorrow(order)


class AbuSlippageBuyMean2(AbuSlippageBuyBase):
    @slippage.sbb.slippage_limit_up
    def fit_price(self):
        if self.kl_pd_buy.pre_close == 0 or (self.kl_pd_buy.open / self.kl_pd_buy.pre_close) < (1 - g_open_down_rate):
            return np.inf
        self.buy_price = np.mean([self.kl_pd_buy['high'], self.kl_pd_buy['low']])
        return self.buy_price


if __name__ == '__main__':
    print(abupy.__version__)


    def calc_commission_us(trade_cnt, price):
        """
        美股计算交易费用：每股0.01，最低消费2.99
        :param trade_cnt: 交易的股数（int）
        :param price: 每股的价格（美元）（暂不使用，只是保持接口统一）
        :return: 计算结果手续费
        """
        # 每股手续费0.01
        commission = trade_cnt * 0.01
        if commission < 2.99:
            # 最低消费2.99
            commission = 2.99
        return commission
    # 使用120天向下突破为卖出信号
    sell_factor1 = {'xd': 120, 'class': AbuFactorSellBreak}
    sell_factor2 = {'stop_loss_n': 0.5, 'stop_win_n': 3.0, 'class': AbuFactorAtrNStop}
    sell_factor3 = {'class': AbuFactorPreAtrNStop, 'pre_art_n': 1.0}

    sell_factor4 = {'class': AbuFactorCloseAtrNStop, 'close_atr_n': 1.5}
    # buy_factors 60日向上突破，42日向上突破两个因子
    buy_factors = [{'slippage': AbuSlippageBuyMean2, 'xd': 60, 'class': AbuFactorBuyBreak},
                   {'xd': 42, 'class': AbuFactorBuyBreak}]
    # 只使用120天向下突破为卖出因子
    sell_factors = [sell_factor1, sell_factor2, sell_factor3, sell_factor4]
    benchmark = AbuBenchmark()

    # 构造一个字典key='buy_commission_func', value=自定义的手续费方法函数
    commission_dict = {'buy_commission_func': calc_commission_us}
    # 将commission_dict做为参数传入AbuCapital
    capital = AbuCapital(1000000, benchmark, user_commission_dict=commission_dict)
    print(benchmark.__str__())

    orders_pd, action_pd, _ = ABuPickTimeExecute.do_symbols_with_same_factors(['usTSLA'],
                                                                              benchmark,
                                                                              buy_factors,
                                                                              sell_factors,
                                                                              capital, show=False)
    print(orders_pd)
    print(action_pd)
    print(capital.commission.commission_df)
