计划安排
====

####第一步：下载数据，并推送关心数据
+ 完善A股财务数据
+ 完善A股分时数据和日数据
+ 筛选关心数据
+ 完善数据的可视化

####第二步，学习股票各种参数的意义




个人记录
====
```
mongod --dbpath /User/momantang/dev/data/db
```
```angular2html

python manage.py makemigrations app
python manage.py sqlmigrate app 0001
python manage.py migrate


```
```angular2html

import pymongo
import json

conn = pymongo.Connection('127.0.0.1', port=27017)
df = ts.get_tick_data('600848',date='2014-12-22')

conn.db.tickdata.insert(json.loads(df.to_json(orient='records')))
```


有用网址
====

项目网址
----
- <https://github.com/shidenggui/easyutils>
- [pytdx]()
- [easyhistory](https://github.com/shidenggui/easyhistory)
- [easyquotation](https://github.com/shidenggui/easyquotation)
- [tushare]() [pro]()
-


