from django.db import models


# Create your models here.

class Stock(models.Model):
    code = models.CharField(u'股票代码', max_length=10, unique=True)
    name = models.CharField(u'股票名称', max_length=30)
    mark = models.CharField(u'股票备注', max_length=200)
