from copy import deepcopy

import numpy as np
import pandas as pd


class QA_DataStruct_Series():
    def __init__(self, series):
        self.series = series.sort_index()

        if isinstance(series.index, pd.core.indexes.multi.MultiIndex):
            self.if_multindex = True
            self.index = series.index.remove_unused_levels()
        else:
            self.if_multindex = False
            self.index = series.index

    def __repr__(self):
        return '< QA_DATASTRUCT_SEIRES >'

    def __call__(self):
        return self.series

    @property
    def code(self):
        if self.if_multiindex:
            return self.index.levels[1].tolist()
        else:
            return None

    @property
    def datetime(self):
        if self.if_multiindex:
            return self.index.levels[0].tolist()
        elif (self.index, pd.core.indexes.datetimes.DatetimeIndex):
            return self.index
        else:
            return None

    @property
    def date(self):
        if self.if_multiindex:
            return np.unique(self.index.levels[0].date).tolist()
        elif (self.index, pd.core.indexes.datetimes.DatetimeIndex):
            return np.unique(self.index.date).tolist()
        else:
            return None

    def new(self, series):
        temp = deepcopy(self)
        temp.__init__(series)
        return temp

    def select_code(self, code):
        return self.new(self.series.loc[(slice(None), code)])

    def select_time(self, start, end=None):
        if end is None:
            return self.new(self.series.loc[(pd.Timestamp(start), slice(None))])
        else:
            return self.new(self.series.loc[(slice(pd.Timestamp(start), pd.Timestamp(end)), slice(None))])
