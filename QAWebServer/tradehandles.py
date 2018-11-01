import datetime
import json
import pandas as pd
import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QAARP import QA_Account, QA_Portfolio, QA_User
from QAWebServer.basehandles import QABaseHandler, QAWebSocketHandler
from QUANTAXIS.QAMarket.QAShipaneBroker import QA_SPEBroker
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas

"""
GET http://localhost:8888/accounts
GET http://localhost:8888/positions
GET http://localhost:8888/orders
POST http://localhost:8888/orders
DELETE http://localhost:8888/orders/O1234
GET http://localhost:8888/clients
"""


class TradeInfoHandler(QABaseHandler):
    """
    trade 信息查询句柄

     Arguments:
        QABaseHandler {[type]} -- [description]

    ?func=ping  ping 服务器
    ?func=clients 查询当前的可用客户端
    ?func=accounts 查询当前的账户
    ?func=positions&account=xxx 查询账户持仓
    ?func=orders&status 查询订单
    下单/撤单功能不在此handler提供

    """
    broker = QA_SPEBroker()

    def funcs(self, func, account, *args, **kwargs):
        if func == 'ping':
            data = self.broker.query_clients()
            return data
        elif func == 'clients':
            data = self.broker.query_clients()
            return data
        elif func == 'accounts':
            data = self.broker.query_accounts(account)
            return data
        elif func == 'positions':
            data = self.broker.query_positions(account)
            if isinstance(data, dict):
                data['hold_available'] = data['hold_available'].to_dict()
            return data
        elif func == 'orders':
            status = self.get_argument('status', '')
            return self.broker.query_orders(account, status)
        elif func == 'cancel_order':
            orderid = self.get_argument('orderid')
            return self.broker.cancel_order(account, orderid)

    def get(self):
        func = self.get_argument('func', 'ping')
        account = self.get_argument('account', None)
        print(account)
        print(func)
        data = self.funcs(func, account)
        print(data)
        if isinstance(data, pd.DataFrame):
            self.write({'result': QA_util_to_json_from_pandas(data)})
        else:
            self.write({'result': data})


class AccModelHandler(QAWebSocketHandler):
    port = QA_Portfolio()

    def open(self):
        self.write_message('QUANTAXIS BACKEND:realtime socket start')

    def on_message(self, message):
        try:
            message = message.split('_')
            self.write_message({'input_param': message})
            if message[0] == 'create':
                if message[1] == 'account':
                    self.account = self.port.new_account()
                    self.write_message('CREATE ACCOUNT :{}'.format(self.account.account_cookie))
                    self.write_message(self.account.init_assets)
            elif message[0] == 'query':
                pass
        except:
            pass
