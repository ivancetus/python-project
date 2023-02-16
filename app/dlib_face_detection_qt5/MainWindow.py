import json
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QListWidgetItem

from LoadModelThread import LoadModelThread
from PictureThread import PictureThread
from ui.ui_mainwindow import Ui_MainWindow
from sdk.IvanCv import IvanCv as cv


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(1920, 1080)

        path = 'E:\project\data\img\\face_detect\\test'
        self.path = path.replace('\\', '/')
        if os.path.exists("path.json"):
            with open("path.json", 'r') as f:
                self.path = json.load(f)
        self.btnPath.clicked.connect(self.btnPathClick)
        self.lblPath.setText(self.path)
        self.loadModelThread = LoadModelThread()
        self.loadModelThread.callback.connect(self.loadModelThreadCallback)
        self.loadModelThread.start()

    def get_descriptor(self, img):
        # if not gpu, remove [0].rect
        try:
            return np.asarray(
                self.detector_recognition.compute_face_descriptor(
                    img, self.detector_shape(img, self.detector_face_gpu(img, 0)[0].rect))
            )
        except:
            return None

    def loadModelThreadCallback(self, data):
        self.detector_face_gpu = data[0]
        self.detector_shape = data[1]
        self.detector_recognition = data[2]
        self.descriptors = data[3]
        self.candidates = data[4]

        self.picThread = PictureThread(self.path)
        self.picThread.callback.connect(self.showPicture)
        self.picThread.start()

    def btnPathClick(self):
        path = QFileDialog.getExistingDirectory()
        if path != '':
            self.path = path.replace('\\', '/')
            with open("path.json", 'w') as f:
                json.dump(self.path, f)
            self.picThread.runFlag = False
            self.picThread = None
            self.lblPath.setText(self.path)
            self.listWidget.clear()
            self.picThread = PictureThread(self.path)
            self.picThread.callback.connect(self.showPicture)
            self.picThread.start()

    def showPicture(self, picture):
        btn = QPushButton()
        btn.setIcon(QIcon(picture))
        btn.setIconSize(QSize(400, 300))
        btn.tag = picture.tag.replace('\\', '/')
        btn.clicked.connect(self.btnPictureClick)
        item = QListWidgetItem()
        item.setSizeHint(QSize(400, 300))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, btn)

    def btnPictureClick(self):
        btn = self.sender()
        file = btn.tag.replace('\\', '/')
        img = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = img[:, :, ::-1].copy()

        # 圖片縮放
        h, w, _ = img.shape
        r = w / h
        lbl_w = self.lblShow.width()
        lbl_h = self.lblShow.height()
        lbl_r = lbl_w / lbl_h

        # 原圖若比例過大, 則縮小, 反之放大, 使得以放入標籤lblShow中
        if r > lbl_r:
            img = cv.resize(img, lbl_w, int(lbl_w / r))
        else:
            img = cv.resize(img, int(lbl_h * r), lbl_h)

        # 偵測
        target = self.get_descriptor(img)
        distance = [np.linalg.norm(target - d) for d in self.descriptors]  # 線性代數取得歐幾里得距離, target vs database
        min_index = np.argmin(distance)  # 最短距離者之索引
        name = self.candidates[min_index]  # 對應的名字

        file_name, _ = os.path.splitext(os.path.basename(file))
        text = f'偵測結果: {name}\n檔案名稱: {file_name}'
        pil = Image.fromarray(img)
        font = ImageFont.truetype('simsun.ttc', 48)
        draw = ImageDraw.Draw(pil, 'RGBA')
        x1 = 0
        y1 = 0
        _, _, t_x2, t_y2 = draw.textbbox(xy=(x1, y1), text=text, font=font)
        x2 = t_x2
        y2 = t_y2
        draw.rectangle((x1, y1, x2, y2), fill=(150, 150, 255, 100))
        draw.text((x1, y1), text, font=font, fill=(0, 255, 0))
        img = np.asarray(pil)

        # 將 cv2格式轉成 QImage, 再轉成 QPixmap才可放入 QLabel中, 寬 高 RGB, 8bit顏色值
        pix = QPixmap(QImage(
            img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)
        )
        self.lblShow.setPixmap(pix)

    def closeEvent(self, event):
        self.picThread.runFlag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
