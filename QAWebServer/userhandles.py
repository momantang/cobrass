import datetime
import json

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QASU.user import QA_user_sign_in, QA_user_sign_up
from QUANTAXIS.QAUtil.QASetting import DATABASE
from QUANTAXIS.QAUtil.QASql import QA_util_sql_mongo_setting
from QAWebServer.basehandles import QABaseHandler


class SignupHandler(QABaseHandler):
    """注册接口

           Arguments:
               QABaseHandler {[type]} -- [description]
               user/signin?user=xxx&password=xx
           Return
               'SUCCESS' if success
               'WRONG' if wrong
           """

    def get(self):
        username = self.get_argument('user', default='admin')
        password = self.get_argument('password', default='admin')
        if QA_user_sign_up(username, password, client=QA_util_sql_mongo_setting()):
            self.write('SUCCESS')
        else:
            self.write('WRONG')


class SigninHandler(QABaseHandler):
    def get(self):
        """登陆接口

             Arguments:
                 QABaseHandler {[type]} -- [description]
                 user/signup?user=xxx&password=xx
             Return
                 'SUCCESS' if success
                 'WRONG' if wrong
             """
        username = self.get_argument('user', default='admin')
        password = self.get_argument('password', default='admin')
        res = QA_user_sign_in(username, password, client=QA_util_sql_mongo_setting())
        if res is not None:
            self.write('SUCCESS')
        else:
            self.set_header(
                'Content-Type', 'text/html; charset=UTF-8')
            self.write('WRONG')


class PersonBlockHandler(QABaseHandler):
    def get(self):
        """
               make table for user: user
               send in ==> {'block',[{'block':xxxx,'code':code}}
               """
        table = DATABASE.user_block
        data = table.find_one()
        print(data)
        data.pop('_id')
        self.write(data)

    def post(self):
        """
        make table for user: user
        send in ==> {'block',[{'block':xxxx,'code':code}}
        """
        param = eval(self.get_argument('block'))
        print(param)
        table = DATABASE.user_block
        table.insert({'block': param})
        # table.find_one_and_update('')


if __name__ == '__main__':
    app = Application(
        handlers=[

            (r"/user/signin", SigninHandler),
            (r"/user/signup", SignupHandler)
        ],
        debug=True
    )
    app.listen(8010)
    tornado.ioloop.IOLoop.instance().start()
