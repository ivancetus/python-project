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


def scrolldown(times):
    i = 0
    driver.maximize_window()
    while i < times:
        i += 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)


targetPage = "https://www.youtube.com/results?search_query=python"
page1 = "https://www.delftstack.com/howto/python/selenium-scroll-down-python/"

ops = Options()  # Chrome選項物件
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
user_agent = UserAgent()
#ops.add_argument('--headless')  # 啟動無頭模式
ops.add_argument('--disable-gpu')  # 不開啟視窗
ops.add_argument('--user-agent=%s' % user_agent.random)  # 加入 headers 資訊躲避反爬蟲偵測
#ops.add_argument('--window-size=1920,1080')  # 避免畫面太小搜尋不到網頁元素
service = Service(ChromeDriverManager(path="E:\ChromeDriver").install())
driver = webdriver.Chrome(service=service, options=ops)
driver.get(targetPage)
driver.maximize_window()
WebDriverWait(driver, 20, 5).until(EC.presence_of_element_located((By.ID, "video-title")))
#WebDriverWait(driver, 20, 5).until(EC.presence_of_element_located((By.TAG_NAME, "div")))

#driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
# time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# print("轉了")

x = 5
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")

i=0
while i<x:
    i+=1
    # Scroll down to bottom
    driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

