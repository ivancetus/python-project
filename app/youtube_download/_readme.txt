ref: http://mahaljsp.asuscomm.com/index.php/2020/08/28/youtube_download/
pip install PyQt5 selenium webdriver-manager packaging pytube fake-useragent
ui 參照 stocx_download 所設計
開啟 qtDesigner 做調整
編譯 .ui

執行 pic_to_string

包裝成 pyinstaller
在系統及 安裝上述 pip 套件

取消 debug視窗
Python38\Lib\site-packages\selenium\webdriver\common\service.py
def _start_process, 底下找到 stdin=PIPE, 改動其下的 creationflags=134217728

cd E:\GitHub\python-project\app\youtube_download
pyinstaller --hidden-import=queue -w -F MainWindow.py
