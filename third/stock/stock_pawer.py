# coding utf-8

from selenium import webdriver
import time
import os
import re

import urllib
import sys
from bs4 import BeautifulSoup

import logging
from datetime import datetime
from datetime import timedelta
from datetime import date

import threading
import json
import xlrd
import xlwt

from xlrd import open_workbook
from xlutils.copy import copy

import nltk

import threading
import time

description_id = 1
browser = webdriver.Chrome()


def start(url, d, today, vstock):
    global description_id
    global browser
    url = url

    try:
        browser.get(url)
        t = browser.page_source

        pn = re.compile(r'(.*)"statuses":(.*?)}]', re.S)
        match = pn.match(t)

        if not match:
            return 0
        result = match.group(2)
        result = result + '}]'
        decode = json.loads(result)

    except:
        pass


if __name__ == '__main__':
    print(browser)
