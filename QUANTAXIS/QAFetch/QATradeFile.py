import csv
import pandas as pd
import QUANTAXIS as QA

_haitong_traderecord = ['成交日期', '证券代码', '证券名称', '买卖标志', '成交价格', '成交数量', '成交金额', '印花税(￥)', '交易征费￥)',
                        '交易费(￥)', '股份交收费(￥)', '佣金(￥)', '交易系统使用费(￥)', '总费用(￥)', '成交编号', '股东代码', '成交时间']

_haitong_traderecord_eng = ['date', 'code', 'name', 'towards', 'price', 'volume', 'money', 'tax_fee', 'sectrade_fee', 'trde_fee',
                            'stock_fee',
                            'stock_settlement_fee', 'commission_fee', 'tradesys_fee', 'total_fee', 'trade_id', 'shareholder',
                            'datetime']


def QA_fetch_get_tdxtraderecord(file):
    """
       QUANTAXIS 读取历史交易记录 通达信 历史成交-输出-xlsfile--转换csvfile
       """
    try:
        with open('./20180606.csv', 'r') as f:
            l = csv.reader(f)
            data = [item for item in l]
        res = pd.DataFrame(data[1:], columns=data[0])
        return res
    except:
        raise IOError('QA CANNOT READ THIS RECORD')
