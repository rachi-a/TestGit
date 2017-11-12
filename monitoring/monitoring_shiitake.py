# coding: utf-8
# 用意するファイル
# 1.monitoring_shiitake.txt
# 2.line_token.csv ← 直接書く場合は不要。

from bs4 import BeautifulSoup
import requests
import csv

# 今まで読み込んだデータを取得 txt形式
with open('monitoring_shiitake.txt', 'r') as f:
    time_data = f.read()

# 現在のtimeタグの情報を取得
r = requests.get('https://ameblo.jp/shiitake-uranai-desuyo/')
soup = BeautifulSoup(r.text, 'lxml') # 定型文と思ってOK
time_tag = soup.select_one('time').get_text()
if 'NEW!' in time_tag:
    time_tag = time_tag.replace('NEW!', '')
title = soup.select_one('#recentEntries > div > div.skin-widgetBody > ul > li:nth-of-type(1) > a').get_text()

# 更新がある場合はLINE送信・データ更新
if time_data != time_tag:
    alert = '\nしいたけブログ更新みたい。\n' + '「' + title + '」\nhttps://ameblo.jp/shiitake-uranai-desuyo/'

    # 以下、LINE送信の定型文 line_notify_token から line_notify まで。
    tokens = []
    with open('line_token.csv', 'r') as f:
        csv_data = csv.reader(f)
        header = next(csv_data) # ヘッダーを読み飛ばす。
        for token in csv_data:
            tokens.extend(token)

    for token in tokens:
        # line_notify_tokenに直接アクセストークン情報を入れる方がシンプル。その場合は tokens = [] から for token in tokens を削除。
        line_notify_token = token
        line_notify_api = 'https://notify-api.line.me/api/notify'

        payload = {'message': alert}
        headers = {'Authorization': 'Bearer ' + line_notify_token}  # トークン
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)

    # 読み込んだデータを更新。
    with open('monitoring_shiitake.txt', 'w') as f:
        f.write(time_tag)
