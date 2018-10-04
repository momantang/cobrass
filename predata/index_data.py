import sys

try:
    from local import local_setting as ls
except ImportError:
    print("import error")
    sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
    sys.path
    from local import local_setting as ls
import numpy as np
import pandas as pd
import tushare as ts
from matplotlib import pyplot as plt


def to_csv(ts_code, begin_year, years):
    ts.set_token(ls.LocalSetting.tushare_token)
    pro = ts.pro_api()
    start_date = str(begin_year) + "0101"
    end_date = str(begin_year + years - 1) + "1231"
    df = pro.index_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    df.to_csv(ls.LocalSetting.data_path + ts_code + "_" + str(begin_year) + ".csv")


if __name__ == '__main__':
    df = pd.DataFrame()
    for i in np.arange(2015, 1990, -5):
        # to_csv('000001.sh', i, 5)
        pass
    for i in np.arange(2015, 1990, -5):
        path = ls.LocalSetting.data_path + "000001.sh_" + str(i) + '.csv'
        df1 = pd.read_csv(path)
        df = df.append(df1)
    print(df.shape)
    df = df.set_index("trade_date")
    print(df.index)
    df.to_csv(ls.LocalSetting.data_path + "000001.sh_2.csv")
    # df1 = pd.read_csv(ls.LocalSetting.data_path + '000001.sh' + "_" + str(i) + ".csv"))
    # to_csv('000001.sh', i, 5)
