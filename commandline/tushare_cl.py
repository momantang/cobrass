"""
tushare commandline 类
"""
import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
import numpy as np
import pandas as pd
import tushare as ts
import django

from sqlalchemy import create_engine
from finance.models import StockBasic

from local import local_setting as ls

__authore__ = "cobrass"


def update_db_stock_basic(list_status):
    pro = ls.get_ts_pro()
    print(pro)
    data = pro.stock_basic(exchange_id='', list_status=list_status,
                           fields='ts_code,symbol,name,area,industry,fullname,enname,'
                                  'market,exchange_id,curr_type,list_status,list_date,delist_date,is_hs')
    if data.shape[0] > 0:
        for row in data.iterrows():
            ts_code, symbol, name, area, industry, fullname, enname, market, exchange_id, curr_type, list_status, list_date, delist_date, is_hs = \
                row[-1]
            stock_basic = StockBasic(ts_code=ts_code, symbol=symbol, name=name, area=area, industry=industry, fullname=fullname,
                                     enname=enname, market=market, exchange_id=exchange_id, curr_type=curr_type,
                                     list_status=list_status, list_date=list_date, delist_date=delist_date, is_hs=is_hs)
            stock_basic.save()


if __name__ == '__main__':
    update_db_stock_basic(list_status='P')
