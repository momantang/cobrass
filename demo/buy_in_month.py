import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
import numpy as np
import pandas as pd
import tushare as ts

from local import local_setting as ls

ts.set_token(ls.LocalSetting.tushare_token)
ts_pro = ts.pro_api()
"""
试试每月第5日交易日买入，年底卖出，看看效果
每月买入资金为￥20000元，不足可以累积下月买入，分别以当天open，high，close买入，当年年底最后一天卖出
"""

capital = 20000
income = []
df = ts_pro.query('daily', ts_code='601318.SH', start_date='20160101', end_date='20161231')
df['date'] = pd.to_datetime(df['trade_date'])
df.set_index("date", inplace=True)
print(df.info())
print(df['2016-09'])
print(df['2016-09'][-5:-4])


def simple_buy(ts_code, capital):
    pass
