import pandas as pd
from QUANTAXIS.QAUtil import QA_util_log_info, QA_util_random_with_topic
from QUANTAXIS.QAUtil.QAParameter import MARKET_TYPE, TRADE_STATUS

"""撮合类

一个无状态的 Serverless Dealer

输入是

self.market_data
self.order
rules

输出是

standard message

"""


class commission():
    if_buyside_commission = False
    if_sellside_commission = True
    if_commission = if_buyside_commission and if_sellside_commission


class QA_Dealer():
    """[summary]


    对于不同的市场规则:
    股票市场 t+1
    期货/期权/加密货币市场 t+0

    股票/加密货币市场不允许卖空
    期货/期权市场允许卖空

    t+1的市场是
    当日的买入 更新持仓- 不更新可卖数量- 资金冻结
    当日的卖出 及时更新可用资金

    t+0市场是:
    当日买入 即时更新持仓和可卖
    当日卖出 即时更新

    卖空的规则是
    允许无仓位的时候卖出证券(按市值和保证金比例限制算)
    """

    def __init__(self, *args, **kwargs):
        self.deal_name = ''
        self.session = {}
