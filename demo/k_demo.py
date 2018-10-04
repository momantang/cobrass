import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
import mpl_finance as mplf
import tushare as ts
import pandas as pd

from local import local_setting as ls
from matplotlib import pyplot as plt
from matplotlib.pylab import date2num
import datetime
from abupy import ABuSymbolPd, ABuMarketDrawing, AbuSymbolCN

__color_up__ = 'red'
__color_down__ = 'green'

if __name__ == '__main__':
    ts.set_token(ls.LocalSetting.tushare_token)
    ts_pro = ts.pro_api()
    df_zgpa = ts_pro.query('daily', ts_code='601318.SH')
    # df_zgpa.to_csv(ls.LocalSetting.data_path + "601318.csv")
    # df_zgpa = pd.read_csv(ls.LocalSetting.data_path + "601318.csv")
    # print(df_zgpa.head())
    df_index = ABuSymbolPd.make_kl_df('000001')
    df = ABuSymbolPd.make_kl_df('601318')
    # df_index = df_zgpa
    # df_index.set_index('trade_date', inplace=True)
    # print(df_zgpa.tail())
    qutotes1 = []
    qutotes2 = []
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 7))
    for index, (d, o, c, h, l) in enumerate(zip(df_index.index, df_index.open, df_index.close, df_index.high, df_index.low)):
        d = date2num(d)
        val = (d, o, c, h, l)
        qutotes1.append(val)
        pass
    print(df_index.dtypes)
    print(df_zgpa.dtypes)
    mplf.candlestick_ochl(ax1, qutotes1, width=0.6, colorup=__color_up__, colordown=__color_down__)
    ax1.xaxis_date()

    for index, (d, o, c, h, l) in enumerate(zip(df_zgpa.trade_date, df_zgpa.open, df_zgpa.close, df_zgpa.high, df_zgpa.low)):
        date_time = datetime.datetime.strptime(d, '%Y%m%d')
        t = date2num(date_time)
        val = (t, o, c, h, l)
        qutotes2.append(val)
        pass
    mplf.candlestick_ochl(ax2, qutotes2, width=0.6, colorup=__color_up__, colordown=__color_down__)
    ax2.xaxis_date()
    plt.show()
