from QUANTAXIS.QAUtil.QARandom import QA_util_random_with_topic

"""标准的QUANTAXIS事件方法,具有QA_Thread,QA_Event等特性,以及一些日志和外部接口"""


class QA_Task():
    def __init__(self, worker, event, engine=None, callback=False):
        self.worker = worker
        self.event = event
        self.res = None
        self.callback = callback
        self.task_id = QA_util_random_with_topic('Task')
        self.engine = engine

    def __repr__(self):
        return '< QA_Task engine {} , worker {} , event {},  id = {} >'.format(self.engine, self.worker, self.event,
                                                                               id(self))

    def do(self):
        self.res = self.worker.run(self.event)
        if self.callback:
            self.callback(self.res)

    @property
    def result(self):
        # return {
        #     'task_id': self.task_id,
        #     'result': self.res,
        #     'worker': self.worker,
        #     'event': self.event
        # }
        return {
            'task_id': self.task_id,
            'result': self.res
        }
