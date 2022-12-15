import time
from PyQt5.QtCore import QThread, pyqtSignal
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchThread(QThread):
    callback = pyqtSignal(object)

    def __init__(self, browser, song):
        super().__init__(None)
        self.browser = browser
        self.song = song

    def scrolldown(self, times):
        SCROLL_PAUSE_TIME = 3

        # Get scroll height
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        i=0
        while i < times:
            i += 1
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def run(self):
        self.browser.get(f'https://www.youtube.com/results?search_query={self.song}')
        self.scrolldown(3)
        links = {}
        try:
            WebDriverWait(self.browser, 20, 5).until(EC.presence_of_element_located((By.ID, "video-title")))
            tags = self.browser.find_elements(By.TAG_NAME, 'a')
            for tag in tags:
                href = tag.get_attribute('href')
                if 'watch' in str(href):
                    title = tag.get_attribute('title')
                    if title == '':
                        try:
                            title = tag.find_element(By.ID, 'video-title').get_attribute('title')
                        except:
                            pass
                    if title != '':
                        links[href] = f'{title} url={href}'
        except:
            pass
        #print(links)
        self.callback.emit(links)