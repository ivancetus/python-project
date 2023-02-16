import os
import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from sdk.IvanCv import IvanCv as cv


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
            # 方法1: pyqt直接讀取成 QPixmap
            # picture = QPixmap(files[idx])
            # picture.scaled(400, 300)
            # picture.tag = files[idx]
            # self.callback.emit(picture)
            # idx += 1
            # QThread.msleep(5)  # 停頓一下, 讓 UI可以顯示

            # 方法2: opencv 讀取, 再轉 QPixmap
            img = cv2.imdecode(np.fromfile(files[idx], dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            img = img[:, :, ::-1].copy()
            img = cv.resize(img, 400, 300)
            pix = QPixmap(QImage(
                img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
            )
            pix.tag = files[idx]
            self.callback.emit(pix)
            idx += 1
            QThread.msleep(5)  # 停頓一下, 讓 UI可以顯示