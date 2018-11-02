import datetime
import json
import time

import pymongo
import tornado
from tornado import gen
from tornado.concurrent import Future
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QAFetch.QAQuery import (QA_fetch_stock_day, QA_fetch_stock_min,
                                       QA_fetch_stock_to_market_date)
from QUANTAXIS.QAFetch.QAQuery_Advance import (QA_fetch_stock_day_adv,
                                               QA_fetch_stock_min_adv)
from QUANTAXIS.QAUtil.QADict import QA_util_dict_remove_key
from QUANTAXIS.QAUtil.QASetting import DATABASE
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas
from QAWebServer.basehandles import QABaseHandler
from QAWebServer.fetch_block import get_block, get_name


class StockdayHandler(QABaseHandler):
    def get(self):
        """
                采用了get_arguents来获取参数
                默认参数: code-->000001 start-->2017-01-01 end-->today
                """
        code = self.get_argument('code', default='000001')
        start = self.get_argument('start', default='2017-01-01')
        end = self.get_argument('end', default=str(datetime.date.today()))
        if_fq = self.get_argument('if_fq', default=False)
        return self.get_data(code, start, end, if_fq)

    def get_data(self, code, start, end, if_fq):
        if if_fq:
            data = QA_util_to_json_from_pandas(
                QA_fetch_stock_day_adv(code, start, end).to_qfq().data)

            self.write({'result': data})
        else:
            data = QA_util_to_json_from_pandas(
                QA_fetch_stock_day(code, start, end, format='pd'))

            self.write({'result': data})
