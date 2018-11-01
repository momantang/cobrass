# 直接获取数据
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
import QUANTAXIS as QA

if __name__ == '__main__':
    data1 = QA.QA_fetch_get_stock_list('tdx')
    data1.plot()
    print(data1.head())
