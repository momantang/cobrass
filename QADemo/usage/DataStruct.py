import os
import sys

sys.path.append(os.path.expanduser('~') + os.sep + 'PycharmProjects' + os.sep + "cobrass")

import QUANTAXIS as QA

if __name__ == '__main__':
    print(sys.path)
    # 首先进行数据获取 多个股票的日线数据

    # QA.QA_fetch_stock_day_adv("000001",'2017-01-01','2017-11-30')
    data = QA.QA_fetch_stock_day_adv(["000001", '000002', '000004'], '2017-01-01', '2017-11-30')

    print(data)
    c = data.data
    print(c.index.levels[0])
    print(data.open)
    data.show()
