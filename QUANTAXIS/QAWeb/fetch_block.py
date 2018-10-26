import QUANTAXIS as QA
from QUANTAXIS.QAUtil import DATABASE
import pandas as pd
import re


def get_block(block):
    block_db = DATABASE.stock_block
    block = [block] if isinstance(block, str) else block
    block_df = pd.DataFrame([item for item in block_db.find({'blockname': {'$in': block}})])
    return block_df.code.drop_duplicates().tolist()


def get_name(code):
    codelist = QA.QA_fetch_stock_list_adv()
    return QA.QA_util_to_json_from_pandas(codelist.set_index('code', drop=False).loc[code].loc[:, ['code', 'name']])


if __name__ == '__main__':
    blocks = (get_block(['苹果概念']))
