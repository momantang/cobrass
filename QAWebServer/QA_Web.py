import os
import sys

sys.path.insert(0, '/Users/momantang/')

import tornado
import tornado.httpserver
from tornado.web import Application, RequestHandler, authenticated
from tornado.options import define, parse_command_line, parse_config_file, options

from QAWebServer.basehandles import QABaseHandler
from QAWebServer.commandhandler import CommandHandler, RunnerHandler
from QAWebServer.datahandles import (StockBlockHandler, StockCodeHandler,
                                     StockdayHandler, StockminHandler,
                                     StockPriceHandler)
from QAWebServer.quotationhandles import (MonitorSocketHandler,
                                          RealtimeSocketHandler,
                                          SimulateSocketHandler)
from QAWebServer.strategyhandlers import BacktestHandler, StrategyHandler
from QAWebServer.tradehandles import AccModelHandler, TradeInfoHandler
from QAWebServer.userhandles import (PersonBlockHandler, SigninHandler,
                                     SignupHandler)

from QAWebServer.jobhandler import JOBHandler
from tornado.web import RequestHandler

from QUANTAXIS.QAUtil.QASetting import QASETTING


class INDEX(RequestHandler):

    def get(self):
        self.render("index.html")


handlers = [
    (r"/", INDEX),
    (r"/marketdata/stock/day", StockdayHandler),
    (r"/marketdata/stock/min", StockminHandler),
    (r"/marketdata/stock/block", StockBlockHandler),
    (r"/marketdata/stock/price", StockPriceHandler),
    (r"/marketdata/stock/code", StockCodeHandler),
]


def main():
    define("port", default=8010, type=int, help='服务器监听端口号')
    define("address", default='0.0.0.0', type=str, help='服务器店主')
    define("content", default=[], type=str, multiple=True, help="控制台输出雷人")
    parse_command_line()

    apps = Application(
        handlers=handlers,
        debug=True,
    )

    # print(options.content)
    # http_server = tornado.httpserver.HTTPServer(apps)
    http_server = tornado.httpserver.HTTPServer(apps)
    http_server.bind(options.port, address=options.address)
    """增加了对于非windows下的机器多进程的支持
    """
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
    pass


if __name__ == '__main__':
    print('run main')
    main()
