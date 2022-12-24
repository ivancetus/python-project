import datetime
import random
import time
import mysql.connector as mysql

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from Gfile.G import G


def get_date(year, month):
    roc_year = year - 1911  # 西元年轉民國年
    # 操作網頁元素
    radio = browser.find_element(By.ID, "D539Control_history1_radYM")
    radio.click()
    Select(browser.find_element(By.ID, 'D539Control_history1_dropYear')).select_by_value(str(roc_year))
    Select(browser.find_element(By.ID, 'D539Control_history1_dropMonth')).select_by_value(str(month))
    browser.find_element(By.ID, 'D539Control_history1_btnSubmit').click()
    rows = []
    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'td')))
        soup = BeautifulSoup(browser.page_source, 'lxml')
        tables = soup.find_all('table', class_='td_hm')
        for table in tables:
            tds = table.find_all('td', class_='td_w')
            # tds[0] 期數, tds[1].text 開獎 xxx/xx/xx, ymd = [y, m, d]
            ymd = tds[1].text.replace('開獎', '').replace('\n', '').split('/')
            row = [f'{int(ymd[0]) + 1911}-{ymd[1]}-{ymd[2]}', tds[0].text.replace(' ', '')]
            # 3~7 d1~d5, 10~14 n1~n5, 15~16 sales prizes, 18~21 1st~4th
            idx = [3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21]
            for i in idx[:10]:
                row.append(tds[i].text)
            for i in idx[10:18]:
                row.append(int(tds[i].text.strip().replace(',', '')))
            rows.append(row)
        rows.reverse()
        time.sleep(random.randint(5, 8) + random.random())
    except Exception as e:
        print("連線有問題", e)
    return rows


def write_data(year, month, cmd):
    rows = get_date(year, month)
    print(f'Getting dailycash {year}/{month:02d}...')
    if (len(rows)) > 0:
        # cur.execute(f"DELETE FROM dailycash WHERE date LIKE '{year}-{month:02d}%'")
        # conn.commit()
        cur.executemany(cmd, rows)
        conn.commit()


if __name__ == '__main__':
    fetch_all = False
    fetch_current = True
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    ser = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=ser, options=opt)
    browser.get("https://www.taiwanlottery.com.tw/lotto/dailycash/history.aspx")
    conn = mysql.connect(host=G.host_loc, user=G.user_loc, password=G.password_loc, database=G.database_loc)
    cur = conn.cursor()
    cmd = "INSERT IGNORE INTO dailycash " \
          "(date, draw, d1, d2, d3, d4, d5, n1, n2, n3, n4, n5, sales, prizes, 1st, 2nd, 3rd, 4th) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s')"
    # fetch all data up to the most recent draw or fetch current (setup to run every day)
    current = datetime.datetime.now()
    cur_y = current.year
    cur_m = current.month
    if fetch_all:
        sta_y = 103+1911
        years = [y for y in range(sta_y, cur_y+1)]
        for year in years:
            if year == cur_y:
                months = [m for m in range(1, cur_m+1)]
            else:
                months = [m for m in range(1, 13)]
            for month in months:
                write_data(year, month, cmd)
    if fetch_current:
        write_data(cur_y, cur_m, cmd)
    cur.close()
    conn.close()
    browser.quit()
