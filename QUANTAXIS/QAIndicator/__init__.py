from QUANTAXIS.QAIndicator.indicators import *
from QUANTAXIS.QAIndicator.base import *

"""
这个模块是对了对应QA_DataStruct

可以被add_func来添加,所以 这个模块的函数必须有一个DataFrame的输入


例如 

import QUANTAXIS as QA
data=QA.QA_fetch_stock_day_adv('000001','2017-01-01','2017-01-31')
data.add_func(QA.)
"""
