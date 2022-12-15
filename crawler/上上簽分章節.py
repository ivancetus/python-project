import os

path="e:/上上簽/"
targetPath="e:/上上簽/分章節"
filename="上上簽.txt"

if not os.path.exists(targetPath):
    os.mkdir(targetPath)

with open(os.path.join(path,filename), encoding="utf-8") as f:
    originalText = f.read()
    splitText = originalText.split("☆、")
    chapter = 1
    for chapter in range(1,len(splitText)):
        with open(os.path.join(targetPath, f"{chapter}.txt"), 'w', encoding="utf-8") as g:
            g.write(splitText[chapter])
