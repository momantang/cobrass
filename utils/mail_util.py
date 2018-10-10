import numpy as np
import pandas as pd
from django.core import mail


def send_email_stock_snapshot(df, how, emails):
    """
    发送瞬时股票信息
    :param df: 股票列表
    :param how:  股票类型 up|down|interest
    :param emails: 目标邮箱地址
    :return:
    """
    df['change'] = (df['now'] - df['open']) / (df['open']) * 100
    df['change_up'] = (df['now'] - df['open'] + 0.01) / (df['open']) * 100
    df['change_down'] = (df['now'] - df['open'] - 0.01) / (df['open']) * 100
    print(df.shape)
    try:
        if how == 'up':
            df = df[np.logical_or(np.logical_and(df['change'] >= 10, df['open'] > 0),
                                  np.logical_and(df['change'] < 10, df['change_up'] >= 10))]
            if df.shape[1] > 0:
                print('发送涨停股票')
                mail.send_mail('发送涨停股票', 'Here is the message.',
                               'cobrass_backend@sina.com', ['momantang@163.com'],
                               fail_silently=True)
                # mail.send_mail('涨停股票', '中国平安65;贵州股票45', 'cobrass_backend@sina.com', ['momantang@163.com'])
        elif how == 'down':
            df = df[np.logical_or(np.logical_and(df['change'] <= -10, df['open'] > 0),
                                  np.logical_and(df['change'] >= -10, df['change_down'] <= -10))]
            print('send down')
            print(df)
        elif how == 'select':
            print(df)
            print('interest')
        else:
            print('unkown how')

    except Exception:
        print("error ")
