import os
import platform
import sys

sys.path.append(os.path.expanduser('~') + os.sep + 'PycharmProjects' + os.sep + "cobrass")
from schedule import snapshot
from utils.mail_util import send_mail_table

if __name__ == '__main__':
    print(' utils testcd')
    df = snapshot.down_market_snapshot(True)
    send_mail_table(df)
    # print(df[:3].to_html())
