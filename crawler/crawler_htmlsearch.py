import re

from bs4 import BeautifulSoup

with open("testescape.html", 'r', encoding="utf-8") as f:
    soup = BeautifulSoup(f, features="lxml")

# 將搜尋結果以 作品名稱: 網址 的形式存成 dict
# aTags = soup.find_all('a', href=re.compile("^/book"))
# aTags_d = {a['title']: f"https://www.sto.cx/{a['href']}" for a in aTags}
# print(aTags_d)

# page = soup.find(id='webPage')  # 回傳div
# nextPageTag = page.find('a', string=re.compile("^\s*上一頁"))
# if nextPageTag.get('disabled'):
#     print("d")

# 取得搜尋結果下一頁的網址
# page = soup.find(id='webPage')  # 回傳div
# nextPageTag = page.find('a', string=re.compile("^\s*下一頁"))  # 若使用 prettify() 導致 "下一頁" 前面堆積了空格, 得用re才找得到
# nextPageLink = f"https://www.sto.cx/{nextPageTag.get('href')}"

keywords = soup.find('h1').text
title = re.search("(?<=《).*(?=》)", keywords).group(0)
author = re.search("(?<=作者：).*", keywords).group(0)

print(title, author)

if "/" in title:
    print("/ detected")

forbiddenchar = ["/","\\","*","?",":","<",">","|","\""]

teststr1 = "五四三\"-ti2558"
teststr2 = "五四三/-t/i2*558"
teststr3 = "\\ktiq一二三//*>><"

x = re.search("\S*[\\\\/*?:<>|\"]", teststr3)
x2 = re.search(r'/\*?":<>|', teststr1)
print(x)

address = "彰化市中山路一段$#509號"\
    .replace("\\","")\
    .replace("/","")\
    .replace(":","")\
    .replace("*","")\
    .replace("?","")\
    .replace("\"","")\
    .replace("<", "")\
    .replace(">", "")\
    .replace("|", "")