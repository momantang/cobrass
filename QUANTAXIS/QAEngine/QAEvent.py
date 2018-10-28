from abc import abstractmethod

"""QUANTAXIS EVENT
EVENT 是会被推送进QUEUE的任务class
通过EVENT_QUEUE.get()拿到标准的event,然后执行"""


class QA_Worker(object):
    """JOB是worker 需要接受QA_EVENT 需要完善RUN方法
        👻QA_Broker 继承这个类
        👻QA_Account 继承这个类
        👻QA_OrderHandler 继承这个类
        这些类都要实现run方法，在其它线程🌀中允许自己的业务代码
    """

    def __init__(self):
        self.type = None

    def __repr__(self):
        return '< QA_Worker {} id = {} >'.format(self.type, id(self))

    @abstractmethod
    def run(self, event):
        '''
        QA_Work是一个抽象类， 继承这个类，需要实现具体的run方法， 在其它线程🌀中执行
        :param event: QA_Event 类型
        :return: None
        '''
        raise NotImplementedError


class QA_Event(object):
    '''
    QA_Event 事件
    '''

    def __init__(self, event_type=None, func=None, message=None, callback=False, *args, **kwargs):
        self.event_type = event_type
        self.func = func
        self.message = message
        self.callback = callback
        # This statement supports dynamic execution of Python code
        for item in kwargs.keys():
            exec('self.{}=kwargs[item]'.format(item))

    # for debug purpose
    def __repr__(self):
        return "< QA_Event {} {} {} , id = {} >".format(self.event_type, self.message, self.callback, id(self))
