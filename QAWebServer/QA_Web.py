import os
import sys
import tornado

from tornado.web import Application, RequestHandler, authenticated
from tornado.options import define, parse_command_line, parse_config_file, options
from QAWebServer.arphandles import (AccountHandler, MemberHandler,
                                    RiskHandler)
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
from tornado_http2.server import Server
from QUANTAXIS.QAUtil.QASetting import QASETTING


class INDEX(QABaseHandler):

    def get(self):
        self.set_header(
            'Content-Type', 'text/html; charset=UTF-8')
        self.render("index.html")


handlers = [
    (r"/", INDEX),
    (r"/marketdata/stock/day", StockdayHandler),
    (r"/marketdata/stock/min", StockminHandler),
    (r"/marketdata/stock/block", StockBlockHandler),
    (r"/marketdata/stock/price", StockPriceHandler),
    (r"/marketdata/stock/code", StockCodeHandler),
    (r"/user/signin", SigninHandler),
    (r"/user/signup", SignupHandler),
    (r"/user/blocksetting", PersonBlockHandler),
    (r"/strategy/content", StrategyHandler),
    (r"/backtest/content", BacktestHandler),
    (r"/trade", AccModelHandler),
    (r"/tradeinfo", TradeInfoHandler),
    (r"/realtime", RealtimeSocketHandler),
    (r"/simulate", SimulateSocketHandler),
    (r"/monitor", MonitorSocketHandler),
    (r"/accounts", AccountHandler),
    (r"/accounts/all", MemberHandler),
    (r"/risk", RiskHandler),
    (r"/command/run", CommandHandler),
    (r"/command/runbacktest", RunnerHandler),
    (r"/command/jobmapper", JOBHandler)
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
