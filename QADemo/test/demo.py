import os
import sys
import pprint
import pandas as pd

sys.path.append(os.path.expanduser('~') + os.sep + 'PycharmProjects' + os.sep + "cobrass")

import QUANTAXIS as QA
import numpy

if __name__ == '__main__':
    data = QA.QA_fetch_financial_report('601318')
    pprint.pprint(data.T)
