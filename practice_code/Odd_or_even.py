'''
奇偶數辨別

寫一個程式, 當使用者輸入一個介於一定範圍(例如 1 到 1000 )的數字, 它能夠辨別奇偶, 並輸出檢驗結果給使用者
'''

if __name__ == '__main__':
    while True:
        num = input("請輸入一個介於 1 ~ 1000 之間的整數: ")
        try:
            inum=int(num)
        except ValueError:
            print("輸入的不是整數, 請再試一次!")
            continue

        if inum<1 or inum>1000:
            print("超過範圍, 請再試一次!")
            continue
        if(inum%2==0):
            print(f"{inum}為偶數")
            break
        else:
            print(f"{inum}為奇數")
            break


