'''
政府資料開放平台
公益彩券開獎號碼及各獎項彩金相關資料
https://data.gov.tw/dataset/72921

1. 建置資料庫 lottery
2. 建置資料表 今彩537
3. 欄位名稱
    期別, 開獎日期, 銷售總額, 總獎金, 獎號1, 獎號2, 獎號3, 獎號4, 獎號5

'''
import os
import pandas as pd
import mysql.connector as mysql  # pip install mysql-connector-python
from G import G

dis = pd.options.display
dis.max_columns = None
dis.max_rows = None
dis.width = None
dis.max_colwidth = None

path = "E:/project/lotterygame/103"
filename = "今彩539_2014.csv"
gamesname = "今彩539"
fname = os.path.join(path, filename)

# conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.database)
# cursor = conn.cursor()

df = pd.read_csv(fname, index_col=False).dropna(axis=1, how="any").drop(columns='遊戲名稱')
cols = [col for col in df.columns]

# 取得欄位名稱
colsStr = ""
colsStrref = ""
for i in range(len(cols)):
    if i != 0:
        colsStr += f", {cols[i]}"
        colsStrref += f", %s"
    else:
        colsStr += f"{cols[i]}"
        colsStrref += "%s"
# insert ignore into ... 忽視多種寫入時產生的錯誤, 若因 UQ 特性重複而無法寫入, 則該行不寫入, 且不產生error
fs = f"insert ignore into {gamesname} ({colsStr}) values ({colsStrref})"
cmd = fs

print(cmd)
# 取得資料
data = df.values.tolist()
print(data)
# for r in df.values:
#     data.append([r[0],str(r[1]),r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]])

# cursor.executemany(cmd, data)  # 只開一次連線, 然後將所有資料一次性寫入
#
# conn.commit()
# cursor.close()
# conn.close()

