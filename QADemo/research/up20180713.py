import os
import sys
import pandas as pd

import QUANTAXIS as QA

if __name__ == '__main__':
    code = QA.QA_fetch_stock_list_adv().code.tolist()
    code1 = QA.QA_fetch_stock_list_adv().set_index('code')
    daydata = QA.QA_fetch_stock_day_adv(code, '2018-07-12', '2018-07-13')
    dailymin_data = QA.QA_fetch_stock_min_adv(code, '2018-07-13', '2018-07-14')
    dailymin5_data = QA.QA_fetch_stock_min_adv(code, '2018-07-13', '2018-07-14', '5min')
    block = QA.QA_fetch_stock_block_adv()
    high_limit = daydata[daydata.close == daydata.high_limit]
    data = dailymin_data.select_code(high_limit.code).fast_moving(0.018)
    print(data)
    # print(daydata.data)
    # print(dailymin_data.data)
    # print(dailymin5_data.data)
