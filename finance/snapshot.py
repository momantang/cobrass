import os
import sys
import django

"""
处理股票快照资料
"""
import numpy as np
import pandas as pd
from finance.models import Stock
from utils import stockutil

df_snapshot = pd.read_csv("/Users/momantang/work/cobrass/data/mark_snapshot/2018-11-09_14-55-43.csv",
                          compression='gzip')


def interest_stock_snapshot(df_snapshot):
    print("interest_stock_snapshot")
    # print(df_snapshot.info(verbose=True))
    interest_stock = Stock.objects.filter(is_interest=True)

    df_stock = pd.DataFrame(columns=['code', 'stname'])
    for stock in interest_stock:
        df_stock = df_stock.append({'code': stockutil.get_stock_type(stock.code) + stock.code, 'stname': stock.name},
                                   ignore_index=True)
    df_stock = df_stock.set_index('code')
    print("df_stock:")
    print(df_stock.head())
    print("df_snapshot:")
    print(df_snapshot.head())
    df = pd.concat([df_stock, df_snapshot], axis=1, join='inner')
    print(df.head())
    return df


if __name__ == '__main__':
    interest_stock_snapshot(df_snapshot)
