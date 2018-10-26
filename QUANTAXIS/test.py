import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

import pytz
import datetime
import requests
from dateutil.tz import *

from QUANTAXIS.QAFetch import QATushare
from QUANTAXIS.QAFetch import QATdx
from QUANTAXIS.QAUtil.QABar import QA_util_make_min_index, trade_date_sse
from QUANTAXIS.QAFetch.QACrawler import QA_fetch_get_sh_margin, QA_fetch_get_sz_margin
from QUANTAXIS.QAFetch.QAThs import QA_fetch_get_stock_day

from QUANTAXIS.QAFetch.QATdx import ping, select_best_ip, QA_fetch_get_security_bars
from QUANTAXIS.QAUtil.host import ip

import pandas as pd
from requests.exceptions import ConnectTimeout

from urllib.parse import urljoin
from QUANTAXIS.QAUtil.QAcrypto import TIMEOUT, ILOVECHINA
from QUANTAXIS.QAFetch.QAfinancial import parse_all, download_financialzip

from QUANTAXIS.QASU.save_tdx import now_time

import QUANTAXIS as QA

test_qatdx = False
test_QAbinance = False
test_QATushare = False
test_DataFetch = False

proxies = {
    "http": "socks5://127.0.0.1:1086",
    'https': 'socks5://127.0.0.1:1086'
}

if __name__ == '__main__':
    if True:
        print(now_time())

    if test_DataFetch:
        QA.QAUtil.QA_util_log_info('日线数据')
        QA.QAUtil.QA_util_log_info('不复圈')
        # data = QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001', '1900-01-01', '2019-01-31')
        # data = QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001', '2017-01-01', '2017-01-31', '01')
        data = QA.QAFetch.QATdx.QA_fetch_get_stock_min('000001', '2017-07-01', '2017-08-01', '5min')
        print(data.shape)
        print(data.head())
        print(data.tail())

    if test_QATushare:
        from local import local_setting as ls
        from QUANTAXIS.QAFetch.QATushare import set_token

        print(ls.LocalSetting.tushare_token)
        set_token(token=ls.LocalSetting.tushare_token)
    # download_financialzip()
    # df=parse_all()
    # print(df.shape)
    # print(df.head())
    # print(df.tail())
    # resp = requests.get("https://www.facebook.com/", proxies=proxies, timeout=5)
    # print(resp.text)
    if test_qatdx:
        for i in ip:
            ping(i[1])
        print("QATdx 测试示例")
    if test_QAbinance:
        import time

        from QUANTAXIS.QAFetch.QAbinance import Binance_base_url, QA_fetch_binance_kline

        tz = pytz.timezone("Asia/Shanghai")
        url = urljoin(Binance_base_url, "/api/vi/klines")
        start = time.mktime(datetime.datetime(2018, 6, 13, tzinfo=tzutc()).timetuple())
        end = time.mktime(datetime.datetime(2018, 6, 14, tzinfo=tzutc()).timetuple())
        print(url)
        print(start)
        data = QA_fetch_binance_kline('ETHBTC', start * 1000, end * 1000, 'id')
        print(len(data))
        print(data[0])
        print(data[-1])

# print(QA_fetch_get_sz_margin('2018-01-25'))
# print(QA_fetch_get_sh_margin('2018-01-25'))
# print(QA_fetch_get_stock_day('000001', '2016-05-01', '2017-07-01', '01'))
