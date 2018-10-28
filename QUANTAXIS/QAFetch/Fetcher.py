from QUANTAXIS.QAFetch import QAEastMoney as QAEM
from QUANTAXIS.QAFetch import QAQuery
from QUANTAXIS.QAFetch import QAQuery_Advance as QAQueryAdv
from QUANTAXIS.QAFetch import QAQuery_Async as QAQueryAsync
from QUANTAXIS.QAFetch import QATdx as QATdx
from QUANTAXIS.QAFetch import QAThs as QAThs
from QUANTAXIS.QAFetch import QATushare as QATushare
# from QUANTAXIS.QAFetch import QAWind as QAWind
from QUANTAXIS.QAUtil.QAParameter import (DATABASE_TABLE, DATASOURCE,
                                          FREQUENCE, MARKET_TYPE,
                                          OUTPUT_FORMAT)
from QUANTAXIS.QAUtil.QASql import QA_util_sql_mongo_setting


class QA_Fetcher():
    def __init__(self, uri='mongodb://127.0.0.1:27017/quantaxis', username='', password=''):
        self.database = QA_util_sql_mongo_setting(uri).quantaxis
        self.history = {}
        self.best_ip = QATdx.select_best_ip()

    def change_ip(self, uri):
        self.database = QA_util_sql_mongo_setting(uri).quantaxis
        return self

    def get_quotation(self, code=None, start=None, end=None, frequence=None, market=None, source=None, output=None):
        """
        Arguments:
            code {str/list} -- 证券/股票的代码
            start {str} -- 开始日期
            end {str} -- 结束日期
            frequence {enum} -- 频率 QA.FREQUENCE
            market {enum} -- 市场 QA.MARKET_TYPE
            source {enum} -- 来源 QA.DATASOURCE
            output {enum} -- 输出类型 QA.OUTPUT_FORMAT
        """
        pass

    def get_info(self, code, frequence, market, source, output):
        if source is DATASOURCE.TDX:
            res = QATdx.QA_fetch_get_stock_info(code, self.best_ip)
        elif source is DATASOURCE.MONGO:
            res = QAQuery.QA_fetch_stock_info(code, format=output, collections=self.database.stock_info)
            return res


# todo 🛠 output 参数没有用到， 默认返回的 是 QA_DataStruct


def QA_quotation(code, start, end, frequence, market, source, output):
    """一个统一的fetch

    Arguments:
        code {str/list} -- 证券/股票的代码
        start {str} -- 开始日期
        end {str} -- 结束日期
        frequence {enum} -- 频率 QA.FREQUENCE
        market {enum} -- 市场 QA.MARKET_TYPE
        source {enum} -- 来源 QA.DATASOURCE
        output {enum} -- 输出类型 QA.OUTPUT_FORMAT

    """
    if market is MARKET_TYPE.STOCK_CN:
        if frequence is FREQUENCE.DAY:
            if source is DATASOURCE.MONGO:
                res = QAQueryAdv.QA_fetch_stock_day_adv(code, start, end)
            elif source is DATASOURCE.TDX:
                res = QATdx.QA_fetch_get_stock_day(code, start, end, '00')
            elif source is DATASOURCE.TUSHARE:
                res = QATushare.QA_fetch_get_stock_day(code, start, end, '00')
        elif frequence in [FREQUENCE.ONE_MIN, FREQUENCE.FIVE_MIN, FREQUENCE.FIFTEEN_MIN, FREQUENCE.THIRTY_MIN,
                           FREQUENCE.SIXTY_MIN]:
            if source is DATASOURCE.MONGO:
                res = QAQueryAdv.QA_fetch_stock_min_adv(
                    code, start, end, frequence=frequence)
            elif source is DATASOURCE.TDX:
                res = QATdx.QA_fetch_get_stock_min(
                    code, start, end, frequence=frequence)
        elif frequence is FREQUENCE.TICK:
            if source is DATASOURCE.TDX:
                res = QATdx.QA_fetch_get_stock_transaction(code, start, end)

    # 指数代码和股票代码是冲突重复的，  sh000001 上证指数  000001 是不同的
    elif market is MARKET_TYPE.INDEX_CN:
        if frequence is FREQUENCE.DAY:
            if source is DATASOURCE.MONGO:
                res = QAQueryAdv.QA_fetch_index_day_adv(code, start, end)

    elif market is MARKET_TYPE.OPTION_CN:
        if source is DATASOURCE.MONGO:
            # res = QAQueryAdv.QA_fetch_option_day_adv(code, start, end)
            raise NotImplementedError('CURRENT NOT FINISH THIS METHOD')
    # print(type(res))
    return res


class AsyncFetcher():
    def __init__(self):
        pass

    async def get_quotation(self, code=None, start=None, end=None, frequence=None, market=MARKET_TYPE.STOCK_CN,
                            source=None, output=None):
        if market is MARKET_TYPE.STOCK_CN:
            if frequence is FREQUENCE.DAY:
                if source is DATASOURCE.MONGO:
                    res = await QAQueryAsync.QA_fetch_stock_day(code, start, end)
                elif source is DATASOURCE.TDX:
                    res = QATdx.QA_fetch_get_stock_day(
                        code, start, end, frequence=frequence)
            elif frequence in [FREQUENCE.ONE_MIN, FREQUENCE.FIVE_MIN, FREQUENCE.FIFTEEN_MIN, FREQUENCE.THIRTY_MIN,
                               FREQUENCE.SIXTY_MIN]:
                if source is DATASOURCE.MONGO:
                    res = await QAQueryAsync.QA_fetch_stock_min(code, start, end, frequence=frequence)
                elif source is DATASOURCE.TDX:
                    res = QATdx.QA_fetch_get_stock_min(
                        code, start, end, frequence=frequence)
        return res


if __name__ == '__main__':
    import asyncio

    # print(QA_quotation('000001', '2017-01-01', '2017-01-31', frequence=FREQUENCE.DAY,
    #                   market=MARKET_TYPE.STOCK_CN, source=DATASOURCE.TDX, output=OUTPUT_FORMAT.DATAFRAME))
    Fetcher = AsyncFetcher()
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.gather(
        # 这几个是异步的
        Fetcher.get_quotation('000001', '2018-07-01', '2018-07-15',
                              FREQUENCE.DAY, MARKET_TYPE.STOCK_CN, DATASOURCE.MONGO),
        Fetcher.get_quotation('000001', '2018-07-12', '2018-07-15',
                              FREQUENCE.FIFTEEN_MIN, MARKET_TYPE.STOCK_CN, DATASOURCE.MONGO),
        # 这个是同步的
        Fetcher.get_quotation('000001', '2018-07-12', '2018-07-15',
                              FREQUENCE.FIFTEEN_MIN, MARKET_TYPE.STOCK_CN, DATASOURCE.TDX),
    ))

    print(res)
