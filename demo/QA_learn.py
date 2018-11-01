import sys

sys.path.insert(0, '/Users/momantang/PyCharmProjects/cobrass')
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_day_adv
import QUANTAXIS as QA
from QUANTAXIS.QASU.save_financialfiles import QA_SU_save_financial_files

if __name__ == '__main__':
    """
    
    print("hello world")
    data1 = QA_fetch_stock_day_adv(['000001','000002'], '2017-01-01', '2017-10-01')
    data1.plot()
    print(type(data1.data))
    """
    # data = qa.QA_fetch_stock_day_adv('600066', '2013-12-01', '2017-10-01')
    # s = qa.QAAnalysis_stock(data)
    # res = qa.QA_fetch_financial_report(['000001', '600100'],
    # ['2017-03-31', '2017-06-30', '2017-09-31', '2017-12-31', '2018-03-31'])
    # res = QA.QA_fetch_get_stock_realtime('tdx', '000001')
    # print(res)
    res = QA.QA_fetch_financial_report(['000001', '600100'],
                                       ['2017-03-31', '2017-06-30', '2017-09-31', '2017-12-31', '2018-03-31'])
    print(res)
