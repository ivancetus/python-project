# pip install selenium, BeautifulSoup4, lxml, webdriver-manager
# chromedriver.exe預設位置 C:\Users\登入名稱\.wdm\drivers\chromedriver\win32\107.x.xxxx.xx\chromedriver.exe

from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserThread(QThread):
    callback = pyqtSignal(object)  # 由callback連上主執行緒

    def __init__(self, path):
        super().__init__(None)
        self.browser = None
        self.path = path

    # 要執行的任務都要放在 run方法之中
    def run(self):
        opt = Options()
        opt.add_argument("--headless")
        opt.add_argument("--disable-gpu")
        #opt.add_experimental_option("detach", True)  # 註解掉, 好讓背景的chromedriver.exe自己關掉
        opt.add_experimental_option("excludeSwitches", ["enable-logging"])  # 允許chrome可以下載

        # 更改預設下載目錄
        prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": self.path}
        opt.add_experimental_option("prefs", prefs)

        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=opt)
        self.callback.emit(browser)  # 發射回主執行緒