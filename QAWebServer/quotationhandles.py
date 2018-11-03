import datetime
import os
import time
import pandas as pd
import pymongo
import tornado
from tornado.iostream import StreamClosedError
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

import QUANTAXIS as QA
from QAWebServer.basehandles import QABaseHandler, QAWebSocketHandler

"""
要实现2个api

1. SIMULATED WEBSOCKET

2. REALTIME WEBSOCKET

"""
client = set()


class INDEX(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class RealtimeSocketHandler(QAWebSocketHandler):
    client = set()

    def open(self):
        self.client.add(self)
        self.write_message('realtime socket start')

    def on_message(self, message):
        try:
            database = QA.DATABASE.get_collection('realtime_{}'.format(datetime.date.today()))
            current = [QA.QA_util_dict_remove_key(item, '_id') for item in
                       database.find({'code': message}, limit=1, sort=[('datetime', pymongo.DESCENDING)])]
            self.write_message(current[0])
        except Exception as e:
            print(e)

    def on_close(self):
        print('connection close')


class SimulateSocketHandler(QAWebSocketHandler):
    def open(self):
        self.write_message('start')

    def on_message(self, message):
        if len(str(message)) == 6:
            data = QA.QA_util_to_json_from_pandas(QA.QA_fetch_stock_day(message, '2017-01-01', '2017-02-05', 'pd'))
            for item in data:
                self.write_message(item)
                time.sleep(0.1)

    def on_close(self):
        print('connection close')


class MonitorSocketHandler(QAWebSocketHandler):
    def open(self):
        self.write_message('start')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print('connection close')


def main():
    app = Application(
        handlers=[
            (r"/", INDEX),
            #        (r"/realtime", RealtimeSocketHandler),
            #        (r"/simulate", SimulateSocketHandler)
        ],
        debug=True
    )
    app.listen(8010)
    tornado.ioloop.IOLoop.instance().start()
