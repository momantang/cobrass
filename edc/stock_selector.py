import os
import sys
import platform
import pprint

import pandas as pd
import pymongo

sys.path.append(os.path.expanduser('~') + os.sep + 'PycharmProjects' + os.sep + "cobrass")
# import QUANTAXIS as QA
from local import local_setting as ls
from utils import mongodutils

pro = ls.get_ts_pro()

df_sh = pro.hs_const(hs_type='SH')
df_sz = pro.hs_const(hs_type='SZ')
print(df_sz.shape)
print(df_sh.shape)

df = pd.concat([df_sh, df_sz], ignore_index=True)
print(df.dtypes)
print(df.head())
df = df.assign(code=df.ts_code.str[0:6])
print(df.head())


coll_hst = mongodutils.mongo_client().quantaxis.hs_const
# coll_hst = QA.DATABASE.hst
coll_hst.create_index(
    [("ts_code", pymongo.ASCENDING), ("in_date", pymongo.ASCENDING)])
coll_hst.insert_many(df.to_dict('records'))
pprint.pprint(df)