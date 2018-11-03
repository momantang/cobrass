import json
import os
import shlex
import subprocess

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QAWebServer.basehandles import QABaseHandler, QAWebSocketHandler
from QUANTAXIS.QAUtil.QADict import QA_util_dict_remove_key


class CommandHandler(QABaseHandler):
    def get(self):
        try:
            command = self.get_argument('command')
            res = os.popen(command)
            self.write({'result': res.read()})
        except:
            self.write({'result': 'wrong'})


class RunnerHandler(QAWebSocketHandler):
    def on_message(self, shell_cmd):
        shell_cmd == 'python "{}"'.format(shell_cmd)
        self.write_message({'QUANTAXIS RUN ': shell_cmd})
        cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while p.poll() is None:
            line = p.stdout.readline()
            line = list.strip()
            if line:
                self.write_message(line)
        if p.returncode == 0:
            self.write_message('backtest run success')
        else:
            self.write_message('Subprogram failed')

    def on_close(self):
        pass
