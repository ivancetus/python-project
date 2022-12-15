# 啟動錯誤訊息顯示 run / edit configurations / execution / emulate terminal in output console / checked
import json
import os.path
import sys
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QCheckBox, QListWidgetItem, QFileDialog
from BrowserThread import BrowserThread
from DownloadThread import DownloadThread
from SearchThread import SearchThread
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # 繪製qtdesigner所設計出來的ui
        self.resize(1920, 1080)  # 設定預設視窗大小
        if os.path.exists("path.json"):
            with open("path.json", 'r') as f:
                self.path = json.load(f)
        else:
            self.path = "c:\\mp3_tmp"  # 設定下載目錄, 一定要用反斜線 \\, Qt的規定
        self.lblPath.setText(self.path)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.disableGui()

        # 由新執行緒處理瀏覽器, 新員工--打電話回來--員工開始工作
        self.browserThread = BrowserThread(self.path)  # 傳入目錄資訊
        self.browserThread.callback.connect(self.browserThreadCallback)
        self.browserThread.start()

        # 當查詢按鈕被按下, 執行btnSearch_clicked 方法
        self.btnSearch.clicked.connect(self.btnSearch_clicked)

        # 當下載按鈕被按下, 執行btnDownload_clicked 方法
        self.btnDownload.clicked.connect(self.btnDownload_clicked)

        # 目錄選擇
        self.btnPath.clicked.connect(self.btnPath_click)

        # 按下Enter就開始查詢
        self.txtSong.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source is self.txtSong):
            if event.text() == '\r':
                self.btnSearch_clicked()
        return super(MainWindow, self).eventFilter(source, event)

    def btnDownload_clicked(self):
        count = self.listWidget.count()
        if count < 1:  # 檢查輸入區域是否有輸入字元
            dialog = QMessageBox()
            dialog.setWindowTitle("YT to MP3")
            dialog.setText("請輸入歌手 / 歌曲")
            dialog.exec()
            return
        boxes = [self.listWidget.itemWidget(self.listWidget.item(i)) for i in range(count)]
        checked = []
        for box in boxes:
            if box.isChecked():
                checked.append(box.text())
        self.disableGui()

        # 由新執行緒處理下載
        self.downloadThread = DownloadThread(self.browser, checked, self.path)
        self.downloadThread.callback.connect(self.downloadThreadCallback)
        self.downloadThread.finished.connect(self.downloadThreadFinished)
        self.downloadThread.start()

    def btnSearch_clicked(self):
        self.listWidget.clear()  # 清除顯示區域, 讓此次查詢結果得以顯示
        self.song = self.txtSong.text()
        if self.song == '':  # 檢查輸入區域是否有輸入字元
            dialog = QMessageBox()
            dialog.setWindowTitle("YT to MP3")
            dialog.setText("請輸入歌手 / 歌曲")
            dialog.exec()
            return
        self.lblStatus.setText("搜尋中...")
        self.disableGui()

        # 新執行緒處理查詢
        self.searchThread = SearchThread(self.browser, self.song)
        self.searchThread.callback.connect(self.searchThreadCallback)
        self.searchThread.start()

    def btnPath_click(self):
        path = QFileDialog.getExistingDirectory()
        if path != '':
            self.path = path.replace("/", "\\")
            with open("path.json", 'w') as f:
                json.dump(self.path, f)
            self.lblPath.setText(self.path)
            self.disableGui()
            self.browser.quit()

            self.browserThread = BrowserThread(self.path)
            self.browserThread.callback.connect(self.browserThreadCallback)
            self.browserThread.start()

    # 若成功啟動瀏覽器執行緒, 則啟用Gui
    def browserThreadCallback(self, browser):
        self.browser = browser
        self.enableGui()

    # 搜尋完畢後啟用Gui
    def searchThreadCallback(self, links):
        self.enableGui()
        self.lblStatus.setText('')
        for key in links.keys():
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            box = QCheckBox(links[key])
            self.listWidget.setItemWidget(item, box)

    def downloadThreadCallback(self, msg):
        self.lblStatus.setText(msg)

    def downloadThreadFinished(self):
        self.lblStatus.setText("下載完成")
        self.enableGui()

    # 禁用Gui
    def disableGui(self):
        self.txtSong.setDisabled(True)
        self.btnSearch.setDisabled(True)
        self.btnDownload.setDisabled(True)
        self.btnPath.setDisabled(True)

    # 啟用Gui
    def enableGui(self):
        self.txtSong.setEnabled(True)
        self.btnSearch.setEnabled(True)
        self.btnDownload.setEnabled(True)
        self.btnPath.setEnabled(True)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "YT to MP3", "確定要關閉嗎?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.browser.quit()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()  # 等待迴圈, 監控滑鼠鍵盤, 更新視窗

