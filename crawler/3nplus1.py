'''
3n+1猜想

對於每一以正整數n為第一項的數列, 其後一項:
    若為奇數, 則乘以3再加1
    若為偶數, 則除以2
    最終結果會得到1
'''

import pandas as pd

def threenplusone(n):
    if n%2==0:
        n=int(n/2)
    else:
        n=n*3+1
    ls.append(n)
    if n!=1:
        threenplusone(n)
    return

if __name__ == '__main__':
    dis = pd.options.display
    dis.max_rows=None

    while True:
        inp=input("請輸入一個正整數: ")
        try:
            num=int(inp)
        except Exception:
            print("輸入數值錯誤")
            continue
        if num<=0:
            print("輸入數值錯誤")
            continue
        ls=[num]
        threenplusone(num)
        df=pd.DataFrame(ls)
        df.rename(columns={0: 'num'}, inplace=True)
        print(df)
        break

