from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_list
from QUANTAXIS.QASU import crawl_eastmoney as crawl_eastmoney_file
from QUANTAXIS.QASU import save_tdx as stdx
from QUANTAXIS.QASU import save_tdx_file as tdx_file
from QUANTAXIS.QASU import save_tushare as sts
from QUANTAXIS.QASU import save_financialfiles
from QUANTAXIS.QAUtil import DATABASE
from QUANTAXIS.QASU import crawl_jrj_financial_reportdate as save_financial_calendar
from QUANTAXIS.QASU import crawl_jrj_stock_divyield as save_stock_divyield

def QA_SU_save_stock_info(engine, client=DATABASE):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_info(client=client)


def QA_SU_save_stock_info_tushare(engine="tushare", client=DATABASE):
    engine = select_save_engine("tushare")
    engine.QA_SU_save_stock_info_tushare()


def QA_SU_save_stock_list(engine, client=DATABASE):
    """save stock_list

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_list(client=client)


def QA_SU_save_index_list(engine, client=DATABASE):
    """save index_list

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_index_list(client=client)


def QA_SU_save_future_list(engine, client=DATABASE):
    """save future_list

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_future_list(client=client)


def QA_SU_save_future_day(engine, client=DATABASE):
    """save future_day

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_future_day(client=client)


def QA_SU_save_future_min(engine, client=DATABASE):
    """save future_min
    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_future_min(client=client)


def QA_SU_save_stock_day(engine, client=DATABASE):
    """save stock_day

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_day(client=client)


def QA_SU_save_option_day(engine, client=DATABASE):
    '''

    :param engine:
    :param client:
    :return:
    '''
    engine = select_save_engine(engine)
    engine.QA_SU_save_option_day(client=client)


def QA_SU_save_option_min(engine, client=DATABASE):
    '''

    :param engine:
    :param client:
    :return:
    '''
    engine = select_save_engine(engine)
    engine.QA_SU_save_option_min(client=client)


def QA_SU_save_option_commodity_min(engine, client=DATABASE):
    '''
    :param engine:
    :param client:
    :return:
    '''
    engine = select_save_engine(engine)
    engine.QA_SU_save_option_commodity_min(client=client)


def QA_SU_save_option_commodity_day(engine, client=DATABASE):
    '''
    :param engine:
    :param client:
    :return:
    '''
    engine = select_save_engine(engine)
    engine.QA_SU_save_option_commodity_day(client=client)


def QA_SU_save_stock_min(engine, client=DATABASE):
    """save stock_min

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_min(client=client)


def QA_SU_save_index_day(engine, client=DATABASE):
    """save index_day

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_index_day(client=client)


def QA_SU_save_index_min(engine, client=DATABASE):
    """save index_min

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_index_min(client=client)


def QA_SU_save_etf_day(engine, client=DATABASE):
    """save etf_day

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_day(client=client)


def QA_SU_save_etf_min(engine, client=DATABASE):
    """save etf_min

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_min(client=client)


def QA_SU_save_stock_xdxr(engine, client=DATABASE):
    """save stock_xdxr

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_xdxr(client=client)


def QA_SU_save_stock_block(engine, client=DATABASE):
    """save stock_block

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_block(client=client)


def select_save_engine(engine):
    '''
    select save_engine , tushare ts Tushare 使用 Tushare 免费数据接口， tdx 使用通达信数据接口
    :param engine: 字符串Str
    :return: sts means save_tushare_py  or stdx means save_tdx_py
    '''
    if engine in ['tushare', 'ts', 'Tushare']:
        return sts
    elif engine in ['tdx']:
        return stdx
    else:
        print(
            'QA Error QASU.main.py call select_save_engine with parameter %s is None of  thshare, ts, Thshare, or tdx',
            engine)


def QA_SU_save_stock_min_5(file_dir, client=DATABASE):
    """save stock_min5

    Arguments:
        file_dir {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})

    Returns:
        [type] -- [description]
    """

    return tdx_file.QA_save_tdx_to_mongo(file_dir, client)


def QA_SU_crawl_eastmoney(action="zjlx", stockCode=None):
    '''

    :param action: zjlx 后期支持其他的操作类型
    :param stockCode: 股票代码
    :return:
    '''
    stockItems = QA_fetch_stock_list()

    if stockCode == "all":
        # 读取tushare股票列表代码
        print("💪 一共需要获取 %d 个股票的 资金流向 , 需要大概 %d 小时" %
              (len(stockItems), (len(stockItems)*5)/60/60))

        code_list = []
        for stock in stockItems:
            code_list.append(stock['code'])
            # print(stock['code'])
        crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(
            code_list)
        # print(stock)

        return
    else:
        # todo 检查股票代码是否合法
        # return crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(stockCode=stockCode)
        code_list = []
        code_list.append(stockCode)
        return crawl_eastmoney_file.QA_request_eastmoney_zjlx(param_stock_code_list=code_list)


def QA_SU_save_financialfiles():
    return save_financialfiles.QA_SU_save_financial_files()

def QA_SU_save_report_calendar_day():
    return save_financial_calendar.QA_SU_save_report_calendar_day()

def QA_SU_save_report_calendar_his():
    return save_financial_calendar.QA_SU_save_report_calendar_his()

def QA_SU_save_stock_divyield_day():
    return save_stock_divyield.QA_SU_save_stock_divyield_day()

def QA_SU_save_stock_divyield_his():
    return save_stock_divyield.QA_SU_save_stock_divyield_his()
