import os
import platform
import sys

sys.path.append(os.path.expanduser('~') + os.sep + 'PyCharmProjects' + os.sep + "cobrass")
import datetime
import easyquotation
import QUANTAXIS as QA
from QUANTAXIS.QAUtil.QADate_trade import QA_util_if_trade, QA_util_if_tradetime
import pandas as pd
from local import local_setting as ls
from utils import pg_util, mail_util

debug = True

stocks = ['sz601318']
columns = ['code', 'now', 'open', 'high', 'low', 'close', 'volume']


def down_market_snapshot(save=True):
    """
    每半小时获取下市场快照
    :return: 市场快照
    """

    if QA_util_if_tradetime():
        date = datetime.datetime.now()
        dateStr = date.strftime('%Y-%m-%d_%H-%M')
        quotation = easyquotation.use('sina')
        snapshot = quotation.market_snapshot(prefix=True)
        # market_snapshot = MarketSnapshot(date=date, context=snapshot)
        # market_snapshot.save()
        df_snapshot = pd.DataFrame.from_dict(snapshot)
        df_snapshot = df_snapshot.T
        df_snapshot.index.name = 'code'
        if save:
            df_snapshot.to_csv(ls.LocalSetting.data_path + "mark_snapshot/" + dateStr + ".csv", compression='gzip')
        return df_snapshot
    else:
        return pd.read_csv('/Users/momantang/work/cobrass/data/mark_snapshot/2018-11-09_15-05.csv', compression='gzip')


def main():
    df = down_market_snapshot()
    print(df.shape)
    print(df.head())
    if QA_util_if_tradetime() or debug:
        df1 = df.loc[
            df['code'].isin(pg_util.get_instere_stock()), columns]
        print(df1.to_html())
        mail_util.send_mail_table(df1)
        """
       
        return ''
        quotation = easyquotation.use('sina')
        easyquotation.update_stock_codes()
        indexs = quotation.stocks(['sh000001', 'sz399001', 'sh000300', 'sz399006'], prefix=True)
        df_indexs = pd.DataFrame.from_dict(indexs).T
        print(df_indexs.to_dict())
         """
        # dict = quotation.market_snapshot(prefix=True)

        # df = pd.DataFrame.from_dict(dict).T
        # print(df[df.index == 'sh000001'])
        # print(type(dict))
        pass
    else:
        QA.QA_util_log_info('非交易时间')
    print(QA.__version__)
    print('hello world')


if __name__ == '__main__':
    main()
