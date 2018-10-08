import tushare
import datetime
import numpy
numpy.set_printoptions(threshold=numpy.nan)

print(datetime.datetime.now())
df_basic = tushare.get_stock_basics()
df_hq = tushare.get_today_all()
print(datetime.datetime.now())
