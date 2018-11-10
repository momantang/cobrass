from jqdatasdk import *
from pyecharts import Kline, Bar, Grid

auth('13925865606', '19844891')
data = get_price('000001.XSHE')
print(data.head())
kline = Kline(width=1360, height=700, page_title='000001')

bar = Bar()
