import random


def QA_util_random_with_zh_stock_code(stockNumber=10):
    """
    随机生成股票代码
    :param stockNumber: 生成个数
    :return:  ['60XXXX', '00XXXX', '300XXX']
    """
    codeList = []
    pt = 0
    for i in range(stockNumber):
        if pt == 0:
            iCode = random.randint(600000, 609999)
            aCode = "%06d" % iCode
        elif pt == 1:
            iCode = random.randint(600000, 600999)
            aCode = "%06d" % iCode
        elif pt == 2:
            iCode = random.randint(2000, 9999)
            aCode = "%06d" % iCode
        elif pt == 3:
            iCode = random.randint(300000, 300999)
            aCode = "%06d" % iCode
        elif pt == 4:
            iCode = random.randint(2000, 2999)
            aCode = "%06d" % iCode
        pt = (pt + 1) % 5
        codeList.append(aCode)
    return codeList


def QA_util_random_with_topic(topic='Acc', lens=8):
    """
        生成account随机值

        Acc+4数字id+4位大小写随机

    """
    _list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    num = random.sample(_list, lens)
    return '{}_{}'.format(topic, ''.join(num))


if __name__ == '__main__':
    print(QA_util_random_with_zh_stock_code(10))
    print(QA_util_random_with_topic(input()))
