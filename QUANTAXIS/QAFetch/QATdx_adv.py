import datetime
import queue
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Timer

import pandas as pd
from pytdx.hq import TdxHq_API

from QUANTAXIS.QAUtil.QADate_trade import QA_util_if_tradetime
from QUANTAXIS.QAUtil.QASetting import DATABASE, stock_ip_list
from QUANTAXIS.QAUtil.QASql import QA_util_sql_mongo_sort_ASCENDING
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas


