import unittest

import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

from QUANTAXIS.QAFetch.QAQuery import *


class QAQuery_test(unittest.TestCase):
    def test_QA_fetch_stock_day(self):
        df = QA_fetch_stock_day('6001318', '2018-09-01', '2018-10-01', format='pd')

    def test__frequence(self):
        self.assertEqual('1min', util_frequence('1m'))


if __name__ == '__main__':
    unittest.main()
