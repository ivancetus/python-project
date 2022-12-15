* pip install selenium, webdriver-manager, packaging, lxml, BeautifulSoup4, pyqt5, fake-useragent, ## pillow, wxPython
* pip3 install importlib-metadata (pre Python 3.8 )
* 啟動錯誤訊息顯示 run / edit configurations / execution / emulate terminal in output console / checked
* chromedriver.exe預設位置 C:\Users\登入名稱\.wdm\drivers\chromedriver\win32\107.x.xxxx.xx\chromedriver.exe
* favicon: https://www.sto.cx/favicon.ico
* AppId https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
* https://stackoverflow.com/questions/56002701/selenium-webdriver-error-invalid-session-id --disable-dev-shm-usage
* macOS pip python3: terminal -> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py -> python3 get-pip.py
* macOS pip3 install pyinstaller, pip3 install --upgrade pyinstaller pyinstaller-hooks-contrib

1. debug 需借助 log
2. 系統級: pip install pyinstaller
    虛擬環境: 專案底下的 venv
    系統級: Python 的安裝路徑 D:\Python\Python37
    命令提示字元 pip install pyinstaller
3. 虛擬環境有安裝的套件, 系統級也必須重新安裝一次
    若漏掉一個沒安裝, 就會造成閃退
4. pip3 install pyqt5, selenium, webdriver-manager, packaging, lxml, BeautifulSoup4, fake-useragent

5. 命令提示字元 進入專案目錄
6. 包裝成執行檔
    pyinstaller --hidden-import=queue -F mp3.py
    包裝完成後, 會在專案底下產生 .spec檔, build 與 dist 目錄, build內為暫存檔, dist內為執行檔
    後面視窗是debug用, 若出錯會出現在後面的視窗內
7. 取消命令視窗: 加上 -w
    一般使用者: end user 沒有任何程式基礎的人
    Power user: 玩家級的人, 達人
    開發者: 撰寫程式的人
    pyinstaller --hidden-import=queue -w -F mp3.py
8. 修正使用 selenium 還是會出現命令視窗的問題
    a.開啟 D:\Python\Python37\Lib\site-packages\selenium\webdriver\common
        系統級Python目錄下
        service.py 開啟編輯
    b. def _start_process, 底下找到 stdin=PIPE, 改動其下的 creationflags=134217728
9. 最好將 exe檔複製到一台沒有安裝python 的電腦做測試執行
    若有問題, 請重新包裝沒有 -w 的執行檔, 查看log
10. 打包 icon 到 windows 圖示
    pyinstaller --hidden-import=queue -w -F --icon=img_handling/favicon.ico stocx.py
    若新建立好的程式icon沒有更新, 進到 %localappdata% 刪除 IconCache.db 重新開機
    有沒有更好的解決辦法呢?
    https://stackoverflow.com/questions/24363719/pyinstaller-cant-change-the-shortcut-icon
    