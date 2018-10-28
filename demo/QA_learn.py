import sys

sys.path.insert(0, '/Users/momantang/PyCharmProjects/cobrass')
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_day_adv
import QUANTAXIS as qa
if __name__ == '__main__':
    print("hello world")
    data1 = QA_fetch_stock_day_adv(['000001','000002'], '2017-01-01', '2017-10-01')
    data1.plot()
    print(type(data1.data))
