import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import re
from fake_useragent import UserAgent  # if Python <3.8 , pip3 install importlib-metadata
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def incrementfilename(f):
    fnew = f
    root, ext = os.path.splitext(f)
    i = 1
    while os.path.exists(fnew):
        i += 1
        fnew = '%s_%i%s' % (root, i, ext)
    return fnew


def download(url):
    driver.get(url)
    # 若需要讀取渲染後的資料, 加入以下等待時間
    # try:
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, '')))
    # except:
    #     print("連線錯誤")
    #     driver.close()
    #     exit()
    s = BeautifulSoup(driver.page_source, "lxml")
    keywords = s.find('h1').text
    try:
        getTitle = re.search("(?<=《).*(?=》)", keywords).group(0)
        getAuthor = re.search("(?<=作者：).*", keywords).group(0)
    except:
        print(f"{keywords} 異常")
        print(s.text)
        driver.close()
        exit()

    # 處理特殊字元
    title = getTitle.replace("\\", "").replace("/", "_").replace(":", "_").replace("*", "")\
        .replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
    author = getAuthor.replace("\\", "").replace("/", "_").replace(":", "_").replace("*", "") \
        .replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")

    # 取得其他頁面的網址, 存成dict, 其中key為頁數號碼, value為網址
    options = s.find_all('option')
    pages = {}
    for option in options:
        pages[option.text] = f"https://www.sto.cx/{option['value']}"

    # 爬蟲/依每個頁面讀寫入成單一個檔案檔案
    # 若檔名相同, 自動加入 _數字
    filename = incrementfilename(os.path.join(path, f"{title}_by_{author}.txt"))
    for key in pages.keys():
        try:
            # filename = os.path.join(filepath, f'{key}.txt')
            driver.get(pages[key])
            sp = BeautifulSoup(driver.page_source, "lxml")
            ct = sp.find(id='BookContent')
            wordlist = ct.get_text("\n",strip=True).splitlines(keepends=True)
            singlestr = '\n'.join(wordlist)
            print(f"目前正在處理{pages[key]}...")
            with open(filename, 'a', encoding="utf-8") as f:
                f.write(singlestr)
        except Exception as e:
            print(f'{pages[key]}<=================error: {e}')
        time.sleep(random.randint(5, 8)+random.random())  # 每次讀取間隔 ? 秒, 減少被偵測到是bot的機會

    print(f"{url}: 處理完畢")


startp = time.perf_counter()

# 輸入網址, 指定存檔磁碟機 / 資料夾, 選擇搜尋方式
targetPage = "https://www.sto.cx/pcindex.aspx"
searchAuthor = "一枚銅錢"
# searchNovel = ""
path = os.path.join("e:/novel", searchAuthor)
if not os.path.exists(path):
    os.mkdir(path)

# webdriver 啟動
ops = Options()  # Chrome選項物件
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
user_agent = UserAgent()
ops.add_argument('--headless')  # 啟動無頭模式
ops.add_argument('--disable-gpu')  # 不開啟視窗
ops.add_argument('--user-agent=%s' % user_agent.random)  # 加入 headers 資訊躲避反爬蟲偵測
ops.add_argument('--window-size=1920,1080')  # 避免畫面太小搜尋不到網頁元素
service = Service(ChromeDriverManager(path="E:\ChromeDriver").install())
driver = webdriver.Chrome(service=service, options=ops)
driver.get(targetPage)

try:
    # (By.TAG_NAME, 'td') 是 tuple 形式
    # 預設每500ms檢查一次, 若超過20秒都沒結果, 就跑except
    # WebDriverWait(browser, 20(等待秒數), 0.1(每0.1秒=100ms檢查一次)
    # 沒有WebDriverWait的話, 直接抓取瀏覽器的輸入層 資料, 若有等待 則抓取渲染層 的資料
    # 什麼時候需要Wait: 使用 JavaScript或ajax產生的資料, 就需要wait
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME,'div')))
except:
    print("連線錯誤")
    driver.close()
    exit()


inputText = driver.find_element(by="id", value="key")
inputText.send_keys(searchAuthor)
# inputText.send_keys(searchNovel)

# 若此行執行失敗, 存下截圖查找問題, 可能是視窗太小, 找不到元素, driver.save_screenshot('page.png')
driver.find_element(by="id",value="sa").click()
# driver.find_element(by="id",value="sn").click()

# 儲存排版後的結果於專案目錄, 於另一個py檔測試語法, 查找需要的元素. 因為每次測試都要爬一次網頁, 減少對網站造成的負擔
# soup = BeautifulSoup(driver.page_source,"lxml")
# with open("test.html", 'w', encoding="utf-8") as f:
#     f.write(soup.prettify())
# driver.close()

aTags_d = {}
while True:
    # 抓取搜尋結果
    soup = BeautifulSoup(driver.page_source,"lxml")

    # 將搜尋結果以 網址: 作品名稱 的形式存成 dict, 同時去除網址重複的情況(若有的話)
    aTags = soup.find_all('a', href=re.compile("^/book"))
    aTags_d.update({f"https://www.sto.cx/{a['href']}": a['title'] for a in aTags})

    # 取得搜尋結果下一頁的網址
    webPage = soup.find(id='webPage')  # 回傳div
    nextPageTag = webPage.find('a', string=re.compile("^\s*下一頁"))  # 若使用 prettify() 導致 "下一頁" 前面堆積了空格, 得用re才找得到
    if nextPageTag.get('disabled'):
        break
    nextPageLink = f"https://www.sto.cx/{nextPageTag.get('href')}"
    try:
        driver.get(nextPageLink)
    except:
        print(soup.text)
        print("=========ERROR=========")
        break

# 檢查是否有抓到目標資訊 網址: 標題
# print(aTags_d)
# driver.close()

for k in aTags_d.keys():
    start = time.perf_counter()
    download(k)
    end = time.perf_counter()
    print(f"{k} 處理時間: {end - start}秒")

endp = time.perf_counter()

print(f"全數處理完畢, 共新增 {len(aTags_d)} 本, 耗費時間: {endp - startp}秒")
driver.close()

