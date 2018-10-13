from django.db import models


# Create your models here.

class Stock(models.Model):
    code = models.CharField(u'股票代码', max_length=10, unique=True)
    name = models.CharField(u'股票名称', max_length=30, null=True)
    mark = models.CharField(u'股票备注', max_length=200, null=True)
    is_interest = models.BooleanField(u'是否关注', default=False)


class StockBasic(models.Model):
    """
    根据tushare的接口:stock_basic
    """
    abu_code = models.CharField(u'abu代码', max_length=10, null=True)  # 用于abupy查询
    ts_code = models.CharField(u'TS代码', max_length=10, null=True)  # 用于tushare查询
    symbol = models.CharField(u'股票代码', max_length=10, unique=True)
    name = models.CharField(u'股票名称', max_length=20, unique=True)
    area = models.CharField(u'所在区域', max_length=20, null=True)
    industry = models.CharField(u'所属行业', max_length=30, null=True)
    fullname = models.CharField(u'股票全称', max_length=80, null=True)
    enname = models.CharField(u'英文全称', max_length=80, null=True)
    market = models.CharField(u'市场类型', max_length=10, null=True)  # （主板/中小板/创业板）
    exchange_id = models.CharField(u'交易所代码', max_length=10, null=True)
    curr_type = models.CharField(u'交易货币', max_length=10, null=True)
    list_status = models.CharField(u'上市状态', max_length=1, null=True)  # 上市状态： L上市 D退市 P暂停上市
    list_date = models.CharField(u'上市日期', max_length=20, null=True)
    delist_date = models.CharField(u'退市日期', max_length=20, null=True)
    is_hs = models.CharField(u'沪深港通', max_length=1, null=True)  # 是否沪深港通标的，N否 H沪股通 S深股通


class MarketSnapshot(models.Model):
    date = models.DateTimeField(u'快照时间', null=True)
    context = models.TextField(u'快照文本', null=True)


class StockIndexSnapShot(models.Model):
    date = models.DateTimeField(u'快照时间', null=True)
    context = models.TextField(u'快照文本', null=True)


class StockIndex(models.Model):
    code = models.CharField(u'股指代码', max_length=10, null=True)
    name = models.CharField(u'股指名称', max_length=30, null=True)
    price = models.FloatField(u'价钱', null=True)


# 记录定时任务
class CrontabAction(models.Model):
    date = models.DateTimeField(u'执行时间')
    name = models.CharField(u'任务名称', max_length=30)
    description = models.CharField(u'任务描述', max_length=100)
