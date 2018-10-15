import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

from QUANTAXIS.QAFetch import QATushare
from QUANTAXIS.QAUtil.QABar import QA_util_make_min_index

if __name__ == '__main__':
    print(QATushare.set_token(''))
    print(QA_util_make_min_index('2018-10-15'))
