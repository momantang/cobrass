from django.test import TestCase
from . import cron
from . import snapshot
from finance.models import Stock
from unittest import skip
from utils import mail_util
from django.test.utils import override_settings


# Create your tests here.

class CornTests(TestCase):
    @skip("dont want to test")
    def test_down_market_snapshot(self):
        df = cron.down_market_snapshot(save=False)
        # df = df[df['open'] > 0]
        # df['change'] = (df['now'] - df['open']) / df['open']
        # print(df[df['change'] > 0.08])
        self.assertEqual(df.shape, (4732, 35))


@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class SnapShotTests(TestCase):
    @skip('')
    def test_interest_stock_snapshot(self):
        stock1 = Stock(name='中国平安', code='601318', is_interest=True)
        stock1.save()
        stock2 = Stock(name='贵州茅台', code='600519', is_interest=True)
        stock2.save()
        stock3 = Stock(name='贵州茅台', code='000001', is_interest=True)
        stock3.save()
        stocks = Stock.objects.filter(is_interest=True)
        df = snapshot.df_snapshot
        mail_util.send_email_stock_snapshot(df, how='up', emails=['448006212@qq.com'])
        # df = snapshot.interest_stock_snapshot(snapshot.df_snapshot)
