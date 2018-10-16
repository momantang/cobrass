import pandas as pd
from QUANTAXIS.QAUtil.QADate_trade import trade_date_sse
from QUANTAXIS.QAUtil.QADate import QA_util_date_str2int

_sh_url = 'http://www.sse.com.cn/market/dealingdata/overview/margin/a/rzrqjygk{}.xls'
_sz_url = 'http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1837_xxpl&txtDate={}&tab2PAGENO=1&ENCODE=1&TABKEY=tab2'


def QA_fetch_get_sh_margin(date):
    """
    return shanghai margin data
    :param date: date format YYYY-MM-DD
    :return: pandas.DataFrame --res for margin data
    """
    if date in trade_date_sse:
        print()
        data = pd.read_excel(_sh_url.format(QA_util_date_str2int(date)), 1).assign(date=date).assign(sse='sh')
        data.columns = ['code', 'name', 'leveraged_balance', 'leveraged_buyout', 'leveraged_payoff', 'margin_left', 'margin_sell',
                        'margin_repay', 'date', 'sse']
        return data
    else:
        pass


def QA_fetch_get_sz_margin(date):
    """return shenzhen margin data

    Arguments:
        date {str YYYY-MM-DD} -- date format

    Returns:
        pandas.DataFrame -- res for margin data
    """

    if date in trade_date_sse:
        return pd.read_excel(_sz_url.format(date)).assign(date=date).assign(sse='sz')


# http://data.eastmoney.com/zjlx/002433.html
def QA_fetch_zjlx(code=None):
    # TODO 获取资金流向
    pass
