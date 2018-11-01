from QUANTAXIS.QAData.QADataStruct import QA_DataStruct_Stock_transaction
from QUANTAXIS.QAFetch.QATdx import QA_fetch_get_stock_transaction, QA_fetch_get_future_transaction_realtime
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_info


class QAAnalysis_Transaction():
    def __init__(self):
        self.data = None
        self.code = None
        self.stock_info = None

    def get_data(self, code, start, end):
        self.code = code
        try:
            self.data = QA_DataStruct_Stock_transaction(QA_fetch_get_stock_transaction(code, start, end))
            return self.data
        except Exception as e:
            raise e

    def get_stock_info(self, code):
        try:
            self.stock_info = QA_fetch_stock_info(code)
        except Exception as e:
            raise e

    def winner(self):
        pass
