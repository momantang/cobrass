from copy import deepcopy, copy
import pandas as pd
from QUANTAXIS.QAFetch.QATdx import QA_fetch_get_stock_realtime


class QA_DataStruct_Stock_block():
    def __init__(self, DateFrame):
        self.data = DateFrame
        assert isinstance(DateFrame.index, pd.MultiIndex)
        self.index = self.data.index.remove_unused_levels()

    def __repr__(self):
        return '<QA_DataStruct_Stock_Block>'

    def __call__(self):
        return self.data

    def new(self, data):
        temp = copy(self)
        temp.__init__(data)
        return temp

    @property
    def len(self):
        return len(self.data)

    @property
    def block_name(self):
        return self.index.levels[0].tolist()

    @property
    def code(self):
        return self.index.levels[1].tolist()

    @property
    def view_code(self):
        """按股票排列的查看blockname的视图"""
        return self.data.groupby(level=1).apply(lambda x: [item for item in x.index.remove_unused_levels().levels[0]])

    @property
    def view_block(self):
        """
        按版块排列查看的code的视图
        :return:
        """
        return self.data.groupby(level=0).apply(lambda x: [item for item in x.index.remove_unused_levels().levels[1]])

    def show(self):
        return self.data

    def get_code(self, code):
        return self.new(self.data.loc[(slice(None), code), :])

    def get_block(self, block_name):
        return self.new(self.data.loc[(block_name, slice(None)), :])

    def get_both_code(self, code):
        """get_both_code 获取几个股票相同的版块

        Arguments:
            code {[type]} -- [description]

        Returns:
            [type] -- [description]
        """

        return self.new(self.data.loc[(slice(None), code), :])

    def get_both_block(self, block_name):
        pass
    # def getdtype(self, dtype):
    #     """getdtype

    #     Arguments:
    #         dtype {str} -- gn-概念/dy-地域/fg-风格/zs-指数

    #     Returns:
    #         [type] -- [description]
    #     """

    #     return QA_DataStruct_Stock_block(self.data[self.data['type'] == dtype])

    # def get_price(self, _block_name=None):
    #     """get_price

    #     Keyword Arguments:
    #         _block_name {[type]} -- [description] (default: {None})

    #     Returns:
    #         [type] -- [description]
    #     """

    #     if _block_name is not None:
    #         try:
    #             code = self.data[self.data['blockname']
    #                              == _block_name].code.unique().tolist()
    #             # try to get a datastruct package of lastest price
    #             return QA_fetch_get_stock_realtime(code)

    #         except:
    #             return "Wrong Block Name! Please Check"
    #     else:
    #         code = self.data.code.unique().tolist()
    #         return QA_fetch_get_stock_realtime(code)
