#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import urllib3
from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

# options = Options()
#
# # ChromeのWebDriverオブジェクトを作成
# # options = webdriver.ChromeOptions()
#
# # prefs = {'download.default_directory' : './'}
# # options.add_experimental_option('prefs',prefs)
# # options.add_argument('--ignore-certificate-errors') # SSLエラー対策
#
# # オプションにヘッドレスを追加。ここをコメントアウトすればヘッドレスじゃなくなる。
# options.add_argument('--headless')
#
# # print(options)
# # Chrome driverのパス
# cd = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(executable_path = cd, chrome_options = options)

# 該当ページを開く
r = requests.get('http://www.jpx.co.jp/markets/statistics-equities/misc/01.html')
soup = BeautifulSoup(r.text, 'lxml')

partUrl = soup.select_one('#readArea > div:nth-of-type(4) > div > table > tr > td > a').get('href')

# print(partUrl)

url = 'http://www.jpx.co.jp' + partUrl

# print(url)

# # # <title>で、ページが正しいことを確認する。
# # assert 'その他統計資料 | 日本取引所グループ' in driver.title
#
# element = driver.find_element_by_xpath('//*[@id="readArea"]/div[4]/div/table/tbody/tr/td/a')
#
# url = element.get_attribute('href')
# driver.close()
#
request_methods = urllib3.PoolManager()
response = request_methods.request('GET', url)
f = open('data.csv', 'wb')
f.write(response.data)
f.close()
