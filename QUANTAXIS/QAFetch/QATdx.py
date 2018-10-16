import datetime

import numpy as np
import pandas as pd
from pytdx.exhq import TdxExHq_API
from pytdx.hq import TdxHq_API

from QUANTAXIS.QAFetch.base import _select_market_code, _select_type
from QUANTAXIS.QAUtil import (QA_Setting, QA_util_date_stamp,
                              QA_util_date_str2int, QA_util_date_valid,
                              QA_util_get_real_date, QA_util_get_real_datelist,
                              QA_util_future_to_realdatetime, QA_util_future_to_tradedatetime,
                              QA_util_get_trade_gap, QA_util_log_info,
                              QA_util_time_stamp, QA_util_web_ping,
                              exclude_from_stock_ip_list, future_ip_list,
                              stock_ip_list, trade_date_sse)
from QUANTAXIS.QAUtil.QASetting import QASETTING


def init_fetcher():
    """
    初始化获取
    :return:
    """


def ping(ip, port=7709, type_='stock'):
    api = TdxHq_API()
    apix = TdxExHq_API()
    __time1 = datetime.datetime.now()
    try:
        if type_ in ['stock']:
            with api.connect(ip, port, time_out=0.7):
                res = api.get_security_list(0, 1)

                if res is not None:
                    if len(api.get_security_list(0, 1)) > 800:
                        return datetime.datetime.now() - __time1
                    else:
                        print('BAD RESPONSE {}'.format(ip))
                        return datetime.timedelta(9, 9, 0)
        elif type_ in ['future']:
            with apix.connect(ip, port, time_out=0.7):
                res = apix.get_instrument_count()
                if res is not None:
                    if res > 40000:
                        return datetime.datetime.now() - __time1
                    else:
                        print('BAD FUTUREIP REPSONSE {}'.format(ip))
                        return datetime.timedelta(9, 9, 0)
                else:
                    print("BAD FUTUREIP REPSONSE {}".format(ip))
                    return datetime.timedelta(9, 9, 0)
    except Exception as e:
        if isinstance(e, TypeError):
            print(e)
            print('Tushare内置的pytdx版本和QUANTAXIS使用的pytdx 版本不同, 请重新安装pytdx以解决此问题')
            print('pip uninstall pytdx')
            print('pip install pytdx')
        else:
            print('BAD RESPONSE {}'.format(ip))
        return datetime.timedelta(9, 9, 0)


def select_best_ip():
    QA_util_log_info('Selecting the Best Server IP of TDX')

    import json
    null = None
    qasetting = QASETTING
    exclude_ip = {'ip': '1.1.1.1', 'port': 7709}
    defaul_ip = {'stock': {'ip': None, 'port': None},
                 'future': {'ip': None, 'port': None}}
    alist = []
    alist.append(exclude_ip)

    ipexclude = qasetting.get_config(section='IPLIST', option='exclude', default_value=alist)
