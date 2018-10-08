import sys
import traceback
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

# 2018-02-06 22:03 来源：证券时报官方微信
__stock_dividend_max__ = {'601398.SH': 5500, '601857.SH': 3959, '601988.SH': 3167, '601288.SH': 3052, '600028.SH': 2230,
                          '601088.SH': 1438, '600036.SH': 947, '600104.SH': 804, '601628.SH': 754, '601328.SH': 726,
                          '600000.SH': 656, '601166.SH': 656, '600900.SH': 634, '600019': 592, '601006.SH': 563, '600519.SH': 436,
                          '000651.SZ': 418, '601318.SH': 405, '601998.SH': 398}
# 2007-2016年连续分红并 '600350.SH': 3.13,
__stock_dividend__ = {'600377.SH': 5.03, '601398.SH': 4.70, '601939.SH': 4.63, '601988.SH': 4.58, '601006.SH': 4.29,
                      '600177.SH': 4.27, '601088.SH': 4.19, '002003.SZ': 3.86, '601328.SH': 3.68, '600066.SH': 3.60,
                      '600011.SH': 3.55, '000568.SZ': 3.52, '000651.SZ': 3.49, '600104.SH': 3.47, '600012.SH': 3.45,
                      '600900.SH': 3.43, '000895.SZ': 3.28, '000726.SZ': 3.27, '600548.SH': 3.26, '600036.SH': 3.12,
                      '600004.SH': 3.11, '600033.SH': 3.10, '000488.SZ': 3.05, '600578.SH': 3.03, '600183.SH': 3.03,
                      '600028.SH': 3.00}


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
    df1['date'] = pd.to_datetime(df1['trade_date'])
    df1.set_index("date", inplace=True)

    df2 = ts_pro.daily(ts_code=ts_code, start_date='19950101', end_date='19991231')
    df2['date'] = pd.to_datetime(df2['trade_date'])
    df2.set_index("date", inplace=True)

    df3 = ts_pro.daily(ts_code=ts_code, start_date='20000101', end_date='20041231')
    df3['date'] = pd.to_datetime(df3['trade_date'])
    df3.set_index("date", inplace=True)

    df4 = ts_pro.daily(ts_code=ts_code, start_date='20050101', end_date='20091231')
    df4['date'] = pd.to_datetime(df4['trade_date'])
    df4.set_index("date", inplace=True)

    df5 = ts_pro.daily(ts_code=ts_code, start_date='20100101', end_date='20141231')
    df5['date'] = pd.to_datetime(df5['trade_date'])
    df5.set_index("date", inplace=True)

    df6 = ts_pro.daily(ts_code=ts_code, start_date='20150101', end_date='20191231')
    df6['date'] = pd.to_datetime(df6['trade_date'])
    df6.set_index("date", inplace=True)

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
    df = df.sort_index()
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


def simple_strategy_test():
    """
    简单尝试购买高股息股票,每月第5个交易日购买，每次资金为2w元，余额留待滚动到下月
    :return:
    """
    df_new = None
    df_total = None
    for ts_code, dividend in __stock_dividend__.items():
        print("ts_code :%s" % ts_code)
        df = read_stock_daily(ts_code)
        df['date2'] = pd.to_datetime(df['date'])
        df.set_index('date2', inplace=True)
        df['action'] = 1
        df['count'] = 0
        df['cap_re'] = 0
        df['cap_total'] = 0
        df['profit'] = 0.0
        df['year'] = df.index.year
        if df_new is None:
            df_new = pd.DataFrame(columns=df.columns)
        if df_total is None:
            df_total = pd.DataFrame(columns=df.columns)
        start_year = df.iloc[0]['year']
        end_year = df.iloc[-1]['year']

        for year in np.arange(start_year, 2017):
            # print(ts_code + " 在 " + str(start_year) + "," + str(start_year) + "中数据：")
            # print(year)
            """
            逐月买入
            """
            cap_re = 0
            cap_evey = 20000
            cap_total = 0
            count_all = 0
            for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                year_month = str(year) + "-" + month
                try:
                    df_temp = df[year_month]
                    if df_temp is not None:
                        df_buy = df[year_month][3:4]
                    else:
                        continue

                    close = df[year_month][3:4]['close'].values[0]
                    count = (cap_evey + cap_re) // (close * 100)
                    count_all = count_all + count
                    cap_re = cap_re + cap_evey - (close * 100) * count
                    cap_total = cap_total + close * 100 * count
                    df_buy['count'] = count
                    df_buy['cap_re'] = cap_re
                    df_buy['cap_total'] = cap_total
                    # df_new = df_new.append(df_buy)
                    # print(df_new.open)
                except Exception as e:
                    traceback.print_exc()
                    info = traceback.format_exc()
            try:
                df_sell = df[str(year)][-1:]
                df_sell['action'] = 0
                close = df_sell['close'].values[0]
                profit = count_all * close * 100 / cap_total - 1
                df_sell['profit'] = profit
                df_sell['count'] = count_all
                df_sell['cap_re'] = cap_re
                df_sell['cap_total'] = cap_total
                df_sell['cap_total'] = cap_total
                # print(df_sell['profit'])
                print(year)
                print("add year")
                df_new = df_new.append(df_sell)
            except Exception:
                # print("error 2")
                pass
            # df_new = pd.concat(df_new, df_sell)
        df_new.to_csv(__path__ + "sing_buy/" + ts_code + "0.csv")

    # print(df['2015-11'][-1:])

    # for i in np.arange(1995, 2019):
    # print(i)
    # print(ts_code)
    # print(dividend)


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


def test2():
    ts_pro = ls.get_ts_pro()
    print(ts_pro)

    df = ts_pro.index_basic(market='SZSE')

    print(df)


def test3():
    ts_pro = ls.get_ts_pro()

    df = ts.get_realtime_quotes('601318')
    print(df)


if __name__ == '__main__':
    simple_strategy_test()
    """
    
    df = read_stock_basic()
    for ts_code in df['ts_code']:
        print(ts_code)
        read_stock_dividend(ts_code)
    # print(df.head())
    # print(df.shape)
    """
