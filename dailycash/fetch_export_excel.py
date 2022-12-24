import mysql.connector as mysql
import pandas as pd
from Gfile.G import G

conn = mysql.connect(
    host=G.host_loc, user=G.user_loc, password=G.password_loc, database=G.database_loc
)
cur = conn.cursor()
cmd = 'SELECT * FROM dailycash ORDER BY date'
cur.execute(cmd)
rows = cur.fetchall()
cols = [c[0] for c in cur.description]
df = pd.DataFrame(data=rows, columns=cols).drop(columns='id')
print(df)
cur.close()
conn.close()
df.to_excel('dailycash_data.xlsx', index=False)
