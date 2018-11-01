class Calendar(firstweekday=0):
    pass


class TRADE_TIME():
    def __init__(self, *args, **kwargs):
        self.trading_days = None

    def get_trading_day(self):
        raise NotImplementedError

    def get_trading_time(self):
        raise NotImplementedError
