import requests
import json
import datetime
import time
import pandas as pd
from requests.exceptions import ConnectTimeout

from urllib.parse import urljoin
from QUANTAXIS.QAUtil.QAcrypto import TIMEOUT, ILOVECHINA

Binance_base_url = "https://api.binance.com"

columne_names = ['start_time', 'open', 'hight', 'low', 'close', 'volume', 'colse_time',
                 'quote_asset_volume', 'num_trades', 'buy_base_asset_volume',
                 'buy_quote_asset_volume', 'Ignore']

proxies = {
    "http": "socks5://127.0.0.1:1086",
    'https': 'socks5://127.0.0.1:1086'
}


def QA_fetch_binance_symbols():
    url = urljoin(Binance_base_url, "/api/v1/exchangeInfo")
    try:
        req = requests.get(url, proxies=proxies, timeout=TIMEOUT)
    except ConnectTimeout:
        raise ConnectTimeout(ILOVECHINA)
    body = json.loads(req.content)
    return body['symbols']


def QA_fetch_binance_kline(symbol, start_time, end_time, frequency):
    datas = list()
    start_time *= 1000
    end_time *= 1000
    while start_time < end_time:
        url = urljoin(Binance_base_url, '/api/v1/klines')
        try:
            req = requests.get(url, params={'symbol': symbol, 'interval': frequency, 'startTime': int(start_time),
                                            'endTime': int(end_time)}, proxies=proxies, timeout=TIMEOUT)
            # 防止频率过快被断连
            time.sleep(0.5)
        except ConnectTimeout:
            raise ConnectTimeout(ILOVECHINA)
        klines = json.loads(req.content)
        if len(klines) == 0:
            break
        datas.extend(klines)
        # TODO 需查看为什么取值[-1][6]
        start_time = klines[-1][6]
    if len(datas) == 0:
        return None
    df = pd.DataFrame(datas)
    df.columns = columne_names
    df['symbol'] = symbol
    return json.loads(df.to_json(orient='records'))
