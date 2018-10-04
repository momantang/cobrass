import sys
import os.path

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
from local import local_setting as ls
import numpy as np
import pandas as pd
import tushare as ts

__path__ = ls.LocalSetting.data_path
__path_dividend__ = __path__ + "dividend/"
__path_daily__ = __path__ + "daily/"
__csv__ = '.csv'


def stock_basic_save(path):
    file_path = __path__ if path is None else path
    ts_pro = ls.get_ts_pro()
    print(ts_pro)
    df = ts_pro.stock_basic(list_status='L', fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_date,is_hs')
    df.to_csv(__path__ + "stock_basic.csv")
    return df


def stock_dividend_save(ts_code):
    print("stock_dividend_save :%s" % ts_code)
    ts_pro = ls.get_ts_pro()
    print(ts_pro)
    if ts_code is None:
        raise Exception
    df = ts_pro.dividend(ts_code=ts_code)
    df.to_csv(__path_dividend__ + ts_code + __csv__)
    return df


def stock_daily_save(ts_code):
    ts_pro = ls.get_ts_pro()
    print(ts_pro)

    df1 = ts_pro.daily(ts_code=ts_code, start_date='19900101', end_date='19941231')
    df2 = ts_pro.daily(ts_code=ts_code, start_date='19950101', end_date='19991231')
    df3 = ts_pro.daily(ts_code=ts_code, start_date='20000101', end_date='20041231')
    df4 = ts_pro.daily(ts_code=ts_code, start_date='20050101', end_date='20091231')
    df5 = ts_pro.daily(ts_code=ts_code, start_date='20100101', end_date='20141231')
    df6 = ts_pro.daily(ts_code=ts_code, start_date='20150101', end_date='20191231')

    # df11 = pd.DataFrame(df1)
    # df22 = pd.DataFrame(df2)
    # df = pd.concat(df11, df22)
    """

    df1['date'] = pd.to_datetime(df1['trade_date'])
    df1.set_index("date", inplace=True)

    df2['date'] = pd.to_datetime(df2['trade_date'])
    df2.set_index("date", inplace=True)
    """
    df = pd.concat([df1, df2, df3, df4, df5, df6])
    df.to_csv(__path_daily__ + ts_code + __csv__)
    return df


def read_stock_daily(ts_code):
    file = __path_daily__ + ts_code + __csv__
    if os.path.isfile(file):
        return pd.read_csv(file)
    else:
        return stock_daily_save(ts_code)


def read_stock_dividend(ts_code):
    file = __path_dividend__ + ts_code + __csv__
    if os.path.isfile(file):
        return pd.read_csv(file)
    else:
        return stock_dividend_save(ts_code)


def read_stock_basic():
    """
    获取简单股票列表，如果本地没有，则尝试利用tushare下载，并保存在本地
    :return:
    """
    file = __path__ + "stock_basic.csv"
    if os.path.isfile(file):
        print("file is exits")
        return pd.read_csv(file)
    else:
        print("try down")
        return stock_basic_save(None)


def test1():
    ts_pro = ls.get_ts_pro()
    print(ts_pro)

    df1 = ts_pro.daily(ts_code='000001.SZ', start_date='19900101', end_date='19941231')
    df2 = ts_pro.daily(ts_code='000001.SZ', start_date='19950101', end_date='19991231')
    df3 = ts_pro.daily(ts_code='000001.SZ', start_date='20000101', end_date='20041231')
    df4 = ts_pro.daily(ts_code='000001.SZ', start_date='20050101', end_date='20091231')
    df5 = ts_pro.daily(ts_code='000001.SZ', start_date='20100101', end_date='20141231')
    df6 = ts_pro.daily(ts_code='000001.SZ', start_date='20150101', end_date='20191231')

    # df11 = pd.DataFrame(df1)
    # df22 = pd.DataFrame(df2)
    # df = pd.concat(df11, df22)
    """

    df1['date'] = pd.to_datetime(df1['trade_date'])
    df1.set_index("date", inplace=True)

    df2['date'] = pd.to_datetime(df2['trade_date'])
    df2.set_index("date", inplace=True)
    """
    df = pd.concat([df1, df2, df3, df4, df5, df6])
    print(df.dtypes)
    print(df.head())
    print(df.tail())


if __name__ == '__main__':

    test1()
    """
    
    df = read_stock_basic()
    for ts_code in df['ts_code']:
        print(ts_code)
        read_stock_dividend(ts_code)
    # print(df.head())
    # print(df.shape)
    """
