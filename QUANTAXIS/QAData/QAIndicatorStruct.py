"""
指标结构
"""
import pandas as pd


class QA_DataStruct_Indicators():
    """
    指标结构
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<QA_DATASTRUCT_INDICATOR FROM {} TO {} WITH {} CODES>'.format(self.data.index.levels[0][0],
                                                                              self.data.index.levels[0][-1],
                                                                              len(self.data.index.levels[1]))

    @property
    def index(self):
        return self.data.index

    def get_indicator(self, time, code, indicator_name=None):
        """
        获取某一时间的某一股票的指标
        :param time:
        :param code:
        :param indicator_name:
        :return:
        """
        try:
            return self.data.loc[(pd.Timestamp(time), code), indicator_name]
        except:
            raise ValueError('CANNOT FOUND THIS DATE&CODE')

    def get_code(self, code):
        """
        获取某一股票的指标系列
        :param code:
        :return:
        """
        try:
            return self.data.loc[(slice(None), code), :]
        except:
            raise ValueError('CANNOT FOUND THIS CODE')

    def get_timerange(self, start, end, code=None):
        """
        获取某一段时间的某一股票的指标
        :param start:
        :param end:
        :param code:
        :return:
        """
        try:
            return self.data.loc[(slice(pd.Timestamp(start), pd.Timestamp(end)), slice(code)), :]
        except:
            return ValueError('CANNOT FOUND THIS TIME RANGE')

    def groupby(self, by=None, axis=0, level=None, as_index=True, sort=False, group_keys=True, squeeze=False, **kwargs):
        """仿dataframe的groupby写法,但控制了by的code和datetime

        Keyword Arguments:
            by {[type]} -- [description] (default: {None})
            axis {int} -- [description] (default: {0})
            level {[type]} -- [description] (default: {None})
            as_index {bool} -- [description] (default: {True})
            sort {bool} -- [description] (default: {True})
            group_keys {bool} -- [description] (default: {True})
            squeeze {bool} -- [description] (default: {False})
            observed {bool} -- [description] (default: {False})

        Returns:
            [type] -- [description]
        """

        if by == self.index.names[1]:
            by = None
            level = 1
        elif by == self.index.names[0]:
            by = None
            level = 0
        return self.data.groupby(by=by, axis=axis, level=level, as_index=as_index, sort=sort, group_keys=group_keys,
                                 squeeze=squeeze)

    def add_func(self, func, *args, **kwargs):
        return self.groupby(level=1, as_index=False, group_keys=False).apply(func, raw=True, *args, **kwargs)
