# coding:utf8
import os
import sys

sys.path.insert(0, os.path.abspath('../'))

import logging
import pandas as pd
from finance.models import Stock, CrontabAction
import datetime
import pytdx
import easyquotation

from local import local_setting as ls

"""
定时任务

"""
logger = logging.getLogger(__name__)
dev = True


def my_scheduled_job():
    crontab_action = CrontabAction()
    crontab_action.date = datetime.datetime.now()
    crontab_action.name = 'my_scheduled_job'
    crontab_action.description = 'first my schedule job'
    crontab_action.save()
    if dev:
        logger.debug('my_scheduled job')
    print(str(datetime.datetime.now()) + "   my_scheduled_job")


def down_market_snapshot(save=True):
    """
    每半小时获取下市场快照
    :return: 市场快照
    """
    dateStr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    quotation = easyquotation.use('sina')
    snapshot = quotation.market_snapshot(prefix=True)
    df_snapshot = pd.DataFrame.from_dict(snapshot)
    df_snapshot = df_snapshot.T
    if save:
        df_snapshot.to_csv(ls.LocalSetting.data_path + "mark_snapshot/" + dateStr + ".csv")
    return df_snapshot


def down_interest_stock():
    """
    下载感兴趣的股票的分时记录
    :return:
    """
    stocks = Stock.Objects.filter(is_interest=True)
    pass


if __name__ == "__main__":
    down_market_snapshot()
