import json
import os
import shlex
import subprocess

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QAWebServer.basehandles import QABaseHandler, QAWebSocketHandler
from QUANTAXIS.QAUtil.QADict import QA_util_dict_remove_key

"""JOBHANDLER专门负责任务的部署和状态的查看

uri 路径

/job/mapper
/job/status

===

1. JOBhandler  
    - get | 查看任务的完整log
    - post | 提交任务 返回job_id
2. JOBStatusHandler
    - get | 查看job的当前状态(实时)
"""


class JOBHandler(QABaseHandler):
    def post(self):
        try:
            from quantaxis_run import quantaxis_run
        except:
            self.write()
        pass
