import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

import pytz
import datetime
import requests
from dateutil.tz import *

from QUANTAXIS.QAFetch import QATushare
from QUANTAXIS.QAUtil.QABar import QA_util_make_min_index, trade_date_sse
from QUANTAXIS.QAFetch.QACrawler import QA_fetch_get_sh_margin, QA_fetch_get_sz_margin
from QUANTAXIS.QAFetch.QAThs import QA_fetch_get_stock_day

from QUANTAXIS.QAFetch.QATdx import ping
from QUANTAXIS.QAUtil.host import ip

import pandas as pd
from requests.exceptions import ConnectTimeout

from urllib.parse import urljoin
from QUANTAXIS.QAUtil.QAcrypto import TIMEOUT, ILOVECHINA
from QUANTAXIS.QAFetch.QAfinancial import parse_all,download_financialzip

test_qatdx = False
test_QAbinance = False

proxies = {
    "http": "socks5://127.0.0.1:1086",
    'https': 'socks5://127.0.0.1:1086'
}

if __name__ == '__main__':
    #download_financialzip()
    df=parse_all()
    print(df.shape)
    print(df.head())
    print(df.tail())
    resp = requests.get("https://www.facebook.com/", proxies=proxies, timeout=5)
    #print(resp.text)
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

print(QATushare.set_token(''))
# print(QA_fetch_get_sz_margin('2018-01-25'))
# print(QA_fetch_get_sh_margin('2018-01-25'))
# print(QA_fetch_get_stock_day('000001', '2016-05-01', '2017-07-01', '01'))
