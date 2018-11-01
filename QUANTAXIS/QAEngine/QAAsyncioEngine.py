import asyncio
import datetime
import threading
import time
import traceback

import future

from QUANTAXIS.QAFetch.QAQuery_Async import QA_fetch_stock_day


"""quantaxis 异步引擎


"""


class QAAsync():
    def __init__(self):
        self.event_loop = asyncio.new_event_loop()
        self.elthread = threading.Thread(target=self.event_loop.run_forever)

        # self.elthread.setDaemon(True)
        self.elthread.start()

    def create_task(self, func, callback, *args, **kwargs):
        # schedule a task

        #task = self.event_loop.create_task(func(*args,**kwargs))
        task = asyncio.ensure_future(func(*args, **kwargs))
        task.add_done_callback(callback)
        return task


    def submit(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self.event_loop)


def callback(future):
    r = future.result()
    print(len(r))
    print(datetime.datetime.now()-time)


"""

run_until_complete 

"""


if __name__ == '__main__':
    time = datetime.datetime.now()
    QAE = QAAsync()

    print(datetime.datetime.now()-time)
    QAE.submit(QA_fetch_stock_day, callback,
               '000001', '1990-01-01', '2018-01-31')
    QAE.submit(QA_fetch_stock_day, callback,
               '000002', '1990-01-01', '2018-01-31')
    QAE.submit(QA_fetch_stock_day, callback,
               '000007', '1990-01-01', '2018-01-31')
    QAE.submit(QA_fetch_stock_day, callback,
               '000004', '1990-01-01', '2018-01-31')
    QAE.submit(QA_fetch_stock_day, callback,
               '000005', '1990-01-01', '2018-01-31')

    # import QUANTAXIS as QA
    # time=datetime.datetime.now()
    # r=QA.QA_fetch_stock_day('000001','1990-01-01', '2018-01-31')
    # print(len(r))
    # #print(datetime.datetime.now()-time)
    # r=QA.QA_fetch_stock_day('000002','1990-01-01', '2018-01-31')
    # print(len(r))
    # r=QA.QA_fetch_stock_day('000007','1990-01-01', '2018-01-31')
    # print(len(r))
    # r=QA.QA_fetch_stock_day('000004','1990-01-01', '2018-01-31')
    # print(len(r))
    # r=QA.QA_fetch_stock_day('000005','1990-01-01', '2018-01-31')
    # print(len(r))
    # print(datetime.datetime.now()-time)
