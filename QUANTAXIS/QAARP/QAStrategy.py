from QUANTAXIS.QAARP.QAAccount import QA_Account
from QUANTAXIS.QAUtil.QAParameter import (AMOUNT_MODEL, FREQUENCE, MARKET_TYPE,
                                          ORDER_DIRECTION, ORDER_MODEL)

class QA_Strategy(QA_Account):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.frequence=FREQUENCE.FIFTEEN_MIN
        self.market_type=MARKET_TYPE.STOCK_CN

    def on_bar(self, event):
        try:
            for item in event.market_data.code:
                if self.sell_available.get(item, 0) > 0:
                    event.send_order(account_id=self.account_cookie,
                                     amount=self.sell_available[item], amount_model=AMOUNT_MODEL.BY_AMOUNT,
                                     time=self.current_time, code=item, price=0,
                                     order_model=ORDER_MODEL.MARKET, towards=ORDER_DIRECTION.SELL,
                                     market_type=self.market_type, frequence=self.frequence,
                                     broker_name=self.broker
                                     )
                else:
                    event.send_order(account_id=self.account_cookie,
                                     amount=100, amount_model=AMOUNT_MODEL.BY_AMOUNT,
                                     time=self.current_time, code=item, price=0,
                                     order_model=ORDER_MODEL.MARKET, towards=ORDER_DIRECTION.BUY,
                                     market_type=self.market_type, frequence=self.frequence,
                                     broker_name=self.broker)
        except Exception as e:
            print(e)
