import os
import sys

sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path
"""
对应的save x 方法
每天凌晨11点执行？
"""
from QUANTAXIS.QASU.main import (QA_SU_save_etf_day, QA_SU_save_etf_min,
                                 QA_SU_save_financialfiles,
                                 QA_SU_save_index_day, QA_SU_save_index_min,
                                 QA_SU_save_stock_block, QA_SU_save_stock_day,
                                 QA_SU_save_stock_info,
                                 QA_SU_save_stock_info_tushare,
                                 QA_SU_save_stock_list, QA_SU_save_stock_min,
                                 QA_SU_save_stock_xdxr,QA_SU_save_report_calendar_day,
                                 QA_SU_save_report_calendar_his,QA_SU_save_stock_divyield_day,
                                 QA_SU_save_stock_divyield_his)
from QUANTAXIS.QASU.save_binance import (QA_SU_save_binance,
                                         QA_SU_save_binance_1day,
                                         QA_SU_save_binance_1hour,
                                         QA_SU_save_binance_1min,
                                         QA_SU_save_binance_symbol)
from QUANTAXIS.QAUtil.QAMySQL import (QA_etl_stock_list, QA_etl_stock_info,
                                      QA_etl_stock_xdxr, QA_etl_stock_day,
                                      QA_etl_stock_financial, QA_etl_stock_calendar,
                                      QA_etl_stock_block, QA_etl_stock_divyield,
                                      QA_etl_process_financial_day)

QA_SU_save_stock_day('tdx')
QA_SU_save_stock_xdxr('tdx')
QA_SU_save_stock_min('tdx')
QA_SU_save_index_day('tdx')
QA_SU_save_index_min('tdx')
QA_SU_save_etf_day('tdx')
QA_SU_save_etf_min('tdx')
QA_SU_save_stock_list('tdx')
QA_SU_save_stock_block('tdx')
QA_SU_save_stock_info('tdx')
#QA_SU_save_stock_divyield_day()
#QA_SU_save_report_calendar_day()
