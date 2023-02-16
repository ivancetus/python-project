import os

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap


class PictureThread(QThread):
    callback = pyqtSignal(object)

    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.path = path
        self.runFlag = True

    def run(self):
        ls = os.listdir(self.path)
        files = []
        for l in ls:
            l_low = l.lower()
            if l_low.endswith('.jpg') or l_low.endswith('.png'):
                files.append(os.path.join(self.path, l_low).replace('\\', '/'))
        idx = 0
        while idx < len(files) and self.runFlag:
            picture = QPixmap(files[idx])
            picture.scaled(400, 300)
            picture.tag = files[idx]
            self.callback.emit(picture)
            idx += 1
            QThread.msleep(5)  # 停頓一下, 讓 UI可以顯示
