# pip install BeautifulSoup / selenium / lxml
# pip3 install importlib-metadata if Python < 3.8
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import re
from webdriver_manager.chrome import ChromeDriverManager


def incrementfilename(f):
    fnew = f
    root, ext = os.path.splitext(f)
    i = 1
    while os.path.exists(fnew):
        i += 1
        fnew = '%s_%i%s' % (root, i, ext)
    return fnew


# 輸入網址, 指定存檔磁碟機 / 資料夾 #
# url = "https://www.sto.cx/book-211398-1.html"
# url = "https://www.sto.cx/book-157475-1.html"
targetPage = "https://www.sto.cx/book-149621-1.html"
path = "e:/novel"

# webdriver 啟動
ops = Options()  # Chrome選項物件
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
user_agent = UserAgent()
ops.add_argument('--headless')  # 啟動無頭模式
ops.add_argument('--disable-gpu')  # 不開啟視窗
ops.add_argument('--user-agent=%s' % user_agent.random)  # 加入 headers 資訊躲避反爬蟲偵測
# ops.add_argument('--window-size=1920,1080')  # 避免畫面太小搜尋不到網頁元素
driver = webdriver.Chrome(ChromeDriverManager(path="E:\ChromeDriver").install(), options=ops)
driver.get(targetPage)

# 取得輸入頁面的資料以利爬蟲 #
soup = BeautifulSoup(driver.page_source,"lxml")
keywords = soup.find('h1').text
try:
    getTitle = re.search("(?<=《).*(?=》)", keywords).group(0)
    getAuthor = re.search("(?<=作者：).*", keywords).group(0)
except:
    print(f"{keywords} 異常")
    print(soup.text)
    driver.close()
    exit()

# 處理特殊字元
title = getTitle.replace("\\", "").replace("/", "_").replace(":", "_").replace("*", "")\
    .replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
author = getAuthor.replace("\\", "").replace("/", "_").replace(":", "_").replace("*", "") \
    .replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")

# 取得其他頁面的網址, 存成dict, 其中key為頁數號碼, value為網址 #
options = soup.find_all('option')
d = {}
for option in options:
    d[option.text] = f"https://www.sto.cx/{option['value']}"

# # 以標題建立存檔目錄, 或不建立 #
# path = os.path.join(path, f"{title}_by_{author}")
# if not os.path.exists(path):
#     os.mkdir(path)

# 爬蟲/依每個頁面讀寫入成單一個檔案檔案  #
filename = incrementfilename(os.path.join(path, f"{title}_by_{author}.txt"))
for key in d.keys():
    try:
        # filename = os.path.join(filepath, f'{key}.txt')
        driver.get(d[key])
        sp = BeautifulSoup(driver.page_source,"lxml")
        ct = sp.find(id='BookContent')
        wordList = ct.get_text("\n",strip=True).splitlines(keepends=True)
        singleStr = '\n'.join(wordList)
        print(f"目前正在處理{d[key]}...")
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(singleStr)

    except Exception as e:
        print(f'{d[key]}<=================error: {e}')
        driver.close()
        exit()

print("全數處理完畢")
driver.close()