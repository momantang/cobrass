import os
import sys
import platform

if platform.system() == 'Darwin':
    print('Darwin')
    sys.path.insert(0, '/Users/momantang/PyCharmProjects/cobrass')
from QAWebServer.QA_Web import main
from QAWebServer.fetch_block import get_block, get_name

if __name__ == "__main__":
    print(get_block(['上海国资改革', '阿里巴巴概念']))
    main()
