"""
挖地兔微信号
https://mp.weixin.qq.com/s/P4Suh-JnBsI9cA43GuftuQ
"""
import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

import tushare as ts
import tushare.futures
import pandas as pd
from local import local_setting as ls

pro = ls.get_ts_pro()

df = pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,name,area,industry,list_date,market')
data = pd.crosstab(df.area, df.market)
print(data)
