import unittest

import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
from QUANTAXIS.QACmd import runner


class Runner_Test(unittest.TestCase):
    def test_run_backtest(self):
        pass

    def test_run(self):
        print(runner.run())


if __name__ == '__main__':
    unittest.main()
