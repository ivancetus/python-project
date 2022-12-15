import string

def wordCount():
    lines=f.read().rstrip()
    lines=lines.translate(lines.maketrans('','',string.punctuation)).lower()
    words=lines.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

if __name__ == '__main__':
    counts = dict()
    fname = input("請輸入要開啟的文字檔案名稱(放置於text內): ")
    try:
        with open("text/" +fname) as f:
            wordCount()
            print(counts)
    except:
        print(fname," 無法開啟")
        quit()

    mx=max(counts.values())
    muw=[]
    for k,v in counts.items():
        if v==mx:
            muw.append(k)

    print(f"The word: '{', '.join(muw)}' is/are the most used word(s), for a total of {mx} times")

