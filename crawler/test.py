from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
import re
#
# h = "《上上签》作者：一枚铜钱"
# title=re.search("(?<=《).*(?=》)",h).group(0)
# author=re.search("(?<=作者：).*",h).group(0)

# url = "https://www.sto.cx/book-211398-1.html"
# path = "e:/"
#
# # webdriver 啟動, 進到輸入頁面 #
# driver = webdriver.Chrome("E:/ChromeDriver/chromedriver.exe")
# driver.get(url)
#
# # 取得輸入頁面的資料以利爬蟲 #
# soup = BeautifulSoup(driver.page_source,"lxml")
# keywords = soup.find('h1')
# k = []
# # for kws in keywords:
# #     if kws is not None:
# #         k.append(kws)
# # title = re.search("(?<=《).*(?=》)", k).group(0)
# # author = re.search("(?<=作者：).*", k).group(0)
# print(keywords)

# path = "e:/novel"
# name = "青龍圖騰_by_淮上.txt"
#
# filename = os.path.join(path, name)
#
# def incrementfilename(f):
#     fnew = f
#     root, ext = os.path.splitext(f)
#     i = 1
#     while os.path.exists(fnew):
#         i += 1
#         fnew = '%s_%i%s' % (root, i, ext)
#     return fnew
#
#
# # print(nextnonexistent(filename))

targetPage = "https://www.sto.cx/book-211398-1.html"
ops = Options()  # Chrome選項物件
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
user_agent = UserAgent()
#ops.add_argument('--headless')  # 啟動無頭模式
ops.add_argument('--disable-gpu')  # 不開啟視窗
ops.add_argument('--user-agent=%s' % user_agent.random)  # 加入 headers 資訊躲避反爬蟲偵測
#ops.add_argument('--window-size=1920,1080')  # 避免畫面太小搜尋不到網頁元素
driver = webdriver.Chrome(executable_path="E:/ChromeDriver/chromedriver.exe", options=ops)
driver.get(targetPage)

import favicon

soup = BeautifulSoup(driver.page_source,"lxml")


driver.close()


# with open("testbr.html", 'r', encoding="utf-8") as f:
#     soup = BeautifulSoup(f, features="lxml")
#
# a = soup.find(id="BookContent")
# b = a.get_text("\n", strip=True).splitlines(keepends=True)
# #print(b)
#
# with open("testbr.txt", 'w', encoding="utf-8") as fa:
#     fa.write("\n".join(b))


