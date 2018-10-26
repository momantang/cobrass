import os
import json
from pytdx.reader import TdxMinBarReader
from QUANTAXIS.QAUtil import DATABASE, QA_util_date_stamp, QA_util_log_info, QA_util_time_stamp


def QA_save_tdx_to_mongo(file_dir, client=DATABASE):
    reader = TdxMinBarReader()
    __coll = client.stock_min_five
    for a, v, files in os.walk(file_dir):
        for file in files:
            if (str(file)[0:2] == 'sh' and int(str(file)[2]) == 6) or (
                    str(file)[0:2] == 'sz' and int(str(file)[2]) == 0) or (
                    str(file)[0:2] == 'sz' and int(str(file)[2]) == 3):
                QA_util_log_info('Now_saving ' + str(file)[2:8] + "\s 5 min tick")
                fname = file_dir + os.sep + file
                df = reader.get_df(fname)
                df['code'] = str(file)[2:8]
                df['market'] = str(file)[0:2]
                df['datetime'] = [str(x) for x in list(df.index)]
                df['date'] = [str(x)[0:10] for x in list(df.index)]
                df['time_stamp'] = df['datetime'].apply(
                    lambda x: QA_util_time_stamp(x))
                df['date_stamp'] = df['date'].apply(
                    lambda x: QA_util_date_stamp(x))
                data_json = json.loads(df.to_json(orient='records'))
                __coll.insert_many(data_json)
