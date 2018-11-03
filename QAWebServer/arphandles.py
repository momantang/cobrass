import datetime
import json

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QAWebServer.basehandles import QABaseHandler
from QAWebServer.util import CJsonEncoder
from QUANTAXIS.QAARP.QAAccount import QA_Account
from QUANTAXIS.QAARP.QARisk import QA_Performance, QA_Risk
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_account, QA_fetch_risk
from QUANTAXIS.QASU.save_account import save_account
from QUANTAXIS.QASU.user import QA_user_sign_in, QA_user_sign_up
from QUANTAXIS.QAUtil.QASetting import DATABASE
from QUANTAXIS.QAUtil.QASql import QA_util_sql_mongo_setting


class MemberHandler(QABaseHandler):
    """
      获得所有的回测member
      """

    def get(self):
        """
        采用了get_arguents来获取参数
        默认参数: code-->000001 start-->2017-01-01 09:00:00 end-->now
        accounts?account_cookie=xxx
        """
        # account_cookie= self.get_argument('account_cookie', default='admin')
        query_account = QA_fetch_account()

        if len(query_account) > 0:
            # TODO 需了解
            def warpper(x):
                return str(x) if isinstance(x, datetime.datetime) else x

            res = []
            for item in query_account:
                res.append(item['portfolio_cookie'],
                           item['account_cookie', str(item['start_date']), str(item['end_date']), 'market_type'])
            self.write({'result': res})
        else:
            self.write('WRONG')


class AccountHandler(QABaseHandler):
    """
    对于某个回测账户
    """

    def get(self):
        """
        采用了get_arguents来获取参数
        默认参数: code-->000001 start-->2017-01-01 09:00:00 end-->now
        accounts?account_cookie=xxx
        """
        account_cookie = self.get_argument('account_cookie', default='admin')

        query_account = QA_fetch_account({'account_cookie': account_cookie})
        # data = [QA_Account().from_message(x) for x in query_account]

        if len(query_account) > 0:
            # data = [QA.QA_Account().from_message(x) for x in query_account]
            def warpper(x):
                return str(x) if isinstance(
                    x, datetime.datetime) else x

            for item in query_account:
                item['trade_index'] = list(map(str, item['trade_index']))
                item['history'] = [list(map(warpper, itemd))
                                   for itemd in item['history']]

            self.write({'result': query_account})
        else:
            self.write('WRONG')


class RiskHandler(QABaseHandler):
    """
    回测账户的风险评价
    """

    def get(self):
        account_cookie = self.get_argument('account_cookie', default='admin')

        query_account = QA_fetch_risk({'account_cookie': account_cookie})
        # data = [QA_Account().from_message(x) for x in query_account]
        if len(query_account) > 0:
            # data = [QA.QA_Account().from_message(x) for x in query_account]

            self.write({'result': query_account})
        else:
            self.write('WRONG')
