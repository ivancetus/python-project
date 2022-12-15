import os
import re
import pandas as pd
import mysql.connector as mysql
from G import G

path = "E:/project/lotterygame"

def DailyCash(fpath):
    # 讀取csv檔案
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')

    # 取得欄位資訊
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"

    # 取得資料
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]])

    # SQL語法, insert ignore into ... 忽視多種寫入時產生的錯誤, 若因 UQ 特性重複而無法寫入, 則該行不寫入, 且不產生error
    fs = f"insert ignore into 今彩539 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # 寫入資料庫
    cursor.executemany(cmd, data)
    conn.commit()


def Lotto649(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def LottoEvent(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def SuperLotto638(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def _3D(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def _4D(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def _38M6(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def _39M6(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def _49M6(fpath):
    df = pd.read_csv(fpath, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
    cols = [col for col in df.columns]
    colsStr = ""
    for i in range(len(cols)):
        if i != 0:
            colsStr += f", {cols[i]}"
        else:
            colsStr += f"{cols[i]}"
    data = []
    for r in df.values:
        data.append([r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]])
    fs = f"insert ignore into 大樂透 ({colsStr})"
    cmd = fs + " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(cmd, data)
    conn.commit()


def writedata(fname, gname):
    df = pd.read_csv(fname, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
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
    print(f"{os.path.basename(fname).split('.')[:-1]}: 已寫入資料庫")


# 建立連線
conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.database)
cursor = conn.cursor()

gamesName = ["今彩539", "大樂透", "大樂透加開獎項", "威力彩", "賓果賓果", "38樂合彩", "39樂合彩", "49樂合彩", "3星彩", "4星彩", "大幅彩", "雙贏彩"]


for root, subdirs, files in os.walk(path):
    for f in files:
        filepath = os.path.join(root, f)
        # 以def 讀取每項遊戲
        if "今彩539" in filepath:
            DailyCash(filepath)
        if "大樂透" in filepath:
            Lotto649(filepath)
        if "大樂透加開獎項" in filepath:
            LottoEvent(filepath)
        if "威力彩" in filepath:
            SuperLotto638(filepath)
        if "賓果賓果" in filepath:
            pass
        if "38樂合彩" in filepath:
            _38M6(filepath)
        if "39樂合彩" in filepath:
            _39M6(filepath)
        if "49樂合彩" in filepath:
            _49M6(filepath)
        if "3星彩" in filepath:
            _3D(filepath)
        if "4星彩" in filepath:
            _4D(filepath)
        if "雙贏彩" in filepath:
            pass


        # 大幅彩 104起
        # 雙贏彩 107起
        # 大幅彩 109消亡
print("全數寫入完畢")
cursor.close()
conn.close()

'''
取得路徑中的檔案名稱, 去除副檔名
filename = os.path.basename(filepath).split(".")[:-1]
for file in filename:
    if re.match("^今彩539", file):
    print(file)
'''