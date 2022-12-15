import os
import re

import pandas as pd
import mysql.connector as mysql  # pip install mysql-connector-python
from G import G

# 政府資料開放平台
# 公益彩券開獎號碼及各獎項彩金相關資料
# https://data.gov.tw/dataset/72921

def writeData(fname, gname):
    df = pd.read_csv(fname, index_col=False).dropna(axis=1, how="any")
    if '遊戲名稱' in df.columns:
        df = df.drop(columns='遊戲名稱')
    if '活動名稱' in df.columns:
        df = df.drop(columns='活動名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    colsStrref = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
            colsStrref += f", %s"
        else:
            colsStr += f"{cols[i]}"
            colsStrref += "%s"
    fs = f"insert ignore into {gname} ({colsStr}) values ({colsStrref})"
    cmd = fs
    data = df.values.tolist()
    cursor.executemany(cmd, data)
    conn.commit()


if __name__ == '__main__':
    gamesName = ["今彩539", "大樂透", "大樂透加開獎項", "威力彩", "賓果賓果", "38樂合彩", "39樂合彩", "49樂合彩", "3星彩", "4星彩", "大福彩", "雙贏彩"]
    path = "E:/project/lotterygame"

    conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.dbLottery)
    cursor = conn.cursor()

    for root, subdirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            for i in range(len(gamesName)):
                if re.search(f"{gamesName[i]}_" ,filepath):
                    writeData(filepath, gamesName[i])
                    print(f"{os.path.basename(filepath).split('.')[:-1]}: 已寫入資料庫")
    print("全數寫入完畢")
    cursor.close()
    conn.close()