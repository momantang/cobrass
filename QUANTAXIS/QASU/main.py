from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_list
from QUANTAXIS.QAUtil import DATABASE

from QUANTAXIS.QASU import save_tdx as stdx
from QUANTAXIS.QASU import save_tdx_file as tdx_file
from QUANTAXIS.QASU import save_tushare as sts


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


def QA_SU_crawl_eastmoney(acion="zjlx", stockCode=None):
    stockItems = QA_fetch_stock_list()

    if stockCode == 'all':
        print("一共需要获取%d 个股票的资金流向，需要大概%d 小时" % (len(stockItems), len(stockItems) * 5 / 60 / 60))

        code_list = []
        for stock in stockItems:
            code_list.append(stock['code'])
