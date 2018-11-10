import psycopg2
import pprint
from utils import stockutil


def connect_pg():
    try:
        conn_string = "host='localhost' dbname='cobrass' user='postgres' password='12345678'"
        conn = psycopg2.connect(conn_string)
        return conn
    except:
        print("I am unable to connect to the database")


def get_instere_stock(prefix=True):
    res = list()
    conn = connect_pg()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM finance_stock')
    records = cursor.fetchall()
    for row in records:
        if (prefix):
            res.append(stockutil.get_stock_type(row[1]) + row[1])
        else:
            res.append(row[1])
    cursor.close()
    conn.close()
    return res


if __name__ == '__main__':
    """
    conn = connect_pg()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM finance_stock')
    records = cursor.fetchall()
    pprint.pprint(records)
    cursor.close()
    conn.close()
        """
    print(get_instere_stock())
