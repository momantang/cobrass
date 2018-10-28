import os
import sys

import pymongo

from QUANTAXIS.QAFetch.QAfinancial import (download_financialzip, parse_all, parse_filelist)
from QUANTAXIS.QASetting.QALocalize import cache_path, download_path, qa_path, setting_path
from QUANTAXIS.QAUtil import DATABASE, QA_util_date_int2str
from QUANTAXIS.QAUtil.QASql import ASCENDING, DESCENDING
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas


def QA_SU_save_financial_files():
    pass
