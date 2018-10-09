from django.test import TestCase
from . import cron


# Create your tests here.

class CornTests(TestCase):
    def test_down_market_snapshot(self):
        df = cron.down_market_snapshot(save=False)
        #df = df[df['open'] > 0]
        #df['change'] = (df['now'] - df['open']) / df['open']
        #print(df[df['change'] > 0.08])
        self.assertEqual(df.shape, (4732, 33))
