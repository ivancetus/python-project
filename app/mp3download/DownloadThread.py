import os
from PyQt5.QtCore import QThread, pyqtSignal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadThread(QThread):
    callback = pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, browser, checked, path):
        super().__init__(None)
        self.browser = browser
        self.checked = checked
        self.path = path

    def run(self):
        files = os.listdir(self.path)
        # 清理下載暫存檔if exist
        for file in files:
            if '.crdownload' in file:
                path = os.path.join(self.path, file)
                os.remove(path)
        for i, chk in enumerate(self.checked):
            title = chk.split(' url=')[0]
            url = chk.split(' url=')[1].replace('youtube', 'backupmp3')
            self.callback.emit(f'正在下載 {title} ...')
            self.browser.get(url)

            # 出現選擇MP3, MP4小視窗時的處理方式
            self.browser.switch_to.frame('IframeChooseDefault')
            try:
                WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'MP3Format')))
                btn = self.browser.find_element(By.ID, 'MP3Format')
                btn.click()
                self.sleep(3)
            except:
                pass

            # 200秒內, 每秒檢查是否下載成功
            try:
                WebDriverWait(self.browser, 200, 1).until(self.download_finished)
            except:
                print(f'{title}無法下載')
        self.finished.emit()

    def download_finished(self, browser):  # until 規定要有參數, 但在此用不到
        files = os.listdir(self.path)
        finished = True
        for file in files:
            if ".crdownload" in file:
                finished = False
        return finished


