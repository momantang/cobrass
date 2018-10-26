from QUANTAXIS.QAUtil import DATABASE
from QUANTAXIS.QASetting.QALocalize import strategy_path
import datetime
import os
import sys
import requests

"""对于策略的存储
"""


def QA_SU_save_strategy(name, portfolio_cookie='default', account_cookie='default', version=1, if_save=False,
                        if_web_request=False, webreuquestsurl='http://localhost:8010/backtest/write'):
    absoult_path = '{}{}strategy_{}.py'.format(strategy_path, os.sep, name)
    with open(sys.argv[0], 'rb') as p:
        data = p.read()
        if if_web_request:
            try:
                requests.get(webreuquestsurl, {'strategy_content': data})
            except:
                pass

        collection = DATABASE.strategy
        collection.insert({'name': name, 'account_cookie': account_cookie,
                           'portfolio_cookie': portfolio_cookie, 'version': version,
                           'last_modify_time': str(datetime.datetime.now()),
                           'content': data.decode('utf-8'),
                           'absoultpath': absoult_path})
        if if_save:
            with open(absoult_path, 'wb') as f:
                f.write(data)


# print(os.path.basename(sys.argv[0]))
if __name__ == '__main__':
    QA_SU_save_strategy('test', if_save=True, if_web_request=True)
