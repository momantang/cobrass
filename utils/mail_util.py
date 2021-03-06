import numpy as np
import pandas as pd
import datetime
from utils.timeutils import get_m_d_HH_MM
from local import local_setting as ls

import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header


def send_mail_table(df):
    try:
        server = smtplib.SMTP(ls.LocalSetting.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(ls.LocalSetting.email_username, ls.LocalSetting.email_password)
        msg = MIMEText("<html><body>" + df.to_html() + "</body></html>", 'html', 'utf-8')
        # msg = MIMEText("<p>test</p>", 'plain', 'utf-8')

        msg['Subject'] = Header('股票表格' + get_m_d_HH_MM(), 'utf-8')
        msg["From"] = ls.LocalSetting.email_from
        msg["To"] = 'momantang@163.com'
        server.sendmail(ls.LocalSetting.email_from, ['momantang@163.com'], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)


def send_email_stock_snapshot(df, how, emails):
    try:
        from finance import snapshot
        from django.core import mail
    except:
        pass
    """
    发送瞬时股票信息
    :param df: 股票列表
    :param how:  股票类型 up|down|interest
    :param emails: 目标邮箱地址
    :return:
    """
    print("send_email_stock_snapshot")
    print(df.shape)
    df = df.drop(df[df.open == 0].index)
    print(df.shape)
    df['change'] = (df['now'] - df['close']) / (df['close']) * 100
    df['change_up'] = (df['now'] - df['close'] + 0.01) / (df['close']) * 100
    df['change_down'] = (df['now'] - df['close'] - 0.01) / (df['close']) * 100
    print(df.shape)
    print(df)
    if how == 'up':
        df = df[np.logical_or(np.logical_and(df['change'] >= 10, df['open'] > 0),
                              np.logical_and(df['change'] < 10, df['change_up'] >= 10))]
        if df.shape[1] > 0:
            print('发送涨停股票')
            content = ""
            for index, row in df.iterrows():
                content = content + index + "_" + str(row.now) + ";"
            content = content[:-1]
            print(content)
            mail.send_mail('发送涨停股票', content,
                           'cobrass_backend@sina.com', ['momantang@163.com'],
                           fail_silently=True)
            # mail.send_mail('涨停股票', '中国平安65;贵州股票45', 'cobrass_backend@sina.com', ['momantang@163.com'])
    elif how == 'down':
        df = df[np.logical_or(np.logical_and(df['change'] <= -10, df['open'] > 0),
                              np.logical_and(df['change'] >= -10, df['change_down'] <= -10))]
        if df.shape[1] > 0:
            print('发送跌停股票')
            content = ""
            for index, row in df.iterrows():
                content = content + index + "_" + str(row.now) + ";"
            content = content[:-1]
            print(content)
            mail.send_mail('发送跌停股票', content,
                           'cobrass_backend@sina.com', ['momantang@163.com'],
                           fail_silently=True)
        print(df)
    elif how == 'select':
        df = snapshot.interest_stock_snapshot(df)
        print(df)
        print('interest')
    else:
        print('unkown how')
