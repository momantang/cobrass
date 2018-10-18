# 基于Pytdx的数据接口,好处是可以在linux/mac上联入通达信行情
# 具体参见rainx的pytdx(https://github.com/rainx/pytdx)
#
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
                        print("sucess Response {}:{}".format(ip, datetime.datetime.now() - __time1))
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

    exclude_from_stock_ip_list(json.loads(ipexclude))

    ipdefault = qasetting.get_config(section='IPLIST', option='default', default_value=defaul_ip)

    ipdefault = eval(ipdefault) if isinstance(ipdefault, str) else ipdefault
    assert isinstance(ipdefault, dict)

    if ipdefault['stock']['ip'] == None:
        data_stock = [ping(x['ip'], x['port'], 'stock') for x in stock_ip_list]
        best_stock_ip = stock_ip_list[data_stock.index(min(data_stock))]
    else:
        if ping(ipdefault['stock']['ip'], ipdefault['stock']['port'], 'stock') < datetime.timedelta(0, 1):
            print('USING DEFAULT STOCK IP')
            best_stock_ip = ipdefault['stock']
        else:
            print('DEFAULT STOCK IP is BAD, RETESTING')
            data_stock = [ping(x['ip'], x['port'], 'stock')
                          for x in stock_ip_list]
            best_stock_ip = stock_ip_list[data_stock.index(min(data_stock))]

    if ipdefault['future']['ip'] == None:

        data_future = [ping(x['ip'], x['port'], 'future')
                       for x in future_ip_list]
        best_future_ip = future_ip_list[data_future.index(min(data_future))]
    else:
        if ping(ipdefault['future']['ip'], ipdefault['future']['port'], 'future') < datetime.timedelta(0, 1):
            print('USING DEFAULT FUTURE IP')
            best_future_ip = ipdefault['future']
        else:
            print('DEFAULT FUTURE IP is BAD, RETESTING')
            data_future = [ping(x['ip'], x['port'], 'future')
                           for x in future_ip_list]
            best_future_ip = future_ip_list[data_future.index(
                min(data_future))]

    ipbest = {'stock': best_stock_ip, 'future': best_future_ip}
    qasetting.set_config(
        section='IPLIST', option='default', default_value=ipbest)

    QA_util_log_info('=== The BEST SERVER ===\n stock_ip {} future_ip {}'.format(
        best_stock_ip['ip'], best_future_ip['ip']))
    return ipbest


global best_ip
best_ip = {
    'stock': {
        'ip': None, 'port': None
    },
    'future': {
        'ip': None, 'port': None
    }
}


# return 1 if sh, 0 if


def get_extensionmarket_ip(ip, port):
    global best_ip
    if ip is None and port is None and best_ip['future']['ip'] is None and best_ip['future']['port'] is None:
        best_ip = select_best_ip()
        ip = best_ip['future']['ip']
        port = best_ip['future']['port']
    elif ip is None and port is None and best_ip['future']['ip'] is not None and best_ip['future']['port'] is not None:
        ip = best_ip['future']['ip']
        port = best_ip['future']['port']
    else:
        pass
    return ip, port


def get_mainmarket_ip(ip, port):
    """[summary]

    Arguments:
        ip {[type]} -- [description]
        port {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    global best_ip
    if ip is None and port is None and best_ip['stock']['ip'] is None and best_ip['stock']['port'] is None:
        best_ip = select_best_ip()
        ip = best_ip['stock']['ip']
        port = best_ip['stock']['port']
    elif ip is None and port is None and best_ip['stock']['ip'] is not None and best_ip['stock']['port'] is not None:
        ip = best_ip['stock']['ip']
        port = best_ip['stock']['port']
    else:
        pass
    return ip, port


def QA_fetch_get_security_bars(code, _type, lens, ip=None, port=None):
    """按bar长度推算数据

       Arguments:
           code {[type]} -- [description]
           _type {[type]} -- [description]
           lens {[type]} -- [description]

       Keyword Arguments:
           ip {[type]} -- [description] (default: {best_ip})
           port {[type]} -- [description] (default: {7709})

       Returns:
           [type] -- [description]
       """
    ip, port = get_mainmarket_ip(ip, port)
    api = TdxHq_API()
    with api.connect(ip, port):
        data = pd.concat([
            api.to_df(api.get_security_bars(_select_type(_type), _select_market_code(code), code, (i - 1) * 800, 800))
            for i in range(1, int(lens / 800) + 2)], axis=0)
        data = data.drop(['year', 'month', 'day', 'hour', 'minute'], axis=1, inplace=False).assign(
            datetime=pd.to_datetime(data['datetime']),
            date=data['datetime'].apply(lambda x: str(x)[0:10]),
            date_stamp=data['datetime'].apply(
                lambda x: QA_util_date_stamp(x)),
            time_stamp=data['datetime'].apply(
                lambda x: QA_util_time_stamp(x)),
            type=_type, code=str(code)).set_index('datetime', drop=False, inplace=False).tail(lens)
        return data


def QA_fetch_get_stock_day(code, start_date, end_date, if_fq='00', frequence='day', ip=None, port=None):
    pass
    """获取日线及以上级别的数据


    Arguments:
        code {str:6} -- code 是一个单独的code 6位长度的str
        start_date {str:10} -- 10位长度的日期 比如'2017-01-01'
        end_date {str:10} -- 10位长度的日期 比如'2018-01-01'

    Keyword Arguments:
        if_fq {str} -- '00'/'bfq' -- 不复权 '01'/'qfq' -- 前复权 '02'/'hfq' -- 后复权 '03'/'ddqfq' -- 定点前复权 '04'/'ddhfq' --定点后复权
        frequency {str} -- day/week/month/quarter/year 也可以是简写 D/W/M/Q/Y
        ip {str} -- [description] (default: None) ip可以通过select_best_ip()函数重新获取
        port {int} -- [description] (default: {None})


    Returns:
        pd.DataFrame/None -- 返回的是dataframe,如果出错比如只获取了一天,而当天停牌,返回None

    Exception:
        如果出现网络问题/服务器拒绝, 会出现socket:time out 尝试再次获取/更换ip即可, 本函数不做处理
    """
    ip, port = get_mainmarket_ip(ip, port)  # 268
    api = TdxHq_API()
    try:
        with api.connect(ip, port, time_out=0.7):
            if frequence in ['day', 'd', 'D', 'DAY', 'Day']:
                frequence = 9
            elif frequence in ['w', 'W', 'Week', 'week']:
                frequence = 5
            elif frequence in ['month', 'M', 'm', 'Month']:
                frequence = 6
            elif frequence in ['quarter', 'Q', 'Quarter', 'q']:
                frequence = 10
            elif frequence in ['y', 'Y', 'year', 'Year']:
                frequence = 11
            start_date = str(start_date)[0:10]
            today_ = datetime.date.today()
            lens = QA_util_get_trade_gap(start_date, today_)

            data = pd.concat([api.to_df(api.get_security_bars(frequence, _select_market_code(
                code), code, (int(lens / 800) - i) * 800, 800)) for i in range(int(lens / 800) + 1)], axis=0)

            # TODO这里的问题是: 如果只取了一天的股票,而当天停牌, 那么就直接返回None了
            if len(data) < 1:
                return None
            data = data[data['open'] != 0]
            data = data.assign(date=data['datetime'].apply(lambda x: str(x[0:10])), code=str(code),
                               date_stamp=data['datetime'].apply(lambda x: QA_util_date_stamp(str(x)[0:10]))) \
                .set_index('date', drop=False, inplace=False)
            data = data.drop(['year', 'month', 'day', 'hour', 'minute', 'datetime'], axis=1)[start_date:end_date]
            if if_fq in ['00', 'bfq']:
                return data
            else:
                print('CURRENTLY NOT SUPPORT REALTIME FUQUAN')
                return None
                # xdxr = QA_fetch_get_stock_xdxr(code)
                # if if_fq in ['01','qfq']:
                #     return QA_data_make_qfq(data,xdxr)
                # elif if_fq in ['02','hfq']:
                #     return QA_data_make_hfq(data,xdxr)

    except Exception as e:
        if isinstance(e, TypeError):
            print('Tushare内置的pytdx版本和QUANTAXIS使用的pytdx 版本不同, 请重新安装pytdx以解决此问题')
            print('pip uninstall pytdx')
            print('pip install pytdx')
        else:
            print(e)
