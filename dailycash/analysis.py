import pandas as pd
import numpy as np
import seaborn as sns
import pylab as plt

from collections import Counter

display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

dates = []
ds = []
ns = []
dsns_label = []
sale_prize = []
sale_prize_label = []
prize_level = []
prize_level_label = []
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
'''
[[1, 2, 3, 4, 5], [] ...]
[[d1, d2, d3, d4, d5], [] ...]
'''
for row in range(len(arr)):
    dsns_label.append([1, 2, 3, 4, 5])
    ds.append([arr[row][2], arr[row][3], arr[row][4], arr[row][5], arr[row][6]])
    ns.append([arr[row][7], arr[row][8], arr[row][9], arr[row][10], arr[row][11]])
    sale_prize_label.append(['sales', 'prizes'])
    sale_prize.append([arr[row][12], arr[row][13]])
    prize_level_label.append(['1st', '2nd', '3rd', '4th'])
    prize_level.append([arr[row][14], arr[row][15], arr[row][16], arr[row][17]])


def dsns_to_df(ls):
    dsnsdf = pd.DataFrame.from_records(list(
        dict(Counter(ls)).items()
    ), columns=['number', 'count']
    ).sort_values(by=['count'], ascending=False)
    return dsnsdf


x = list(np.concatenate(dsns_label))
dy = list(np.concatenate(ds))
ny = list(np.concatenate(ns))

df_d = pd.DataFrame({'x': x, 'y': dy})
df_n = pd.DataFrame({'x': x, 'y': ny})
sns.set_style('whitegrid')

# sns.boxplot(x="x", y="y", data=df_d)
# plt.title('not ordered wining number')
# plt.savefig('img/box_not_ordered_wining_number.png')

# sns.boxenplot(x="x", y="y", data=df_d)
# plt.title('not ordered wining number')
# plt.savefig('img/boxen_not_ordered_wining_number.png')

# sns.boxplot(x="x", y="y", data=df_n)
# plt.title('ordered wining number')
# plt.savefig('img/box_ordered_wining_number.png')

# sns.boxenplot(x="x", y="y", data=df_n)
# plt.title('ordered wining number')
# plt.savefig('img/boxen_ordered_wining_number.png')

# plt.xlabel('wining number 1 to 5')
# plt.ylabel('number range')

# df_c = pd.DataFrame({'number': dy})
# sns.countplot(x='number', data=df_c)
# plt.title('total hit count for each number')
# plt.savefig('img/countplot_total_hit_count_for_each_number')
# plt.show()
n1s = []
n2s = []
n3s = []
n4s = []
n5s = []
for i in range(len(arr)):
    n1s.append(arr[i][7])
    n2s.append(arr[i][8])
    n3s.append(arr[i][9])
    n4s.append(arr[i][10])
    n5s.append(arr[i][11])

# df_n1 = pd.DataFrame.from_dict(a, orient='index', columns=['count']).reset_index()
df_n1s = dsns_to_df(n1s)
df_n2s = dsns_to_df(n2s)
df_n3s = dsns_to_df(n3s)
df_n4s = dsns_to_df(n4s)
df_n5s = dsns_to_df(n5s)
df_n1s['percent'] = (df_n1s['count'] / df_n1s['count'].sum()) * 100
df_n2s['percent'] = (df_n2s['count'] / df_n2s['count'].sum()) * 100
df_n3s['percent'] = (df_n3s['count'] / df_n3s['count'].sum()) * 100
df_n4s['percent'] = (df_n4s['count'] / df_n4s['count'].sum()) * 100
df_n5s['percent'] = (df_n5s['count'] / df_n5s['count'].sum()) * 100

print(
    f'df_n1s: \n{df_n1s}\n\n df_n2s: \n{df_n2s}\n\n df_n3s: \n{df_n3s}\n\n df_n4s: \n{df_n4s}\n\n df_n5s: \n{df_n5s}\n'
)
with pd.ExcelWriter('xlsx/all_time_for_each_position.xlsx') as writer:
    df_n1s.to_excel(writer, sheet_name='n1s')
    df_n2s.to_excel(writer, sheet_name='n2s')
    df_n3s.to_excel(writer, sheet_name='n3s')
    df_n4s.to_excel(writer, sheet_name='n4s')
    df_n5s.to_excel(writer, sheet_name='n5s')
