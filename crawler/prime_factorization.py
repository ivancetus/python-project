'''
質因數分解
輸入一正整數(界定範圍), 進行質因數分解
輸入: 45
輸出: 3*3*5 或 為質數
'''

def primefac(value):
    for i in range(2,value+1):
        if value % i == 0:
            value = int(value / i)
            factors.append(i)
            break
    if value == 1:
        return
    else:
        primefac(value)


if __name__ == '__main__':
    while True:
        rmin=2
        rmax=2**32
        inp=input(f"請輸入一個介於{rmin} ~ {rmax:,}的正整數: ")
        try:
            num=int(inp)
        except TypeError:
            print("輸入數值錯誤! 請檢查")
            continue
        except ValueError:
            print("輸入數值錯誤! 請檢查")
            continue
        if num < rmin or num > rmax:
            print("請輸入範圍內的數字!")
            continue

        factors=list()
        primefac(num)
        sf=""
        if factors[0] != num:
            for factor in factors:
                sf+=str(factor)+"*"
            sf=sf.rstrip("*")
            print(f"{num} = " + sf)
        else:
            print(f"{num} 為質數")
        break
