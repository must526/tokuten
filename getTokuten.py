# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

# ゲーマーズ特典のあるページにアクセス
url = "https://www.gamers.co.jp/tokuten/filter/tokuten_media:146%7Cdate:20180227,20180227/"
request = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request)

#分析
soup = BeautifulSoup(response, "html.parser")

# liのカウンタを増やすと次のアイテムをゲットできる．
# 最大値はどうやって取得すればよいか
#タイトル
print(soup.select_one("#layouts > div.contentsbox > div:nth-of-type(2) > ul > li:nth-of-type(1) > div > p:nth-of-type(1)").text)
#特典種類
print(soup.select_one("#layouts > div.contentsbox > div:nth-of-type(2) > ul > li:nth-of-type(1) > div > span").text)
#発売日
print(soup.select_one("#layouts > div.contentsbox > div:nth-of-type(2) > ul > li:nth-of-type(1) > div > p:nth-of-type(2)").text)
#イラスト
print(soup.select_one("#layouts > div.contentsbox > div:nth-of-type(2) > ul > li:nth-of-type(1) > a > img")['src'])