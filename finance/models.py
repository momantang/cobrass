from django.db import models


# Create your models here.

class Stock(models.Model):
    code = models.CharField(u'股票代码', max_length=10, unique=True)
    name = models.CharField(u'股票名称', max_length=30, null=True)
    mark = models.CharField(u'股票备注', max_length=200, null=True)
    is_interest = models.BooleanField(u'是否关注', default=False)


# 记录定时任务
class CrontabAction(models.Model):
    date = models.DateTimeField(u'执行时间')
    name = models.CharField(u'任务名称', max_length=30)
    description = models.CharField(u'任务描述', max_length=100)
