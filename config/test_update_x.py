import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
import unittest

from QUANTAXIS.QASU.main import QA_SU_save_stock_day

from config import update_x


class update_x_test(unittest.TestCase):
    def test_QA_SU_save_stock_day(self):
        QA_SU_save_stock_day('tdx')


if __name__ == '__main__':
    unittest.main()
