import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
from QUANTAXIS.QASU.save_tdx_code import QA_SU_save_stock_min_list
from QUANTAXIS.QAFetch.QATdx import QA_fetch_get_stock_list

stock_list = QA_fetch_get_stock_list().code.tolist()
l = list()
for stock in stock_list:
    if stock.startswith('601'):
        l.append(stock)
QA_SU_save_stock_min_list(stock_list=l)
print(l)
