# coding:utf8
"""
    some copy from https://github.com/shidenggui/easyutils/blob/master/easyutils/stock.py
"""
import re
import datetime
import requests
import io


def get_stock_type(stock_code):
    """判断股票ID对应的证券市场
       匹配规则
       ['50', '51', '60', '90', '110'] 为 sh
       ['00', '13', '18', '15', '16', '18', '20', '30', '39', '115'] 为 sz
       ['5', '6', '9'] 开头的为 sh， 其余为 sz
       :param stock_code:股票ID, 若以 'sz', 'sh' 开头直接返回对应类型，否则使用内置规则判断
       :return 'sh' or 'sz'"""
    assert type(stock_code) is str, 'stock code need str type'
    if stock_code.startswith(("sh", "sz")):
        return stock_code[:2]
    if stock_code.startswith(
            ("50", "51", "60", "90", "110", "113", "132", "204")
    ):
        return "sh"
    if stock_code.startswith(
            ("00", "13", "18", "15", "16", "18", "20", "30", "39", "115", "1318")
    ):
        return "sz"
    if stock_code.startswith(("5", "6", "9", "7")):
        return "sh"
    return "sz"


def get_code_type(code):
    """
    判断代码是属于那种类型，目前仅支持 ['fund', 'stock']
    :return str 返回code类型, fund 基金 stock 股票
    """
    if code.startswith(("00", "30", "60")):
        return "stock"
    return "fund"


def get_all_stock_codes():
    """获取所有股票 ID"""
    all_stock_codes_url = "http://www.shdjt.com/js/lib/astock.js"
    grep_stock_codes = re.compile("~(\d+)`")
    response = requests.get(all_stock_codes_url)
    stock_codes = grep_stock_codes.findall(response.text)
    return stock_codes


def round_price_by_code(price, code):
    """
    根据代码类型[股票，基金] 截取制定位数的价格
    :param price: 证券价格
    :param code: 证券代码
    :return: str 截断后的价格的字符串表示
    """
    if isinstance(price, str):
        return price

    typ = get_code_type(code)
    if typ == "fund":
        return "{:.3f}".format(price)
    return "{:.2f}".format(price)


def get_ipo_info(only_today=False):
    import pyquery

    response = requests.get(
        "http://vip.stock.finance.sina.com.cn/corp/go.php/vRPD_NewStockIssue/page/1.phtml",
        headers={"accept-encoding": "gzip, deflate, sdch"},
    )
    html = response.content.decode("gbk")

    html_obj = pyquery.PyQuery(html)
    table_html = html_obj("#con02-0").html()

    import pandas as pd

    df = pd.read_html(
        io.StringIO(table_html),
        skiprows=3,
        converters={"证券代码": str, "申购代码": str},
    )[0]
    if only_today:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        df = df[df["上网发行日期↓"] == today]
    return df


if __name__ == '__main__':
    df = get_all_stock_codes()
    print(df)
