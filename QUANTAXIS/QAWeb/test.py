import os
import sys
import pandas as pd
sys.path.insert(0, '/Users/momantang/PycharmProjects/cobrass/')
sys.path

from QUANTAXIS.QAWeb.fetch_block import get_block

if __name__ == '__main__':
    #url = "ths_block.csv"
    #df=pd.read_csv(url).set_index('code', drop=False)
    #print(df.head())
    blocks = (get_block(['苹果概念']))
    print(sys.version_info)