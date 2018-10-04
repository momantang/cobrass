import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
import numpy as np
import pandas as pd
import tushare as ts

from local import local_setting as ls

__dividend_path__ = ls.LocalSetting.data_path + "dividend/"
__CSV__ = '.csv'


def make_dividend_local():
    pass


def make_dividend_tushare(ts_code):
    ts.set_token(ls.LocalSetting.tushare_token)
    ts_pro = ts.pro_api()
    df = ts_pro.dividend(ts_code=ts_code)
    df.to_csv(__dividend_path__ + ts_code + __CSV__)
    return df


"""

ts.set_token(ls.LocalSetting.tushare_token)
ts_pro = ts.pro_api()

df = ts_pro.dividend(ts_code='601318.SH')
df.to_csv(ls.LocalSetting.data_path + "dividend/" + "601318.SH" + ".csv")
print(df)
"""
