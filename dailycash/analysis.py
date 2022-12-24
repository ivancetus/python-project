import pandas as pd
import numpy as np

display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

dates = []
ds = []
ns = []
sale_prize = []
prize_level = []
df = pd.read_excel('dailycash_data.xlsx')
# print(df)
arr = df.to_numpy()
'''
information about this arr
arr[0]:
[Timestamp('2014-01-01 00:00:00') 103000001 26 13 5 34 24 5 13 24 26 34 47817100 20518500 1 264 8477 93908]
len(arr): 2811
len(arr[0]): 18
'''
