#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import urllib3
from bs4 import BeautifulSoup
import requests

# 該当ページを開く
r = requests.get('http://www.jpx.co.jp/markets/statistics-equities/misc/01.html')
soup = BeautifulSoup(r.text, 'lxml')

partUrl = soup.select_one('#readArea > div:nth-of-type(4) > div > table > tr > td > a').get('href')

url = 'http://www.jpx.co.jp' + partUrl

request_methods = urllib3.PoolManager()
response = request_methods.request('GET', url)
f = open('data.csv', 'wb')
f.write(response.data)
f.close()
