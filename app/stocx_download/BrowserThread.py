from PyQt5.QtCore import QThread, pyqtSignal
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserThread(QThread):
    callback = pyqtSignal(object)

    def __init__(self, path):
        super().__init__(None)
        self.browser = None
        self.path = path

    def run(self):
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--window-size=1280,720')
        # random header info
        user_agent = UserAgent()
        opt.add_argument('--user-agent=%s' % user_agent.random)
        opt.add_experimental_option("excludeSwitches", ["enable-logging"])
        opt.add_argument('--disable-dev-shm-usage')

        ser = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=ser, options=opt)
        self.callback.emit(browser)
